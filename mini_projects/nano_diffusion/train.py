import gzip
import hashlib
import struct
import time
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
from diffusion import make_linear_schedule, prepare_batch
from model import TinyDenoiser
from sample import sample_loop
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

REPO_ROOT = next(
    path
    for path in Path(__file__).resolve().parents
    if (path / "mini_projects" / "nano_diffusion").is_dir()
)
CACHE = REPO_ROOT / "scratch" / "w16_train_tiny_ddpm_mnist"
OUT_DIR = REPO_ROOT / "scratch" / "nano_diffusion"


# Train configuration
@dataclass(frozen=True)
class TrainConfig:
    seed: int = 16
    T: int = 1000
    epochs: int = 2
    channels: int = 16
    learning_rate: float = 1e-3
    n_train: int = 5000
    batch_size: int = 64
    beta_start: float = 1e-4
    beta_end: float = 0.02
    n_samples: int = 16
    image_shape: tuple[int, int, int] = (1, 28, 28)


def load_mnist_images(cache_dir: Path = CACHE) -> np.ndarray:
    """Return the verified MNIST training images as uint8."""
    filename = "train-images-idx3-ubyte.gz"
    checksum = "f68b3c2dcbeaaa9fbdd348bbdeb94873"
    target = cache_dir / filename

    if target.is_file():
        payload = target.read_bytes()
    else:
        url = "https://ossci-datasets.s3.amazonaws.com/mnist/" + filename
        with urllib.request.urlopen(url, timeout=60) as response:
            payload = response.read()

    if hashlib.md5(payload).hexdigest() != checksum:
        raise ValueError(f"MNIST image checksum mismatch for {target}")

    if not target.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)

    raw = gzip.decompress(payload)
    assert struct.unpack(">IIII", raw[:16]) == (2051, 60000, 28, 28)
    return np.frombuffer(raw, dtype=np.uint8, offset=16).reshape(-1, 28, 28)


def make_train_loader(
    n_train: int, batch_size: int, seed: int, cache_dir: Path = CACHE
) -> DataLoader:
    """Return a reproducible DataLoader of n_train MNIST images scaled to [-1, 1]."""
    images = load_mnist_images(cache_dir=cache_dir)
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(images), n_train, replace=False)
    train_x = torch.from_numpy(images[indices, None]).float() / 127.5 - 1.0
    return DataLoader(
        TensorDataset(train_x),
        batch_size=batch_size,
        shuffle=True,
        generator=torch.Generator().manual_seed(seed),
    )


def train_step(
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    x_t: torch.Tensor,
    t: torch.Tensor,
    noise: torch.Tensor,
) -> float:
    """Perform one optimizer update and return its noise-MSE loss."""
    prediction = model(x_t, t)
    loss = nn.functional.mse_loss(prediction, noise)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss.item()


def training_loop(
    model: nn.Module,
    optimizer: torch.optim.Optimizer,
    train_loader: DataLoader,
    epochs: int,
    alpha_bar: torch.Tensor,
    betas: torch.Tensor,
    train_generator: torch.Generator,
    image_shape: tuple[int, int, int],
    n_samples: int,
    sample_seed: int,
) -> dict[str, list]:
    """Return the loss curve and the training time."""
    batch_losses = []
    training_times = []
    sample_times = []
    grids = []
    epoch_losses = []
    for epoch in range(epochs):
        # Training loop
        model.train()
        start_epoch_training_time = time.perf_counter()
        # Loop in batches through dataset
        for (clean_batch,) in train_loader:
            x_t, t, noise = prepare_batch(
                clean=clean_batch, alpha_bar=alpha_bar, generator=train_generator
            )
            step_loss = train_step(model, optimizer, x_t, t, noise)
            batch_losses.append(step_loss)

        epoch_mean = sum(batch_losses[-len(train_loader) :]) / len(train_loader)
        epoch_losses.append(epoch_mean)
        epoch_training_time = time.perf_counter() - start_epoch_training_time
        training_times.append(epoch_training_time)
        print(
            f"Epoch {epoch + 1} | loss: {epoch_mean:.4f} | train: {epoch_training_time:.2f}s"
        )

        # Sampling
        model.eval()
        start_sample_time = time.perf_counter()
        sample_generator = torch.Generator().manual_seed(sample_seed)
        sample = sample_loop(
            model=model,
            n_samples=n_samples,
            image_shape=image_shape,
            alpha_bar=alpha_bar,
            betas=betas,
            dtype=betas.dtype,
            device=betas.device,
            generator=sample_generator,
        )
        end_sample_time = time.perf_counter()
        sample_time = end_sample_time - start_sample_time
        sample_times.append(sample_time)
        print(f"Sample time for epoch {epoch + 1}: {sample_time:.2f}s")
        grids.append(sample)

    return {
        "batch_losses": batch_losses,  # per-batch loss
        "epoch_losses": epoch_losses,  # mean loss per epoch
        "grids": grids,  # one (grid_count, 1, 28, 28) tensor per epoch
        "train_times": training_times,  # seconds spent training each epoch
        "sample_times": sample_times,  # seconds spent sampling each epoch
    }


if __name__ == "__main__":
    # Get train configuration
    cfg = TrainConfig()
    torch.manual_seed(cfg.seed)
    train_generator = torch.Generator().manual_seed(cfg.seed)
    # Model with 1000 timesteps and 16 channels as in week 16
    model = TinyDenoiser(timesteps=cfg.T, channels=cfg.channels)

    # Prepare training arguments
    train_loader = make_train_loader(
        n_train=cfg.n_train, batch_size=cfg.batch_size, seed=cfg.seed
    )
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    betas, alpha_bar = make_linear_schedule(
        T=cfg.T, beta_start=cfg.beta_start, beta_end=cfg.beta_end
    )

    # Training run
    results = training_loop(
        model=model,
        optimizer=optimizer,
        train_loader=train_loader,
        epochs=cfg.epochs,
        alpha_bar=alpha_bar,
        betas=betas,
        train_generator=train_generator,
        image_shape=cfg.image_shape,
        n_samples=cfg.n_samples,
        sample_seed=cfg.seed,
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    artifact_path = OUT_DIR / f"baseline_{timestamp}_{cfg.epochs}.pt"
    torch.save({"config": asdict(cfg), **results}, artifact_path)
    print(f"Saved run artifacts to {artifact_path}")

import math

import torch
from diffusion import make_linear_schedule, prepare_batch
from model import TinyDenoiser
from torch import nn


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


if __name__ == "__main__":
    torch.manual_seed(16)
    generator = torch.Generator().manual_seed(16)
    # Model with 1000 timesteps and 16 channels as in week 16
    model = TinyDenoiser(timesteps=1000, channels=16)
    T = 1000
    beta_start = 1e-4
    beta_end = 0.02

    # Generate batch of images (random pixels), shapes from MNIST
    betas, alpha_bar = make_linear_schedule(
        T=T, beta_start=beta_start, beta_end=beta_end
    )
    clean = torch.randn((2, 1, 28, 28), generator=generator)

    # Prepare batch for training
    x_t, t, noise = prepare_batch(clean=clean, alpha_bar=alpha_bar, generator=generator)

    # Run a training step
    lr = 1e-3
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    params_before = [p.detach().clone() for p in model.parameters()]
    loss = train_step(model=model, optimizer=optimizer, x_t=x_t, t=t, noise=noise)
    assert math.isfinite(loss)

    assert any(
        not torch.equal(before, after)
        for before, after in zip(params_before, model.parameters(), strict=True)
    )

    print(f"train_step check passed. Loss: {loss:.4f}")

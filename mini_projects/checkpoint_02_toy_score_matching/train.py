import json
from datetime import datetime
from pathlib import Path
from time import perf_counter, time
from types import SimpleNamespace

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_blobs

from mini_projects.checkpoint_02_toy_score_matching.model import BlobsMLP

NUM_SAMPLES = 1500
CENTERS: tuple[tuple[float, float], ...] = (
    (-2.0, -2.0),
    (0.0, 2.0),
    (2.0, -1.0),
)
CLUSTER_STD = 0.5
RANDOM_SEED = 42
TRAIN_PERCENTAGE = 0.8
MAX_ITERS = 20
FORWARD_SIGMA = 0.5
TRAIN_CONFIG = {
    "dataset_features": 2,
    "mlp_blocks": 2,
    "internal_neurons": 32,
    "objective": "x0",  # or "score"
    "learning_rate": 0.1,
}

# Artifact locations
PROJECT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = PROJECT_DIR / "results"
CHECKPOINTS_DIR = PROJECT_DIR / "checkpoints"


def create_toy_dataset(
    num_samples: int = NUM_SAMPLES,
    centers: tuple[tuple[float, float], ...] = CENTERS,
    cluster_std: float = CLUSTER_STD,
    random_seed: int = RANDOM_SEED,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate reproducible samples from balanced isotropic Gaussian blobs.

    This follows the dataset construction used in the Week 1 forward-noising
    notebook while making the component centers explicit.
    """
    x0, labels = make_blobs(
        n_samples=num_samples,
        centers=centers,
        cluster_std=cluster_std,
        random_state=random_seed,
    )
    return x0, labels


def train() -> None:
    """Train the MLP on one fixed-noise denoising or score objective."""
    # Record the start time and create a readable, unique run identifier.
    start_time = perf_counter()
    human_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_timestamp = time()
    experiment_id = f"toy_score_matching_exp_{human_timestamp}_{unique_timestamp}"

    # Seed PyTorch operations and the NumPy data split independently.
    torch.manual_seed(RANDOM_SEED)
    rng = np.random.default_rng(RANDOM_SEED)

    # Select the available accelerator or fall back to CPU.
    device = (
        torch.accelerator.current_accelerator().type
        if torch.accelerator.is_available()
        else "cpu"
    )

    model_config = SimpleNamespace(**TRAIN_CONFIG)
    model = BlobsMLP(config=model_config).to(device)

    x0, _ = create_toy_dataset()

    # Create a reproducible random train-validation split.
    indices = np.arange(len(x0))
    rng.shuffle(indices)

    train_size = int(len(x0) * TRAIN_PERCENTAGE)

    train_indices = indices[:train_size]
    val_indices = indices[train_size:]

    train_x0 = x0[train_indices]
    val_x0 = x0[val_indices]

    # Convert clean samples to tensors on the selected device.
    train_x0 = torch.tensor(train_x0, dtype=torch.float32).to(device)
    val_x0 = torch.tensor(val_x0, dtype=torch.float32).to(device)

    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=TRAIN_CONFIG["learning_rate"])

    history_records = []

    # Reuse one noisy validation set so losses are comparable across iterations.
    val_noise = torch.randn_like(val_x0)
    val_xt = val_x0 + FORWARD_SIGMA * val_noise

    if TRAIN_CONFIG["objective"] == "x0":
        val_target = val_x0
    elif TRAIN_CONFIG["objective"] == "score":
        val_target = -(val_xt - val_x0) / FORWARD_SIGMA**2

    iteration = 0
    while True:
        iteration += 1

        # Training
        model.train()

        train_noise = torch.randn_like(train_x0)
        train_xt = train_x0 + FORWARD_SIGMA * train_noise

        predictions = model(train_xt)

        if TRAIN_CONFIG["objective"] == "x0":
            target = train_x0
        elif TRAIN_CONFIG["objective"] == "score":
            # Conditional Gaussian score target: -(xt - x0) / sigma^2.
            target = -(train_xt - train_x0) / FORWARD_SIGMA**2
        else:
            raise ValueError(
                f"Unsupported objective: {TRAIN_CONFIG['objective']!r}. "
                "Expected 'x0' or 'score'."
            )

        optimization_loss = loss_fn(predictions, target)

        optimizer.zero_grad()
        optimization_loss.backward()
        optimizer.step()

        # Validation
        model.eval()
        with torch.no_grad():
            train_predictions = model(train_xt)
            train_loss = loss_fn(train_predictions, target)

            val_predictions = model(val_xt)
            val_loss = loss_fn(val_predictions, val_target)

        print(
            f"Iteration: {iteration}; train_loss: {train_loss.item():.4f}; "
            f"val_loss: {val_loss.item():.4f}"
        )

        history_records.append(
            {
                "run_id": experiment_id,
                "objective": TRAIN_CONFIG["objective"],
                "learning_rate": TRAIN_CONFIG["learning_rate"],
                "max_iterations": MAX_ITERS,
                "iteration": iteration,
                "train_loss": train_loss.item(),
                "val_objective_loss": val_loss.item(),
            }
        )
        if iteration >= MAX_ITERS:
            break

    end_time = perf_counter()
    runtime = end_time - start_time
    print(f"Training runtime: {runtime:.3f} seconds")

    # Save artifacts.
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    CHECKPOINTS_DIR.mkdir(parents=True, exist_ok=True)

    history_path = RESULTS_DIR / "training_history.csv"
    summary_path = RESULTS_DIR / "experiment_summary.csv"
    checkpoint_path = CHECKPOINTS_DIR / f"{experiment_id}.pt"

    torch.save(
        {
            "run_id": experiment_id,
            "model_state_dict": model.state_dict(),
            "train_config": dict(TRAIN_CONFIG),
            "data_config": {
                "num_samples": NUM_SAMPLES,
                "centers": CENTERS,
                "cluster_std": CLUSTER_STD,
                "train_percentage": TRAIN_PERCENTAGE,
                "noise_level": FORWARD_SIGMA,
                "seed": RANDOM_SEED,
            },
        },
        checkpoint_path,
    )

    # Append per-iteration metrics to the shared training history.
    history_df = pd.DataFrame(history_records)
    history_df.to_csv(
        history_path,
        mode="a",
        header=not history_path.exists(),
        index=False,
    )

    # Append one summary row for the completed training run.
    summary_record = pd.DataFrame(
        [
            {
                "run_id": experiment_id,
                "objective": TRAIN_CONFIG["objective"],
                "seed": RANDOM_SEED,
                "noise_level": FORWARD_SIGMA,
                "learning_rate": TRAIN_CONFIG["learning_rate"],
                "iterations": MAX_ITERS,
                "final_train_objective_loss": train_loss.item(),
                "final_val_objective_loss": val_loss.item(),
                "val_score_mse": None,  # Reserved for evaluation output.
                "runtime": runtime,
                "status": "training_completed",
                "num_samples": NUM_SAMPLES,
                "centers": json.dumps(CENTERS),
                "cluster_std": CLUSTER_STD,
                "train_percentage": TRAIN_PERCENTAGE,
                "dataset_features": TRAIN_CONFIG["dataset_features"],
                "mlp_blocks": TRAIN_CONFIG["mlp_blocks"],
                "internal_neurons": TRAIN_CONFIG["internal_neurons"],
                "checkpoint_path": str(checkpoint_path.relative_to(PROJECT_DIR)),
                "optimizer": "SGD",
            }
        ]
    )
    summary_record.to_csv(
        summary_path,
        mode="a",
        header=not summary_path.exists(),
        index=False,
    )


if __name__ == "__main__":
    train()

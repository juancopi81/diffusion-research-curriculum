import argparse
from pathlib import Path
from types import SimpleNamespace

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch

from mini_projects.checkpoint_02_toy_score_matching.model import BlobsMLP
from mini_projects.checkpoint_02_toy_score_matching.train import create_toy_dataset

PROJECT_DIR = Path(__file__).resolve().parent
CHECKPOINTS_DIR = PROJECT_DIR / "checkpoints"
FIGURES_DIR = PROJECT_DIR / "figures"
SUMMARY_PATH = PROJECT_DIR / "results" / "experiment_summary.csv"

GRID_MIN = -4.0
GRID_MAX = 4.0
GRID_RESOLUTION = 30
QUIVER_SCALE = 50


def gaussian_mixture_score(
    points: np.ndarray,
    component_centers: np.ndarray,
    component_std: float,
) -> np.ndarray:
    """Return the exact score of an equal-weight isotropic Gaussian mixture.

    The centers are the means of the generating Gaussian components, not the
    observed samples. Each output row is the responsibility-weighted average
    of the component scores at the corresponding input point.
    """
    differences = component_centers[None, :, :] - points[:, None, :]
    squared_distances = np.sum(differences**2, axis=2)

    log_responsibilities = -squared_distances / (2 * component_std**2)
    log_responsibilities -= np.max(log_responsibilities, axis=1, keepdims=True)
    responsibilities = np.exp(log_responsibilities)
    responsibilities /= np.sum(responsibilities, axis=1, keepdims=True)

    component_scores = differences / component_std**2
    return np.sum(
        responsibilities[:, :, None] * component_scores,
        axis=1,
    )


def load_experiment(
    experiment_id: str,
    device: str | torch.device,
) -> tuple[BlobsMLP, dict, dict]:
    """Reconstruct a trained model and its saved configuration."""
    checkpoint_path = CHECKPOINTS_DIR / f"{experiment_id}.pt"
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=True)

    train_config = checkpoint["train_config"]
    data_config = checkpoint["data_config"]
    model = BlobsMLP(config=SimpleNamespace(**train_config)).to(device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    return model, train_config, data_config


def predict_score(
    model: torch.nn.Module,
    noisy_points: torch.Tensor,
    objective: str,
    forward_sigma: float,
) -> np.ndarray:
    """Convert model predictions to a score field."""
    with torch.no_grad():
        predictions = model(noisy_points)

        if objective == "x0":
            # Tweedie's identity converts E[x0 | xt] to the marginal score.
            scores = (predictions - noisy_points) / forward_sigma**2
        elif objective == "score":
            scores = predictions
        else:
            raise ValueError(
                f"Unsupported objective: {objective!r}. Expected 'x0' or 'score'."
            )

    return scores.cpu().numpy()


def create_score_grid() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Create the shared plotting grid and its flattened point representation."""
    coordinates = np.linspace(GRID_MIN, GRID_MAX, GRID_RESOLUTION)
    grid_x, grid_y = np.meshgrid(coordinates, coordinates)
    grid_points = np.column_stack((grid_x.ravel(), grid_y.ravel()))
    return grid_x, grid_y, grid_points


def save_score_field(
    *,
    grid_x: np.ndarray,
    grid_y: np.ndarray,
    scores: np.ndarray,
    clean_data: np.ndarray,
    title: str,
    color: str,
    save_path: Path,
) -> None:
    """Render one score field over the clean dataset."""
    field_shape = grid_x.shape
    horizontal_scores = scores[:, 0].reshape(field_shape)
    vertical_scores = scores[:, 1].reshape(field_shape)

    figure, axis = plt.subplots(figsize=(8, 8))
    axis.scatter(
        clean_data[:, 0],
        clean_data[:, 1],
        alpha=0.1,
        color="blue",
        s=10,
        label="Clean data samples",
    )
    axis.quiver(
        grid_x,
        grid_y,
        horizontal_scores,
        vertical_scores,
        color=color,
        alpha=0.6,
        scale=QUIVER_SCALE,
        headwidth=3,
    )
    axis.set(
        title=title,
        xlim=(GRID_MIN, GRID_MAX),
        ylim=(GRID_MIN, GRID_MAX),
        xlabel="X",
        ylabel="Y",
    )
    axis.legend()
    axis.grid(True, linestyle="--", alpha=0.3)
    figure.tight_layout()

    save_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved vector field to {save_path}")


def recreate_dataset(data_config: dict) -> np.ndarray:
    """Recreate the clean dataset described by a checkpoint."""
    clean_data, _ = create_toy_dataset(
        num_samples=data_config["num_samples"],
        centers=tuple(tuple(center) for center in data_config["centers"]),
        cluster_std=data_config["cluster_std"],
        random_seed=data_config["seed"],
    )
    return clean_data


def create_validation_points(
    clean_data: np.ndarray,
    data_config: dict,
    device: str | torch.device,
) -> tuple[torch.Tensor, np.ndarray]:
    """Recreate a deterministic noisy validation set.

    Noise is generated on CPU so the evaluation points remain identical when
    the model is evaluated on CPU, MPS, or another accelerator.
    """
    seed = int(data_config["seed"])
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(clean_data))
    train_size = int(len(clean_data) * data_config["train_percentage"])

    validation_clean = torch.tensor(
        clean_data[indices[train_size:]],
        dtype=torch.float32,
    )
    noise_generator = torch.Generator(device="cpu").manual_seed(seed)
    validation_noise = torch.randn(
        validation_clean.shape,
        generator=noise_generator,
        dtype=validation_clean.dtype,
    )
    validation_noisy = (
        validation_clean + data_config["noise_level"] * validation_noise
    )

    return validation_noisy.to(device), validation_noisy.numpy()


def update_experiment_summary(experiment_id: str, score_mse: float) -> None:
    """Store the common score metric for one completed evaluation."""
    if not SUMMARY_PATH.exists():
        raise FileNotFoundError(f"Could not find experiment summary at {SUMMARY_PATH}")

    summary = pd.read_csv(SUMMARY_PATH)
    matching_rows = summary["run_id"] == experiment_id
    if matching_rows.sum() != 1:
        raise ValueError(
            f"Expected exactly one summary row for {experiment_id}, "
            f"found {matching_rows.sum()}."
        )

    summary.loc[matching_rows, "val_score_mse"] = score_mse
    summary.loc[matching_rows, "status"] = "evaluation_completed"
    summary.to_csv(SUMMARY_PATH, index=False)


def evaluate_experiment(
    experiment_id: str,
    device: str | torch.device,
) -> float:
    """Evaluate one checkpoint against the exact noisy-mixture score."""
    model, train_config, data_config = load_experiment(experiment_id, device)
    clean_data = recreate_dataset(data_config)

    forward_sigma = float(data_config["noise_level"])
    component_centers = np.asarray(data_config["centers"], dtype=np.float64)
    # Gaussian convolution adds the clean component and forward-noise variances.
    noisy_component_std = np.sqrt(
        data_config["cluster_std"] ** 2 + forward_sigma**2
    )

    grid_x, grid_y, grid_points = create_score_grid()
    analytical_grid_scores = gaussian_mixture_score(
        grid_points,
        component_centers,
        noisy_component_std,
    )
    model_grid_scores = predict_score(
        model,
        torch.tensor(grid_points, dtype=torch.float32, device=device),
        train_config["objective"],
        forward_sigma,
    )

    save_score_field(
        grid_x=grid_x,
        grid_y=grid_y,
        scores=model_grid_scores,
        clean_data=clean_data,
        title=f"Predicted Score Vector Field ({train_config['objective']} objective)",
        color="red",
        save_path=FIGURES_DIR / f"{experiment_id}_vector_field.png",
    )
    save_score_field(
        grid_x=grid_x,
        grid_y=grid_y,
        scores=analytical_grid_scores,
        clean_data=clean_data,
        title="True Analytical Score Vector Field",
        color="green",
        save_path=FIGURES_DIR / "true_analytical_vector_field.png",
    )

    validation_noisy, validation_noisy_numpy = create_validation_points(
        clean_data,
        data_config,
        device,
    )
    predicted_validation_scores = predict_score(
        model,
        validation_noisy,
        train_config["objective"],
        forward_sigma,
    )
    analytical_validation_scores = gaussian_mixture_score(
        validation_noisy_numpy,
        component_centers,
        noisy_component_std,
    )
    score_mse = float(
        np.mean((analytical_validation_scores - predicted_validation_scores) ** 2)
    )

    update_experiment_summary(experiment_id, score_mse)
    print(
        f"{experiment_id} ({train_config['objective']} objective): "
        f"val_score_mse={score_mse:.6f}"
    )
    return score_mse


def select_device() -> str:
    """Select the available accelerator or fall back to CPU."""
    if torch.accelerator.is_available():
        return torch.accelerator.current_accelerator().type
    return "cpu"


def parse_args() -> argparse.Namespace:
    """Parse the experiment IDs to evaluate."""
    parser = argparse.ArgumentParser(
        description="Evaluate toy score models against the exact noisy MoG score."
    )
    parser.add_argument(
        "experiment_ids",
        nargs="+",
        help="One or more checkpoint run IDs from experiment_summary.csv.",
    )
    return parser.parse_args()


def main() -> None:
    """Evaluate every requested checkpoint."""
    args = parse_args()
    device = select_device()
    print(f"Evaluation device: {device}")
    for experiment_id in args.experiment_ids:
        evaluate_experiment(experiment_id, device)


if __name__ == "__main__":
    main()

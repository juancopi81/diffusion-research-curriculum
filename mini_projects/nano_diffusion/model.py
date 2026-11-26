import torch
from torch import nn


class TinyDenoiser(nn.Module):
    """Predict image-shaped noise from a noisy image and its timestep."""

    def __init__(self, timesteps: int, channels: int):
        super().__init__()
        self.timesteps = timesteps
        self.input_conv = nn.Conv2d(1, channels, kernel_size=3, padding=1)
        self.time_projection = nn.Sequential(
            nn.Linear(1, channels),
            nn.SiLU(),
            nn.Linear(channels, channels),
        )
        self.output_layers = nn.Sequential(
            nn.SiLU(),
            nn.Conv2d(channels, channels, kernel_size=3, padding=2, dilation=2),
            nn.SiLU(),
            nn.Conv2d(channels, 1, kernel_size=3, padding=1),
        )

    def forward(self, x_t: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        t_scaled = t.to(dtype=x_t.dtype).reshape(-1, 1) / self.timesteps
        time_features = self.time_projection(t_scaled)[:, :, None, None]
        return self.output_layers(self.input_conv(x_t) + time_features)


if __name__ == "__main__":
    generator = torch.Generator().manual_seed(16)
    # Model with 1000 timesteps and 16 channels as in week 16
    model = TinyDenoiser(timesteps=1000, channels=16)

    # Generate batch of images (random pixels), shapes from MNIST
    x_t = torch.randn((2, 1, 28, 28), generator=generator)
    t = torch.tensor([1, 3], dtype=torch.long)

    # Run model
    predicted_noise = model(x_t, t)

    assert predicted_noise.shape == x_t.shape
    assert torch.isfinite(predicted_noise).all()
    print(f"TinyDenoiser check passed. Output shape: {predicted_noise.shape}")

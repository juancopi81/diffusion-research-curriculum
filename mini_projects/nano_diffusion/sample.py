import torch
from diffusion import coefficient_at, make_linear_schedule
from torch import nn


def single_step_reverse(
    x_t: torch.Tensor,
    t: int,
    model: nn.Module,
    alpha_bar: torch.Tensor,
    betas: torch.Tensor,
    generator: torch.Generator,
) -> torch.Tensor:
    """Return one step of reverse diffusion"""

    # Prepare variables
    t_tensor = torch.full((x_t.shape[0],), t, dtype=torch.long, device=x_t.device)
    predicted_noise = model(x_t, t_tensor)
    alpha_bar_t = coefficient_at(alpha_bar, t_tensor, x_t)
    alpha_bar_t_minus_one = coefficient_at(alpha_bar, t_tensor - 1, x_t)
    beta_t = coefficient_at(betas, t_tensor, x_t)

    # Reverse mean from noisy prediction. Derived in week 17 day 3
    mean = (x_t - (beta_t * predicted_noise / (1 - alpha_bar_t).sqrt())) / (
        1 - beta_t
    ).sqrt()

    # For x_0, we don't add noise to the mean
    if t > 1:
        z = torch.randn(
            x_t.shape, dtype=x_t.dtype, device=x_t.device, generator=generator
        )
    else:
        z = torch.zeros_like(x_t)

    # Variance as derived in week 17 day 2
    variance = beta_t * (1 - alpha_bar_t_minus_one) / (1 - alpha_bar_t)

    # Sample x t-1
    return mean + torch.sqrt(variance) * z


@torch.no_grad()
def sample_loop(
    model: nn.Module,
    n_samples: int,
    image_shape: tuple[int, int, int],
    alpha_bar: torch.Tensor,
    betas: torch.Tensor,
    dtype: torch.dtype,
    device: torch.device,
    generator: torch.Generator,
) -> torch.Tensor:
    """Return a sample from the model."""
    x_t = torch.randn(
        (n_samples, *image_shape),
        dtype=dtype,
        device=device,
        generator=generator,
    )
    T = alpha_bar.shape[0] - 1
    for t in range(T, 0, -1):
        x_t = single_step_reverse(
            x_t=x_t,
            t=t,
            model=model,
            alpha_bar=alpha_bar,
            betas=betas,
            generator=generator,
        )
    return x_t


if __name__ == "__main__":
    betas, alpha_bar = make_linear_schedule(T=2, beta_start=0.2, beta_end=0.2)
    x_t = torch.full((2, 1, 1, 1), 0.9)
    dtype = betas.dtype
    device = betas.device

    def constant_model(x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        return torch.full_like(x, 0.3)

    reference_rng = torch.Generator().manual_seed(16)
    sampler_rng = torch.Generator().manual_seed(16)

    z = torch.randn(x_t.shape, generator=reference_rng)
    expected = 0.89442719 + z / 3
    actual = single_step_reverse(
        x_t, 2, constant_model, alpha_bar=alpha_bar, betas=betas, generator=sampler_rng
    )
    torch.testing.assert_close(actual, expected)

    # Also verify t = 1 doesn't touch the generator
    state_before = sampler_rng.get_state()
    _ = single_step_reverse(
        x_t, 1, constant_model, alpha_bar=alpha_bar, betas=betas, generator=sampler_rng
    )
    assert torch.equal(state_before, sampler_rng.get_state())
    print("single_step_reverse checks passed.")

    # Testing sample loop
    betas_3, alpha_bar_3 = make_linear_schedule(T=3, beta_start=0.1, beta_end=0.3)
    print(f"betas_3: {betas_3}, alpha_bar_3: {alpha_bar_3}")
    seen_timesteps: list[list[int]] = []

    def recording_constant_model(x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        seen_timesteps.append(t.tolist())
        return torch.full_like(x, 0.3)

    image_shape = (1, 4, 4)
    n_samples = 2

    x_0_sampled = sample_loop(
        recording_constant_model,
        n_samples,
        image_shape,
        alpha_bar=alpha_bar_3,
        betas=betas_3,
        dtype=betas_3.dtype,
        device=betas_3.device,
        generator=sampler_rng,
    )

    assert x_0_sampled.shape == (2, 1, 4, 4)
    assert seen_timesteps == [[3, 3], [2, 2], [1, 1]]
    assert torch.isfinite(x_0_sampled).all()
    print("sampled_loop checks passed")

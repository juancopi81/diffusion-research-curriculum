import torch


def make_linear_schedule(
    T: int, beta_start: float, beta_end: float
) -> tuple[torch.Tensor, torch.Tensor]:
    """Creates a linear schedule and cumulative alphas for diffusion (DDPM)"""
    betas = torch.cat((torch.zeros(1), torch.linspace(beta_start, beta_end, T)))
    alphas = 1 - betas
    alpha_bar = torch.cumprod(alphas, dim=0)
    return betas, alpha_bar


def coefficient_at(
    table: torch.Tensor, t: torch.Tensor, batch: torch.Tensor
) -> torch.Tensor:
    """Gather one coefficient per image and broadcast over its coordinates"""
    assert t.dtype == torch.long and t.shape == (batch.shape[0],)
    return table[t].reshape(batch.shape[0], 1, 1, 1)


def prepare_batch(
    clean: torch.Tensor, alpha_bar: torch.Tensor, generator: torch.Generator
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Prepare batch with x_t, timestep, and generated noise"""
    t = torch.randint(
        1, alpha_bar.shape[0], (len(clean),), device=clean.device, generator=generator
    )
    noise = torch.randn(
        clean.shape, dtype=clean.dtype, device=clean.device, generator=generator
    )
    # Forward process DDPM
    a_bar_t = coefficient_at(alpha_bar, t, clean)
    x_t = a_bar_t.sqrt() * clean + (1 - a_bar_t).sqrt() * noise
    return x_t, t, noise


# To be deleted, just for testing while developing
if __name__ == "__main__":
    # Some testing variables
    T = 3
    beta_start = 0.1
    beta_end = 0.3
    seed = 42
    generator = torch.Generator().manual_seed(42)
    # Test make_linea_scheduler
    betas, alpha_bar = make_linear_schedule(T, beta_start, beta_end)
    print(f"betas from linear scheduler: {betas}")
    print(f"alpha_bar from linear scheduler: {alpha_bar}")
    # Test coefficient at
    test_batch = torch.randn(size=(2, 1, 28, 28))
    test_t = torch.tensor([1, 3], dtype=torch.long)
    print(f"Shape of test batch {test_batch.shape}")
    test_coefficient = coefficient_at(alpha_bar, test_t, test_batch)
    print(f"test_coefficient: {test_coefficient}")
    torch.testing.assert_close(alpha_bar, torch.tensor([1.0, 0.9, 0.72, 0.504]))
    assert test_coefficient.shape == (2, 1, 1, 1)
    torch.testing.assert_close(test_coefficient.flatten(), torch.tensor([0.9, 0.504]))
    print(f"test_coefficient shape: {test_coefficient.shape}")

    # Check prepare_batch with a tiny batch of zeros
    zero_batch = torch.zeros(size=(2, 1, 4, 4))
    x_t, t, noise = prepare_batch(zero_batch, alpha_bar, generator)

    expected_x_t = (1 - coefficient_at(alpha_bar, t, zero_batch)).sqrt() * noise
    assert torch.allclose(x_t, expected_x_t)
    print(f"t: {t}")
    print("Zero-batch scaling check passed.")

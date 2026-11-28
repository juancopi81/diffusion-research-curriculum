# Two-epoch MNIST baseline

Juan ran the extracted DDPM on November 27, 2026. A second invocation in a fresh process reproduced all 158 batch losses and both tensors of 16 generated images exactly.

From the repository root, run:

```sh
uv run python mini_projects/nano_diffusion/train.py
```

## Setup

Both runs used PyTorch 2.13.0 on Apple silicon, CPU. The fresh process used the default of six PyTorch intra-op threads. The config selected 5,000 MNIST training images with seed 16, scaled them to $[-1,1]$, and shuffled batches of 64. Each epoch had 79 optimizer updates, with eight images in the last batch. The denoiser had 16 channels, Adam used a learning rate of 0.001, and the linear schedule ran from 0.0001 to 0.02 over 1,000 steps. Sampling restarted its generator at seed 16 each epoch and produced 16 grayscale images of size 28 × 28.

## Results

Each epoch loss is the arithmetic mean of its 79 batch noise MSEs, as in the [Week 16 notebook](../../../../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb).

| Epoch | Mean noise MSE, both runs | Training seconds, Juan / repeat | Sampling seconds, Juan / repeat | Juan’s samples |
| --- | ---: | ---: | ---: | --- |
| 1 | 0.4860353755 | 1.98 / 2.02 | 1.77 / 1.74 | [Epoch 1 grid](epoch_1.png) |
| 2 | 0.2043889097 | 1.94 / 1.95 | 1.84 / 1.80 | [Epoch 2 grid](epoch_2.png) |

The epoch means match the precision printed in Week 16. Rendering Juan’s sample tensors with the notebook’s plotting code produced eight differing pixels at epoch 1 and 17 at epoch 2 out of 150,876 pixels per figure. Each differed by one grayscale level. An additional run using the notebook’s four-thread setting reproduced both saved notebook figures pixel for pixel.

The local PyTorch artifacts in `scratch/nano_diffusion/` contain the config, all batch and epoch losses, the sample tensors, and separate training and sampling times. Juan’s artifact is `baseline_2026-11-27_18-12-26_2.pt`. The fresh-process repeat is `baseline_2026-11-27_18-14-10_2.pt`.

## What to compare in a longer run

Epoch 2 has more white area than epoch 1, and whole digits are still hard to recognize. In the Week 16 run, the epoch-mean training noise MSE reached 0.0543 by epoch 30. Some samples showed strokes and loops suggestive of digits even though many shapes remained ambiguous. For Week 18, follow the loss trend and compare the same fixed-seed tiles across epochs for strokes that join into recognizable digits. [Week 16 observations](../../../../notes/w16_hf_ddpm_training.md#what-i-see-in-the-experiment)

# Week 14 Checkpoint — Manuscript and Evidence

[report.md](report.md) is a first manuscript draft assembled from the reviewed
opening, compact comparison table, three evidence passages, and diffusion
connection in [draft.md](draft.md). Those passages are unchanged. Section
headings, figure placement, alt text, and source pointers provide structure;
review notes and the repeated expanded model answers are excluded.

During blog editing on 2026-10-26, the author's "Models and Experiments"
roadmap was added before the table, with light language corrections and
links to the existing notes and experiments. Its reviewed wording is also
recorded in the working draft. The score-section revision and the author's
closing open questions remain pending.

The author reviewed the draft on 2026-10-26 and said the wording sounds good
so far. Connections between sections and the final blog title remain for
blog editing. The Week 14 study checkpoint closed on 2026-10-27 after
[Day 7's review and corrections](../../notes/w14_study_plan.md#day-7-completion-decision).
That record distinguishes reference use and guided corrections from unaided
recall. This local manuscript has not been published.

## Figure Provenance

All cell and output indices below are zero-based. PNGs were extracted from
saved output bytes or copied from the existing figure; notebooks were not
executed or modified, and the images were not edited.

| Figure | Saved source | Cell index and ID | Output identity |
| --- | --- | --- | --- |
| [VAE reconstructions](figures/w11_vae_reconstructions.png) | [Week 11 solved notebook](../../notebooks/w11_minimal_vae_mnist_solved.ipynb) | 23, `reconstructions` | Output 0, `display_data`, `image/png`; execution count 16 |
| [RealNVP first-coordinate comparison](figures/w12_realnvp_first_coordinate_comparison.png) | [Week 12 solved notebook](../../notebooks/w12_realnvp_2d_blobs_solved.ipynb) | 20, `9c459c26` | Output 0, `display_data`, `image/png`; execution count 11 |
| [Score clipping comparison](figures/w13_score_clipping_comparison.png) | [Existing Week 13 figure](../../notes/figures/w13_score_clipping_comparison.png), identical to the [Week 13 solved notebook](../../notebooks/w13_optimizers_sanity_solved.ipynb) output | 29, `s7-results` | Output 1, `display_data`, `image/png`; execution count 16 |

## Verified Run Context

### VAE

Configuration is recorded in Week 11 cell 2 (`setup`), with training in cell
20 (`training`). The run uses MNIST, 10,000 training and 1,000 held-out images,
seed 11, 784 input coordinates, two latent coordinates, hidden width 128,
batch size 128, Adam learning rate 0.001, and five epochs on CPU. The Gaussian
decoder has fixed observation variance 0.1.

The selected panel uses one held-out example of each digit. Its four rows
show inputs, initial reconstructions using encoder means, trained
reconstructions using encoder means, and trained reconstructions using
sampled encoder latents. The decoder displays mean images in every
reconstruction row. Latent sampling in this panel uses seed 18.

### RealNVP

Configuration and data are recorded in Week 12 cell 2 (`b3fad07f`), training
in cell 14 (`bd55c4a5`), and the one-layer comparison in cell 19 (`a2d29281`).
The data use seed 12, 2,000 training and 400 held-out points, four centers at
the combinations of −1.8 and 1.8, and component standard deviation 0.35.
The models use a standard normal base, hidden width 32, batch size 256,
and Adam learning rate 0.002 on CPU.

The six-layer model uses 450 updates and initialization seed 22; the
one-layer model uses 200 updates and initialization seed 32. Their minibatch
generators use seeds 23 and 33, respectively. The plotted model samples use
the same 1,000 base draws, seeded with 17, and are compared with the 400
held-out data points.

Training budgets and training seeds differ between the two models. This
figure is not a controlled depth-only comparison. The unchanged first
coordinate in the one-layer model is an architectural constraint.

### Fixed-noise Score Toy

The [Week 13 stability note](../../notes/w13_training_stability_for_diffusion.md)
is the reference for this selected result. Notebook cells 21 (`s7-setup`),
23 (`s7-matching`), 28 (`s7-runner`), and 29 (`s7-results`) record the paired
configuration and saved comparison.

Both conditions use 1,200 training and 300 held-out points from the same
Gaussian-blob construction, corruption standard deviation 0.5, plain SGD
learning rate 0.1, and 20 updates on CPU. Data, split, and initialization
seeds are 42; the shared fresh training-noise sequence uses seed 43, and the
fixed held-out noisy set uses seed 44. The intervention is global L2
parameter-gradient clipping off versus a threshold of 0.5.

Training MSE uses conditional Gaussian corruption scores; held-out MSE uses
the analytical marginal score of the noisy mixture. Both metrics average
over examples and coordinates. The final held-out score MSE is 1.240304
without clipping and 1.345339 with clipping, from a shared initial value of
1.869517. These are Week 13 measurements, not the earlier Week 8 run's
results. No reverse sampler is implemented in this comparison.

### Comparison Scope

The three experiments use different datasets and training objectives; their
raw loss values do not form a matched benchmark or rank the model families.
The manuscript compares what each approach learns and the saved evidence
from its own experiment.

## SHA256 Audit

Hashes record the saved sources used for this assembly.

| Repository source | SHA256 |
| --- | --- |
| `notebooks/w11_minimal_vae_mnist_solved.ipynb` | `80290078d2943b1bfc9878aa7b81de80f3763c36f81186ee512230b8414ed8f2` |
| `notebooks/w12_realnvp_2d_blobs_solved.ipynb` | `da0a4d0bd3beceabb8328585637a99decc3c6b702a704c3db938beb8b72e898f` |
| `notebooks/w13_optimizers_sanity_solved.ipynb` | `f8a996e8d04433693cef13c7a87da5bb3db1e54c4b27dea5b48f75a76ce944b8` |
| `notes/figures/w13_score_clipping_comparison.png` | `f2ee20b68e061594bf8ad159211af9792be41898e0c33e0b47a990ad32143646` |
| `notes/w13_training_stability_for_diffusion.md` | `a0cce7a360b3e7ef005d87e64ed575bab5e230e087b384a10ecb85e297c5c667` |
| `notes/w06_stat110_transformations_convolutions.md` | `8cf0ab0e7ae8e66c3cfdc330b9f4fed890dc28a0d0b7c3b19b70c97ae1a1a908` |

Each exported PNG matches its saved notebook output byte for byte. The score
PNG also matches the existing figure byte for byte.

| Local figure | Dimensions (pixels) | Bytes | SHA256 |
| --- | --- | --- | --- |
| `w11_vae_reconstructions.png` | 1308 × 575 | 67,052 | `ea2c2f704c3904e7f97e4c0094ccd570eddab74104709bfe4b4e2b0b09877cae` |
| `w12_realnvp_first_coordinate_comparison.png` | 990 × 390 | 64,142 | `864e5a4f5203f74acdb492fc00abbe8c24183f1bbba0b9ca41584efc0dc18b5e` |
| `w13_score_clipping_comparison.png` | 1552 × 430 | 109,116 | `f2ee20b68e061594bf8ad159211af9792be41898e0c33e0b47a990ad32143646` |

# Diffusion from First Principles

**A working research notebook for rebuilding diffusion models from probability foundations.**

A 12-month personal research notebook from probability foundations to diffusion, score-based models, SDEs, and flow matching, with proofs, notebooks, and implementations.

This is a personal learning and research project.

## 📍 The Curriculum

The full, 52-week study plan is documented in **[CURRICULUM.md](./CURRICULUM.md)**. Portfolio-ready outputs are tracked in **[MILESTONES.md](./MILESTONES.md)**.

It is divided into five phases:

1. **Probability Core**
2. **Generative Basics** (Current Phase: linear algebra, VAEs, and flows)
3. **Diffusion in Depth** (DDPM/DDIM)
4. **The SDE View** (Score-based models)
5. **Research & Replication** (Paper reproductions)

---

## 🚀 Current Progress

- **Phase:** 2 (Linear Algebra + Generative Modeling Basics)
- **Completed:** Phase 1 and Weeks 9–15 (Week 15 completed on 2026-11-05)
- **Latest work:** [Week 15 closeout](./notes/w15_forward_process_discrete.md#day-6--consolidating-the-forward-process-and-closing-week-15) — Forward derivation, completed MNIST notebook, linear/cosine comparison, Monte Carlo verification, final explanation, and learner questions consolidated; independent recall and added explanations distinguished
- **Next:** [Week 16](./CURRICULUM.md#week-16--first-full-toy-diffusion-training-small): training objective, timestep-conditioned denoising, prediction parameterizations, and reverse sampling. The optional cosine-schedule/blog exploration is enrichment. The checkpoint's blog editing continues separately.

See **[PROGRESS.md](./PROGRESS.md)** for detailed task tracking.

---

## Best Artifacts

| Artifact | Why it matters |
| --- | --- |
| [Checkpoint 01 - Conditioning in Code](./mini_projects/checkpoint_01_conditioning_in_code/) | Shows how conditioning changes the probability model, verified with Monte Carlo. |
| [Checkpoint 02 - Toy Score Matching](./mini_projects/checkpoint_02_toy_score_matching/) | Compares two learned score objectives against the exact score of a noisy Gaussian mixture. |
| [Checkpoint 03 - Generative Toolkit](./mini_projects/checkpoint_03_generative_toolkit_report/) | Compares VAE, RealNVP, and score learning using sourced experiments and a completed study review; the blog edition remains in editing. |
| [Canonical forward diffusion on MNIST](./notebooks/w15_forward_diffusion_mnist_solved.ipynb) | Connects the Gaussian derivation to two schedules, saved image grids, fixed-input Monte Carlo checks, and the final conceptual review. |
| [Multivariate Gaussian score and conditioning](./notebooks/w10_mv_gaussian_score_solved.ipynb) | Connects Cholesky sampling, analytic and numerical scores, Gaussian conditioning, and the DDPM forward kernel. |
| [PCA/SVD projection and reconstruction](./notebooks/w09_pca_svd_solved.ipynb) | Connects projections, eigendecomposition, SVD, low-rank reconstruction, and latent compression. |
| [Gaussian score derivation](./notes/w03_score_of_gaussian.md) | Builds the first exact score function used later in diffusion. |
| [Joint Gaussian conditioning notebook](./notebooks/w05_joint_gaussians_solved.ipynb) | Connects covariance and conditional distributions to denoising intuition. |
| [2D Gaussian score field](./notebooks/w05_2d_gaussian_score_field_solved.ipynb) | Shows the score as a vector field pointing toward higher-density regions. |

---

## 🛠️ Tech Stack & Setup

This project uses **[`uv`](https://github.com/astral-sh/uv)** for fast, reproducible Python environment management.

```bash
# Install dependencies
uv sync

# Run a notebook
uv run jupyter lab

```

---

## 📁 Structure

- `notes/`: Weekly markdown files summarizing key math/theory.
- `notebooks/`: Practical simulations, Stat110 exercises, and toy models.
- `proofs/`: Clean, written solutions to Strategic Practice Problems.
- `mini_projects/`: Code and reports for monthly milestones.
- `papers/`: [Paper Radar](./papers/README.md) for optional future reading, plus paper summaries and derivations.
- `sources/`: Provenance catalogs and local, potentially gitignored copies of third-party references.

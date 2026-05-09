# Diffusion Research Curriculum

**Diffusion from First Principles — a working research notebook.**

A 12-month path from probability foundations to diffusion, score-based models, SDEs, and flow matching, with proofs, notebooks, and implementations.

## 📍 The Curriculum

The full, 52-week study plan is documented in **[CURRICULUM.md](./CURRICULUM.md)**. Portfolio-ready outputs are tracked in **[MILESTONES.md](./MILESTONES.md)**.

It is divided into five phases:

1. **Probability Core** (Current Phase)
2. **Generative Basics** (VAEs & Flows)
3. **Diffusion in Depth** (DDPM/DDIM)
4. **The SDE View** (Score-based models)
5. **Research & Replication** (Paper reproductions)

---

## 🚀 Current Progress

- **Phase:** 1 (Probability Core)
- **Week:** 6 — Transformations + KL Divergence 🔄
- **Completed:** Weeks 1-5 (through joint distributions, covariance, conditional Gaussians, and 2D Gaussian scores)
- **Next Milestone:** Complete Week 6 core artifacts (`w06_kl_gaussians.ipynb` + KL intuition note)

See **[PROGRESS.md](./PROGRESS.md)** for detailed task tracking.

---

## Best Artifacts

| Artifact | Why it matters |
| --- | --- |
| [Checkpoint 01 - Conditioning in Code](./mini_projects/checkpoint_01_conditioning_in_code/) | Shows how conditioning changes the probability model, verified with Monte Carlo. |
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
- `papers/`: Summaries and key derivations from core research papers.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a 12-month self-study curriculum for learning diffusion models, score-based generative models, and flow matching. The curriculum progresses from probability foundations through implementation of production-level generative AI.

## Commands

```bash
# Install dependencies
uv sync

# Run Jupyter notebooks
uv run jupyter lab

# Run Python scripts
uv run python <script.py>
```

## Repository Structure

- `notes/` - Weekly markdown summaries (1-2 pages each)
- `notebooks/` - Jupyter notebooks for simulations, exercises, and toy models
- `proofs/` - Clean solutions to selected problems
- `mini_projects/` - Monthly checkpoint projects with reports
- `papers/` - Paper summaries and key derivations

## Markdown LaTeX Style (GitHub-safe)

- Use inline math as `$...$` for equations in prose and list items.
- Do not use inline `$$...$$`.
- Use display math only as standalone blocks with opening/closing `$$` on their own lines.
- Inside list items, keep equations inline when possible; for long/complex equations, place a standalone display block outside the list.
- Keep `\begin{cases}` and `\begin{aligned}` in standalone display math blocks (not inline).

## Curriculum Phases

1. **Phase 1 (Weeks 1-8)**: Probability core (Stat110) + minimal diffusion toys
2. **Phase 2 (Weeks 9-16)**: Linear algebra + VAE/flows + first diffusion training
3. **Phase 3 (Weeks 17-28)**: DDPM/DDIM/CFG implementation and ablations
4. **Phase 4 (Weeks 29-40)**: SDE/ODE view + flow matching
5. **Phase 5 (Weeks 41-52)**: Paper reproduction + portfolio

## Key Technical Context

- Python 3.11+ required
- Uses `uv` for environment management (not pip/conda)
- Weekly artifacts include: theory notes, problem solutions, and code notebooks
- Every week includes "diffusion contact" (45-60 min of diffusion-related work)
- Notebooks typically use 2D blob data (mixture of Gaussians) for toy experiments

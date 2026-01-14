# Diffusion Research Curriculum

A structured, year-long deep dive from **foundational probability** to **Stochastic Differential Equations (SDEs)** and **Flow Matching**. This repository tracks my progress through a self-imposed curriculum designed to bridge the gap between academic theory and production-level generative AI.

## 📍 The Curriculum

The full, 52-week study plan is documented in **[CURRICULUM.md](./CURRICULUM.md)**.

It is divided into five phases:

1. **Probability Core** (Current Phase)
2. **Generative Basics** (VAEs & Flows)
3. **Diffusion in Depth** (DDPM/DDIM)
4. **The SDE View** (Score-based models)
5. **Research & Replication** (Paper reproductions)

---

## 🚀 Current Progress

- **Phase:** 1 (Probability Core)
- **Target:** Week 8 — Stat110 Lectures 7 & 8 (Gambler's Ruin, RVs & Distributions)
- **Next Milestone:** [Checkpoint 02] Toy Score Matching on 2D Blobs.

---

## 🛠️ Tech Stack & Setup

This project uses **[`uv`](<https://www.google.com/search?q=%5Bhttps://github.com/astral-sh/uv%5D(https://github.com/astral-sh/uv)>)** for fast, reproducible Python environment management.

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

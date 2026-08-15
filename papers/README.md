# Papers

Paper summaries and derivations. One note per paper, filename aligned with the paper name.

This folder is the **parallel track**: it runs alongside the weekly curriculum rather than
waiting for Phase 5. The foundations track tells you what you can verify; this track tells
you what is open. Both are needed, and the second one takes just as long to develop.

Target cadence: **one paper every two weeks**, at whatever pass depth is honest.
A pass-1 note is a complete artifact under Rule 1. An unread paper is not.

---

## How to read (three passes)

**Pass 1 — What and why (~30 min).** Abstract, figures, results. What problem, what claim,
what evidence. Works on any paper regardless of your current math.

**Pass 2 — The load-bearing equation.** Find the one result the paper turns on. Write down
what you would need in order to verify it. This is where the reading list for the
foundations track comes from — it is Rule 3 (just-in-time math) sourced from a real need.

**Pass 3 — Verification.** Actually check the derivation. Only for papers where you can.
Skipping pass 3 is normal and is not a failure.

### On unfamiliar background

In a pass-1 read, **unfamiliar background is context until proven otherwise.** The test:
does the unfamiliar thing appear in the paper's *result*, or only in its *motivation*?
If it lives in the intro or related-work section, keep reading. If it appears inside the
main derivation, stop and get the minimum version of it.

---

## Status

| Paper | Tier | Pass reached | Note |
| --- | --- | --- | --- |
| Vincent (2011), Denoising Score Matching | 1 | — | [`vincent2011_denoising_score_matching.md`](vincent2011_denoising_score_matching.md) |

---

## Backlog

### Tier 1 — reachable with Weeks 1-8 math

Gaussian identities, conditioning, KL between Gaussians, conditional expectation, MVN.

| Paper | Why now | Connects to |
| --- | --- | --- |
| **Vincent (2011)**, A Connection Between Score Matching and Denoising Autoencoders. *Neural Computation* 23(7):1661-1674 | 14 pages, entirely Gaussian algebra you own. The result `checkpoint_02` tested empirically without knowing it existed. | `mini_projects/checkpoint_02_toy_score_matching/`, blog post *Two Ways to Learn the Same Score Field* |
| **Ho, Jain & Abbeel (2020)**, Denoising Diffusion Probabilistic Models. [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) — sections 2 and 3 only | You have every ingredient: closed-form forward marginal, reparameterization, Gaussian posterior, KL between Gaussians. Section 3.2 is where noise-prediction drops out. Skip Appendix B. | `notes/w02_expectation_toolkit.md`, `notebooks/w06_kl_gaussians_solved.ipynb`, blog post *Sampling Our Way Down* |
| **Song & Ermon (2019)**, Generative Modeling by Estimating Gradients of the Data Distribution. [arXiv:1907.05600](https://arxiv.org/abs/1907.05600) | Motivates *why* multiple noise levels are needed. Early figures are 2D toy distributions — same setting as Week 5. Langevin is stated, not derived, which suits the current level. | `notes/w05_2d_gaussian_score.md`, blog post *When the Score Does Not Point Straight to the Mean* |

### Tier 2 — small stretch, good pass-2 targets

| Paper | Why | Blocked on |
| --- | --- | --- |
| **Luo (2022)**, Understanding Diffusion Models: A Unified Perspective. [arXiv:2208.11970](https://arxiv.org/abs/2208.11970) | Shows every ELBO step explicitly rather than waving at them. The most direct route to the variational bound, which is the main gap between here and all of DDPM. | Nothing hard — Jensen is in `notes/w08_stat110_inequalities.md` |
| **Song, Meng & Ermon (2020)**, Denoising Diffusion Implicit Models. [arXiv:2010.02502](https://arxiv.org/abs/2010.02502) | Non-Markovian forward process, deterministic sampling. Math is Gaussian conditioning. No SDEs. | Planned milestone `ddim_sampler_comparison` |
| **Nichol & Dhariwal (2021)**, Improved DDPM. [arXiv:2102.09672](https://arxiv.org/abs/2102.09672) | Mostly empirical — cosine schedule, learned variances, ablations. Read partly as a *template* for the Phase 3 Checkpoint 4 ablation report. | Nothing |
| **Hyvärinen (2005)**, Estimation of Non-Normalized Statistical Models by Score Matching. *JMLR* 6:695-709 | The original score matching, and the Hessian-trace form that Vincent's result replaces. Read after Vincent, for contrast. | Nothing hard |

### Tier 3 — pass 1 only until Phase 4

Read the abstract, figures, and claims. Write down precisely which machinery blocks you.
Do not attempt to verify these yet.

| Paper | Revisit at |
| --- | --- |
| **Sohl-Dickstein et al. (2015)**, Deep Unsupervised Learning using Nonequilibrium Thermodynamics. [arXiv:1503.03585](https://arxiv.org/abs/1503.03585) — §2.1 is the small-step argument already derived in the *Sampling Our Way Down* post | Partly readable now; full paper Phase 3 |
| **Anderson (1982)**, Reverse-Time Diffusion Equation Models. [doi:10.1016/0304-4149(82)90051-5](https://doi.org/10.1016/0304-4149(82)90051-5) | Phase 4 (Weeks 29-34) |
| **Song et al. (2021)**, Score-Based Generative Modeling through SDEs. [arXiv:2011.13456](https://arxiv.org/abs/2011.13456) | Phase 4 (Weeks 33-34) |
| **Lipman et al. (2023)**, Flow Matching for Generative Modeling. [arXiv:2210.02747](https://arxiv.org/abs/2210.02747) | Phase 4 (Weeks 35-36) |
| **Karras et al. (2022)**, Elucidating the Design Space of Diffusion Models. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364) | Engineering content readable now; notation assumes the SDE view. Low priority |

---

## Historical map

Useful for placing any paper you pick up. Diffusion has **two ancestries** that only merged
around 2020-21, which is why the same identities appear in two different notations.

| Year | Work | Added |
| --- | --- | --- |
| 1982 | Anderson | A diffusion SDE run backwards is also a diffusion SDE, with the score in its drift |
| 2005 | Hyvärinen | How to fit a model by matching scores, dodging the partition function |
| 2011 | Vincent | Denoising with Gaussian noise is score matching. Makes score learning cheap |
| 2015 | Sohl-Dickstein et al. | The generative framing: destroy structure forward, learn the reverse, sample |
| 2019 | Song & Ermon | Score matching at **many** noise levels, plus annealed Langevin |
| 2020 | Ho et al. | Simplified objective, noise-prediction, image quality |
| 2021 | Song et al. | Unifies both lineages; applies Anderson's reversal |

- **Lineage A** (score / energy-based): Hyvärinen → Vincent → Song & Ermon
- **Lineage B** (variational / thermodynamic): Sohl-Dickstein → Ho

The gap between "the math exists" and "the thing works" was roughly nine years, and it was
closed by synthesis and engineering rather than new mathematics. Anderson's reversal sat
unused in the stochastic-processes literature for decades because nobody in ML was reading
it. The openings were at the **seams between literatures**.

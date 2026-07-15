# Progress Tracker

## Current Status

- **Phase:** 1 (Probability Core)
- **Week:** 8 🔄
- **Started:** 2025-01-14
- **Week 1 Completed:** 2025-01-19
- **Week 2 Completed:** 2025-01-23
- **Week 3 Completed:** 2025-01-31
- **Week 4 Completed:** 2026-02-26
- **Week 5 Completed:** 2026-05-07
- **Week 6 Completed:** 2026-06-02
- **Week 7 Completed:** 2026-06-23

---

## Phase 1 — Probability Core + Minimal Diffusion Toys

### Week 1 — Random Variables + First Diffusion Toy ✅

| Task                                  | Status | Date       | Notes                                    |
| ------------------------------------- | ------ | ---------- | ---------------------------------------- |
| S1: Lecture 7 (Gambler's Ruin, RVs)   | ✅     | 2025-01-14 |                                          |
| S1: Lecture 8 (RV Distributions)      | ✅     | 2025-01-19 | Bernoulli, Binomial, Hypergeometric      |
| S2: Problems (PMF/CDF basics)         | ✅     | 2025-01-19 | 3 problems: conditioning, Bin sums, ruin |
| S3: `w01_forward_noising_blobs.ipynb` | ✅     | 2025-01-19 | Linear vs geometric schedules            |
| Diffusion: sigma(t) schedules         | ✅     | 2025-01-19 | Comparison figure generated              |

### Week 2 — Expectation Mastery ✅

| Task                                            | Status | Date       | Notes                                             |
| ----------------------------------------------- | ------ | ---------- | ------------------------------------------------- |
| S1: Lecture 9 (Expectation, Indicators)         | ✅     | 2025-01-19 | CDF, linearity, indicators                        |
| S1: Lecture 10 (Expectation Continued)          | ✅     | 2025-01-20 | Linearity proof, NegBin, St. Petersburg           |
| S2: Problems (LOTUS, variance)                  | ✅     | 2025-01-23 | 5 problems in `proofs/w02_stat110_expectation.md` |
| S3: `w02_expectation_toolkit.md`                | ✅     | 2025-01-23 | Patterns + distributions reference                |
| Diffusion: $E[x_t \mid x_0], Var(x_t \mid x_0)$ | ✅     | 2025-01-23 | Derived + verified in `w02_forward_moments.ipynb` |

### Week 3 — Continuous Distributions + The Normal ✅

| Task                                  | Status | Date       | Notes                                                       |
| ------------------------------------- | ------ | ---------- | ----------------------------------------------------------- |
| S1: Lecture 12 (Continuous, Uniform)  | ✅     | 2025-01-26 | PDF, CDF, Uniform, LOTUS, inverse CDF                       |
| S1: Lecture 13 (Normal Distribution)  | ✅     | 2025-01-27 | Inverse CDF, Normal PDF, mean/variance                      |
| S2: Problems (PDF/CDF, Normal)        | ✅     | 2025-01-27 | 4 problems solved in `w03_stat110_continuous_normal.md`     |
| S3: `w03_gaussian_properties.ipynb`   | ✅     | 2025-01-31 | 5 checkpoints: PDF, CDF, linear transform, sums, 68-95-99.7 |
| Diffusion: `w03_score_of_gaussian.md` | ✅     | 2025-01-31 | Score derivation + verification notebook                    |

### Week 4 (Checkpoint 1) — LOTUS + Conditioning Mastery ✅

| Task                                                  | Status | Date       | Notes                                            |
| ----------------------------------------------------- | ------ | ---------- | ------------------------------------------------ |
| S1: Lecture 14 (LOTUS)                                | ✅     | 2026-02-02 | Notes in `notes/w04_stat101_normal_loc_scale.md` |
| S1: Review Lectures 4–6 (conditioning)                | ✅     | 2026-02-02 | Completed review (no separate artifact)          |
| S2: Mixed problems (Lecture 14 + conditioning review) | ✅     | 2026-02-02 | Completed in `proofs/w04_stat110_lotus_conditioning.md` |
| S3: `checkpoint_01_conditioning_in_code/`             | ✅     | 2026-02-26 | Completed analysis in `mini_projects/checkpoint_01_conditioning_in_code/analysis.md` |
| Diffusion: `w04_conditioning_in_diffusion.md`         | ✅     | 2026-02-26 | Derivations, empirical check, and reflection completed |

### Week 5 — Joint Distributions + Covariance

| Task                                 | Status | Date | Notes |
| ------------------------------------ | ------ | ---- | ----- |
| S1: Lecture 19 (Joint distributions) | ✅     | 2026-03-13 | Notes in `notes/w05_stat110_joint_conditional_marginal.md` |
| S1: Lecture 21 (Covariance)          | ✅     | 2026-03-13 | Notes in `notes/w05_stat110_covariance_correlation.md` |
| S2: Problems (joint, covariance)     | ✅     | 2026-04-28 | Completed in `proofs/w05_stat110_joint_conditional_marginal_covariance_correlation.md` |
| S3: `w05_joint_gaussians.ipynb`      | ✅     | 2026-05-07 | Solved notebook executes; optional Plotly explorer in `notebooks/w05_bivariate_gaussian_explorer.html` |
| Diffusion: 2D score vector field     | ✅     | 2026-05-07 | Completed note and solved notebook; analytic score verified against finite differences |

### Week 6 — Transformations + KL Divergence

| Task                                 | Status | Date | Notes |
| ------------------------------------ | ------ | ---- | ----- |
| S1: Lecture 22 (Transformations)     | ✅     | 2026-05-11 | Notes in `notes/w06_stat110_transformations_convolutions.md`; intuition artifact in `notebooks/w06_change_of_variables_intuition_artifact.html` |
| S2: Problems (change of variables)   | ✅     | 2026-05-27 | Completed in `proofs/w06_stat110_transformations_convolutions.md`; source-verified book comparisons, intuition notes, and memory cards included |
| S3: `w06_kl_gaussians.ipynb`         | ✅     | 2026-06-02 | Solved notebook completed and executed; analytic KL, Monte Carlo estimate, histogram estimate, sensitivity plot, and reflection included |
| Diffusion: `w06_where_kl_appears.md` | ✅     | 2026-06-02 | Completed one-page bridge note connecting KL, variational objectives, transformations, and diffusion/flow distribution matching |

### Week 7 — Conditional Expectation + Inequalities

| Task                                              | Status | Date | Notes |
| ------------------------------------------------- | ------ | ---- | ----- |
| S1: Lecture 26 (Conditional Expectation)          | ✅     | 2026-06-08 | Notes in `notes/w07_stat110_conditional_expectation.md`; includes the Lecture 25 preview |
| S1: Lecture 27 ($E[Y \mid X=x]$)                  | ✅     | 2026-06-08 | Notes in `notes/w07_stat110_conditional_expectation_given_rv.md` |
| S2: Problems (tower property)                     | ✅     | 2026-06-16 | Completed in `proofs/w07_stat110_conditional_expectation.md`; 4 selected problems with source-verified book comparisons, correction notes, intuition notes, and memory cards |
| S3: `w07_conditional_expectation_in_diffusion.md` | ✅     | 2026-06-23 | Completed conceptual diffusion bridge: tower property, MSE-optimal denoising, and Gaussian score identity |

### Week 8 (Checkpoint 2) — CLT + Toy Score Matching

| Task                                    | Status | Date | Notes |
| --------------------------------------- | ------ | ---- | ----- |
| S1: Lecture 28 (Inequalities)           | ✅     | 2026-06-24 | Notes in `notes/w08_stat110_inequalities.md` |
| S1: Lecture 29 (LLN, CLT)               | ✅     | 2026-06-29 | Notes in `notes/w08_stat110_lln_clt.md` |
| S1: Lecture 30 (MV Normal, skim)        | ✅     | 2026-06-30 | Notes in `notes/w08_stat110_chi_square_student_t_mvn.md` |
| S2: Mini-exam (6 problems)              | ✅     | 2026-07-15 | Completed in two sittings; reviewed solutions in `proofs/phase1_exam/w08_phase1_mini_exam.md` |
| S3: `checkpoint_02_toy_score_matching/` | ⬜     |      |       |

---

## Legend

- ⬜ Not started
- 🔄 In progress
- ✅ Completed
- ⏭️ Skipped (intentionally)

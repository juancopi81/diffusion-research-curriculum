# Progress Tracker

## Current Status

- **Phase:** 2 (Linear Algebra + Generative Modeling Basics)
- **Week:** 14 ✅ — completed 2026-10-27; Week 15 is next
- **Started:** 2025-01-14
- **Phase 1 Completed:** 2026-07-24
- **Week 9 Completed:** 2026-08-25
- **Week 10 Completed:** 2026-09-04
- **Week 11 Completed:** 2026-09-15
- **Week 12 Completed:** 2026-09-28
- **Week 13 Completed:** 2026-10-14
- **Week 14 Completed:** 2026-10-27
- **Next study step:** Week 15 — Bridge to diffusion math: the forward process
- **Week 14 closeout:** [Day 7 completion decision](notes/w14_study_plan.md#day-7-completion-decision); all four problems, study report, and final review complete; reference use and guided corrections recorded; blog editing continues separately

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

### Week 5 — Joint Distributions + Covariance ✅

| Task                                 | Status | Date | Notes |
| ------------------------------------ | ------ | ---- | ----- |
| S1: Lecture 19 (Joint distributions) | ✅     | 2026-03-13 | Notes in `notes/w05_stat110_joint_conditional_marginal.md` |
| S1: Lecture 21 (Covariance)          | ✅     | 2026-03-13 | Notes in `notes/w05_stat110_covariance_correlation.md` |
| S2: Problems (joint, covariance)     | ✅     | 2026-04-28 | Completed in `proofs/w05_stat110_joint_conditional_marginal_covariance_correlation.md` |
| S3: `w05_joint_gaussians.ipynb`      | ✅     | 2026-05-07 | Solved notebook executes; optional Plotly explorer in `notebooks/w05_bivariate_gaussian_explorer.html` |
| Diffusion: 2D score vector field     | ✅     | 2026-05-07 | Completed note and solved notebook; analytic score verified against finite differences |

### Week 6 — Transformations + KL Divergence ✅

| Task                                 | Status | Date | Notes |
| ------------------------------------ | ------ | ---- | ----- |
| S1: Lecture 22 (Transformations)     | ✅     | 2026-05-11 | Notes in `notes/w06_stat110_transformations_convolutions.md`; intuition artifact in `notebooks/w06_change_of_variables_intuition_artifact.html` |
| S2: Problems (change of variables)   | ✅     | 2026-05-27 | Completed in `proofs/w06_stat110_transformations_convolutions.md`; source-verified book comparisons, intuition notes, and memory cards included |
| S3: `w06_kl_gaussians.ipynb`         | ✅     | 2026-06-02 | Solved notebook completed and executed; analytic KL, Monte Carlo estimate, histogram estimate, sensitivity plot, and reflection included |
| Diffusion: `w06_where_kl_appears.md` | ✅     | 2026-06-02 | Completed one-page bridge note connecting KL, variational objectives, transformations, and diffusion/flow distribution matching |

### Week 7 — Conditional Expectation + Inequalities ✅

| Task                                              | Status | Date | Notes |
| ------------------------------------------------- | ------ | ---- | ----- |
| S1: Lecture 26 (Conditional Expectation)          | ✅     | 2026-06-08 | Notes in `notes/w07_stat110_conditional_expectation.md`; includes the Lecture 25 preview |
| S1: Lecture 27 ($E[Y \mid X=x]$)                  | ✅     | 2026-06-08 | Notes in `notes/w07_stat110_conditional_expectation_given_rv.md` |
| S2: Problems (tower property)                     | ✅     | 2026-06-16 | Completed in `proofs/w07_stat110_conditional_expectation.md`; 4 selected problems with source-verified book comparisons, correction notes, intuition notes, and memory cards |
| S3: `w07_conditional_expectation_in_diffusion.md` | ✅     | 2026-06-23 | Completed conceptual diffusion bridge: tower property, MSE-optimal denoising, and Gaussian score identity |

### Week 8 (Checkpoint 2) — CLT + Toy Score Matching ✅

| Task                                    | Status | Date | Notes |
| --------------------------------------- | ------ | ---- | ----- |
| S1: Lecture 28 (Inequalities)           | ✅     | 2026-06-24 | Notes in `notes/w08_stat110_inequalities.md` |
| S1: Lecture 29 (LLN, CLT)               | ✅     | 2026-06-29 | Notes in `notes/w08_stat110_lln_clt.md` |
| S1: Lecture 30 (MV Normal, skim)        | ✅     | 2026-06-30 | Notes in `notes/w08_stat110_chi_square_student_t_mvn.md` |
| S2: Mini-exam (6 problems)              | ✅     | 2026-07-15 | Completed in two sittings; reviewed solutions in `proofs/phase1_exam/w08_phase1_mini_exam.md` |
| S3: `checkpoint_02_toy_score_matching/` | ✅     | 2026-07-24 | Completed Nano-Diffusion v0 comparison, exact MoG evaluation, vector fields, and `report.md` |

---

## Phase 2 — Linear Algebra Refresh + Generative Modeling Basics

### Week 9 — Linear Algebra Essentials ✅

| Task                                      | Status | Date       | Notes |
| ----------------------------------------- | ------ | ---------- | ----- |
| S1: Selected MML Ch. 2–4                  | ✅     | 2026-08-18 | Consolidated linear algebra, geometry, eigendecomposition, SVD, and approximation in `notes/w09_mml_linear_algebra.md` |
| S2: Selected MML exercises                | ✅     | 2026-08-19 | Reviewed solutions in `proofs/w09_mml_linear_algebra.md`, including the four curriculum exercises, optional Exercise 4.10, and additional foundation practice |
| S3: `w09_pca_svd.ipynb`                   | ✅     | 2026-08-25 | Solved notebook executes top-to-bottom; one component retained 96.3% of variance and two reconstructed to floating-point precision |
| Diffusion: linear algebra in architectures | ✅     | 2026-08-25 | Connected linear maps, nonlinear blocks, latent compression, low-rank intuition, and LoRA in `notes/w09_linear_algebra_in_unets.md` |

---

### Week 10 — Multivariate Gaussian + Score ✅

| Task | Status | Date | Notes |
| --- | --- | --- | --- |
| S1: MML gradients and multivariate Gaussians | ✅ | 2026-09-04 | Consolidated gradient conventions, affine transformations, covariance geometry, and sampling in [the Week 10 note](notes/w10_mml_multivariate_gaussian.md) |
| S2: Gaussian score and conditioning | ✅ | 2026-09-04 | Derived the analytic score and block conditional; completed the shared 2D example and normalized-slice visualization in [the Week 10 proof](proofs/w10_multivariate_gaussian_score.md) |
| S3: multivariate Gaussian notebook | ✅ | 2026-09-04 | The [solved notebook](notebooks/w10_mv_gaussian_score_solved.ipynb) executes top-to-bottom; Cholesky moments, analytic versus finite-difference score, and empirical conditional moments agree |
| Diffusion: Gaussian identities | ✅ | 2026-09-04 | Extended the [Gaussian identities sheet](notes/gaussian_identities.md) through the DDPM forward-kernel score |

---

### Week 11 — VAE Foundations ✅

| Task | Status | Date | Notes |
| --- | --- | --- | --- |
| S1: CS236 VAE foundations | ✅ | 2026-09-09 | Lectures 5–6, amortized inference, ELBO interpretation, and reparameterization consolidated in [the foundations note](notes/w11_cs236_vae.md) |
| S2: ELBO and Gaussian derivations | ✅ | 2026-09-14 | Two ELBO derivations, scalar and diagonal Gaussian KL, reparameterization proof, and loss mapping in [the derivation note](notes/w11_elbo_derivation.md) |
| S3: minimal MNIST VAE | ✅ | 2026-09-15 | [Solved notebook](notebooks/w11_minimal_vae_mnist_solved.ipynb): three implementations, checks, five-epoch training, plots, and reviewed observations completed |
| Diffusion: why latent diffusion | ✅ | 2026-09-15 | Reviewed [one-page bridge](notes/w11_why_latent_diffusion.md): PCA → PPCA → VAE, compression tradeoffs, and the separate roles of the autoencoder and latent diffusion |

---

### Week 12 — Normalizing Flows ✅

| Task | Status | Date | Notes |
| --- | --- | --- | --- |
| S1: CS236 flow foundations | ✅ | 2026-09-24 | Change of variables, Jacobians, affine coupling, and layer composition in [the foundations note](notes/w12_cs236_normalizing_flows.md) |
| S2: change-of-variables derivations | ✅ | 2026-09-24 | Worked examples, inverse maps, and coupling log-determinants in [the proof note](proofs/w12_change_of_variables_flows.md) |
| S3: RealNVP on 2D blobs | ✅ | 2026-09-28 | [Solved notebook](notebooks/w12_realnvp_2d_blobs_solved.ipynb): implementation checks, six-layer NLL and samples, and one-layer failure comparison |
| Diffusion: flows versus score models | ✅ | 2026-09-28 | Reviewed [comparison note](notes/w12_flows_vs_diffusion.md): exact model likelihood, score prediction, and generation paths |

---

### Week 13 — Optimization Basics ✅

| Task | Status | Date | Notes |
| --- | --- | --- | --- |
| S1: MML §7.1 and Adam foundations | ✅ | 2026-10-14 | [Optimization note](notes/w13_optimization.md): geometry, learning rate, momentum, stochastic gradients, Adam, three-model review, and instability checkpoint consolidated |
| S2: optimizer-update derivations | ✅ | 2026-10-14 | [Proof note](proofs/w13_optimizer_updates.md): first two GD, momentum, and Adam updates, coordinate recurrences, and bias correction finalized |
| S3: optimizer comparison notebook | ✅ | 2026-10-12 | [Solved notebook](notebooks/w13_optimizers_sanity_solved.ipynb): implementations, hand-calculation checks, trajectories, losses, gradient norms, divergence, and learning-rate grids reviewed |
| Diffusion: controlled score-training clipping | ✅ | 2026-10-14 | [Stability note](notes/w13_training_stability_for_diffusion.md): matched experiment reviewed on 2026-10-13; clipping activated 20/20 times but gave higher final held-out score MSE in this setting |

---

### Week 14 (Checkpoint 3) — Generative Modeling Toolkit Consolidation ✅

The [Day 1 diagnostic](notes/w14_study_plan.md#day-1-review-record) closed on
2026-10-19, [Day 2](notes/w14_study_plan.md#day-2-review-record) was reviewed on
2026-10-20, [Day 3](notes/w14_study_plan.md#day-3-review-record) on 2026-10-21,
[Day 4](notes/w14_study_plan.md#day-4-review-record) on 2026-10-22,
and [Day 5](notes/w14_study_plan.md#day-5-review-record) on 2026-10-23.
All four mixed problems and the VAE/flow/score evidence discussions are reviewed.
The [Day 6 manuscript draft](mini_projects/checkpoint_03_generative_toolkit_report/report.md)
was assembled and reviewed by the author on 2026-10-26; its
[draft record](notes/w14_study_plan.md#day-6-draft-record) closes Day 6's study
writing and records connections between sections for final blog editing.
[Day 7's review and corrections](notes/w14_study_plan.md#day-7-review-record)
closed the study checkpoint on 2026-10-27. Gaussian conditioning used a formula
reference; distinguishing the conditional mean clean point from the score
needed guidance and a follow-up application. Those consolidation points carry
into Week 15 without a claim of fluent unaided recall. Blog editing continues
separately. The proposed longer clipping comparison has not been run.

| Task | Status | Date | Notes |
| --- | --- | --- | --- |
| S1: review Weeks 9–13 | ✅ | 2026-10-23 | Bounded model, Gaussian, optimizer, and saved-evidence reviews completed; Day 7 rechecks completed on 2026-10-27 with reference use and guidance recorded |
| S2: four mixed problems | ✅ | 2026-10-23 | [Mixed set](proofs/w14_generative_toolkit_mixed_set.md): all four problems reviewed, including convergence cases, clipping interpretation, and a proposed controlled follow-up |
| S3: toolkit report | ✅ | 2026-10-26 | [Study draft](mini_projects/checkpoint_03_generative_toolkit_report/report.md), source README, and three saved figures assembled; author read-through completed; connections between sections remain for final blog editing |
| Final recall and corrections | ✅ | 2026-10-27 | [Review record](notes/w14_study_plan.md#day-7-review-record): fresh Gaussian/flow checks and VAE/score/clipping explanations completed; Gaussian lookup and guided score correction retained as consolidation points |
| Diffusion: explain the score-model connection | ✅ | 2026-10-27 | Forward corruption, training targets, missing multiple noise levels and sampler explained; feedback clarified noise-level conditioning and fixed model weights during sampling |

---

## Legend

- ⬜ Not started
- 🔄 In progress
- ✅ Completed
- ⏭️ Skipped (intentionally)

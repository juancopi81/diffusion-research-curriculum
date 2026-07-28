# 12-Month Curriculum: Probability → Diffusion / Score / Flow Matching (3 sessions/week)

Goal: become a strong “paper-reading + implementation” researcher/practitioner in diffusion / score-based / flow-matching models in ~12 months (≤24 months max), by combining:

- just-enough math foundations (probability + linear algebra + SDE intuition)
- continuous contact with diffusion concepts from Week 1
- steady artifacts (notes + proofs + code) that compound
- a recurring **Nano-Diffusion / Nano-Flow** research spine where each implementation improves the same small system

---

## 0) Canonical resource index (free unless marked)

Use these short tags throughout the plan.

### Probability + proofs (Phase 1 backbone)

- **[Stat110-YT]** Stat110 full lecture playlist:  
  [https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)
- **[Stat110-Practice]** Strategic Practice Problems + HW sets (contains problems + solutions):  
  [https://stat110.hsites.harvard.edu/strategic-practice-problems](https://stat110.hsites.harvard.edu/strategic-practice-problems)
- **[Stat110-Text]** Stat110 online textbook (Blitzstein & Hwang):  
  [https://projects.iq.harvard.edu/stat110/book](https://projects.iq.harvard.edu/stat110/book)
- **[BoP]** Book of Proof (Hammack, free PDF):  
  [https://richardhammack.github.io/BookOfProof/Main.pdf](https://richardhammack.github.io/BookOfProof/Main.pdf)
- **[MIT-6042]** Mathematics for Computer Science (MIT 6.042J OCW notes + assignments):
  [https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/)  
  Video playlist: [https://www.youtube.com/playlist?list=PLB7540DEDD482705B](https://www.youtube.com/playlist?list=PLB7540DEDD482705B)

### Linear algebra + optimization (Phase 2 backbone)

- **[MML-Book]** Mathematics for Machine Learning (free PDF):  
  [https://mml-book.github.io/book/mml-book.pdf](https://mml-book.github.io/book/mml-book.pdf)
- **[MIT-1806]** MIT 18.06 Linear Algebra (optional, for intuition/drills):  
  [https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- **[Adam]** Kingma & Ba, “Adam: A Method for Stochastic Optimization”:
  [https://arxiv.org/abs/1412.6980](https://arxiv.org/abs/1412.6980)

### Deep generative models (VAE/Flows/Diffusion theory support)

- **[CS236-Site]** Stanford CS236 course site + syllabus + slides/notes:  
  [https://deepgenerativemodels.github.io/](https://deepgenerativemodels.github.io/)  
  Syllabus with topic-by-week: [https://deepgenerativemodels.github.io/syllabus.html](https://deepgenerativemodels.github.io/syllabus.html)
- **[CS236-YT]** Stanford CS236 YouTube playlist (2023):  
  [https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8](https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8)

### Diffusion / score resources (implementation + literacy)

- **[HF-DiffCourse]** Hugging Face Diffusion Course (hands-on, free):  
  [https://huggingface.co/learn/diffusion-course](https://huggingface.co/learn/diffusion-course)
- **[HF-DiffCourse-Code]** Source notebooks for the Hugging Face Diffusion Course:
  [https://github.com/huggingface/diffusion-models-class](https://github.com/huggingface/diffusion-models-class)
- **[HF-AnnotatedDiff]** “Annotated Diffusion” blog (walkthrough + code):  
  [https://huggingface.co/blog/annotated-diffusion](https://huggingface.co/blog/annotated-diffusion)
- **[Diffusers-Docs]** Hugging Face Diffusers docs:  
  [https://huggingface.co/docs/diffusers/index](https://huggingface.co/docs/diffusers/index)
- **[Song-Tut]** Yang Song’s score-based tutorial hub:  
  [https://yang-song.net/blog/2021/score/](https://yang-song.net/blog/2021/score/)
- **[Weng]** Lilian Weng blog (useful for intuition + summaries):  
  [https://lilianweng.github.io/](https://lilianweng.github.io/)

### Flow matching / ODE/SDE view (Phase 4 backbone)

- **[MIT-6S184]** MIT course “Flow Matching and Diffusion Models” (notes + lectures + labs):  
  [https://diffusion.csail.mit.edu/](https://diffusion.csail.mit.edu/)
- **[MIT-6S184-Notes]** Direct lecture notes PDF:  
  [https://diffusion.csail.mit.edu/lecture-notes.pdf](https://diffusion.csail.mit.edu/lecture-notes.pdf)

### Core papers (open access)

- **[DDPM]** Ho et al. “Denoising Diffusion Probabilistic Models”: [https://arxiv.org/abs/2006.11239](https://arxiv.org/abs/2006.11239)
- **[DDIM]** Song et al. “Denoising Diffusion Implicit Models”: [https://arxiv.org/abs/2010.02502](https://arxiv.org/abs/2010.02502)
- **[ScoreSDE]** Song et al. “Score-Based Generative Modeling through SDEs”: [https://arxiv.org/abs/2011.13456](https://arxiv.org/abs/2011.13456)
- **[FlowMatching]** Lipman et al. “Flow Matching for Generative Modeling”: [https://arxiv.org/abs/2210.02747](https://arxiv.org/abs/2210.02747)
- **[RectifiedFlow]** (rectified flow line of work; pick a canonical arXiv paper you like and pin it here once chosen)

### SDE numerics (free references)

- **[Higham-SDE]** Higham “An Algorithmic Introduction to Numerical Simulation of SDEs” (PDF):  
  [https://www.maths.ed.ac.uk/~dhigham/Publications/Papers/sdes.pdf](https://www.maths.ed.ac.uk/~dhigham/Publications/Papers/sdes.pdf)
- **[SarkkaSolin]** Särkkä & Solin “Applied Stochastic Differential Equations” (PDF/notes):  
  [https://users.aalto.fi/~asolin/sde-book/sde-book.pdf](https://users.aalto.fi/~asolin/sde-book/sde-book.pdf)
- **[MIT-18445]** MIT 18.445 Stochastic Processes (OCW):  
  [https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/](https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/)

> Rule: if a link breaks, replace it with an equivalent official mirror and update README (don’t stall the curriculum).

---

## You are here (completed)

You already finished up to:

**Stat110**

- Lectures 1–6 (probability fundamentals, conditioning, Monty Hall, Simpson's Paradox)
- Lecture 7 (Gambler's Ruin and Random Variables) + exercises

So you are ready to continue with:

- Finish Lecture 8 (Random Variables and Their Distributions)
- Complete Week 1 artifact (forward noising notebook)
- Start minimal diffusion contact immediately

---

## Rules of the game (so you don’t get stuck in prerequisites)

1. **Every week produces an artifact** (a note, a proof write-up, or a runnable notebook).
2. **Diffusion contact every week** (minimum 45 minutes) from Week 1 onward.
3. **Math is “just in time”**: learn enough to understand a derivation you need _now_.
4. **Checkpoints matter more than coverage**: you can skip/trim content if artifacts keep moving.
5. **One canonical repo** where everything lives.
6. **One cumulative implementation spine**: when an artifact touches diffusion, score models, samplers, or flow matching, prefer extending the Nano-Diffusion/Nano-Flow spine over starting disconnected experiments.

---

## Nano-Diffusion / Nano-Flow spine

This curriculum has one recurring implementation leit motif:

> Build a tiny, readable, end-to-end diffusion/flow research system over time, in the spirit of a "nano" project: minimal code, reproducible runs, clear metrics, and short written results.

The spine evolves in stages:

- **Nano-Diffusion v0:** 2D blobs, forward noising, analytic scores, and toy score/noise prediction.
- **Nano-Diffusion v1:** tiny MNIST DDPM with one clean training loop, one sampling loop, fixed seeds, and sample grids.
- **Nano-Diffusion v2:** DDIM, schedule sweeps, guidance, and controlled ablations on top of the same baseline.
- **Nano-Flow v0:** flow matching on the same toy distributions used by Nano-Diffusion.
- **Nano-Flow v1:** small image-level flow matching compared against the diffusion baseline.

Start in notebooks while the idea is still exploratory. Once code is reused across weeks, graduate it into `mini_projects/nano_diffusion/` with shared modules, configs, experiment outputs, and a local `README.md`. Nano-Flow can begin inside the same project as a comparison track, then split only if it becomes cleaner.

Every serious run should leave a small result record:

- question or hypothesis
- config, seed, data, model size, schedule, sampler
- metrics: loss curve, analytic-target MSE when available, sampling steps/NFE, wall-clock time, sample grid or vector field
- failure notes
- one-paragraph conclusion and the next experiment

This spine does not replace proofs or paper reading. It is the implementation thread where each week's math gets tested against code.

---

## Weekly template (3 sessions/week)

**S1 (Theory | ~2h)**

- Watch/read lecture(s)
- Take short notes (1–2 pages max)
- Write 3–5 “active recall” questions (things you can re-derive/explain)

**S2 (Problems | ~2h)**

- 4–8 good problems (or 2–4 hard ones)
- Write solutions cleanly (correct + readable)

**S3 (Artifact | ~2h)**
Choose ONE:

- a proof write-up
- a code notebook
- a mini-derivation note tied to diffusion/score/flow matching

**Non-negotiable inside S3 (every week):**

- 45–60 min “Diffusion contact” (toy implementation / derivation / small reading)
- If the contact is implementation-heavy, connect it to Nano-Diffusion/Nano-Flow or record why it remains standalone.

---

## Repository structure (recommended)

- `notes/` (short markdown notes, 1–2 pages each)
- `proofs/` (clean solutions to selected problems)
- `notebooks/` (runnable experiments)
- `mini_projects/` (monthly checkpoints)
- `mini_projects/nano_diffusion/` (cumulative Nano-Diffusion/Nano-Flow code, configs, experiment logs, and reports once reuse begins)
- `papers/` (one-page summaries + “key derivation” per paper)
- `README.md` (links to milestones + how to run notebooks)

---

## Phases overview (12 months)

- **Phase 1 (Weeks 1–8): Probability core + minimal diffusion toys**
- **Phase 2 (Weeks 9–16): Linear algebra refresh + generative modeling basics (VAE/flows)**
- **Phase 3 (Weeks 17–28): Diffusion in depth (DDPM/DDIM/CFG), Nano-Diffusion baseline + ablations**
- **Phase 4 (Weeks 29–40): SDE/ODE view + Nano-Flow, compare the theories in code**
- **Phase 5 (Weeks 41–52): Paper pass + reproduction + portfolio (blog + OSS)**

---

# Phase 1 — Probability core + minimal diffusion toys (Weeks 1–8)

**Phase goal:** become fluent in (1) RV mechanics, (2) expectation/variance, (3) Gaussian identities, (4) conditioning,
while building "diffusion-adjacent" intuition every week.

> For Stat110 problems: use **[Stat110-Practice]** and pick the set matching your lecture/topic.

**Lectures covered:** 7–10, 12–14, 19, 21–22, 26–30 (15 lectures total, ~2/week)

**Lectures skipped (not essential for diffusion):** 11 (Poisson), 15 (Midterm Review), 16 (Exponential), 17–18 (MGFs), 20 (Multinomial/Cauchy), 23–24 (Beta/Gamma), 25 (Order Statistics)

### Week 1 — Random Variables + First Diffusion Toy

- S1 (~2h): **Stat110 Lectures 7–8** via **[Stat110-YT]**
  - Lecture 7: Gambler's Ruin and Random Variables
  - Lecture 8: Random Variables and Their Distributions (PMF, CDF)
- S2 (~2h): **[Stat110-Practice]** 6–8 problems on:
  - PMF/CDF basics
  - Computing probabilities for discrete RVs
  - Binomial, Geometric distributions
- S3 (~2h): `notebooks/w01_forward_noising_blobs.ipynb`
  - Generate 2D data (mixture of Gaussians "blobs")
  - Implement forward noising: `x_t = x_0 + sigma(t) * eps`
  - Plot histograms / scatter across t
  - Save 1 figure to `notes/figures/w01_*.png`

Diffusion contact (45–60 min):

- Implement `sigma(t)` schedules (linear + geometric) and compare how fast the distribution "washes out".

### Week 2 — Expectation Mastery

- S1 (~2h): **Stat110 Lectures 9–10** (**[Stat110-YT]**)
  - Lecture 9: Expectation, Indicator Random Variables, Linearity
  - Lecture 10: Expectation Continued (variance intro)
- S2 (~2h): **[Stat110-Practice]** 6–10 problems on:
  - LOTUS + "compute E[g(X)]"
  - Indicator variable tricks
  - Variance shortcuts: Var(aX+b), decomposition
- S3 (~2h): `notes/w02_expectation_toolkit.md`
  - A one-page "Expectation toolkit":
    - Linearity of expectation
    - Indicator method pattern
    - Symmetry argument pattern
    - Conditioning trick pattern ("condition on first thing that happens")

Diffusion contact (45–60 min):

- Derive and code-check `E[x_t|x_0]` and `Var(x_t|x_0)` for your forward noising model.

### Week 3 — Continuous Distributions + The Normal

- S1 (~2h): **Stat110 Lectures 12–13** (**[Stat110-YT]**)
  - Lecture 12: Discrete vs. Continuous, the Uniform
  - Lecture 13: Normal Distribution
- S2 (~2h): **[Stat110-Practice]** 6–10 problems on:
  - PDF/CDF relationships
  - Computing probabilities by integration
  - Normal distribution properties, standardization
- S3 (~2h): `notebooks/w03_gaussian_properties.ipynb`
  - Explore Gaussian properties computationally:
    - Plot PDF/CDF, verify area = 1
    - Demonstrate closure under linear transformation
    - Show sum of independent Gaussians is Gaussian
    - Visualize the "68-95-99.7 rule"

Diffusion contact (45–60 min):

- `notes/w03_score_of_gaussian.md`: compute the score of a Gaussian:
  - `∇_x log N(x; μ, σ²) = -(x - μ)/σ²`
  - Verify with finite differences on a grid

### Week 4 (Checkpoint 1) — LOTUS + Conditioning Mastery

- S1 (~1.5h): **Stat110 Lecture 14** (**[Stat110-YT]**)
  - Lecture 14: Location, Scale, and LOTUS
  - Review: conditioning concepts from Lectures 4–6
- S2 (~2h): 4–6 mixed problems from **[Stat110-Practice]**:
  - 2–3 on Lecture 14 topics (Location/Scale, standardization, LOTUS)
  - 2–3 **hard** conditioning review problems:
    - Bayes + LOTP
    - "Condition on a useful event / first step"
- S3 (~2h, Project): `mini_projects/checkpoint_01_conditioning_in_code/`
  - Pick 1 concrete problem (e.g., medical test Bayes, urns, gambler's ruin step)
  - Write:
    - `analysis.md` (clean derivation)
    - `simulate.py` (Monte Carlo)
    - `results.ipynb` (plots + comparison)

Diffusion contact (45–60 min):

- `notes/w04_conditioning_in_diffusion.md`:
  - 1 page: where conditioning shows up (Gaussian posterior, denoising as conditional expectation)

### Week 5 — Joint Distributions + Covariance

- S1 (~2h): **Stat110 Lectures 19, 21** (**[Stat110-YT]**)
  - Lecture 19: Joint, Conditional, and Marginal Distributions
  - Lecture 21: Covariance and Correlation
- S2 (~2h): **[Stat110-Practice]** 6–10 problems on:
  - Joint → marginal integration
  - Conditional density derivation
  - Computing covariance and correlation
- S3 (~2h): `notebooks/w05_joint_gaussians.ipynb`
  - Sample correlated 2D Gaussians from covariance matrix
  - Visualize conditional slices
  - Compute conditional mean analytically, verify empirically
  - Show: conditional of joint Gaussian is Gaussian
  - Optional visual supplement: `notebooks/w05_bivariate_gaussian_explorer.html` for interactive covariance, correlation, and conditional-slice intuition

Diffusion contact (45–60 min):

- Extend score computation to 2D Gaussian
- `∇_x log N(x; μ, Σ) = -Σ⁻¹(x - μ)`
- Visualize score as vector field

### Week 6 — Transformations + KL Divergence

- S1 (~1h): **Stat110 Lecture 22** (**[Stat110-YT]**)
  - Lecture 22: Transformations and Convolutions
- S2 (~2h): **[Stat110-Practice]** 6–8 problems on:
  - Change of variables (1D and 2D)
  - Jacobian computation
  - Simple transformations of known distributions
- S3 (~2h): `notebooks/w06_kl_gaussians.ipynb`
  - Derive KL divergence for 1D Gaussians analytically
  - Implement histogram-based KL estimate
  - Compare analytic vs empirical, show sensitivity to binning

Diffusion contact (45–60 min):

- `notes/w06_where_kl_appears.md`:
  - 1 page: KL in variational objectives, why "matching distributions" keeps showing up in diffusion/flow formulations.

### Week 7 — Conditional Expectation + Inequalities

- S1 (~2h): **Stat110 Lectures 26–27** (**[Stat110-YT]**)
  - Lecture 26: Conditional Expectation Continued
  - Lecture 27: Conditional Expectation Given an R.V.
- S2 (~2h): **[Stat110-Practice]** 6–8 problems on:
  - Computing E[Y|X] for various distributions
  - Tower property: E[E[Y|X]] = E[Y]
  - Conditional variance
- S3 (~2h): `notes/w07_conditional_expectation_in_diffusion.md`
  - Tower property: why we can compute E[x_0] by iterated conditioning
  - Denoising score matching: the score is related to E[x_0|x_t]
  - Connection: ∇_x log p(x_t) ∝ (E[x_0|x_t] - x_t)

Diffusion contact (integrated into S3):

- The note IS the diffusion contact this week.

### Week 8 (Checkpoint 2) — CLT + Toy Score Matching

- S1 (~2.5h): **Stat110 Lectures 28–30** (**[Stat110-YT]**)
  - Lecture 28: Inequalities (Markov, Chebyshev, Jensen)
  - Lecture 29: Law of Large Numbers and Central Limit Theorem
  - Lecture 30: Chi-Square, Student-t, Multivariate Normal (skim for MV Normal)
- S2 (~2h): mini-exam:
  - 6 problems total (mix from all Phase 1 topics)
  - Timebox ~20–30 min per hard problem
  - Write clean solutions in `proofs/phase1_exam/`
- S3 (~2h, Project): `mini_projects/checkpoint_02_toy_score_matching/`
  - Train a tiny MLP on 2D blobs to predict:
    - Either noise `eps` (denoising)
    - Or score `∇ log p_t(x)`
  - Plot learned vector field vs true (for Gaussian or MoG)
  - Write `report.md` (1–2 pages: setup, results, what broke, what you learned)
  - Treat this as **Nano-Diffusion v0**:
    - same 2D data generator used in earlier noising/score notebooks
    - fixed seed + tiny config block
    - metrics: denoising/score MSE, vector-field error where analytic score is known, runtime, and one failure note

Diffusion contact (integrated into S3):

- The entire checkpoint IS diffusion contact

---

# Phase 2 — Linear algebra refresh + VAE/flows + first “real” diffusion (Weeks 9–16)

**Phase goal:** get comfortable with multivariate Gaussians, SVD intuition, change of variables,
and basic deep generative modeling primitives.

Each week should form a learning chain:

> S1 introduces and consolidates the theory → S2 practices the exact derivations or
> calculations needed → S3 turns them into a runnable experiment → diffusion contact
> explains where the same idea appears in diffusion models.

### Week 9 — Linear algebra essentials (MML)

- S1:
  - **[MML-Book]** selected Ch. 2–3 (vectors, linear maps, geometry, projections)
  - Ch. 4 §§4.2, 4.4–4.6 (eigenvalues, SVD, matrix approximation)
  - consolidate the durable ideas in `notes/w09_mml_linear_algebra.md`
- S2: solve MML Exercises 2.10(a), 2.17, 3.6, and 4.9 in
  `proofs/w09_mml_linear_algebra.md`
  - the kernel/image parts of Exercise 2.17 are optional
  - Exercise 4.10 is an optional low-rank-approximation extension
- S3: `notebooks/w09_pca_svd.ipynb`
  - use MML Ch. 10 §§10.1–10.4 as a targeted PCA reference, not another full reading assignment
  - PCA on synthetic data (2D → 1D)
  - project, reconstruct, and compare reconstruction error for one vs two components

Diffusion contact:

- `notes/w09_linear_algebra_in_unets.md`: 1 page connecting matrix operations,
  projections, low-rank structure, convolutions, attention, and residual transformations.

Learning chain: linear maps and projections → small calculations by hand → PCA as
projection/reconstruction → linear operations and compressed representations in diffusion models.

### Week 10 — Multivariate Gaussian + score (core)

- S1:
  - **[MML-Book]** §§5.2 and 5.5 (gradients and useful identities)
  - **[MML-Book]** §6.5, especially §§6.5.1, 6.5.3, and 6.5.4
    (Gaussian conditionals, linear transformations, and sampling)
  - Optional: refresh with Stat110 continuous/joint
  - consolidate in `notes/w10_mml_multivariate_gaussian.md`
- S2:
  - derive the score of a multivariate Gaussian
  - derive the conditional of a joint Gaussian using the block-matrix formula
  - work one concrete 2D numerical example
  - write the derivations in `proofs/w10_multivariate_gaussian_score.md`
- S3: `notebooks/w10_mv_gaussian_score.ipynb`
  - sample, compute analytic score, visualize in 2D
  - verify the analytic score numerically
  - verify conditional mean and covariance against empirical samples

Diffusion contact:

- Add “Gaussian identities” cheat-sheet in `notes/gaussian_identities.md` (this becomes a living doc).

Learning chain: Gaussian matrix identities → score and conditioning derivations →
numerical verification → the Gaussian kernels used in forward noising and denoising.

### Week 11 — VAE foundations (theory + minimal code)

- S1:
  - use the named **VAE** lectures/slides in the Fall 2023 **[CS236-Site]**
    syllabus rather than relying on playlist numbers
  - Optional bridge: **[MML-Book]** §10.7 (latent-variable perspective on PCA)
  - consolidate in `notes/w11_cs236_vae.md`
- S2:
  - derive the ELBO for a simple Gaussian latent-variable model
  - identify the reconstruction and KL terms
  - derive the reparameterized sample used by the training code
  - write `notes/w11_elbo_derivation.md`
- S3: `notebooks/w11_minimal_vae_mnist.ipynb`
  - minimal VAE on MNIST (small model, few epochs)
  - log reconstruction samples, KL/reconstruction losses, and a latent traversal

Diffusion contact:

- `notes/w11_why_latent_diffusion.md`: 1 page on representation compression,
  reconstruction tradeoffs, and why diffusion is often performed in a learned latent space.

Learning chain: latent-variable model and ELBO → derive the trainable loss →
implement encoding/decoding → understand the compression stage used by latent diffusion.

### Week 12 — Normalizing flows (RealNVP on 2D)

- S1:
  - use the named **Normalizing Flows** lectures/slides in the Fall 2023
    **[CS236-Site]** syllabus
  - **[MML-Book]** §5.3 (Jacobians) and §6.7 (change of variables)
  - consolidate in `notes/w12_cs236_normalizing_flows.md`
- S2:
  - practice three change-of-variables examples: 1D monotone, multivariate affine,
    and a simple coupling transform
  - for the coupling transform, identify the triangular Jacobian and log-determinant
  - write `proofs/w12_change_of_variables_flows.md`
- S3: `notebooks/w12_realnvp_2d_blobs.ipynb`
  - implement RealNVP on 2D blobs
  - report NLL curve, transformed samples, and one failure case

Diffusion contact:

- `notes/w12_flows_vs_diffusion.md`: compare exact likelihood through invertibility
  with score/noise-prediction training and iterative sampling.

Learning chain: Jacobians and change of variables → coupling-layer log-determinant
by hand → RealNVP likelihood in code → contrast invertible flows with diffusion training.

### Week 13 — Optimization basics (just enough)

- S1:
  - **[MML-Book]** §7.1 only (gradient descent, step size, momentum, SGD)
  - **[Adam]** Algorithm 1 for Adam; constrained and convex optimization are deferred
  - consolidate in `notes/w13_optimization.md`
- S2:
  - derive the GD, momentum, and Adam update rules
  - compute the first two updates by hand on a small objective
  - write `proofs/w13_optimizer_updates.md`
- S3: `notebooks/w13_optimizers_sanity.ipynb`
  - implement GD, momentum, and Adam from scratch on the same toy objective
  - compare GD vs momentum vs Adam
  - show failure modes (too large LR, exploding gradients)

Diffusion contact:

- run one controlled stabilization experiment on the Week 8 toy score training loop
  (EMA, gradient clipping, or LR warmup) and document it in
  `notes/w13_training_stability_for_diffusion.md`.

Learning chain: optimizer updates → manual steps → controlled implementation →
one isolated training-stability change in the existing diffusion toy.

### Week 14 (Checkpoint 3) — Generative modeling toolkit consolidation

- S1: review Weeks 9–13 by comparing, for each model, its representation,
  objective, sampling procedure, and characteristic failure mode
- S2: solve a bounded four-problem mixed set:
  - multivariate Gaussian score/conditioning
  - ELBO/KL
  - flow change of variables and log-determinant
  - optimizer stability
- S3: `mini_projects/checkpoint_03_generative_toolkit_report/`
  - `report.md` (2–3 pages):
    - VAE: what objective, what failure mode
    - Flow: what objective, what failure mode
    - Score toy: what objective, what failure mode
  - reuse the strongest 1–2 existing diagnostic plots per model; do not retrain
    models only to create the report

Diffusion contact:

- The checkpoint comparison itself is the diffusion contact: explain what the
  score model shares with, and does differently from, the VAE and flow.

Learning chain: retrieve the core theory → solve mixed distinctions →
synthesize existing experiments → state which toolkit applies to diffusion and why.

### Week 15 — Bridge to diffusion math (forward process)

- S1:
  - **[HF-AnnotatedDiff]** forward-process sections
  - **[HF-DiffCourse]** Unit 1 “Diffusion Models from Scratch,” specifically
    the DDPM comparison’s corruption-process section
  - treat the notebook’s initial uniform-corruption example as intuition, not as canonical DDPM
  - Optional: the named **Score Based Diffusion Models** material in **[CS236-Site]**
- S2:
  - derive \(q(x_t \mid x_{t-1})\)
  - derive the closed form \(q(x_t \mid x_0)\)
  - identify the signal and noise coefficients, mean, and variance
  - consolidate the reading and derivations in `notes/w15_forward_process_discrete.md`
- S3: `notebooks/w15_forward_diffusion_mnist.ipynb`
  - implement canonical Gaussian forward diffusion on MNIST (no training yet)
  - compare two beta schedules
  - visualize \(x_t\), signal decay, and variance growth across timesteps
  - empirically verify the derived mean/variance at selected timesteps

Diffusion contact:

- Connect the discrete schedule to the single-noise-level forward processes from
  Weeks 1 and 8; the whole week is direct diffusion preparation.

Learning chain: canonical forward-process notation → derive one-step and
closed-form noising → verify both in code → understand the inputs Week 16 will train on.

### Week 16 — First full toy diffusion training (small)

- S1:
  - **[HF-DiffCourse]** Unit 1 sections on the training objective, timestep
    conditioning, and sampling
  - use **[HF-DiffCourse-Code]** as a reference, adapting it to the current
    project environment rather than copying installation cells
  - consolidate in `notes/w16_hf_ddpm_training.md`
- S2:
  - derive the fixed-timestep relationships among \(x_0\)-prediction,
    noise prediction, and score prediction
  - explain why the model must receive the timestep/noise level
  - write `notes/w16_prediction_parameterizations.md`
- S3: `notebooks/w16_train_tiny_ddpm_mnist.ipynb`
  - train a tiny timestep-conditioned convolutional denoiser on low-res MNIST
    for a few epochs using the noise-prediction objective
  - implement the reverse sampling loop; training without sampling is incomplete
  - save sample grid per epoch
  - keep the architecture intentionally small; deeper U-Net/attention study remains in Weeks 25–26
  - Treat this as the first image-level **Nano-Diffusion v1** run:
    - record config, seed, beta schedule, model size, training loss, sample grid, runtime
    - identify which code should graduate from notebook cells into `mini_projects/nano_diffusion/`

Diffusion contact:

- The entire training-and-sampling run is diffusion contact and is the prototype
  that becomes the clean DDPM baseline in Weeks 17–18.

Learning chain: DDPM objective and sampler → connect prediction parameterizations
algebraically → train a timestep-conditioned model and sample → graduate the working
pieces into Nano-Diffusion.

---

# Phase 3 — Diffusion in depth (DDPM/DDIM/CFG) (Weeks 17–28)

**Phase goal:** build **Nano-Diffusion** into a clean, reproducible baseline and learn the “engineering moves”
(schedules, EMA, sampling variants, conditioning, evaluation) by improving the same small system.

### Weeks 17–18 — DDPM from scratch (clean baseline)

- S1:
  - Read **[DDPM]** (focus on algorithm + objective)
  - Follow implementation guidance in **[HF-DiffCourse]** / **[HF-AnnotatedDiff]**
- S3 Artifact: `mini_projects/nano_diffusion/`
  - graduate reusable Week 16 code into a small shared project
  - reproducible DDPM training loop
  - config file for schedules + model size
  - EMA, logging, sample snapshots
  - `README.md` with exact “run this” commands
  - `experiments/ddpm_baseline_mnist/` records for each run: config, metrics, samples, notes

### Weeks 19–20 — Sampling methods (DDPM sampler + DDIM)

- S1: read **[DDIM]** (focus on sampling algorithm)
- S3 Artifact:
  - implement DDIM sampler + `eta` control
  - notebook: `notebooks/w20_ddpm_vs_ddim_steps.ipynb`
    - compare sample quality vs #steps at fixed compute
  - Add this as **Nano-Diffusion v2**:
    - same trained checkpoint when possible
    - compare DDPM vs DDIM by sampling steps/NFE, runtime, loss-independent visual quality, and failure modes

### Weeks 21–22 — Guidance & conditioning (CFG in a small setting)

- S1:
  - Use **[Diffusers-Docs]** CFG/conditioning concepts (and/or any good reference in **[MIT-6S184-Notes]**)
- S3 Artifact:
  - class-conditional MNIST diffusion
  - CFG scale sweep (e.g., 0, 1, 2, 3, 5)
  - produce a grid + short interpretation in `notes/w22_cfg_tradeoffs.md`

### Weeks 23–24 (Checkpoint 4) — Controlled ablations report

Run 2–3 controlled changes (one at a time):

- beta schedule
- loss weighting
- steps / DDIM eta

Artifact: `mini_projects/nano_diffusion/reports/checkpoint_04_ablations.md`

- “mini-paper” report (2–4 pages):
  - setup
  - results (tables/figures)
  - conclusions (what mattered, what didn’t)
  - Use Nano-Diffusion experiment logs as the source of truth; the report should summarize the strongest controlled comparisons rather than re-run everything ad hoc.

### Weeks 25–26 — Architecture literacy (U-Net, attention, conditioning)

- S1:
  - skim/learn from **[Diffusers-Docs]**
  - optional: architecture discussion in **[MIT-6S184-Notes]**
- S3:
  - refactor code into clean modules
  - add:
    - config system
    - deterministic seeds
    - clearer sampling API

### Weeks 27–28 — Evaluation literacy (lightweight)

- S1: Stanford CS236 evaluation lecture (typically Lecture 15) via **[CS236-YT]**
- S3 Artifact:
  - evaluation notebook: `notebooks/w28_eval_sanity_checks.ipynb`
  - include:
    - overfitting signs
    - diversity checks
    - (optional) lightweight FID / cleanfid

---

# Phase 4 — SDE/ODE view + Flow Matching (Weeks 29–40)

**Phase goal:** read modern score-SDE / probability-flow ODE / flow-matching papers comfortably
and connect the theories to the Nano-Diffusion code you already have.

### Weeks 29–30 — Brownian motion + Itô intuition (light, practical)

- S1 (Primary): **[MIT-6S184]** lectures/notes sections introducing SDE view
- S1 (Support): **[Higham-SDE]** (numerical simulation intuition)
- S2: implement Euler–Maruyama on simple SDEs
- S3: `notebooks/w30_euler_maruyama_stability.ipynb`
  - compare step sizes, show instability regimes
  - replicate 1 figure from Higham (in your own words)

### Weeks 31–32 — Reverse-time intuition + Fokker–Planck overview

- S1: **[MIT-6S184-Notes]** sections on forward diffusion ↔ reverse process story
- S2: write a “derivation narrative” (not full rigor) in:
  - `notes/w32_reverse_time_story.md`
- S3: notebook:
  - `notebooks/w32_probability_flow_ode_demo.ipynb`
  - implement a toy ODE sampler for a simple known score field (2D Gaussian / MoG)

### Weeks 33–34 — Score-SDE view (paper reading light + code mapping)

- S1: read selected sections of **[ScoreSDE]**
- S3:
  - implement VE/VP schedules variants in your codebase
  - `notes/w34_ve_vp_mapping.md`: “paper symbols ↔ my code variables”

### Weeks 35–36 — Flow matching / rectified flow (toy first)

- S1:
  - read **[FlowMatching]**
  - also use **[MIT-6S184]** flow matching lectures for intuition
- S3: `notebooks/w36_flow_matching_2d.ipynb`
  - implement flow matching on 2D blobs
  - compare:
    - training stability
    - sampling speed
    - failure cases
  - write 1 page: `notes/w36_diffusion_vs_flowmatching.md`
  - Treat this as **Nano-Flow v0**:
    - reuse the same 2D distributions from Nano-Diffusion v0
    - compare learned vector fields, sampling trajectories, runtime, and failure cases under matched model size where possible

### Weeks 37–38 — Flow matching on images (small)

- S1: **[MIT-6S184]** relevant lecture/lab (image-level flow matching)
- S3:
  - minimal flow-matching model on MNIST
  - `notebooks/w38_flow_matching_mnist.ipynb`
  - log samples + stability notes
  - Treat this as **Nano-Flow v1**:
    - compare against the Nano-Diffusion MNIST baseline using the same data preprocessing, seed discipline, sample-grid format, runtime logging, and model-size notes

### Weeks 39–40 (Checkpoint 5) — Bridge report

Artifact: `mini_projects/checkpoint_05_bridge_report/bridge_report.md` (3–5 pages)
Explain (with diagrams):

- discrete diffusion (DDPM/DDIM)
- score-SDE formulation
- probability-flow ODE
- flow matching / rectified flow
  Include:
- what objective is optimized (high level)
- what changes in implementation (what you literally changed in code)

---

# Phase 5 — Paper pass + reproduction + portfolio (Weeks 41–52)

**Phase goal:** “expert starts showing”: you can read, reproduce, and explain.

### Weeks 41–44 — Paper pass 1 (diffusion core)

Pick 2–3:

- **[DDPM]**
- **[DDIM]**
- **[ScoreSDE]**

For each paper:

- `papers/<paper_key>/summary.md` (1 page)
- `papers/<paper_key>/derivation.md` (one derivation you can reproduce without looking)
- `papers/<paper_key>/code_alignment.md` (“where this appears in my repo”)

### Weeks 45–48 — Reproduction target (one solid reproduction)

Pick ONE target you can finish:

- a clean DDPM/DDIM baseline with strong ablations
- OR a flow-matching baseline with comparisons
- OR a unified Nano-Diffusion vs Nano-Flow report if both baselines are stable enough

Artifact:

- `mini_projects/reproduction_target/`
- “mini-paper” report + reproducible code + configs + results
  - Prefer reusing `mini_projects/nano_diffusion/` as the codebase and making the reproduction target a polished report layer over the strongest runs.

### Weeks 49–50 — Write a technical blog post

Write one post (Markdown in repo, or publish externally):

- “Diffusion from scratch: forward process, training loss, sampling, and why it works”
  Include:
- your own visuals
- references to your notebooks
- a “how to run” section

### Weeks 51–52 — Open-source polish

- Clean repo + `README.md` as a portfolio landing page:
  - what you built
  - quickstart
  - results gallery
  - links to reports/posts
- Optional:
  - small demo notebook
  - integrate parts with **[Diffusers-Docs]** style components (only if motivating)

---

## What to postpone (optional deep dives)

Use these only as needed:

- **[MIT-RealAnalysis]** MIT 18.100B Real Analysis (OCW): [https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/)
- **[Boyd-Book]** Convex Optimization (book): [https://web.stanford.edu/~boyd/cvxbook/](https://web.stanford.edu/~boyd/cvxbook/)
- Full rigor SDE texts (only if you truly want) — otherwise rely on **[MIT-6S184]**, **[Higham-SDE]**, **[SarkkaSolin]**

---

## Success metrics (you’re on track if…)

Every 4 weeks you have:

- ≥1 checkpoint project in `mini_projects/`
- ≥4 weekly artifacts (notes/proofs/notebooks)
- one “diffusion contact” improvement per week (even tiny)
- at least one Nano-Diffusion/Nano-Flow run record whenever the period includes implementation work

By Month 6 you should be able to:

- implement DDPM/DDIM on MNIST cleanly
- explain the training loss and sampling loop clearly
- derive basic score identities for Gaussians and noisy variables
- compare two Nano-Diffusion runs using the same metrics and config discipline

By Month 12 you should be able to:

- read diffusion/flow-matching papers without “drowning”
- reproduce at least one baseline + ablation report
- communicate the ideas (blog/notes) with your own derivations
- show a coherent Nano-Diffusion/Nano-Flow project history: what improved, what failed, and which metrics justify the conclusions

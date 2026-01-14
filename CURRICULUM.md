# 12-Month Curriculum: Probability → Diffusion / Score / Flow Matching (3 sessions/week)

Goal: become a strong “paper-reading + implementation” researcher/practitioner in diffusion / score-based / flow-matching models in ~12 months (≤24 months max), by combining:

- just-enough math foundations (probability + linear algebra + SDE intuition)
- continuous contact with diffusion concepts from Week 1
- steady artifacts (notes + proofs + code) that compound

---

## 0) Canonical resource index (free unless marked)

Use these short tags throughout the plan.

### Probability + proofs (Phase 1 backbone)

- **[Stat110-YT]** Stat110 full lecture playlist:  
  https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo
- **[Stat110-Practice]** Strategic Practice Problems + HW sets (contains problems + solutions):  
  https://stat110.hsites.harvard.edu/strategic-practice-problems
- **[Stat110-Text]** Stat110 online textbook (Blitzstein & Hwang):  
  https://projects.iq.harvard.edu/stat110/book
- **[BoP]** Book of Proof (Hammack, free PDF):  
  https://richardhammack.github.io/BookOfProof/Main.pdf
- **[MIT-6042]** Mathematics for Computer Science (MIT 6.042J OCW notes + assignments):  
  https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-sc-science-fall-2005/  
  Video playlist: https://www.youtube.com/playlist?list=PLB7540DEDD482705B

### Linear algebra + optimization (Phase 2 backbone)

- **[MML-Book]** Mathematics for Machine Learning (free PDF):  
  https://mml-book.github.io/book/mml-book.pdf
- **[MIT-1806]** MIT 18.06 Linear Algebra (optional, for intuition/drills):  
  https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/

### Deep generative models (VAE/Flows/Diffusion theory support)

- **[CS236-Site]** Stanford CS236 course site + syllabus + slides/notes:  
  https://deepgenerativemodels.github.io/  
  Syllabus with topic-by-week: https://deepgenerativemodels.github.io/syllabus.html
- **[CS236-YT]** Stanford CS236 YouTube playlist (2023):  
  https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8

### Diffusion / score resources (implementation + literacy)

- **[HF-DiffCourse]** Hugging Face Diffusion Course (hands-on, free):  
  https://huggingface.co/learn/diffusion-course
- **[HF-AnnotatedDiff]** “Annotated Diffusion” blog (walkthrough + code):  
  https://huggingface.co/blog/annotated-diffusion
- **[Diffusers-Docs]** Hugging Face Diffusers docs:  
  https://huggingface.co/docs/diffusers/index
- **[Song-Tut]** Yang Song’s score-based tutorial hub:  
  https://yang-song.net/blog/2021/score/
- **[Weng]** Lilian Weng blog (useful for intuition + summaries):  
  https://lilianweng.github.io/

### Flow matching / ODE/SDE view (Phase 4 backbone)

- **[MIT-6S184]** MIT course “Flow Matching and Diffusion Models” (notes + lectures + labs):  
  https://diffusion.csail.mit.edu/
- **[MIT-6S184-Notes]** Direct lecture notes PDF:  
  https://diffusion.csail.mit.edu/lecture-notes.pdf

### Core papers (open access)

- **[DDPM]** Ho et al. “Denoising Diffusion Probabilistic Models”: https://arxiv.org/abs/2006.11239
- **[DDIM]** Song et al. “Denoising Diffusion Implicit Models”: https://arxiv.org/abs/2010.02502
- **[ScoreSDE]** Song et al. “Score-Based Generative Modeling through SDEs”: https://arxiv.org/abs/2011.13456
- **[FlowMatching]** Lipman et al. “Flow Matching for Generative Modeling”: https://arxiv.org/abs/2210.02747
- **[RectifiedFlow]** (rectified flow line of work; pick a canonical arXiv paper you like and pin it here once chosen)

### SDE numerics (free references)

- **[Higham-SDE]** Higham “An Algorithmic Introduction to Numerical Simulation of SDEs” (PDF):  
  https://www.maths.ed.ac.uk/~dhigham/Publications/Papers/sdes.pdf
- **[SarkkaSolin]** Särkkä & Solin “Applied Stochastic Differential Equations” (PDF/notes):  
  https://users.aalto.fi/~asolin/sde-book/sde-book.pdf
- **[MIT-18445]** MIT 18.445 Stochastic Processes (OCW):  
  https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/

> Rule: if a link breaks, replace it with an equivalent official mirror and update README (don’t stall the curriculum).

---

## You are here (completed)

You already finished up to:

**Stat110**

- S1: Lectures 5–6
- S2: Discrete RV problems (Bernoulli, Binomial, Geometric)

So you are ready to continue with:

- Continuous RVs, expectation/variance, joint distributions, conditioning, CLT
- Start minimal diffusion artifacts immediately (tiny toy setups)

---

## Rules of the game (so you don’t get stuck in prerequisites)

1. **Every week produces an artifact** (a note, a proof write-up, or a runnable notebook).
2. **Diffusion contact every week** (minimum 45 minutes) from Week 1 onward.
3. **Math is “just in time”**: learn enough to understand a derivation you need _now_.
4. **Checkpoints matter more than coverage**: you can skip/trim content if artifacts keep moving.
5. **One canonical repo** where everything lives.

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

---

## Repository structure (recommended)

- `notes/` (short markdown notes, 1–2 pages each)
- `proofs/` (clean solutions to selected problems)
- `notebooks/` (runnable experiments)
- `mini_projects/` (monthly checkpoints)
- `papers/` (one-page summaries + “key derivation” per paper)
- `README.md` (links to milestones + how to run notebooks)

---

## Phases overview (12 months)

- **Phase 1 (Weeks 1–8): Probability core + minimal diffusion toys**
- **Phase 2 (Weeks 9–16): Linear algebra refresh + generative modeling basics (VAE/flows)**
- **Phase 3 (Weeks 17–28): Diffusion in depth (DDPM/DDIM/CFG), solid implementation baseline**
- **Phase 4 (Weeks 29–40): SDE/ODE view + flow matching, connect the theories**
- **Phase 5 (Weeks 41–52): Paper pass + reproduction + portfolio (blog + OSS)**

---

# Phase 1 — Probability core + minimal diffusion toys (Weeks 1–8)

**Phase goal:** become fluent in (1) continuous RV mechanics, (2) conditioning, (3) Gaussian identities,
while building “diffusion-adjacent” intuition every week.

> For Stat110 problems: use **[Stat110-Practice]** and pick the set matching your lecture/topic (search the page for the lecture number or keywords like “continuous”, “expectation”, “joint”, “CLT”, etc.).

### Week 1 — Continuous RVs + first diffusion toy

- S1 (Theory): **Stat110 Lectures 7–8** via **[Stat110-YT]** (continuous RVs: pdf/cdf, common continuous dists)
- S2 (Problems): from **[Stat110-Practice]** choose 6–10 on:
  - pdf/cdf basics
  - computing probabilities by integration
  - change of variables (simple transforms)
- S3 (Artifact): `notebooks/w01_forward_noising_blobs.ipynb`
  - Generate 2D data (mixture of Gaussians “blobs”)
  - Implement forward noising: `x_t = x_0 + sigma(t) * eps`
  - Plot histograms / scatter across t
  - Save 1 figure to `notes/figures/w01_*.png`

Diffusion contact (must do):

- 45–60 min: implement `sigma(t)` schedules (linear + geometric) and compare how fast the distribution “washes out”.

### Week 2 — Expectation / variance (make it automatic)

- S1: **Stat110 Lectures 9–10** (**[Stat110-YT]**) (expectation, LOTUS, indicators, variance tricks)
- S2: **[Stat110-Practice]** 6–10 problems on:
  - LOTUS + “compute E[g(X)]”
  - indicators + linearity
  - variance shortcuts (e.g., Var(aX+b), decomposition)
- S3: `notes/w02_expectation_toolkit.md`
  - A one-page “Expectation toolkit”:
    - linearity
    - indicators
    - symmetry
    - conditioning trick pattern (“condition on the first thing that happens”)

Diffusion contact:

- Derive and code-check `E[x_t|x_0]` and `Var(x_t|x_0)` for your forward noising model.

### Week 3 — Joint distributions + independence

- S1: **Stat110 Lectures 11–12** (**[Stat110-YT]**) (joint, conditional density, independence)
- S2: **[Stat110-Practice]** 6–10 problems on:
  - joint → marginal
  - conditional density
  - independence checks
- S3: `notebooks/w03_joint_gaussians_conditionals.ipynb`
  - sample correlated Gaussians in 2D/3D
  - visualize conditional slices / regression line intuition
  - compare analytic conditional mean vs empirical

Diffusion contact:

- `notes/w03_score_of_gaussian.md`: compute the score of a Gaussian:
  - `∇_x log N(x; μ, Σ) = -Σ^{-1}(x-μ)`
  - verify with finite differences on a grid

### Week 4 (Checkpoint 1) — Conditioning mastery

- S1: Stat110 conditioning coverage as needed (**[Stat110-YT]** + **[Stat110-Text]**)
- S2: 4–6 **hard** conditioning problems from **[Stat110-Practice]**:
  - Bayes + LOTP
  - “condition on a useful event / first step”
- S3 (Project): `mini_projects/checkpoint_01_conditioning_in_code/`
  - Pick 1 concrete problem (e.g., medical test Bayes, urns, gambler’s ruin step)
  - Write:
    - `analysis.md` (clean derivation)
    - `simulate.py` (Monte Carlo)
    - `results.ipynb` (plots + comparison)

Diffusion contact:

- `notes/w04_conditioning_in_diffusion.md`:
  - 1 page: where conditioning shows up (Gaussian posterior, denoising as conditional expectation)

### Week 5 — LLN/CLT intuition + empirical verification

- S1: **Stat110 Lectures 13–14** (**[Stat110-YT]**) (LLN, CLT, Chebyshev)
- S2: **[Stat110-Practice]** problems on:
  - Chebyshev bounds
  - CLT approximations
  - sanity checks with simulation
- S3: `notebooks/w05_clt_simulations.ipynb`
  - simulate sums/means of RVs
  - show convergence to Normal (plots + short explanations)

Diffusion contact:

- Connect denoising to “estimating signal from noise” (Gaussian conditioning story):
  - write 5–10 bullet points + 1 equation you can re-derive.

### Week 6 — Entropy / KL / cross-entropy (research literacy)

- S1:
  - Read **[MML-Book]** sections covering KL / entropy (Part I probability chapter)
  - Optional intuition: skim any diffusion KL discussion in **[MIT-6S184-Notes]**
- S2:
  - Derive KL for 1D Gaussians then multivariate Gaussians (write it cleanly)
  - Implement a numeric KL estimate (histograms) and compare to closed form
- S3: `notebooks/w06_kl_gaussians.ipynb`
  - histogram-KL estimate vs analytic KL for Gaussians
  - show failure modes (binning sensitivity)

Diffusion contact:

- `notes/w06_where_kl_appears.md`:
  - 1 page: KL in variational objectives, why “matching distributions” keeps showing up in diffusion/flow formulations.

### Week 7 — MGFs/characteristic functions OR skip (optional)

- If you feel shaky: do MGFs basics via **[Stat110-YT/Text]**.
- Otherwise: **skip** and use the time to strengthen your weakest Phase-1 topic (conditioning/joint/CLT).
- S3 (Artifact): `notes/w07_mgf_onepager.md` **or** a “weak-topic repair” note.

Diffusion contact:

- `notebooks/w07_score_mog.ipynb`:
  - score of a mixture of Gaussians (analytic) vs finite differences on a grid
  - visualize vector field arrows

### Week 8 (Checkpoint 2) — Probability mini-exam + toy score matching

- S1: review your weak points (re-watch 1–2 Stat110 lectures if needed)
- S2: mini-exam:
  - 6 problems total
  - timebox ~20–30 min per hard problem
  - write clean solutions in `proofs/phase1_exam/`
- S3 (Project): `mini_projects/checkpoint_02_toy_score_matching/`
  - Train a tiny MLP on 2D blobs to predict:
    - either noise `eps` (denoising)
    - or score `∇ log p_t(x)`
  - Plot learned vector field vs true (for Gaussian or MoG)
  - Write `report.md` (1–2 pages: setup, results, what broke, what you learned)

---

# Phase 2 — Linear algebra refresh + VAE/flows + first “real” diffusion (Weeks 9–16)

**Phase goal:** get comfortable with multivariate Gaussians, SVD intuition, change of variables,
and basic deep generative modeling primitives.

### Week 9 — Linear algebra essentials (MML)

- S1: **[MML-Book]** Ch. 2–3 (vectors/matrices, eigen/SVD)
- S2: MML exercises: projections + SVD/PCA intuition
- S3: `notebooks/w09_pca_svd.ipynb`
  - PCA on synthetic data (2D → 1D)
  - show reconstruction error vs #components

Diffusion contact:

- `notes/w09_linear_algebra_in_unets.md`: 1 page (convolutions, attention, residuals = linear ops + nonlinearity).

### Week 10 — Multivariate Gaussian + score (core)

- S1:
  - **[MML-Book]** probability chapter sections on Gaussians
  - Optional: refresh with Stat110 continuous/joint
- S2:
  - Derive score for multivariate Gaussian
  - Derive conditional of a joint Gaussian (block matrix formula)
- S3: `notebooks/w10_mv_gaussian_score.ipynb`
  - sample, compute analytic score, visualize in 2D
  - verify conditional mean vs empirical

Diffusion contact:

- Add “Gaussian identities” cheat-sheet in `notes/gaussian_identities.md` (this becomes a living doc).

### Week 11 — VAE foundations (theory + minimal code)

- S1 (Theory): Stanford CS236 **VAE lectures** (typically Lectures 5–6) via **[CS236-YT]** + slides on **[CS236-Site]**
- S2 (Derivation): ELBO for a simple latent variable model
  - Write the derivation in `notes/w11_elbo_derivation.md`
- S3 (Code): `notebooks/w11_minimal_vae_mnist.ipynb`
  - minimal VAE on MNIST (small model, few epochs)
  - log recon samples + latent traversal

Diffusion contact:

- `notes/w11_why_latent_diffusion.md`: 1 page on why diffusion often goes “latent”.

### Week 12 — Normalizing flows (RealNVP on 2D)

- S1: Stanford CS236 **Normalizing Flows lectures** (typically Lectures 7–8) via **[CS236-YT]**
- S2: practice change-of-variables theorem
  - write 3 examples by hand (1D monotone transform, affine, simple coupling)
- S3: `notebooks/w12_realnvp_2d_blobs.ipynb`
  - implement RealNVP on 2D blobs
  - report NLL curve + samples

Diffusion contact:

- `notes/w12_flows_vs_diffusion.md`: compare “likelihood via invertibility” vs “likelihood-free score field”.

### Week 13 — Optimization basics (just enough)

- S1: **[MML-Book]** Chapter 7 (Continuous Optimization: GD, constraints, convexity)
- S2: implement GD + Adam from scratch on a toy objective
- S3: `notebooks/w13_optimizers_sanity.ipynb`
  - compare GD vs momentum vs Adam
  - show failure modes (too large LR, exploding gradients)

Diffusion contact:

- add one stabilization trick to your diffusion toy training loop (EMA, grad clipping, LR warmup) and document it.

### Week 14 (Checkpoint 3) — Generative modeling toolkit consolidation

- S1: review notes (Weeks 9–13)
- S2: mixed set (ELBO, KL, change of variables, Gaussians)
- S3: `mini_projects/checkpoint_03_generative_toolkit_report/`
  - `report.md` (1–2 pages):
    - VAE: what objective, what failure mode
    - Flow: what objective, what failure mode
    - Score toy: what objective, what failure mode
  - include 2–3 plots per model

### Week 15 — Bridge to diffusion math (forward process)

- S1:
  - **[HF-AnnotatedDiff]** (focus on forward process + training objective)
  - Optional: Stanford CS236 diffusion lecture(s) (typically Lecture 16) **[CS236-YT]**
- S2: derive forward noising equations (discrete time)
  - write: `notes/w15_forward_process_discrete.md`
- S3: `notebooks/w15_forward_diffusion_mnist.ipynb`
  - implement forward diffusion on MNIST (no training yet)
  - visualize x_t across timesteps, schedules

Diffusion contact:

- implement 2 beta schedules and show their effect (variance growth, signal decay).

### Week 16 — First full toy diffusion training (small)

- S1: **[HF-DiffCourse]** units on training (noise prediction / denoising objective)
- S2: derive equivalence (high-level) of predicting noise vs predicting score
  - `notes/w16_noise_vs_score.md`
- S3: `notebooks/w16_train_tiny_ddpm_mnist.ipynb`
  - tiny UNet/MLP denoiser, low-res MNIST, few epochs
  - save sample grid per epoch

---

# Phase 3 — Diffusion in depth (DDPM/DDIM/CFG) (Weeks 17–28)

**Phase goal:** build a clean, reproducible diffusion baseline and learn the “engineering moves”
(schedules, EMA, sampling variants, conditioning, evaluation).

### Weeks 17–18 — DDPM from scratch (clean baseline)

- S1:
  - Read **[DDPM]** (focus on algorithm + objective)
  - Follow implementation guidance in **[HF-DiffCourse]** / **[HF-AnnotatedDiff]**
- S3 Artifact: `mini_projects/ddpm_baseline_mnist/`
  - reproducible training loop
  - config file for schedules + model size
  - EMA, logging, sample snapshots
  - `README.md` with exact “run this” commands

### Weeks 19–20 — Sampling methods (DDPM sampler + DDIM)

- S1: read **[DDIM]** (focus on sampling algorithm)
- S3 Artifact:
  - implement DDIM sampler + `eta` control
  - notebook: `notebooks/w20_ddpm_vs_ddim_steps.ipynb`
    - compare sample quality vs #steps at fixed compute

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

Artifact: `mini_projects/checkpoint_04_ablations/`

- “mini-paper” report (2–4 pages):
  - setup
  - results (tables/figures)
  - conclusions (what mattered, what didn’t)

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
and connect the theories to code you already have.

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

### Weeks 37–38 — Flow matching on images (small)

- S1: **[MIT-6S184]** relevant lecture/lab (image-level flow matching)
- S3:
  - minimal flow-matching model on MNIST
  - `notebooks/w38_flow_matching_mnist.ipynb`
  - log samples + stability notes

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

Artifact:

- `mini_projects/reproduction_target/`
- “mini-paper” report + reproducible code + configs + results

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

- **[Tao-Analysis]** Analysis I (draft): https://www.math.ucla.edu/~tao/Analysis1.pdf
- **[Boyd-Book]** Convex Optimization (book): https://web.stanford.edu/~boyd/cvxbook/
- Full rigor SDE texts (only if you truly want) — otherwise rely on **[MIT-6S184]**, **[Higham-SDE]**, **[SarkkaSolin]**

---

## Success metrics (you’re on track if…)

Every 4 weeks you have:

- ≥1 checkpoint project in `mini_projects/`
- ≥4 weekly artifacts (notes/proofs/notebooks)
- one “diffusion contact” improvement per week (even tiny)

By Month 6 you should be able to:

- implement DDPM/DDIM on MNIST cleanly
- explain the training loss and sampling loop clearly
- derive basic score identities for Gaussians and noisy variables

By Month 12 you should be able to:

- read diffusion/flow-matching papers without “drowning”
- reproduce at least one baseline + ablation report
- communicate the ideas (blog/notes) with your own derivations

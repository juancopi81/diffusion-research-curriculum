# Week 14 — Generative Toolkit Checkpoint: Study Plan

**Status:** Planned on 2026-10-19. Week 13 is complete as of 2026-10-14;
Week 14 study tasks are not yet started.

**Pacing:** Seven study days, about seven hours total. Day 1 means the next
day you study; these are flexible sessions rather than calendar deadlines.
If a problem needs another sitting, carry it forward and move the remaining
days with it.

## What This Week Is For

The [curriculum checkpoint](../CURRICULUM.md#week-14-checkpoint-3--generative-modeling-toolkit-consolidation)
asks you to retrieve and connect Weeks 9–13: representations, objectives,
generation procedures, and failure modes. The main comparison is the MNIST
VAE, the 2D RealNVP, and the fixed-noise score toy. PCA and Gaussian identities
provide supporting tools; optimizers explain how the objectives become
parameter updates.

Follow the familiar sequence: intuition → derivation → implementation
evidence → diffusion connection. Here the implementation evidence already
exists. Use saved outputs and reviewed notes; no new lecture series or model
training is required.

By the end, you should be able to explain what each model learns, solve four
mixed problems, and support a short comparison with your own results.

## Outputs to Complete During the Week

- Four reviewed solutions in `proofs/w14_generative_toolkit_mixed_set.md`.
- A 2–3-page report in
  `mini_projects/checkpoint_03_generative_toolkit_report/report.md`, with a
  compact comparison table and 1–2 existing diagnostic plots per model.
  Start with one plot per model; add a second only if it supports a distinct claim.
- A short `README.md` beside the report linking the source notebooks and
  explaining where the reused evidence came from. Export saved notebook
  figures into that checkpoint's `figures/` directory if needed.

These outputs are planned, not completed artifacts. Write your answers first,
review them together, then consolidate the final Markdown in your own words.

## Day-by-Day Schedule

| Day | Time | Focus | Concrete stopping point |
| --- | --- | --- | --- |
| 1 | 45 min | Retrieve the model map | A rough VAE/flow/score comparison and at most three gaps to revisit |
| 2 | 60 min | Gaussian score and conditioning | Problem 1 attempted, checked, and explained geometrically |
| 3 | 60 min | VAE: ELBO, KL, and generation | Problem 2 reviewed; one observed VAE limitation tied to existing evidence |
| 4 | 60 min | Flow: density, inverse, and expressivity | Problem 3 reviewed; one-layer failure explained from the mapping |
| 5 | 75 min | Score learning and optimizer stability | Problem 4 reviewed; training target, evaluation target, and sampling distinguished |
| 6 | 90 min | Assemble the checkpoint report | A 2–3-page draft with traceable figures and bounded conclusions |
| 7 | 30 min | Explain, correct, and close | Final oral review, remaining corrections, and an honest completion decision |

### Day 1 — Retrieve the Model Map

Spend the first 15 minutes without notes. For each of the three models, write
one or two sentences about its representation, training objective, generation
path, and a limitation you actually observed. Mark uncertainty instead of
filling gaps with guesses.

Then use the source map below to correct the comparison. Recall how the Week 9
PCA bottleneck differs from learned VAE compression and dimension-preserving
RealNVP transformations. Use the Week 13 three-model review as a check after
your own recall attempt.

**Stop when:** you have a small working comparison table and no more than three
questions to resolve on Days 2–5. This table can become part of the report;
it does not need a separate polished note.

### Day 2 — Gaussian Score and Conditioning

Allow about 10 minutes for recall, 35 for Problem 1, and 15 to review the
derivation against your Week 10 work. Explain the score's direction using
covariance geometry, then distinguish conditioning from taking a marginal.

**Stop when:** the gradient and conditional distribution are correct, and you
can explain why covariance changes both the score field and conditional
uncertainty. Correct the reasoning before polishing the solution.

### Day 3 — VAE: What the Objective Buys Us

Use roughly 35 minutes for Problem 2, 15 to inspect saved VAE loss curves and
reconstructions, and 10 to record the interpretation.

Separate reconstruction through the encoder from generation using the prior.
Remember that the notebook displays decoder means; those are different from
full samples of its Gaussian observation model. Pick one visible limitation
from the reviewed experiment, and distinguish the observation from possible
causes such as bottleneck size, model capacity, or brief training.

**Stop when:** you can connect the ELBO to the implemented loss and say what
the saved reconstruction or generation plot establishes. Do not diagnose
posterior collapse merely because a reconstruction looks blurry.

### Day 4 — Flow: Exact Density and an Architectural Limit

Use roughly 35 minutes for Problem 3, 15 to inspect the saved six-layer versus
one-layer comparison, and 10 to record the interpretation.

Keep the notebook's convention explicit: forward maps data to latent space;
inverse generates from the Gaussian base. Connect the unchanged coordinate
in a single coupling layer to the observed first-coordinate marginal.

**Stop when:** the inverse and determinant sign agree, and you can distinguish
exact evaluation of the model's density from an exact fit to the data.

### Day 5 — Score Learning and Optimization

Spend about 20 minutes revisiting the Week 8 report and Week 13 score-objective
review, 35 on Problem 4, and 20 connecting the pieces.

Explain these three objects separately: the conditional Gaussian score used
as a training target, the marginal noisy-mixture score used for evaluation,
and the parameter gradient used by the optimizer. Then state what our toy
does not yet provide: a model across noise levels and a reverse sampler.

**Stop when:** you can interpret the clipping result without claiming either
that clipping always helps or that it is generally harmful. Identify the
missing ingredients for diffusion sampling; implementing them belongs later.

### Day 6 — Write the Report from Existing Evidence

Use approximately 20 minutes to select evidence, 55 to write, and 15 to check
claims and links. A compact structure is enough:

1. The comparison question and a model table: representation, objective,
   generation procedure, and observed limitation.
2. One short evidence-based section per model, each connecting its objective
   to a result and a limitation in the saved experiment.
3. A closing explanation of which tools carry into diffusion and what remains
   to be learned in Weeks 15–16.

Useful evidence choices:

- **VAE:** the saved input/reconstruction panel; include separate reconstruction
  and KL curves only if they add to the interpretation.
- **Flow:** the saved one-layer versus six-layer sample/marginal comparison;
  the held-out NLL curve can provide a second diagnostic.
- **Score toy:** analytical and learned vector fields from the Week 8 report,
  or the Week 13 clipping comparison with held-out score MSE. Keep the run
  identities clear if discussing both experiments.

Record the source artifact and run/configuration for each figure. The VAE uses
MNIST, the flow uses four 2D blobs, and the score toy uses three 2D blobs: this
is a conceptual and diagnostic comparison, not a matched model benchmark.
Do not rank the models by raw ELBO, NLL, or score-training loss, which measure
different things. Generated sample quality was not tested by the score toy.

**Stop when:** every result claim points to existing evidence and every causal
explanation is either supported or explicitly a hypothesis. Reusing saved
outputs is sufficient; do not retrain just to improve a figure.

### Day 7 — Review and Decide Whether the Checkpoint Is Complete

Explain the report aloud without reading it, then review any weak answer:

- Why does the VAE use a bound, while this flow evaluates its density exactly?
- Why can exact flow likelihood coexist with a visibly imperfect fit?
- Why is a score a vector field rather than a probability or a sample?
- Why can smaller applied gradients coexist with worse held-out score MSE?
- What do Weeks 15–16 add beyond our single-noise-level score toy?

Use the remaining time for corrections. If a central answer is still unclear,
leave that item open and add a short review sitting rather than marking the
week complete on schedule.

## Four Bounded Practice Problems

These are independent checkpoint prompts based on the completed material,
not exercises attributed to a book or an official solution set. Attempt each
before consulting the linked derivations. Solutions will be written and
reviewed during the week; they are intentionally not supplied here.

### Problem 1 — Gaussian Score and Conditioning

Let $X=(X_1,X_2)^\top$ be Gaussian with

$$
\mu=\begin{bmatrix}1\\-1\end{bmatrix},
\qquad
\Sigma=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

1. Derive $\nabla_x\log p_X(x)$ and evaluate it at $x=(2,0)^\top$.
2. Find the mean and variance of $X_2\mid X_1=2$.
3. Compare that conditional distribution with the marginal distribution of
   $X_2$, and explain the changes using the positive covariance.

### Problem 2 — ELBO, KL, and the Implemented Loss

For one fixed observation $x$, use a scalar latent with
$q_\phi(z\mid x)=\mathcal N(1,1/4)$, prior $p(z)=\mathcal N(0,1)$, and decoder
$p_\theta(x\mid z)=\mathcal N(m_\theta(z),\tau^2 I_D)$ with fixed $\tau^2$.

1. Write the identity relating $\log p_\theta(x)$, the ELBO, and the posterior
   KL. Explain why the ELBO is a lower bound.
2. Calculate $D_{\mathrm{KL}}(q_\phi(z\mid x)\Vert p(z))$.
3. Write the one-sample negative-ELBO estimate, retaining the reconstruction
   scale and identifying any omitted constant. Explain where the latent is
   drawn from during reconstruction versus unconditional generation.

### Problem 3 — Change of Variables and an Unchanged Coordinate

Use the data-to-latent map $z=f(x)$ with standard-normal base $p_Z$ in 2D:

$$
z_1=x_1,\qquad
z_2=x_2\exp(s(x_1))+t(x_1),\qquad
s(x_1)=\log 2,\quad t(x_1)=x_1.
$$

1. Derive $f^{-1}$, the forward Jacobian, and its log absolute determinant.
2. Write $\log p_X(x)$ and evaluate it at $x=(1,0)^\top$. Check the sign of
   the volume correction using the inverse map.
3. Explain why any single layer of this form leaves the generated
   first-coordinate marginal standard normal, even if its scale and shift
   functions are trained. Connect this to the one-layer failure plot.

### Problem 4 — Stability and What Clipping Actually Established

Return to $L(\theta)=\tfrac12(\theta_1^2+10\theta_2^2)$ with
$\theta^{(0)}=(2,1)^\top$.

1. Derive the coordinate recurrences for plain GD and the learning-rate range
   that makes both coordinates converge to zero.
2. Classify the behavior at $\eta=0.05$, $0.15$, and $0.25$, distinguishing
   decaying oscillation from divergence.
3. Revisit the Week 13 clipping table: which result supports a bound on the
   applied gradient, and which result evaluates score accuracy? Explain why
   they do not establish the same claim, and propose one controlled next test
   without running it.

## Source Map

Use these authored artifacts first; reopen their cited primary sources only
if a specific derivation needs checking.

| Topic | Review material | Existing implementation/evidence |
| --- | --- | --- |
| Linear algebra and Gaussian tools | [Week 9 architecture bridge](w09_linear_algebra_in_unets.md); [Week 10 derivations](../proofs/w10_multivariate_gaussian_score.md) | [Gaussian solved notebook](../notebooks/w10_mv_gaussian_score_solved.ipynb) |
| VAE | [ELBO derivation](w11_elbo_derivation.md); [latent-diffusion bridge](w11_why_latent_diffusion.md) | [VAE solved notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb) |
| Flow | [Change-of-variables derivations](../proofs/w12_change_of_variables_flows.md); [flow/score comparison](w12_flows_vs_diffusion.md) | [RealNVP solved notebook](../notebooks/w12_realnvp_2d_blobs_solved.ipynb) |
| Score learning | [Week 8 report](../mini_projects/checkpoint_02_toy_score_matching/report.md); [Week 13 model-objective review](w13_optimization.md#session-8--connect-the-objectives-and-diagnose-training) | [Week 8 saved vector fields](../mini_projects/checkpoint_02_toy_score_matching/report.md#visual-evidence) |
| Optimization | [Update derivations](../proofs/w13_optimizer_updates.md); [clipping report](w13_training_stability_for_diffusion.md) | [Optimizer solved notebook](../notebooks/w13_optimizers_sanity_solved.ipynb) |

## Completion Gate

- [ ] Four mixed solutions are correct and reviewed; optional follow-up questions are recorded separately.
- [ ] The report compares representation, objective, generation procedure, and observed limitations for all three models.
- [ ] Existing figures and numerical claims have traceable sources and appropriate limitations.
- [ ] The score-model discussion distinguishes training targets, marginal scores, and the sampling work still ahead.
- [ ] The final explanation is clear in your own words; the report and local README are ready to skim.
- [ ] Update `PROGRESS.md`, `README.md`, `CURRICULUM.md`, and `MILESTONES.md` after actual completion, then make Week 15 the next step.

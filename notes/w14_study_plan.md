# Week 14 — Generative Toolkit Checkpoint: Study Plan

**Status:** Week 14 is complete as a study checkpoint on 2026-10-27.
Day 1's recall diagnostic closed on
2026-10-19; Day 2 and Problem 1 were reviewed on 2026-10-20; Day 3, Problem 2,
and the VAE evidence discussion were reviewed on 2026-10-21. Day 4, Problem 3,
and the flow evidence discussion were reviewed on 2026-10-22. Day 5, Problem 4,
and the score/optimizer discussion were reviewed on 2026-10-23. All four
mixed problems are reviewed. A full report draft was assembled and reviewed
by the author on 2026-10-26, closing Day 6's study writing. Day 7's final
review and corrections are recorded below, including reference use and
guided score-expectation practice. Blog editing continues separately and
does not block curriculum completion. Week 15's forward-process work is next.

**Pacing:** The original budget was seven study days and about seven hours.
Day 1 exceeded its 45-minute budget; the other days retained their planned
active-study budgets. The times below are budgets, not a measured total.
These are flexible sessions,
not calendar deadlines. Include short follow-up checks within each session's
budget. Stop at the time limit or concrete stopping point, record unresolved
items, and carry them forward instead of extending a recall session indefinitely.

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

- Four reviewed solutions in the [mixed problem set](../proofs/w14_generative_toolkit_mixed_set.md): all four reviewed through 2026-10-23, with reference use and guided corrections recorded.
- A compact [report draft](../mini_projects/checkpoint_03_generative_toolkit_report/report.md)
  (target: 2–3 pages), assembled on 2026-10-26 with a comparison table and
  one existing diagnostic figure per model. The author completed the read-through;
  connections between sections remain for final blog editing.
- A [source README](../mini_projects/checkpoint_03_generative_toolkit_report/README.md)
  linking the notebooks and recording saved-output identities and run settings.
  The three figures are exported into the checkpoint's `figures/` directory.

The mixed problem set is reviewed. A
[Day 6 working draft](../mini_projects/checkpoint_03_generative_toolkit_report/draft.md)
was started on 2026-10-26 and preserves the reviewed answers and corrections.
The readable manuscript and source README are assembled, and the author has
reviewed the wording. Day 6's study writing is closed.
Day 7 checked the identified gaps and recorded the assistance used. The
[completion decision](#day-7-completion-decision) distinguishes checkpoint
completion from fluent unaided formula recall and final blog publication.

## Day-by-Day Schedule

| Day | Time | Focus | Concrete stopping point |
| --- | --- | --- | --- |
| 1 | 45 min planned; exceeded | Retrieve the model map — diagnostic closed 2026-10-19 | Working comparison and three follow-ups recorded below |
| 2 | 60 min budget | Gaussian score and conditioning — reviewed 2026-10-20 | Problem 1 correct; conditioning formula used with notes, with recall recheck assigned to Day 7 |
| 3 | 60 min budget | VAE: ELBO, KL, and generation — reviewed 2026-10-21 | Problem 2 and reconstruction evidence reviewed; bottleneck explanation retained as a hypothesis |
| 4 | 60 min budget | Flow: density, inverse, and expressivity — reviewed 2026-10-22 | Problem 3 and saved plots reviewed; determinant/logarithm corrections and exact-density versus exact-fit distinction recorded |
| 5 | 75 min budget | Score learning and optimizer stability — reviewed 2026-10-23 | Problem 4 and clipping evidence reviewed; longer paired comparison proposed; score-loss floor and diffusion ingredients clarified |
| 6 | 90 min budget | Study draft reviewed; session closed 2026-10-26 | Opening, comparison table, three sourced figures, and diffusion connection reviewed; connections between sections carried forward to blog editing |
| 7 | 30 min active-study budget | Final review and corrections — closed 2026-10-27 | Gaussian reference use and guided score corrections recorded; study checkpoint complete, with two consolidation points carried forward |

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

#### Day 1 Review Record

**Closed on 2026-10-19 as a recall diagnostic.** The discussion covered all
three models and identified enough follow-up work. It expanded beyond the
intended scope, especially into sampling intuition. Several explanations
became correct after hints or worked examples; independent retention still
needs checking on later days.

Working comparison summarized from the discussion, to refine in your own words:

| Model | Representation | Training objective | Generation | Limitation / evidence still to review |
| --- | --- | --- | --- | --- |
| VAE | Encoder gives an image-conditioned Gaussian's mean and log variance; a latent is sampled from it | Maximize the ELBO: reconstruction log-likelihood minus KL to the prior | Draw from the prior, then decode; our notebook displays decoder means | An exact posterior encoder does not guarantee a good generator; inspect reconstruction/generation evidence on Day 3 |
| RealNVP | Invertible, dimension-preserving data-to-latent map | Exact model log-likelihood with the forward Jacobian correction | Draw from the Gaussian base, then apply the inverse map | A single coupling layer leaves one generated marginal unchanged; revisit the one-layer comparison on Day 4 |
| Fixed-noise score toy | Vector field on corrupted inputs | MSE against conditional Gaussian score targets; the population optimum is the marginal noisy-data score | The toy has no implemented sampler; a sampler targeting its fixed-noise density would reproduce the noisy distribution | Score ascent concentrates near modes; it does not reproduce the distribution's spread, and the fixed-noise target is not the clean-data distribution |

**Recall demonstrated:** encoder parameters versus sampled-latent randomness;
the reconstruction/KL tradeoff and prior-to-decoder generation; invertibility
and volume correction; the unchanged-coordinate restriction and alternating
coupling layers; the score's local direction and the need to preserve a
distribution's spread when sampling. Some of these explanations followed
correction, so this is evidence of current understanding, not yet a claim of
independent mastery.

Keep the follow-up list to these three clusters:

| Follow-up | Why it was flagged | Scheduled check |
| --- | --- | --- |
| Score targets, predictions, and sampling scope | Noise scaling needed correction; target averages were initially confused with averaged losses. The weighted-mean example and nonzero loss floor became clear with guidance; sampling intuition is still new | Day 2: a brief noise-scaling check within recall time. Day 5: independently explain the conditional target, marginal score, residual target MSE, and why this toy represents noisy data |
| VAE inference versus generative quality | The posterior is defined by the current model, and its KL gap is different from the prior KL in the ELBO. A fixed-decoder example clarified why exact inference does not improve generation by itself | Day 3: distinguish the two KL terms and explain the fixed-decoder case before reviewing Problem 2 |
| Flow Jacobian direction | The forward and inverse volume factors were initially reversed, then corrected | Day 4: derive the correction using probability mass and check both directions in Problem 3 |

PCA/Gaussian calculations, optimizer stability, and interpretation of saved
experimental results were not independently assessed today. They remain in
the existing schedule; do not count them as diagnosed weaknesses.

**Sampling boundary:** Day 5 needs a conceptual account of what the fixed-noise
toy learns and what a diffusion generator still needs. Sampler derivations,
implementation, and convergence theory belong to later lessons and do not
block closing Day 1.

For each scheduled check, attempt a fresh small example without notes or hints
first. Record whether it was independent or guided. Revisit unresolved items
on Day 7; do not add a new extended Day 1 session.

### Day 2 — Gaussian Score and Conditioning

Allow about 10 minutes for recall, 35 for Problem 1, and 15 to review the
derivation against your Week 10 work. Explain the score's direction using
covariance geometry, then distinguish conditioning from taking a marginal.
Use at most five minutes of the recall period to recheck the Day 1 noise-scaling
slip before moving to Problem 1.

**Stop when:** the gradient and conditional distribution are correct, and you
can explain why covariance changes both the score field and conditional
uncertainty. Correct the reasoning before polishing the solution.

#### Day 2 Review Record

**Reviewed on 2026-10-20; move to Day 3.** The warm-up's noise scaling was
correct; the initial marginal notation was corrected to the conditional
corruption density. The Gaussian score derivation, numerical evaluation,
conditional calculation, and marginal comparison are recorded in
[Problem 1](../proofs/w14_generative_toolkit_mixed_set.md#problem-1--gaussian-score-and-conditioning).

The conditioning formula was looked up in the Week 10 proof note and then
applied correctly. The mean-shift and variance-reduction explanation was
also correct. Count this as correct application with notes; unaided recall
of the conditioning formula remains to be checked briefly with changed
numbers on Day 7. No extra Day 2 session is needed for that recall check.

### Day 3 — VAE: What the Objective Buys Us

Use roughly 35 minutes for Problem 2, 15 to inspect saved VAE loss curves and
reconstructions, and 10 to record the interpretation.
Within the problem time, start with a brief independent explanation of the
two KL terms and why improving only the encoder leaves generation unchanged.

Separate reconstruction through the encoder from generation using the prior.
Remember that the notebook displays decoder means; those are different from
full samples of its Gaussian observation model. Pick one visible limitation
from the reviewed experiment, and distinguish the observation from possible
causes such as bottleneck size, model capacity, or brief training.

**Stop when:** you can connect the ELBO to the implemented loss and say what
the saved reconstruction or generation plot establishes. Do not diagnose
posterior collapse merely because a reconstruction looks blurry.

#### Day 3 Review Record

**Reviewed on 2026-10-21; move to Day 4.** The
[Problem 2 solution](../proofs/w14_generative_toolkit_mixed_set.md#problem-2--elbo-kl-and-the-implemented-loss)
records the ELBO identity, analytic Gaussian KL, sampled negative-ELBO loss,
and the VAE evidence interpretation.

The ELBO identity was recalled without notes. Review clarified that the
true posterior is a distribution defined by the model, equality with the
ELBO is allowed, and increasing the ELBO forces the posterior gap down only
when the generative model is fixed. The Gaussian KL calculation used the
Week 11 note and the learner's KL post; a base-10 numerical evaluation was
corrected to natural logarithms. The reconstruction scaling, positive KL
sign, and omitted constant were correct. A log-variance/variance notation
slip in the sampling setup was also corrected.

The learner identified improved reconstruction, remaining ambiguous digits,
and a plausible two-dimensional bottleneck explanation. The record separates
reconstruction evidence from unconditional generation and keeps the proposed
cause as a hypothesis. Include the fixed-model ELBO-gap qualification in
the existing Day 7 VAE check; no additional Day 3 session is needed.

### Day 4 — Flow: Exact Density and an Architectural Limit

Use roughly 35 minutes for Problem 3, 15 to inspect the saved six-layer versus
one-layer comparison, and 10 to record the interpretation.
Use Problem 3 itself to recheck forward versus inverse volume correction;
no additional exercise set is needed.

Keep the notebook's convention explicit: forward maps data to latent space;
inverse generates from the Gaussian base. Connect the unchanged coordinate
in a single coupling layer to the observed first-coordinate marginal.

**Stop when:** the inverse and determinant sign agree, and you can distinguish
exact evaluation of the model's density from an exact fit to the data.

#### Day 4 Review Record

**Reviewed on 2026-10-22; move to Day 5.** The
[Problem 3 solution](../proofs/w14_generative_toolkit_mixed_set.md#problem-3--change-of-variables-and-an-unchanged-coordinate)
records the inverse, Jacobians, evaluated density, architectural limitation,
and interpretation of the saved Week 12 plots.

The inverse and the latent point were correct on the first attempt.
Feedback corrected a swapped Jacobian row, base-10 versus natural logarithms,
and applying a logarithm twice. The learner self-corrected the inverse
determinant to the reciprocal of the determinant after initially suggesting
the reciprocal of its logarithm. The positive forward correction was
recalled correctly.

After clarifying that generation starts from the Gaussian base, the learner
explained the one-layer restriction and why alternating coordinates improves
the first marginal. The learner also identified generated bridges between
the four blobs as evidence that exact model-density evaluation does not
guarantee exact fit. The follow-up explanation separated this issue from
floating-point roundoff and distinguished an ideal transformation's existence
from what our finite architecture and training can achieve.

These are reviewed answers with corrections, not independent mastery of
every detail. Keep a brief determinant/log-determinant check and the exact-fit
explanation inside the existing Day 7 flow review. No additional Day 4
session or new training is required.

### Day 5 — Score Learning and Optimization

Spend about 20 minutes revisiting the Week 8 report and Week 13 score-objective
review, 35 on Problem 4, and 20 connecting the pieces.
Include a brief independent check of the Day 1 score-target distinction in
the review time. Keep sampler discussion at the conceptual boundary above.

Explain these three objects separately: the conditional Gaussian score used
as a training target, the marginal noisy-mixture score used for evaluation,
and the parameter gradient used by the optimizer. Then state what our toy
does not yet provide: a model across noise levels and a reverse sampler.

**Stop when:** you can interpret the clipping result without claiming either
that clipping always helps or that it is generally harmful. Identify the
missing ingredients for diffusion sampling; implementing them belongs later.

#### Day 5 Review Record

**Reviewed on 2026-10-23; move to Day 6.** The
[Problem 4 solution](../proofs/w14_generative_toolkit_mixed_set.md#problem-4--stability-and-what-clipping-actually-established)
records the score warm-up, gradient-descent derivation, clipping interpretation,
and the proposed follow-up.

The learner recalled the conditional Gaussian target and its noise scaling
correctly without notes, identified its conditional density, and chose the
weighted mean as the MSE-optimal prediction. The expected-error expression
was correct; evaluating the nonzero loss floor needed a prompt to use the
two target values and weights. Review explained why that residual target
MSE can coexist with a correct marginal score prediction.

The quadratic gradient, both coordinate recurrences, the common learning-rate
range, and all three convergence classifications were correct in the staged
first attempts. The learner also correctly separated the applied-gradient
bound from held-out score accuracy and limited the conclusion to the saved run.

The proposed next test extends both clipping conditions to the same longer
budget while preserving matched controls, then compares held-out score MSE
at common intermediate checkpoints and the end. This is a design only;
no new training was run.

The learner identified multiple noise levels and reverse sampling as missing
ingredients. Review added that the model must receive the noise level and
clarified that an analytical real-data score is not required for training;
the known Gaussian corruption supplies the target. Keep that clarification
and the loss-floor check inside the existing Day 7 score discussion.

All four problems and the planned evidence reviews are now reviewed.
The report and final recall review remained at Day 5's close; both were
subsequently completed in Days 6–7. No additional Day 5 exercises were assigned.

### Day 6 — Write the Report from Existing Evidence

**Study draft reviewed; Day 6 closed on 2026-10-26.** The
[working draft](../mini_projects/checkpoint_03_generative_toolkit_report/draft.md)
preserves the reviewed evidence paragraphs, all three model answers, and
a compact comparison table. The brief diffusion connection is also reviewed,
with corrections distinguishing backpropagation from reverse sampling and
score-error evidence from generated samples. The author's opening, table,
figures, and closing connection are now in the
[readable manuscript](../mini_projects/checkpoint_03_generative_toolkit_report/report.md).
The author plans to use this text as a blog post as well as the checkpoint
report. Website preparation is separate from the 90-minute drafting budget.

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

#### Day 6 Draft Record

**Assembled on 2026-10-26.** The author supplied the reader aim, three
evidence interpretations, model-comparison answers, diffusion connection,
and personal opening. The working record preserves technical corrections;
the manuscript contains the reviewed prose, comparison table, and three
unchanged saved figures. The source README records the experiment settings
and distinguishes the separate datasets, objectives, and flow training budgets.

**Author read-through completed on 2026-10-26.** The author said the wording
sounds good so far and identified connections between sections as remaining
work for the final blog. Day 6's study writing is closed. Those connections,
the title, and website preparation can follow during blog editing.
Guided corrections do not establish independent recall. The identified checks
were carried into Day 7 and completed with assistance recorded below.

### Day 7 — Review and Decide Whether the Checkpoint Is Complete

Include a brief recheck of the Day 2 conditioning formula with changed
numbers before opening notes. Keep it within this session's 30-minute budget.
Within the existing flow review, briefly recheck a determinant, its natural
logarithm, and the inverse correction using fresh numbers.
Use the existing score questions to recheck why target MSE can remain
nonzero and why analytical marginal scores are not required for training.
Within the existing diffusion-ingredients question, distinguish
backpropagation during training from the reverse procedure used to generate
samples; the Day 6 paragraph needed this correction.

Explain the report aloud without reading it, then review any weak answer:

- Why does the VAE use a bound, while this flow evaluates its density exactly? In the VAE explanation, state when increasing the ELBO necessarily decreases the posterior KL gap.
- Why can exact flow likelihood coexist with a visibly imperfect fit, even with exact arithmetic?
- Why is a score a vector field rather than a probability or a sample?
- Why can smaller applied gradients coexist with worse held-out score MSE?
- What do Weeks 15–16 add beyond our single-noise-level score toy?

Use the remaining time for corrections. If a central answer is still unclear,
leave that item open and add a short review sitting rather than marking the
week complete on schedule.

#### Day 7 Review Record

**Closed on 2026-10-27; 30-minute active-study budget.** The four mixed
problems and study draft were already reviewed. This session checked the
recorded gaps and included brief corrections, with reference use and guided
answers distinguished from independent recall. The author is handling the
blog in a separate thread.

First attempts were requested without notes; subsequent reference use and
prompting are recorded below. The first check used fresh Gaussian conditioning values: mean
vector (-1, 2), covariance rows (4, 2) and (2, 3), conditioning on the first
coordinate being 3.

- **Conditional Gaussian formula recall:** The learner remembered covariance
  blocks and a mean-dependent shift, but could not recall the exact formulas.
  A reference lookup was used; this is not unaided formula recall.
- **Conditional Gaussian application:** Correct with the formulas available.
  The learner selected the covariance entries correctly and calculated a
  conditional mean of 4 and variance of 2. Interpretation was not separately
  rechecked in this answer.
- **VAE ELBO and posterior KL gap:** Correct without notes. The learner
  recalled the likelihood/ELBO/gap identity and held log-likelihood at 4:
  raising the ELBO from 1 to 3 lowers the posterior KL gap from 3 to 1.
  Feedback connects fixed likelihood to holding the prior, decoder, and
  observed input fixed while changing the encoder; joint training need not
  keep likelihood fixed.
- **VAE versus RealNVP likelihood:** The learner correctly recalled the
  central distinction without notes: an invertible change of variables for
  RealNVP versus integrating over latent values in the VAE. Feedback makes
  the tractable Jacobian determinant explicit and corrects sampling wording:
  inverse sampling draws from the learned model, which need not equal the
  true data distribution.
- **Flow Jacobian calculation:** Correct inverse mapping and forward
  Jacobian for z1 = x1 and z2 = 3*x2 - 2*x1. The forward determinant is 3,
  the inverse determinant is 1/3, and the data log-density correction is
  +ln(3). Feedback clarifies notation: use f(x) when f maps data to latents;
  g-inverse(x) is equivalent if g denotes the generative map.
- **Exact likelihood versus data fit:** Correct conceptual distinction.
  The learner explained that exact likelihood evaluation does not remove the
  need to fit the model to the data through training. Feedback clarifies
  terminology: likelihood evaluates the model density on observed data;
  this does not establish equality with the underlying data distribution.
- **Ideal score prediction, first attempt:** The learner described weighting
  possible clean origins for a fixed noisy input, but wrote E[Xt | X0].
  The conditioning is reversed, and the averaged quantity must be the
  conditional corruption score target rather than the noisy input.
  This prompted the guided correction and transfer check recorded below.
- **Score prediction, guided second attempt:** The learner wrote E[X0 | Xt],
  fixing the conditioning direction but averaging the clean point rather than
  the score target. This is the posterior mean clean point, not the score.
- **Score-prediction correction:** Feedback explained that the ideal predictor is E[Y | Xt],
  equal to (E[X0 | Xt] - Xt)/sigma^2 for this Gaussian corruption. This is
  the marginal noisy-data score. The learner correctly applied the supplied
  relationship with noisy input 5, posterior clean-point mean 3, and noise
  variance 2, obtaining (3 - 5)/2 = -1. This is a correct guided application;
  it does not establish unaided recall of the conditional-expectation identity.
- **Score-loss floor:** Correct conceptual explanation. The learner described
  the expected training MSE as score error plus an irreducible floor: several
  clean origins can produce the same noisy input, so predicting the conditional
  mean cannot match every individual target. Their example uses clean values
  2 and 4, each corrupted to 3, with weights 0.75 and 0.25.
- **Score-prediction transfer check:** With those weights conditional on
  noisy input 3 and noise variance 1, the learner correctly calculated the
  posterior mean clean point as 2.5 and set up (2.5 - 3)/1 for the score.
  They reported -1.5; feedback corrects the subtraction to -0.5. The setup
  demonstrates the clean-mean versus score distinction after guidance;
  the remaining error in this answer was arithmetic.
- **Training targets without an analytical marginal score:** Correct.
  The learner supplied Y = -(Xt - X0)/sigma^2 and identified the clean image,
  corrupted input, and known noise scale as sufficient to compute it. They
  correctly distinguished this from the generally unknown analytical marginal
  noisy-data score. Feedback notes that the analytical marginal score in the
  blob experiment supported evaluation, not construction of training targets.
- **Gradient clipping versus score accuracy:** Correct interpretation.
  The learner explained that clipping does not guarantee lower held-out score
  MSE, can help control very large gradients, and can also provide no benefit
  or worsen results. They explicitly treated slower convergence from smaller
  updates as a hypothesis. Feedback preserves the observed 20-update result
  separately from this untested longer-training explanation.
- **Diffusion ingredients and training versus sampling:** The learner
  correctly described Gaussian forward corruption, a computable training
  target, learning the model's weights, and the missing reverse sampler and
  multiple noise levels. Feedback makes the noise-level/timestep input
  explicit. It also specifies that backpropagation computes gradients and
  the optimizer updates weights during training; sampling uses fixed trained
  weights to update noisy samples. The broad distinction was recalled; these
  implementation details were clarified rather than independently tested.

The learner completes questions between other tasks. Count estimated active
study time toward the 30-minute budget, excluding breaks between responses.

#### Day 7 Completion Decision

**Week 14 study checkpoint complete on 2026-10-27.** The four reviewed
problems, comparison report with sourced figures, and final model review
meet the checkpoint's study outcomes. The final review supports moving to
Week 15; it does not establish unaided mastery of every formula.

Two consolidation points carry forward into the next week's normal study:

- Gaussian conditioning was applied correctly with a formula reference.
  Keep that reference available; full block-matrix formula memorization was
  not required for this checkpoint.
- Distinguishing a conditional mean clean point from a conditional mean score
  target needed guidance. The learner then set up the transformation correctly
  in a fresh example, with one arithmetic correction. Briefly revisit this
  distinction while studying the forward process; do not treat the guided
  work as independent recall of the identity.

The blog's section connections, score-section revision, title, and publication
remain separate editorial work. The proposed longer clipping comparison
remains an unrun follow-up experiment, not a requirement for closing Week 14.

## Four Bounded Practice Problems

These are independent checkpoint prompts based on the completed material,
not exercises attributed to a book or an official solution set. Attempt each
before consulting the linked derivations. The [reviewed solutions](../proofs/w14_generative_toolkit_mixed_set.md)
are kept separately so these prompts can still be used for recall practice.

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

Completed on 2026-10-27; the [completion decision](#day-7-completion-decision)
records the reference use and guided corrections behind this outcome.

- [x] Four mixed solutions are correct and reviewed; optional follow-up questions are recorded separately.
- [x] The report compares representation, objective, generation procedure, and observed limitations for all three models.
- [x] Existing figures and numerical claims have traceable sources and appropriate limitations.
- [x] The score-model discussion distinguishes training targets, marginal scores, and the sampling work still ahead.
- [x] The final explanation is clear in your own words; the report and local README are ready to skim.
- [x] `PROGRESS.md`, `README.md`, `CURRICULUM.md`, and `MILESTONES.md` record completion and Week 15 as the next step.

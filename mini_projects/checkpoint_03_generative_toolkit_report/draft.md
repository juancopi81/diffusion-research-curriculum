# Week 14 — Day 6 Working Draft

**Updated:** 2026-10-27 (study closeout; blog editing remains separate).

**Status:** Working record of the author's answers after technical review.
Grammar and technical corrections are incorporated below. The author reviewed
the study draft on 2026-10-26; Day 6 is closed. Week 14's study checkpoint
closed on 2026-10-27 after the final review and corrections. Connections
between sections and the title remain for final blog editing.

**Use:** Keep this file as the session record while writing. The readable
first manuscript is now [report.md](report.md), with figure provenance in
[README.md](README.md). All three model rows, the evidence paragraphs, the
brief diffusion connection, and the author's opening are recorded here.
The author has completed the read-through. The
[Day 7 closeout](../../notes/w14_study_plan.md#day-7-completion-decision)
records reference use and guided corrections. Preserve the remaining blog
work recorded below; blog editing and the study review use separate threads.
This working record can be consolidated or removed after finalization.

## Opening — Reviewed Paragraphs

Over the past few days, I have been working with three different approaches
to generative modeling: VAE, RealNVP, and score models—in this case, a "toy"
version with one fixed noise level. They all use probability theory and
distributions from which we know how to sample, like a standard normal, to
study complex data distributions, such as distributions over images.

These methods have different strategies, with their own advantages and
limitations, and show us how researchers come up with different architectures
using common knowledge. Seeing them in retrospect could make you feel like
"I could have thought of that..." but
["hindsight is 20/20"](https://www.merriam-webster.com/dictionary/twenty-twenty%20hindsight).
All three use clever insights and engineering tricks that are worth studying
carefully.

On a personal note, I believe RealNVP is a very clever idea and a wonderful
implementation. When I first learned about the change-of-variables theorem
in [Stats 110](../../notes/w06_stat110_transformations_convolutions.md),
I immediately thought that these transformations should be useful in a
generative model, and here I am reading about normalizing flows. I wonder
if we can still squeeze any more out of this method.

Today, I want to briefly summarize some notes and experiments about the
aforementioned models, aiming to better organize what I have learned before
moving forward.

**Review note:** Grammar, tense, and the idiom's spelling were corrected.
"One fixed noise level" clarifies the toy's scope. The opening no longer
implies that all three experiments already generate samples from a standard
normal: the score toy uses Gaussian corruption noise and has no sampler.
The personal assessment of RealNVP and the author's open question are retained.

## Models and Experiments — Reviewed Roadmap

This post does not aim to go into the details of each model or explain the
specifics of the code used as learning material to explore the concepts in
a practical manner. For that, I highly recommend going to the following links:

- VAE: [Notes](../../notes/w11_cs236_vae.md) — [Experiment](../../notebooks/w11_minimal_vae_mnist_solved.ipynb).
- RealNVP: [Notes](../../notes/w12_cs236_normalizing_flows.md) — [Experiment](../../notebooks/w12_realnvp_2d_blobs_solved.ipynb).
- Toy Score Model: [Notes](../../notes/w07_conditional_expectation_in_diffusion.md) — [Experiment](../checkpoint_02_toy_score_matching/report.md).

Instead, what I would like to do here is show a concise comparison of these
methods (see the table below) and share some general observations about the
artifacts generated during the experiments.

Finally, I want to add a small section about how these models connect with
diffusion models and leave some open questions that I might revisit later
in the blog.

**Review note:** Added from the author's blog-editing draft on 2026-10-26.
Corrected spelling and grammar, using "aim" for the intended meaning of
"pretend" and "general observations about" for "global observations of."
Removed pasted line-break escapes and the trailing HTML space entity.
The link placeholders now point to the existing theory notes and solved
experiments; the score links cover conditional expectation and the Week 8
toy experiment. Public destinations will be checked during website preparation.
The promised open questions remain for the author to supply.

## Reader Aim and Scope

I want the reader to understand what these three models learn, their training
objectives, and how generation works for each approach. Using our experiments,
I'll discuss the strengths and limitations we observed, then explain which
ideas connect to diffusion.

- Write one comparison that can serve as both a blog post and the checkpoint
  report. The author retains the question, title, framing, and prose voice.
- Keep the comparison grounded in the MNIST VAE, the 2D RealNVP, and the
  fixed-noise score toy. These use different datasets and objectives, so raw
  loss values do not rank the three approaches.
- Keep the diffusion connection brief. Flow matching is outside this draft's
  agreed scope. The [score-loss-floor study](../../notebooks/w13_score_loss_floor_study.html)
  remains material for a separate focused post.
- Retain the 90-minute Day 6 drafting budget. Website preparation and
  publication are separate from today's writing. Reuse saved results.

## Model Comparison — Reviewed Answers

### VAE

**What the model learns**

The VAE learns two conditional probability distributions:

- Encoder: a distribution over latent representations given an original image.
- Decoder: a distribution over images given a latent representation.

We choose a prior from which we know how to sample, such as a standard normal.
The KL term encourages the encoder's distributions to stay close to this
prior; it does not require every image to have the same latent distribution.

**Training objective**

Maximize the ELBO, or in practice minimize the negative ELBO. The negative
ELBO consists of the expected reconstruction loss plus the KL divergence
from the encoder's conditional distribution (the approximate posterior)
to the prior. The ELBO is a lower bound on the model log-likelihood.

**How we generate a new sample**

We sample a latent from the prior and send it through the decoder. In our
notebook, we display the decoder's mean image.

**Observed limitation**

Some reconstructed digits remained blurry and ambiguous, with different
input digits producing similar reconstructions.

### RealNVP

**What the model learns**

RealNVP learns an invertible (bijective) mapping between data space and latent
space, with a simple base distribution from which we know how to sample,
such as a standard normal. The mapping is invertible by construction;
training aims to make the resulting model distribution fit the data.

**Training objective**

Maximize the exact model log-likelihood using the Jacobian correction,
or equivalently minimize the negative log-likelihood.

**How we generate a new sample**

We sample a latent from the base distribution and apply the inverse of our
data-to-latent mapping.

**Observed limitation**

In our one-layer model, the first coordinate remains unchanged, so its
generated marginal stays Gaussian and cannot match the data's bimodal
first-coordinate shape. The six-layer model captures the two peaks more
closely, but its sample histogram still differs from the data histogram.

### Fixed-noise Score Toy

**What the model learns**

In this experiment, we trained a model to approximate the marginal score of
the noisy-data distribution:

$$
s_\theta(x_t)\approx\nabla_{x_t}\log p_\sigma(x_t).
$$

The model parameters belong to the score predictor. The target density is
determined by the data distribution and the chosen corruption level.
We do not train an explicit normalized density model in this toy.

**Training objective**

Minimize the mean squared error between the model's output and the
conditional Gaussian corruption score. For our additive corruption,

$$
x_t=x_0+\sigma\epsilon,\qquad \epsilon\sim\mathcal N(0,I),
$$

the target is

$$
y=-\frac{\epsilon}{\sigma}
=-\frac{x_t-x_0}{\sigma^2}
=\frac{x_0-x_t}{\sigma^2}.
$$

The objective averages over clean samples, fresh corruption noise, and
the input coordinates:

$$
\mathcal L(\theta)=
\mathbb E_{x_0,\epsilon}\left[
\frac{1}{d}\left\|s_\theta(x_t)-y\right\|_2^2
\right].
$$

The denominator uses the corruption standard deviation, not the model
parameters. These conditional targets provide supervision for learning
the marginal score.

**How we generate a new sample**

We have not implemented a sampler in this experiment. Our toy learns and
evaluates a score field at one noise level. Sampling from a standard normal
and simply following this fixed score field is not, by itself, a valid
generation procedure for our data.

For the later diffusion connection, the missing components are learning
across noise levels with noise-level conditioning and using a reverse
sampler from a suitable high-noise starting distribution.

**Observed limitation**

We trained our toy score model for only 20 updates. At the end of this budget,
its predictions still differed from the analytical marginal score on
held-out noisy data. The short budget is a possible contributor to this
remaining error, but this run does not isolate its cause or establish
what longer training would achieve.

The [Week 13 stability note](../../notes/w13_training_stability_for_diffusion.md)
records the held-out score error for the clipping comparison selected here.
The earlier [Week 8 report](../checkpoint_02_toy_score_matching/report.md)
also describes underfitting in its direct-score run; its measurements are
from a separate experiment.

## Compact Comparison Table

Condensed from the reviewed answers above for use in the author's manuscript.

| Model | What it learns | Training objective | Generation in our experiment | Observed limitation |
| --- | --- | --- | --- | --- |
| VAE | Encoder and decoder conditional distributions | Minimize negative ELBO: expected reconstruction loss plus KL from approximate posterior to prior | Sample a latent from the prior and display the decoder's mean image | Several reconstructed digits remained blurry or ambiguous |
| RealNVP | An invertible mapping between data and latent spaces | Maximize exact model log-likelihood with the Jacobian correction | Sample from the base distribution and apply the inverse data-to-latent map | One layer leaves the first generated marginal Gaussian; the six-layer sample histogram still differs from the data histogram |
| Fixed-noise score toy | The marginal score of the noisy-data distribution at one noise level | Minimize MSE against conditional Gaussian corruption scores | Not implemented; the experiment learns and evaluates a score field | Held-out marginal-score error remained after 20 updates |

## Selected Evidence — Reviewed Paragraphs

### VAE Reconstruction Panel

**Source:** [Week 11 solved notebook](../../notebooks/w11_minimal_vae_mnist_solved.ipynb),
cell ID `reconstructions` (zero-based cell 23), saved figure titled
"Same inputs, before and after learning."

This panel demonstrates how our VAE experiment learns to reconstruct selected
images from MNIST. The first row shows the original images. In the second
row, we see the noisy-looking outputs produced before training. Rows 3 and 4
show how, after training, the reconstructions begin to resemble the input
digits. Row 3 uses the encoder's mean latent vector, while row 4 uses a latent
sampled from the encoder's distribution.

Reconstructions in rows 3 and 4 still show limitations. The digits 0 and 1
are recognizable, while several other digits remain blurry and ambiguous.
For example, the reconstructions of 4, 5, 8, and 9 look very similar despite
coming from different input digits.

### RealNVP One-layer and Six-layer Comparison

**Source:** [Week 12 solved notebook](../../notebooks/w12_realnvp_2d_blobs_solved.ipynb),
cell ID `9c459c26` (zero-based cell 20), saved two-panel figure with the titles
"One layer: first coordinate stays Gaussian" and "First-coordinate marginal."

This figure shows results from RealNVP models trained on two-dimensional
data. On the left, we have the synthetic data from our experiment compared
against generated samples from a one-layer model. The right panel compares
the first-coordinate marginal of the original data with those of the one-
and six-layer models' generated samples.

The one-layer model leaves its first coordinate unchanged, so its generated
first-coordinate marginal has the same Gaussian distribution as the first
coordinate of our base distribution. The six-layer model alternates which
coordinate is transformed, allowing both coordinates to change across
layers. In the right panel, it captures the bimodal shape of the data's
first coordinate.

Still, even with six layers, the green histogram does not perfectly align
with the blue data histogram, although it captures the two main peaks.

### Score-model Clipping Comparison

**Source:** [Week 13 stability note](../../notes/w13_training_stability_for_diffusion.md)
and its [saved figure](../../notes/figures/w13_score_clipping_comparison.png),
exported from the [Week 13 solved notebook](../../notebooks/w13_optimizers_sanity_solved.ipynb).
The source note records the matched initialization, data, noise draws, and
SGD configuration for the 20-update comparison.

The three-panel figure shows an experiment applying gradient clipping to
our toy score model. When clipping was on, we capped the global gradient
norm used for each parameter update at 0.5. Without clipping, we applied
the gradients without that restriction as the control condition.

In this experiment, clipping bounded the applied gradient norm as intended,
but it did not improve held-out score accuracy over 20 updates. The model
trained without clipping achieved lower held-out marginal-score MSE.

## Connection to Diffusion — Reviewed Paragraph

The score toy is a step toward a score-based diffusion model: it already
includes Gaussian forward corruption and a training objective that teaches
the network to approximate the marginal score of the noisy-data distribution.
The model learned through gradient-based training, with improvement shown
by the decrease in held-out marginal-score MSE. We still need to train across
multiple noise levels, give the model the corresponding noise level, and add
a proper sampling procedure that moves from a suitable high-noise
distribution toward the data distribution.

**Review note:** The author's first version described a backward process and
generated samples. Review clarified that backpropagation computes parameter
gradients for training; it is not reverse-process sampling. The score toy
did not generate samples. The correction above uses the saved held-out
score-error curve as evidence. Day 7 rechecked the broad training-versus-sampling
distinction; feedback added noise-level conditioning and clarified that sampling
changes noisy samples while trained weights stay fixed. The
[review record](../../notes/w14_study_plan.md#day-7-review-record) separates
recalled ideas from those refinements.

## Technical Corrections to Preserve During Final Writing

These are review notes, not additional prose automatically assigned to the post.

- The VAE panel shows reconstructions of the supplied inputs. It does not
  demonstrate generation from the prior. The displayed decoder outputs are
  mean images; no observation noise was added to those panels.
- The negative ELBO adds reconstruction loss and KL; the ELBO itself uses
  expected reconstruction log-likelihood minus KL. The KL direction is from
  the approximate posterior to the prior.
- Accurate VAE posterior inference alone does not guarantee a good generator.
  That theoretical distinction does not establish the cause of our blurry
  reconstructions. The two-dimensional latent bottleneck remains a hypothesis
  if discussed as a cause.
- For RealNVP, an invertible transformation and exact evaluation of the model
  density do not guarantee an exact fit to the data distribution. The six-layer
  result does not establish that an exact fit is impossible in principle.
- The RealNVP plots use generated samples, not reconstructions. Finite-sample
  histograms can differ partly through sampling variability; describe the
  observed agreement without treating every bin difference as proven density
  error.
- Clipping bounds applied parameter gradients. Raw gradients can still exceed
  the threshold. The score comparison concerns held-out marginal-score MSE,
  with a conclusion limited to the saved configuration and 20-update budget.
- In the score row, model parameters belong to the score predictor; the
  target noisy-data density is fixed by the data and corruption. Correct the
  author's noise-scale symbol from theta to sigma and remove the extra minus
  sign when writing the target with clean point minus noisy point.
- Deterministically following a fixed score field toward density peaks is not
  a complete sampling procedure. The toy's noisy three-blob distribution at
  its fixed noise level is not a standard normal starting distribution.
- Residual held-out marginal-score error shows an imperfect learned field.
  Nonzero training-target MSE alone would not establish underfitting: even an
  ideal marginal-score predictor can have a nonzero target-loss floor.
- A neural-network forward pass computes predictions; backpropagation computes
  parameter gradients for training, which the optimizer uses to update weights.
  These operations are distinct from forward corruption and reverse-process
  sampling. A generative reverse procedure updates noisy samples using the
  trained model. Our toy includes corruption and score training, but no
  generative reverse sampler.

## Manuscript Assembly — 2026-10-26

The [first manuscript](report.md) combines the reviewed opening, comparison
table, three evidence paragraphs and figures, and diffusion connection.
These reviewed passages are unchanged in the assembly. The added headings,
image placement, alt text, and source pointers provide structure.
The [source README](README.md) records each saved figure's identity and run
configuration, including the different training budgets in the flow comparison.

The original source notebooks were not executed or modified. All three
exported figures match their saved sources. The study-review annotations
remain here rather than becoming additional manuscript prose.

## Author Read-through — 2026-10-26

The author said that "what I read sounds good so far" and noted that the
final blog needs connections between sections. This closes Day 6 at the
study-draft stage; it does not mark the final blog ready for publication.

## Remaining Blog Editing

1. The author's "Models and Experiments" roadmap is now before the comparison
   table. Continue making connections between the model sections explicit,
   preserving the author's voice and the reviewed claims.
2. Refocus the score section on what the model learns. The author identified
   its current emphasis on clipping; the saved analytical and learned score
   fields from Week 8 are proposed replacements for the main figure.
   Figure selection and the revised interpretation remain to be reviewed.
3. Finish the diffusion connection and add the author's open questions,
   as promised in the roadmap.
4. The final blog title remains the author's choice. Website formatting,
   cards, and publication are separate from the checkpoint writing session.
   No blog post or card has been created or published.

Week 14's study checkpoint is complete. Day 7 recorded Gaussian formula
reference use and guided score-expectation corrections as consolidation points
for later study; final blog editing remains separate from that completion.

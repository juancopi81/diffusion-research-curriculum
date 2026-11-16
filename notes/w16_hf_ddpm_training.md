# Week 16 — DDPM Training and Sampling

**Status:** Day 1 completed on 2026-11-16, including Juan's read-through
and approval of this consolidated note. Week 16 is in progress;
the parameterization derivations, sampler study, and experiment remain ahead.
The [daily plan](w16_study_plan.md) gives the sequence.

## Day 1 — My Explanation of One Training Example

The following preserves Juan's opening explanation after reading, with
notation and wording cleaned. It was not a notes-closed recall test.

We take an image from our dataset and call it $x_0$, treating it as a
sample from the original, possibly complex data distribution $q(x_0)$.
We sample a timestep uniformly from $1$ to $T$; the DDPM example uses
$T=1000$. Then we sample standard Gaussian noise $\epsilon$.

Using the "nice property" from Week 15, we construct

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon,
\qquad \epsilon\sim\mathcal N(0,I).
$$

We send $x_t$ and $t$ through the neural network and get its predicted
noise, $\epsilon_\theta(x_t,t)$. We compare that output with the actual
noise we used to create the input, calculate MSE, backpropagate the loss,
and update the model's weights.

**Notation clarified by Codex:** For an image with $d$ scalar coordinates,
one example's MSE is

$$
\operatorname{MSE}
=\frac{1}{d}\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|_2^2.
$$

The simplified population objective is conventionally written without the
constant $1/d$:

$$
\mathcal L_{\mathrm{simple}}
=\mathbb E_{x_0,t,\epsilon}
\left[\left\|\epsilon-\epsilon_\theta(x_t,t)\right\|_2^2\right].
$$

The expectation averages over clean examples, sampled timesteps, and
Gaussian draws. In practice, we estimate it with batches. The target is
available because we generated the corruption ourselves; evaluating an
analytic MNIST density or score is unnecessary for constructing it.

## My Questions About the Reading

I asked why predicting noise changes the implicit weighting of errors,
how the VAE/ELBO connection leads to this objective, and why we predict
noise instead of directly predicting the reverse mean.

**Overview added by Codex:** The noisy states $x_1,\ldots,x_T$ act as latent
variables. The fixed forward distribution $q(x_{1:T}\mid x_0)$ plays the
inference role, while the learned reverse chain defines the generative
model starting from a Gaussian prior. With fixed reverse variances, the
variational bound's intermediate Gaussian KL terms give weighted errors
between reverse means. Expressing those means through noise predictions gives weighted
noise errors. DDPM's simplified objective drops the bound's
timestep-dependent weights. Changing the predicted quantity and changing
the loss weights are distinct choices. See [DDPM, Sections 2–3](https://arxiv.org/pdf/2006.11239#page=2).

Clean-image and noise errors also differ by a timestep-dependent scale
when the predictions are converted consistently. Consequently, their
unweighted MSE objectives emphasize timesteps differently. The
[HF training-objective subsection](https://huggingface.co/learn/diffusion-course/en/unit1/3#training-objective)
introduces this distinction; deriving the factor remains Day 2 work.
These were explanations supplied during discussion, not derivations Juan
completed today.

## Reverse Mean, Predicted Noise, and Fresh Sampling Noise

Codex supplied the following reference formula, also given in
[Annotated Diffusion's objective section](https://huggingface.co/blog/annotated-diffusion#defining-an-objective-function-by-reparametrizing-the-mean):

$$
\mu_\theta(x_t,t)
=\frac{1}{\sqrt{\alpha_t}}
\left(
x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}
\epsilon_\theta(x_t,t)
\right).
$$

My first response correctly identified that the schedule's scaling matters
and that a mean is used to generate $x_{t-1}$. I also suggested that
$x_t-\epsilon_\theta(x_t,t)$ might recover $x_{t-1}$, and mixed the
predicted noise with the randomness used to sample the preceding state.

**Correction supplied by Codex:** Raw subtraction uses the wrong scaling.
The displayed mean already includes the required coefficients. For our
chosen Gaussian reverse transition, sampling uses

$$
x_{t-1}=\mu_\theta(x_t,t)+\sigma_t z,
\qquad z\sim\mathcal N(0,I).
$$

The predicted noise is used inside the mean; $z$ is a fresh draw around
that mean. The reverse standard deviation $\sigma_t$ follows the chosen
variance rule. Our planned sampler adds no fresh noise in the final
transition to $x_0$.

With that explanation and formula available, I correctly answered that
holding $x_t$, $t$, and trained weights fixed holds the predicted noise,
mean, and variance fixed. Independent $z$ draws produce different samples
around that same mean when the variance is positive. I noted that
independence alone does not forbid equal draws; Codex clarified that exact
equality has probability zero for independent continuous Gaussian draws.

I explicitly checked that we had not yet derived $\mu_\theta$. Codex
confirmed: the derivation uses the tractable Gaussian posterior
$q(x_{t-1}\mid x_t,x_0)$ and rewrites its mean through the forward-noising
relationship. The reference formula and conceptual explanation do not
count as a completed derivation.

## Fresh Draws and a Fixed Conditional Distribution

I initially described $\epsilon$ as noise accumulated through corruption,
but suggested that one draw would be shared across timesteps.

**Correction supplied by Codex:** Sequential forward noising uses fresh,
independent noise at each step. Direct construction instead draws one
fresh effective $\epsilon$ for the selected timestep, representing the
accumulated effect in distribution. Training examples normally resample
both $t$ and $\epsilon$. The standard Gaussian law stays the same; the
particular draw is not fixed.

In the follow-up with $x_0$ and $t$ held fixed, I correctly explained:

> The mean and variance stay fixed because $x_0$ and $t$ are fixed. What
> changes is epsilon, so we get different samples of $x_t$ from the same
> conditional distribution $q(x_t\mid x_0)$.

This matches the [Week 15 conditional law](w15_forward_process_discrete.md):

$$
q(x_t\mid x_0)
=\mathcal N\!\left(
x_t;\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I
\right).
$$

The response correctly applies a fixed-law/fresh-draw distinction after
the explanation; it is not evidence of unaided recall before guidance.

## Why Supply the Timestep?

My initial explanation called $t$ a useful "hint" that we can also provide
at inference. That availability observation was correct: generation follows
a chosen reverse timestep sequence. I suggested that specific noise might
look different at different timesteps.

**Clarification supplied by Codex:** The standardized target noise has
the same Gaussian distribution at every timestep. With a fixed schedule,
$t$ identifies the signal and noise multipliers and therefore the
conditional denoising task. An observed value can have different plausible
signal/noise explanations at different corruption levels. The network
learns to use its timestep input; it need not receive the schedule
coefficients explicitly.

My final restatement after that clarification was:

> So $t$, together with our schedule, tells the model how we scaled $x_0$
> and epsilon to construct $x_t$. Epsilon still comes from the same
> standard Gaussian distribution; what changes is the scaling.

That restatement is correct and followed guidance.

## Day 1 Review and Next Step

The opening reading-based training explanation correctly identified all
three draws, direct noising, model inputs/output, the known noise target,
and weight optimization. MSE notation was refined. The discussion then
corrected predicted versus fresh sampling noise, fresh draws versus a
fixed Gaussian law, and what the timestep identifies. Follow-up answers
and the final restatement were correct with those explanations available.

The conceptual VAE/ELBO and weighting overview was supplied by Codex; its
independent reproduction was not assessed. The parameterization and
loss-weighting algebra remain Day 2 work. The reverse mean was supplied
as a reference, not derived; sampler study remains Day 3 work. No model
was trained or sampler implemented today.

**Day 1 complete:** Juan read and approved this consolidated note on
2026-11-16. The discussion and read-through meet today's conceptual
stopping point. Active study time was not measured.

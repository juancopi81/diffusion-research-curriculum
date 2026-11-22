# Week 16 — DDPM Training and Sampling

**Week 16 is in progress.** Day 1 was reviewed on 2026-11-16 and the
[Day 2 derivations](w16_prediction_parameterizations.md) on 2026-11-17.
Juan reviewed and approved the [Day 3 sampler note](#day-3--sampling-from-a-trained-ddpm)
on 2026-11-18 and the [Day 4 training note](#day-4--training-on-a-fixed-mnist-batch)
on 2026-11-19. The [Day 5 MNIST run](#day-5--training-and-generating-from-noise)
is complete as of 2026-11-20. The [daily plan](w16_study_plan.md) gives the
sequence.

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

## Day 3 — Sampling from a Trained DDPM

**Day 3 complete on 2026-11-18, including Juan's read-through.**

### Tracing one reverse step

After the sampling readings, I described starting from Gaussian noise with
the shape of an image and working backward to $x_0$. I distinguished the
network's predicted noise, which goes into the reverse mean, from the fresh
noise $z$, which determines where the sample lands around that mean. Codex
clarified two inputs in my first description. We set $t=T$ and draw
$x_T\sim\mathcal N(0,I)$. On each step the network receives **both** the
current image $x_t$ and its timestep $t$.

I used the reverse-mean formula supplied on Day 1 to trace one scalar
coordinate at $t>1$. The example gave $x_t=0.9$, a model prediction of
$0.3$, $\alpha_t=0.8$, $\beta_t=0.2$, and $\bar\alpha_t=0.64$. This gave

$$
\mu_\theta(x_t,t)
=\frac{1}{\sqrt{0.8}}\left(0.9-\frac{0.2}{\sqrt{1-0.64}}\times 0.3\right)
=\frac{0.9-0.1}{\sqrt{0.8}}
\approx 0.894427.
$$

In my [handwritten trace](figures/w16_day3_01_reverse_step_handwritten.png)
I set up the mean and sampling update correctly, then made an arithmetic
slip in the last multiplication for the mean. Codex pointed to that line
and I recalculated it. With the supplied $\sigma_t=1/3$ and $z=-0.6$, my
corrected sample was $x_{t-1}=0.894427-0.2\approx 0.694427$. The draw
moved this coordinate $0.2$ below its mean.

### My sampling loop, with the indexing corrected

I drafted the [full loop](figures/w16_day3_02_sampling_loop_handwritten.png)
from an open prompt. My draft initialized $x_T$ and wrote updates from
$x_t$ to $x_{t-1}$, but started the loop at $T-1$ and ended at $0$.
Codex pointed out the mismatch. I corrected the loop to run from $T$ down
to $1$, and after a follow-up prompt corrected the fresh-noise condition to
$t>1$. The blog's code index is one less than our mathematical timestep.
Its index zero denotes the update that takes $x_1$ to $x_0$.
[DDPM, Algorithm 2](https://arxiv.org/pdf/2006.11239#page=4) ·
[Annotated Diffusion, Sampling](https://huggingface.co/blog/annotated-diffusion#sampling)

```text
draw x[T] from N(0, I) with the desired image shape
for t from T down to 1 inclusive:
    predicted_noise = trained_model(x[t], t)
    mean = (x[t] - beta[t] * predicted_noise / sqrt(1 - alpha_bar[t])) / sqrt(alpha[t])
    if t > 1:
        draw fresh z from N(0, I) with the same shape as x[t]
        x[t-1] = mean + sigma[t] * z
    else:
        x[0] = mean
return x[0]
```

The trained weights stay fixed while $x_t$ and $t$ change. Each update
uses the schedule values for the current $t$. The outer square root uses
$\alpha_t$ for this single step, and the noise coefficient inside the mean
uses the cumulative $\bar\alpha_t$.

### The clean estimate and the open question

Asked how to proceed when the original clean image is unknown, I suggested
using $m_t(x_t)=\mathbb E[X_0\mid X_t=x_t,t]$, the mean of the possible
clean images given this observation. When prompted to connect it to Day 2,
I wrote the [conversion from predicted noise](figures/w16_day3_03_clean_estimate_handwritten.png).
Codex clarified the distinction between my model's estimate and the ideal
conditional mean. Using a hat for the estimate, my formula is

$$
\hat m_{\theta,t}(x_t)=
\frac{x_t-\sqrt{1-\bar\alpha_t}\,\epsilon_\theta(x_t,t)}
{\sqrt{\bar\alpha_t}}.
$$

This estimates the **clean endpoint** $x_0$. For the sampler I used
$\mu_\theta(x_t,t)$ to take **one step** toward that endpoint.

**Pending — posterior averaging.** If we knew $x_0$, the Gaussian
posterior $q(x_{t-1}\mid x_t,x_0)$ would give us a mean for the previous
state. Given only $x_t$, why does averaging those means over plausible
clean images yield $\mathbb E[X_{t-1}\mid X_t=x_t,t]$? Codex supplied
that connection at the end and I said it was still confusing. I used the
reverse-mean formula as a reference in this session. Its derivation and
the reason for that averaging remain open for a later discussion.

I found the pace comfortable with room to propose the loop and the clean
estimate. The indexing corrections followed hints. Active study time was
not measured. I read and approved this note on 2026-11-18.

## Day 4 — Training on a Fixed MNIST Batch

**Day 4 complete on 2026-11-19, including Juan's read-through.**

In the [working notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb),
I completed the two exercises. I drew one timestep per image and Gaussian
noise with the same shape as the clean batch. I used the forward equation
to make $x_t$ and kept that noise as the target. The training step predicts
noise from $x_t$ and $t$, computes MSE, clears gradients before backpropagation,
and updates the model with Adam.

### One schedule coefficient per image

When we traced my code together, I identified the output shape of
$\bar\alpha_t$ after the lookup and reshape as $(16,1,1,1)$. It lines up with
the image batch $(16,1,28,28)$. The batch dimensions already agree, and
broadcasting applies each image's scalar across its pixels. Codex clarified
that the lookup first returns shape $(16,)$ and that broadcasting behaves
as if the scalar were repeated without storing the copies.

### What the fixed batch showed

On CPU, the check used seed 16 for data selection and model initialization
and seed 17 for corruption. It held 16 clean images, their sampled
timesteps, and their noise targets fixed across 20 optimizer updates.
The shape, finiteness, and gradient checks passed, and the optimizer
changed the model parameters. Noise MSE fell from **0.9683 to 0.6795**.
Codex reran all code cells from a fresh Python session and reproduced
that result.

Asked what the result showed, I explained that the model got better at
predicting the noise on that same batch, which shows that the training step
can improve the objective. For Day 5, I want to see whether we can start
from pure noise and generate recognizable digits using the reverse loop.

I read and approved this note on 2026-11-19. Active study time was not measured.

## Day 5 — Training and Generating from Noise

**Day 5 complete on 2026-11-20.** Juan implemented the reverse step,
sampling loop, and epoch loop in the
[working notebook](../notebooks/w16_train_tiny_ddpm_mnist_solved.ipynb).

### Sampler implementation and checks

The first reverse step used the cumulative $\bar\alpha_t$ in the
outer denominator of the mean, branched on a batch of timestep labels,
and used $\beta_t$ as its variance. After Codex's review, Juan used the
single-step $\alpha_t$ for that denominator, kept a scalar timestep for
the branch and a batch of labels for the model, and used the supplied
fixed posterior variance $\tilde\beta_t$. The revised step reproduced
the Day 3 result of $0.694427$ for each image in a two-image test and
returned the mean at $t=1$ without drawing fresh noise.

Juan's loop started with Gaussian noise and carried the output of each
reverse step into the next one. He made the sample count an argument
after review. Codex verified the seeded Gaussian start, the full timestep
sequence, finite image-shaped output, and unchanged model weights.
The posterior-variance derivation and the posterior-averaging
connection remain open.

### Saved MNIST run

| Setting | Value |
| --- | --- |
| Data | 5,000 MNIST training images at $28\times28$, scaled to $[-1,1]$ |
| Model and optimizer | TinyDenoiser with 2,929 parameters, Adam at $10^{-3}$, batch size 64 |
| Forward schedule | 1,000 linear steps, $\beta_t$ from $10^{-4}$ to $0.02$ |
| Training | CPU, 30 epochs, 2,370 optimizer updates |
| Seeds and grids | Seed 16 for setup and training. Reset sampling seed 16 for each 16-image grid. |
| Runtime | About 62.2 s training and 51.9 s sampling, summed from the per-epoch logs |

The notebook retains the batch and epoch noise-MSE curves and one grid
per epoch. Mean batch MSE by epoch was **0.4860** at epoch 1, **0.2044**
at epoch 2, **0.0610** at epoch 20, and **0.0543** at epoch 30. Codex
reran the updated notebook with a two-epoch configuration in memory and
reproduced the first two losses and the loss plot for that run.

**Visual review by Codex.** Epoch 2 shows mostly broad patches. Later
grids show darker backgrounds and brighter, more defined strokes.
At epoch 30, most samples still contain fragments or disconnected marks,
with a few shapes resembling parts of digits. The run demonstrates
training and generation from Gaussian noise. Consistent production of
recognizable digits remains an open empirical question.

Active study time was not measured.

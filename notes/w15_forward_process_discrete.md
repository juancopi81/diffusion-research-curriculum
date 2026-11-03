# Week 15 — The Discrete Forward Diffusion Process

**Status:** Day 1 completed and its note approved by the learner on
2026-10-30. Day 2 reading and discussion completed on 2026-10-30; Day 3's
handwritten derivation and guided review completed on 2026-11-02. The
learner read and approved the Day 2 and Day 3 sections on 2026-11-02,
completing Days 1–3.
Day 4's notebook implementation and observation discussion completed on
2026-11-03; the learner read and approved the Day 4 note and notebook
observations on the same date, completing Days 1–4.
Day 5's second schedule and Monte Carlo verification are next in the
[study plan](w15_study_plan.md).

**Day 1 reading:** [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion),
the introductory explanation and the beginning of its mathematical section,
through the forward trajectory from $x_0$ to $x_T$. The reading stopped
before the reverse-conditional discussion. The explanations and numerical
example below consolidate our own discussion rather than quote the article.

## The Overall Picture

Like the generative models studied earlier, diffusion models generate a
data sample starting from noise drawn from a simple distribution. The
article takes a discrete-time perspective: a chosen forward process corrupts
data, while a learned reverse process generates by progressively denoising.

We start with a clean sample $x_0$ from the data distribution $q(x_0)$.
For images, the whole image can be treated as a vector. Forward steps
attenuate the previous image's signal and add Gaussian noise. This scaling
acts across pixel values; the image keeps its shape and number of pixels.

The number of steps $T$ is a design choice. The DDPM setup described in the
article uses $T=1000$.

## One-Step Gaussian Corruption

Choose a schedule with $0<\beta_t<1$. The article presents increasing
variances; the values are known in advance. At each step, draw fresh noise
independently of the previous state:

$$
\epsilon_t\sim\mathcal N(0,I),
\qquad
x_t=\sqrt{1-\beta_t}\,x_{t-1}+\sqrt{\beta_t}\,\epsilon_t.
$$

This gives the conditional distribution

$$
q(x_t\mid x_{t-1})
=\mathcal N\!\left(
x_t;\sqrt{1-\beta_t}\,x_{t-1},\beta_t I
\right).
$$

The transition is a modeling choice. Its conditional Gaussian law follows
from the affine transformation of standard Gaussian noise.

Given $x_{t-1}$ and $t$, the schedule and signal term are fixed. The fresh
noise draw supplies the randomness. The noise multiplier is
$\sqrt{\beta_t}$, so its covariance contribution is $\beta_t I$.

For the scalar example $x_{t-1}=2$ and $\beta_t=0.04$,

$$
x_t=2\sqrt{0.96}+0.2\epsilon,
\qquad \epsilon\sim\mathcal N(0,1),
$$

and therefore

$$
x_t\mid x_{t-1}=2
\sim\mathcal N\!\left(2\sqrt{0.96},0.04\right).
$$

The signal multiplier is $\sqrt{0.96}$; the entire deterministic term
also includes the given value $2$. The noise standard deviation is $0.2$,
and its variance is $0.04$.

## Conditional Gaussian Does Not Imply a Gaussian Marginal

The conditioning matters. Suppose the previous value is equally likely to
be $-2$ or $+2$, and write $m=\sqrt{0.96}$. The next value has density

$$
q_t(x)
=\tfrac12\mathcal N(x;2m,0.04)
+\tfrac12\mathcal N(x;-2m,0.04).
$$

Each starting value gives a Gaussian conditional distribution. Across both
starting values, we have a mixture with two peaks near $-2m$ and $+2m$.
This example shows why Gaussian corruption does not automatically make the
whole noisy-data distribution Gaussian.

Here we choose a component and sample from it. The formula adds weighted
**densities**. A weighted sum of independent Gaussian **random variables**
would be a different construction and would remain Gaussian.

## What Happens at the Endpoint?

My corrected understanding: after finitely many steps, some contribution
from $x_0$ remains, scaled down by the signal multipliers. With a suitable
schedule and enough steps, that contribution becomes very small. For
general image data, the intended endpoint is therefore approximately
standard Gaussian noise. The size of the remaining signal depends on the
whole schedule and the number of steps.

The thought experiment $\beta_T=1$ would make the final signal multiplier
zero and give $x_T=\epsilon_T$ exactly. This lies outside the schedule
constraint $0<\beta_t<1$ used above.

Day 2 below expresses the accumulated signal and noise directly from
$x_0$; Day 3 provides the derivation.

## Day 1 Discussion Record

- The initial explanation correctly distinguished the chosen schedule from
  the randomness of each noise draw and identified the conditional mean
  and covariance.
- Codex restored the missing square roots in the pasted sampling equation.
  In the scalar check, the learner identified both multipliers correctly
  and included the factor $x_{t-1}=2$ after a hint.
- In the prompted two-starting-value example, the learner correctly
  identified an equal-weight Gaussian mixture and its two-peak shape.
  Codex clarified conditional versus marginal distributions and a mixture
  of densities versus a sum of Gaussian random variables.
- After the endpoint question, the learner correctly explained that some
  scaled contribution from $x_0$ remains. Codex qualified the approximation
  as depending on sufficient accumulated signal attenuation.

The reading, guided discussion, and learner's read-through are complete.
The learner approved this cleaned note on 2026-10-30. At that point, the
later derivations and numerical checks had not yet been attempted.

## Day 2 — Direct Sampling from the Clean Image

**Reading:** The direct-noising passage in
[Annotated Diffusion](https://huggingface.co/blog/annotated-diffusion#defining-an-objective-function-by-reparametrizing-the-mean),
and the later corruption subsection within
[HF Unit 1's DDPM comparison](https://huggingface.co/learn/diffusion-course/en/unit1/3#comparison-to-ddpm).
The selected passages and discussion were completed on 2026-10-30. The
formula below was read and interpreted; its derivation is recorded in Day 3.

### One Step Versus Accumulated Corruption

Define

$$
\alpha_t:=1-\beta_t,
\qquad
\bar\alpha_t:=\prod_{s=1}^{t}\alpha_s.
$$

The individual $\alpha_t$ describes the current step. The product
$\bar\alpha_t$ accounts for all the steps from the clean input to the
chosen time. Knowing only $\beta_t=0.01$ tells me $\alpha_t=0.99$, but
generally does not tell me how much of $x_0$ remains. I also need the
earlier schedule values, or the already computed product. At $t=1$,
$\bar\alpha_1=\alpha_1$, so that special case needs only the first value.

### The Direct Conditional Distribution

Instead of simulating every intermediate step, I can sample the endpoint
at a chosen time directly from

$$
q(x_t\mid x_0)
=\mathcal N\!\left(
x_t;\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I
\right).
$$

Equivalently, draw $\epsilon\sim\mathcal N(0,I)$ independently of $x_0$
and set

$$
x_t=\sqrt{\bar\alpha_t}\,x_0
+\sqrt{1-\bar\alpha_t}\,\epsilon.
$$

The signal multiplier is $\sqrt{\bar\alpha_t}$ and the noise multiplier
is $\sqrt{1-\bar\alpha_t}$. Given $x_0$, the covariance is
$(1-\bar\alpha_t)I$, without a square root. The product defining
$\bar\alpha_t$ ends at the chosen $t$. These distinctions correct the
notation slips in the HF course passage.

### Reading the Coefficient Plot

The course plot shows the signal multiplier decreasing while the noise
multiplier increases. These are amplitudes. Their squares add to one:

$$
\left(\sqrt{\bar\alpha_t}\right)^2
+\left(\sqrt{1-\bar\alpha_t}\right)^2=1.
$$

My handwritten crossing calculation sets the two coefficients equal:

$$
\sqrt{\bar\alpha_t}=\sqrt{1-\bar\alpha_t}
\quad\Longrightarrow\quad
\bar\alpha_t=1-\bar\alpha_t
\quad\Longrightarrow\quad
\bar\alpha_t=\frac12.
$$

At the crossing, each multiplier is $1/\sqrt2\approx0.7071$, matching
the plot. The conditional noise covariance there is $0.5I$.

![Original handwritten derivation of the coefficient crossing](figures/w15_coefficient_crossover_handwritten.png)

The original handwritten attempt is preserved above; the typeset version
records the same reasoning.

### What Agreement Between the Two Methods Means

Even two direct samples can differ because they use different noise draws.
Sequential sampling draws fresh noise at every step; direct sampling uses
one noise draw to produce the chosen endpoint. Separately sampled runs
therefore need not match pixel for pixel.

For fixed $x_0$ and $t$, both methods have the same full conditional
distribution $q(x_t\mid x_0)$. Equal conditional means and covariances are
consequences of that agreement. Across different clean images, the
marginal distribution still need not be Gaussian.

Codex noted that the weighted independent Gaussian noise terms in the
sequential construction combine into an effective Gaussian noise term.
Day 3 below derives its coefficient and establishes the closed form explicitly.

### Normalization in the Image Experiment

For an original pixel value $u\in[0,1]$, the transformation $x=2u-1$
maps its range to $[-1,1]$. This centers the pixel range around zero and
sets the image scale relative to the standard Gaussian noise. It does not
guarantee zero dataset mean, unit variance, or Gaussian image data.

The forward equations apply with either scaling, but the image's scale
affects the balance between signal and noise. Corrupted values can extend
beyond $[-1,1]$. The notebook will record its normalization and keep
display clipping separate from the values used in calculations.

### Day 2 Discussion Record

- The initial reading summary correctly stated both schedule definitions,
  the direct conditional law, and the sampling equation, including the
  covariance-versus-noise-multiplier distinction.
- In the first check, the learner correctly explained why the current
  $\beta_t$ alone is insufficient and identified the $t=1$ exception.
- In the second check, the learner supplied the handwritten derivation
  $\bar\alpha_t=1/2$ and both coefficients approximately $0.7071$.
  Codex confirmed the calculation and identified the conditional noise
  covariance as $0.5I$.
- In the final check, the learner correctly explained why separately
  sampled endpoints can differ and that the two constructions agree in
  distribution. Codex made the conditioning on $x_0$ explicit and noted
  that the agreement is stronger than matching a few moments.
- Codex explained the normalization convention in response to the
  learner's question. It has not yet been applied in the weekly experiment.

The Day 2 reading and discussion are complete. The learner read and
approved this section on 2026-11-02. The derivation follows below; numerical
verification remains for Days 4–5.

## Day 3 — Deriving the Forward Distributions

**Basis:** The learner's handwritten attempt and our guided review on
2026-11-02. This is a consolidation of that derivation, rather than an
attributed solution from either reading. The original pages and assistance
used are recorded below. The learner read and approved this cleaned
section on 2026-11-02.

### Setup and the One-Step Law

Use a deterministic schedule with $0<\beta_t<1$,
$\alpha_t=1-\beta_t$, and $\bar\alpha_t=\prod_{s=1}^{t}\alpha_s$.
All fresh noise vectors $\epsilon_s\sim\mathcal N(0,I)$ are mutually
independent and independent of $x_0$. The step is

$$
x_t=\sqrt{\alpha_t}\,x_{t-1}+\sqrt{\beta_t}\,\epsilon_t.
$$

Given $x_{t-1}$, the first term is fixed, the noise has zero mean and
covariance $I$, and the affine transformation is Gaussian. Hence

$$
\begin{aligned}
\mathbb E[x_t\mid x_{t-1}]&=\sqrt{\alpha_t}\,x_{t-1},\\
\operatorname{Cov}(x_t\mid x_{t-1})&=\beta_t I,
\end{aligned}
$$

which establishes the chosen one-step Gaussian kernel.

### Expand Two Steps

Substitute the first step into the second:

$$
\begin{aligned}
x_1&=\sqrt{\alpha_1}\,x_0+\sqrt{\beta_1}\,\epsilon_1,\\
x_2&=\sqrt{\alpha_2}\,x_1+\sqrt{\beta_2}\,\epsilon_2\\
&=\sqrt{\alpha_1\alpha_2}\,x_0
+\sqrt{\alpha_2\beta_1}\,\epsilon_1
+\sqrt{\beta_2}\,\epsilon_2.
\end{aligned}
$$

Given $x_0$, its term is a fixed shift. Independence from $x_0$ gives
$\mathbb E[\epsilon_1\mid x_0]=\mathbb E[\epsilon_2\mid x_0]=0$.
By linearity,

$$
\mathbb E[x_2\mid x_0]
=\sqrt{\alpha_1\alpha_2}\,x_0.
$$

For the covariance, the fixed shift contributes zero and independence
eliminates the cross-covariance terms. Squaring the noise multipliers gives

$$
\begin{aligned}
\operatorname{Cov}(x_2\mid x_0)
&=(\alpha_2\beta_1+\beta_2)I\\
&=\bigl[\alpha_2(1-\alpha_1)+(1-\alpha_2)\bigr]I\\
&=(1-\alpha_1\alpha_2)I\\
&=(1-\bar\alpha_2)I.
\end{aligned}
$$

The learner's Gaussianity argument: after conditioning on $x_0$, we have
a fixed shift plus two scaled independent Gaussian vectors. Together the
noise vectors are jointly Gaussian, and their affine combination remains
Gaussian. The calculated moments therefore identify the full conditional
law:

$$
x_2\mid x_0
\sim\mathcal N\!\left(
\sqrt{\bar\alpha_2}\,x_0,(1-\bar\alpha_2)I
\right).
$$

### Generalize by Induction

The one-step law supplies the base case. Assume that, at time $t-1$,

$$
x_{t-1}\mid x_0
\sim\mathcal N\!\left(
\sqrt{\bar\alpha_{t-1}}\,x_0,
(1-\bar\alpha_{t-1})I
\right).
$$

Apply one more step with fresh independent noise. Its conditional mean is

$$
\begin{aligned}
\mathbb E[x_t\mid x_0]
&=\sqrt{\alpha_t}\,\mathbb E[x_{t-1}\mid x_0]\\
&=\sqrt{\alpha_t\bar\alpha_{t-1}}\,x_0\\
&=\sqrt{\bar\alpha_t}\,x_0.
\end{aligned}
$$

The new noise is independent of the entire previous history and of $x_0$,
so the conditional covariance is

$$
\begin{aligned}
\operatorname{Cov}(x_t\mid x_0)
&=\alpha_t\operatorname{Cov}(x_{t-1}\mid x_0)+\beta_t I\\
&=\bigl[\alpha_t(1-\bar\alpha_{t-1})+\beta_t\bigr]I\\
&=(1-\alpha_t\bar\alpha_{t-1})I\\
&=(1-\bar\alpha_t)I.
\end{aligned}
$$

Gaussianity follows from the same affine-Gaussian argument. This completes
the induction and establishes, for $t\geq1$,

$$
q(x_t\mid x_0)
=\mathcal N\!\left(
x_t;\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I
\right).
$$

Thus we can generate a direct sample at the chosen time using a standard
Gaussian vector:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0
+\sqrt{1-\bar\alpha_t}\,\epsilon,
\qquad\epsilon\sim\mathcal N(0,I).
$$

This direct representation has the same conditional law as the sequential
endpoint. A separately drawn $\epsilon$ need not reproduce the endpoint
of a particular previously sampled trajectory.

### Boundary Checks

At $t=1$, $\bar\alpha_1=\alpha_1=1-\beta_1$. The direct formula becomes

$$
x_1=\sqrt{1-\beta_1}\,x_0+\sqrt{\beta_1}\,\epsilon_1,
$$

recovering the original one-step construction and its conditional law.

At $t=0$, use the empty-product convention $\bar\alpha_0=1$. The signal
multiplier is one and the noise multiplier is zero, so the formula returns
$x_0$ exactly. Its covariance conditional on $x_0$ is the zero matrix.
The conditional law is a point mass at the observed clean image; there is
no ordinary nondegenerate Gaussian density at this boundary. Before
conditioning, a clean sample can still be random under the data
distribution $q(x_0)$.

### Original Handwritten Pages

All five supplied pages are preserved unchanged, including the initial
notation and subsequent correction:

1. [Two-step substitution and expansion](figures/w15_two_step_expansion_handwritten.png).
2. [Initial conditional mean and covariance calculation](figures/w15_two_step_moments_initial_handwritten.png).
3. [Covariance simplification with the identity matrix retained](figures/w15_two_step_covariance_handwritten.png).
4. [Induction step](figures/w15_forward_induction_handwritten.png).
5. [Boundary checks](figures/w15_forward_boundaries_handwritten.png).

### Day 3 Review Record

The independent attempt exceeded the suggested 15–20-minute starting
budget; no exact duration was recorded. The learner brought the unfinished
work for review after correctly expanding two steps, calculating the
conditional mean, and obtaining the covariance coefficient
$\alpha_2\beta_1+\beta_2$.

- Codex pointed out the missing $I$ in the final vector covariance. The
  learner included it on the next page.
- Codex prompted substitution of $\beta_s=1-\alpha_s$. The learner
  correctly simplified the covariance to $(1-\bar\alpha_2)I$.
- Asked to justify Gaussianity, the learner correctly explained the fixed
  shift and scaled independent Gaussian noise terms.
- Codex supplied the induction hypothesis as a scaffold. The learner
  correctly obtained the general conditional mean, covariance, and law.
  Codex then supplied the intermediate covariance recurrence to make the
  independence and scaling explicit.
- With the two boundary checks prompted and the empty-product convention
  supplied, the learner correctly recovered the first step and explained
  the absence of conditional uncertainty at $t=0$. Codex clarified the
  distinction from randomness in the unconditioned dataset.

The derivation and guided review are complete on 2026-11-02. This records
correct reasoning with the assistance above, rather than a fully unaided
proof. The learner read and approved this cleaned section and the earlier
Day 2 section on 2026-11-02. Numerical verification remains for Days 4–5.

## Day 4 — Implementing and Interpreting Forward Noising

**Status:** Day 4 completed on 2026-11-03, including the learner's approval
of this note and the notebook's consolidated observations. This
section consolidates Juan's answers and our subsequent discussion. The
corrections and added explanations are recorded below.

**Evidence:** The completed
[working notebook](../notebooks/w15_forward_diffusion_mnist_solved.ipynb)
implements the schedule coefficients, one-step corruption, and direct
sampling. Codex checked the implementations and executed all 16 code cells
in a fresh namespace on the cached MNIST data. All supplied assertions
passed, including the clean boundary, first step, two-step formula,
per-image broadcasting, finite shapes, and preservation of raw values.

The run uses NumPy on CPU, seed 15, $T=1000$, and a linear schedule from
$\beta_1=10^{-4}$ to $\beta_T=0.02$. It selects digits 0, 1, 4, and 7,
maps their pixels to $[-1,1]$, and displays times 0, 1, 50, 100, 250, 500,
and 1000. Sequential and direct plots use separate seeded noise streams.

### Boundary and Scale

My $t=0$ result shows the clean image $x_0$: the signal multiplier is one
and the noise multiplier is zero.

For each standard-normal noise coordinate, about 68% of draws lie within
$[-1,1]$, but the distribution has unbounded support. Nothing guarantees
that every noise value stays in that range. Adding a scaled noise value
to a scaled clean pixel can therefore produce a result outside the
normalized image range.

The saved run illustrates this: terminal raw values range approximately
from $-3.32$ to $3.70$ in the sequential sample and from $-3.45$ to $3.76$
in the direct sample. Plotting clips a copy for display; the arrays used
for calculations retain these raw values.

### Curves and Images at an Intermediate Time

At $t=100$, I can still recognize the four digits despite visible noise.
The recorded coefficients give

$$
x_{100}\approx0.9471\,x_0+0.3209\,\epsilon.
$$

The signal coefficient is close to one, so rescaling the clean pixel values
preserves much of the visible structure. Every clean pixel is multiplied
by that coefficient. The noise coefficient scales each corresponding
noise draw: a draw of $1$ contributes about $0.3209$, while a draw of $0.1$
contributes about $0.03209$. Signed noise can raise or lower a pixel value.

The conditional noise variance per coordinate is
$0.3209^2\approx0.10298$. My initial interpretation described this as
roughly 10% noise and 90% image. The correction is that conditional variance
is not a percentage of the image or an amplitude weight.

**Clarification added during review:** Given a fixed $x_0$, the signal
term is deterministic and all conditional variance comes from the noise.
Across different clean images, the relative contributions to marginal
variance also depend on the clean-data covariance. Mapping the pixel range
to $[-1,1]$ does not impose unit data variance.

I also briefly mixed the direct formula with an update from $x_{99}$.
The corrected single-step expression is

$$
x_{100}=\sqrt{1-\beta_{100}}\,x_{99}
+\sqrt{\beta_{100}}\,\epsilon_{100},
$$

whereas the direct formula starts from $x_0$ and uses the cumulative
coefficient $\bar\alpha_{100}$.

![Day 4 coefficient amplitudes and conditional variance](figures/w15_day4_schedule.png)

### Two Constructions and the Numerical Check Still Ahead

The sequential and direct grids show similar qualitative corruption and
both recover the clean images at $t=0$. For the same fixed $x_0$ and $t$,
they sample from the same conditional distribution established on Day 3.
Their conditional means and covariances therefore agree, even though
independently generated samples need not match pixel by pixel.

I initially suggested checking the proof mathematically and comparing
pixel-by-pixel differences. The proof already establishes the theoretical
agreement. Pixel differences between individual independent draws do not
test whether the two implementations sample the same distribution.

After discussing what numerical evidence would help, I proposed a Monte
Carlo approximation: make many draws, for example 100, record them, and
estimate their mean and variance. The planned Day 5 check fixes a clean
coordinate $x_{0,j}$ and a timestep, repeats each sampling construction,
and compares its empirical moments with

$$
\mu_{t,j}=\sqrt{\bar\alpha_t}\,x_{0,j},
\qquad
v_{t,j}=1-\bar\alpha_t.
$$

**Clarification added by Codex:** Estimate variance across the individual
draws around their sample mean. Keep the clean input and timestep fixed;
averaging different pixels or images estimates a different quantity.
Sampling error is expected with 100 draws, and a larger sample makes the
comparison more precise. This check has been proposed, not yet run in the
weekly experiment. It will test implementation behavior against the
derived law; the four pictures alone do not establish that agreement.

![Sequential forward trajectory on the four selected clean digits](figures/w15_day4_sequential.png)

![Independent direct samples at the selected times](figures/w15_day4_direct.png)

The figures above are copies of the saved Day 4 notebook figures under
the ignored scratch directory. The fresh execution reproduced the checks,
coefficient values, and reported raw terminal ranges.

### Day 4 Review Record

- Juan completed all three implementation exercises correctly. The saved
  outputs and the fresh execution passed all provided checkpoints.
- The original boundary and Gaussian-support explanation was correct.
  Codex clarified that the 68% statement applies to an individual standard
  Gaussian noise coordinate.
- The coefficients at $t=100$ were identified correctly, but interpreting
  the variance as a percentage needed correction. Codex also clarified
  that every clean pixel is rescaled and that noise can raise or lower its
  value. Juan correctly rewrote the single-step formula and distinguished
  its $x_{99}$ input from direct sampling's $x_0$.
- With a prompt to fix a clean pixel and timestep, Juan proposed repeated
  sampling and Monte Carlo moment estimates. Codex clarified the variance
  calculation and the role of sampling error. The empirical comparison
  remains for Day 5, alongside the second schedule.

Day 4 is complete on 2026-11-03, including learner read-through and approval
of the cleaned note and the notebook's final observation cells. This
records correct code and understanding reached through review; it does not
claim that all initial interpretations were correct. Day 5's second
schedule and Monte Carlo experiment remain ahead.

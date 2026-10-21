# Week 14 — Generative Toolkit Mixed Problem Set

**Status:** In progress. Problem 1 reviewed on 2026-10-20 and Problem 2 on
2026-10-21; Problems 3–4 remain unattempted.

**Source basis:** Problem 1 consolidates the handwritten calculations and
explanation reviewed during Day 2. The Gaussian conditioning formulas were
looked up in the [Week 10 derivation](w10_multivariate_gaussian_score.md)
before applying them. This records a correct application with notes, not
unaided recall of those formulas. The prompts are in the
[Week 14 study plan](../notes/w14_study_plan.md#four-bounded-practice-problems).

Problem 2 consolidates the Day 3 handwritten work and evidence interpretation,
with review corrections identified below. The ELBO identity was recalled
without notes. The Gaussian KL calculation used the
[Week 11 derivation](../notes/w11_elbo_derivation.md) and the author's
[KL-divergence post](https://juancopi81.github.io/posts/2026-08-06-kl-divergence-is-not-a-distance.html)
as references.

| Problem | Status | Review evidence |
| --- | --- | --- |
| 1 — Gaussian score and conditioning | Reviewed 2026-10-20 | Score derivation and numerical evaluation correct; conditioning applied correctly with notes; marginal comparison explained correctly |
| 2 — ELBO, KL, and the implemented loss | Reviewed 2026-10-21 | ELBO identity recalled without notes; Gaussian KL applied with references and a log-base correction; reconstruction loss and saved-result interpretation reviewed |
| 3 — Change of variables and an unchanged coordinate | Pending | Scheduled for Day 4 |
| 4 — Stability and clipping | Pending | Scheduled for Day 5 |

## Day 2 Warm-up — Gaussian Corruption

For additive Gaussian corruption,

$$
x_t=x_0+\sigma\epsilon,
\qquad \epsilon\sim\mathcal N(0,I),
$$

the conditional score is

$$
\nabla_{x_t}\log q(x_t\mid x_0)
=-\frac{x_t-x_0}{\sigma^2}
=-\frac{\sigma\epsilon}{\sigma^2}
=-\frac{\epsilon}{\sigma}.
$$

The handwritten noise-scaling calculation was correct. The first line's
marginal-density notation was corrected during review to show conditioning
on the clean input; the final handwritten line already showed that conditioning.

## Problem 1 — Gaussian Score and Conditioning

### Setup

Let

$$
X\sim\mathcal N(\mu,\Sigma),
\qquad
\mu=\begin{bmatrix}1\\-1\end{bmatrix},
\qquad
\Sigma=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

Evaluate the score at

$$
x=\begin{bmatrix}2\\0\end{bmatrix}.
$$

### 1. Derive and evaluate the score

Taking the logarithm of the Gaussian density gives

$$
\log p(x)
=-\frac d2\log(2\pi)
-\frac12\log|\Sigma|
-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu).
$$

The first two terms do not depend on the input. Define

$$
z=x-\mu,
\qquad A=\Sigma^{-1}.
$$

Since the mean is constant, the Jacobian of this shift is the identity.
Use the quadratic-form gradient

$$
\nabla_z(z^\top A z)=(A+A^\top)z.
$$

The covariance is symmetric positive definite, so its inverse is symmetric.
Therefore,

$$
\begin{aligned}
s(x)=\nabla_x\log p(x)
&=-\frac12\left[\Sigma^{-1}+(\Sigma^{-1})^\top\right](x-\mu)\\
&=-\Sigma^{-1}(x-\mu).
\end{aligned}
$$

For the given covariance,

$$
\det\Sigma=2\cdot2-1\cdot1=3,
\qquad
\Sigma^{-1}=\frac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}.
$$

Thus,

$$
\begin{aligned}
s\!\left(\begin{bmatrix}2\\0\end{bmatrix}\right)
&=-\frac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}
\left(\begin{bmatrix}2\\0\end{bmatrix}-\begin{bmatrix}1\\-1\end{bmatrix}\right)\\
&=-\frac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}\\
&=\begin{bmatrix}-1/3\\-1/3\end{bmatrix}.
\end{aligned}
$$

**Review interpretation:** at this particular point, the score points
directly toward the mean, with the displacement scaled by one third.

### 2. Find the conditional distribution

The second coordinate is the unknown and the first coordinate is observed.
Using the Gaussian conditioning formulas from Week 10,

$$
\begin{aligned}
\mathbb E[X_2\mid X_1=2]
&=\mu_2+\Sigma_{21}\Sigma_{11}^{-1}(2-\mu_1)\\
&=-1+(1)\left(\frac12\right)(2-1)\\
&=-\frac12,
\end{aligned}
$$

and

$$
\begin{aligned}
\operatorname{Var}(X_2\mid X_1=2)
&=\Sigma_{22}-\Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}\\
&=2-(1)\left(\frac12\right)(1)\\
&=\frac32.
\end{aligned}
$$

Hence, with the second normal parameter denoting variance,

$$
X_2\mid X_1=2\sim\mathcal N\!\left(-\frac12,\frac32\right).
$$

### 3. Compare with the marginal

The marginal distribution is

$$
X_2\sim\mathcal N(-1,2).
$$

Explanation given during review:

> The mean increases from -1 to -1/2 because X1 is above its mean and they
> are positively correlated. The variance decreases from 2 to 3/2 since
> knowing X1 reduces our uncertainty about X2.

The calculation and interpretation are correct. The remaining recall item
is the conditioning formula itself: include a short check with changed
numbers during Day 7, before consulting notes. Problem 1 is reviewed; this
does not claim unaided formula recall has already been demonstrated.

## Problem 2 — ELBO, KL, and the Implemented Loss

### Setup

For one fixed image, the scalar approximate posterior and prior are

$$
q_\phi(z\mid x)=\mathcal N\!\left(1,\frac14\right),
\qquad p(z)=\mathcal N(0,1).
$$

The decoder defines a Gaussian observation model with fixed positive variance:

$$
p_\theta(x\mid z)=\mathcal N\!\left(m_\theta(z),\tau^2 I_D\right).
$$

### 1. ELBO identity and the two KL terms

The identity recalled without notes was correct:

$$
\log p_\theta(x)
=\operatorname{ELBO}(x)
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\Vert\,p_\theta(z\mid x)\right).
$$

The gap compares the encoder's approximate posterior with the posterior
implied by the current generative model. That posterior is a conditional
distribution determined by the prior and decoder, not a unique latent code
or a ground-truth latent label attached to the image.

Nonnegativity of KL gives

$$
\operatorname{ELBO}(x)\leq\log p_\theta(x).
$$

Equality is allowed when the posterior KL is zero. If the prior and decoder
are fixed, increasing the ELBO by changing the encoder decreases this gap.
During joint training the model log-likelihood also changes, so an ELBO
increase alone does not imply a decrease in the posterior KL.

The KL inside the training objective compares different distributions:

$$
\operatorname{ELBO}(x)
=\mathbb E_{z\sim q_\phi(z\mid x)}\!\left[\log p_\theta(x\mid z)\right]
-D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\Vert\,p(z)\right).
$$

This second KL compares the approximate posterior with the chosen prior.
The distinction between the two KL terms, equality at zero gap, and the
fixed-generative-model qualification were clarified during review.

### 2. Compute the KL to the prior

Using the scalar Gaussian-to-standard-normal formula from the references,

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\Vert\,p(z)\right)
&=\frac12\left[\sigma_\phi^2(x)+\mu_\phi^2(x)-\ln\sigma_\phi^2(x)-1\right]\\
&=\frac12\left[\frac14+1-\ln\!\left(\frac14\right)-1\right]\\
&=\frac12\left[\frac14-\ln\!\left(\frac14\right)\right]\\
&=\frac18+\ln2\\
&\approx0.818147\text{ nats}.
\end{aligned}
$$

The formula and substitution were correct. The initial numerical evaluation
used a base-10 logarithm; the correction was to use the natural logarithm
required by this formula. This was a reference-assisted calculation.

### 3. One-sample negative ELBO

During training/reconstruction, draw the latent from the image-conditioned
approximate posterior. For this scalar example,

$$
\epsilon\sim\mathcal N(0,1),
\qquad z=1+\frac12\epsilon,
\qquad z\sim q_\phi(z\mid x).
$$

The encoder can output a mean and log-variance, but the Gaussian's variance
is the variance itself. Exponentiating half the log-variance gives the
standard deviation for reparameterization. The first handwritten sampling
line used log-variance as the Gaussian parameter; the subsequent density
line used the correct variance, and the notation was clarified in review.

For the decoder likelihood,

$$
-\log p_\theta(x\mid z)
=\frac{1}{2\tau^2}\sum_{j=1}^{D}\left(x_j-m_{\theta,j}(z)\right)^2
+\frac D2\ln(2\pi\tau^2).
$$

Replace the expected reconstruction log-likelihood with one sampled-latent
evaluation and retain the analytic KL. The negative-ELBO estimate is

$$
\widehat{\mathcal J}(x)
=\frac{1}{2\tau^2}\sum_{j=1}^{D}\left(x_j-m_{\theta,j}(z)\right)^2
+\frac D2\ln(2\pi\tau^2)
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\,\Vert\,p(z)\right).
$$

The dimension and observation variance are fixed, so the omitted additive
term has no gradient with respect to the trainable parameters:

$$
C=\frac D2\ln(2\pi\tau^2).
$$

The optimization-equivalent loss for this fixed example is therefore

$$
\widehat{\mathcal L}(x)
=\frac{1}{2\tau^2}\sum_{j=1}^{D}\left(x_j-m_{\theta,j}(z)\right)^2
+0.818147\ldots.
$$

The reconstruction scaling, positive KL sign, Monte Carlo approximation,
and omitted constant were all derived correctly. The numeric KL belongs
to the fixed approximate posterior in this exercise; during training the
analytic KL depends on the encoder parameters. The notebook uses two
latent dimensions and sums the corresponding diagonal-Gaussian KL terms.

### 4. Reconstruction, generation, and decoder means

Reconstruction uses the image-conditioned encoder distribution. Unconditional
generation draws from the prior and then decodes, without an input image or
encoder pass. Thus changing only the encoder while keeping the prior and
decoder fixed does not change unconditional generation.

The decoder network outputs the Gaussian's mean; its observation variance
is fixed. The main reconstruction panels display decoder means without
additional observation noise. A full draw from the Gaussian observation
model would add that noise. The panel compares both decoding the encoder
mean and decoding a sampled latent; both routes display decoder means.

### 5. Saved VAE evidence

**Source:** saved outputs in the
[Week 11 solved VAE notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb),
under “Let the model learn” and “What did encoding and decoding preserve?”.
The reviewed run uses a two-dimensional latent and five training epochs.
The loss curves show scaled reconstruction error and KL to the prior, the
two nonnegative components of the negative-ELBO objective with the Gaussian
constant omitted. Both declined over the saved epochs in this run.

The following preserves the learner's three observations with wording
refined during review:

1. Reconstruction of MNIST digits improved during training. The loss curves
   show declining reconstruction error and KL to the prior. Before training,
   the displayed decoder means look noise-like; afterward, some digits,
   such as 0 and 1, are recognizable.
2. Some reconstructions remain blurry or ambiguous. In the displayed examples,
   the reconstructed 8 and 9 are difficult to distinguish. This observation
   does not establish that some digit classes are inherently harder to learn.
3. One hypothesis is the two-dimensional bottleneck: compressing an image
   with 784 input coordinates into only two latent coordinates may limit
   the information preserved for reconstruction. These figures do not
   isolate latent dimension as the cause of the remaining blur or ambiguity.

The before/after panel starts from held-out input images, so it supports a
claim about reconstruction quality. Unconditional generation requires the
separate prior-sample panel; reconstruction improvement alone does not
establish its quality.

**Review outcome:** Problem 2 and the Day 3 evidence discussion are reviewed.
During the existing Day 7 VAE check, briefly revisit why increasing the
ELBO forces the posterior gap down only when the generative model is fixed.
No extra Day 3 session or new model training is required.

## Problem 3 — Change of Variables and an Unchanged Coordinate

Pending Day 4 attempt and review. Use the prompt in the study plan.

## Problem 4 — Stability and What Clipping Actually Established

Pending Day 5 attempt and review. Use the prompt in the study plan.

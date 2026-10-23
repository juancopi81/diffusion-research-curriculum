# Week 14 — Generative Toolkit Mixed Problem Set

**Status:** All four problems reviewed. Problem 1 was reviewed on 2026-10-20,
Problem 2 on 2026-10-21, Problem 3 on 2026-10-22, and Problem 4 on 2026-10-23.
The Week 14 report and final recall review remain pending.

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

Problem 3 consolidates the Day 4 handwritten work and saved flow-plot
interpretation. The initial calculations were attempted without notes;
corrections and the follow-up explanation are recorded separately from
independent recall.

Problem 4 consolidates the Day 5 score-target recall, handwritten
gradient-descent calculations, and interpretation of the
[saved Week 13 clipping comparison](../notes/w13_training_stability_for_diffusion.md).
The learner proposed a longer matched training comparison; this remains
an experiment design, not a new result.

| Problem | Status | Review evidence |
| --- | --- | --- |
| 1 — Gaussian score and conditioning | Reviewed 2026-10-20 | Score derivation and numerical evaluation correct; conditioning applied correctly with notes; marginal comparison explained correctly |
| 2 — ELBO, KL, and the implemented loss | Reviewed 2026-10-21 | ELBO identity recalled without notes; Gaussian KL applied with references and a log-base correction; reconstruction loss and saved-result interpretation reviewed |
| 3 — Change of variables and an unchanged coordinate | Reviewed 2026-10-22 | Inverse recalled correctly; Jacobian/logarithm slips corrected; inverse determinant self-corrected; unchanged marginal and imperfect generated samples explained after clarification |
| 4 — Stability and clipping | Reviewed 2026-10-23 | Gradient, recurrences, stability range, and three learning-rate cases correct; clipping evidence interpreted correctly; longer matched comparison proposed, not run |

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

### Setup

The forward map sends data to a two-dimensional standard-normal base:

$$
z=f(x),\qquad
z_1=x_1,\qquad z_2=2x_2+x_1,\qquad
Z\sim\mathcal N(0,I_2).
$$

This is the problem's coupling layer with constant log-scale and linear shift:

$$
s(x_1)=\ln2,\qquad t(x_1)=x_1.
$$

### 1. Inverse and both Jacobians

Solving for the data coordinates gives

$$
x_1=z_1,\qquad x_2=\frac{z_2-z_1}{2}.
$$

The inverse was derived correctly in the first attempt. The forward Jacobian
and determinant are

$$
J_f=
\begin{bmatrix}1&0\\1&2\end{bmatrix},
\qquad
\det J_f=2,\qquad
\ln|\det J_f|=\ln2\approx0.693147.
$$

The first handwritten Jacobian swapped the two derivatives in the second
row. This was corrected after feedback. The subsequent numerical logarithm
used base 10; the calculation requires the natural logarithm.

The inverse Jacobian provides a consistency check:

$$
J_{f^{-1}}=
\begin{bmatrix}1&0\\-1/2&1/2\end{bmatrix},
\qquad
\det J_{f^{-1}}=\frac12,
\qquad
\ln|\det J_{f^{-1}}|=-\ln2.
$$

The learner initially suggested reciprocating the log-determinant, then
self-corrected to reciprocating the determinant before further feedback.
The forward map doubles area; the inverse halves it. Inverting a map
reciprocates its absolute determinant and negates its log absolute determinant.

### 2. Evaluate the model log density

Preserving probability mass gives the forward volume correction:

$$
p_X(x)\,dx=p_Z(f(x))\,dz,\qquad
dz=|\det J_f(x)|\,dx.
$$

Therefore,

$$
\ln p_X(x)=\ln p_Z(f(x))+\ln|\det J_f(x)|.
$$

For the two-dimensional standard-normal base and this particular map,

$$
\begin{aligned}
\ln p_Z(z)&=-\ln(2\pi)-\frac12(z_1^2+z_2^2),\\
\ln p_X(x)&=-\ln(2\pi)
-\frac12\left[x_1^2+(2x_2+x_1)^2\right]+\ln2.
\end{aligned}
$$

At the requested point,

$$
x=\begin{bmatrix}1\\0\end{bmatrix}
\quad\Longrightarrow\quad
z=f(x)=\begin{bmatrix}1\\1\end{bmatrix}.
$$

Thus,

$$
\ln p_X(1,0)=-\ln(2\pi)-1+\ln2=-\ln\pi-1
\approx-2.144730.
$$

The learner correctly found the latent point, evaluated the Gaussian term,
and used the positive forward-Jacobian correction without notes. The
substitution initially took a logarithm of the already-computed log-determinant.
Review corrected this to adding the log-determinant once. These are reviewed
calculations with specific corrections, not a claim of error-free recall.

### 3. Why one coupling layer cannot change the first marginal

For learned scale and shift functions, the more general layer is

$$
z_1=x_1,\qquad
z_2=x_2e^{s(x_1)}+t(x_1).
$$

Its inverse is

$$
x_1=z_1,\qquad
x_2=\left[z_2-t(z_1)\right]e^{-s(z_1)}.
$$

Generation begins with a Gaussian base draw, so

$$
Z_1\sim\mathcal N(0,1),\qquad
X_1=Z_1
\quad\Longrightarrow\quad
X_1\sim\mathcal N(0,1).
$$

The first generated marginal is imposed by the unchanged coordinate; it is
not learned from the training data. No choice of the scale and shift functions
can give that marginal two separated modes. Alternating which coordinate is
transformed allows both coordinates to change while preserving invertibility.

The learner correctly connected the unchanged coordinate to the one-layer
limitation after clarifying that generation starts from the Gaussian base.
The phrase “learning just the standard normal” was refined to “keeping the
standard-normal marginal imposed by the architecture.”

### 4. Saved flow evidence

**Source:** saved outputs in the
[Week 12 solved RealNVP notebook](../notebooks/w12_realnvp_2d_blobs_solved.ipynb),
under “Inspect both directions” and “One controlled failure: only one coupling
layer.” The plots were extracted from saved outputs; training was not rerun.

The learner's observations, with minimal wording corrections:

1. With one layer, the first generated coordinate remains standard normal.
   The orange marginal is centered near zero, unlike the blue data's two
   peaks. With alternating layers, the first coordinate can also change;
   the six-layer green marginal follows the two peaks more closely.
2. Exact model-density evaluation does not guarantee an exact fit. The
   six-layer generated-samples panel contains many points between the four
   blobs, where the displayed held-out data are sparse.

For context, the notebook uses 2,000 training points and 400 held-out points.
Its saved held-out NLL is about 2.44 for six layers and 4.57 for one layer.
The runs use 450 and 200 optimizer steps respectively, so the numerical
gap is not an isolated measurement of the first-coordinate restriction.
That restriction follows directly from the map, regardless of training time.

### 5. Clarification: exact density evaluation versus exact fit

The learner correctly identified the mismatch, then asked whether floating-point
approximations explain it and whether an exact fit is possible in theory.
This section records the explanation supplied during review.

Change of variables evaluates the density defined by any fixed valid flow.
Even an identity flow has an exactly evaluable standard-normal density while
fitting the four blobs poorly. Training must choose a transformation that
fits the target distribution. Limited architecture, finite data, and
incomplete optimization can leave a mismatch even with perfect arithmetic.
The plots do not isolate which factor explains the six-layer model's bridges.

The [Week 12 comparison note](../notes/w12_flows_vs_diffusion.md#what-each-model-learns)
already states this distinction briefly. Floating-point roundoff affects
numerical evaluation, but “exact likelihood” here means an exact model-density
formula rather than a variational bound or a latent-integral estimate.

An ideal smooth invertible transformation can map a Gaussian to this smooth,
positive Gaussian-mixture density. Existence of such a transformation does
not establish exact representation by our fixed six-layer architecture or
guarantee that training finds it. For the existence result and its conditions,
see [Papamakarios et al., Section 2.2](https://jmlr.org/papers/volume22/19-1028/19-1028.pdf#page=4).
The target Gaussians also have tails between blobs: sparse observed regions
are not regions of exactly zero true density.

**Review outcome:** Problem 3 and the flow evidence discussion are reviewed.
Within the existing Day 7 flow check, revisit determinant versus log-determinant,
the inverse correction, and why a fit can remain imperfect even with exact
arithmetic. The theoretical clarification was explained today; unaided
recall of it has not been assessed. No additional Day 4 exercises are assigned.

## Problem 4 — Stability and What Clipping Actually Established

### 1. Score-target recall and the MSE optimum

For the fixed-noise toy,

$$
x_t=x_0+\sigma\epsilon,\qquad
\epsilon\sim\mathcal N(0,I).
$$

The direct-score training target is

$$
Y=\nabla_{x_t}\log q_\sigma(x_t\mid x_0)
=-\frac{x_t-x_0}{\sigma^2}
=-\frac{\epsilon}{\sigma}.
$$

The learner recalled both forms correctly without notes and identified the
target as the conditional corruption score. The network receives the noisy
input during training as well as inference; the clean point constructs the
target. The analytical marginal noisy-data score is the toy's evaluation
reference.

Under squared-error training, the ideal population predictor is

$$
s_\sigma^*(x_t)
=\mathbb E[Y\mid X_t=x_t]
=\nabla_{x_t}\log p_\sigma(x_t).
$$

The conditional-mean identity was explained during review. To check the
averaging step, consider these possible scalar targets at one fixed noisy input:

$$
\Pr(Y=-3\mid X_t=x_t)=0.25,\qquad
\Pr(Y=1\mid X_t=x_t)=0.75.
$$

The learner correctly chose the expected target:

$$
a^*=(-3)(0.25)+(1)(0.75)=0.
$$

The expected target MSE at that prediction is

$$
\mathbb E[(Y-a^*)^2\mid X_t=x_t]
=0.25(-3)^2+0.75(1)^2
=3.
$$

The learner correctly wrote the expected squared error and reduced it to
the expected squared target when the prediction is zero. A prompt to use
the two numerical targets and their weights was needed before evaluating
the result. The nonzero minimum reflects conditional target variability;
at this input, the optimal prediction still has zero error against the
marginal score. Record the loss-floor calculation as reviewed with guidance.

Both conditional and marginal scores differentiate log densities with
respect to the noisy input. The optimizer instead uses a loss gradient
with respect to model parameters, as in the calculation below.

### 2. Gradient and coordinate recurrences

Use the quadratic and initial point

$$
L(\theta)=\frac12\left(\theta_1^2+10\theta_2^2\right),
\qquad
\theta^{(0)}=\begin{pmatrix}2\\1\end{pmatrix}.
$$

The learner used lambda for the learning rate. Differentiation gives

$$
\nabla_\theta L(\theta)
=\begin{pmatrix}\theta_1\\10\theta_2\end{pmatrix}.
$$

Substituting into plain gradient descent,

$$
\theta^{(n)}
=\theta^{(n-1)}
-\lambda\nabla_\theta L(\theta^{(n-1)}),
$$

gives

$$
\theta_1^{(n)}=(1-\lambda)\theta_1^{(n-1)},
\qquad
\theta_2^{(n)}=(1-10\lambda)\theta_2^{(n-1)}.
$$

The gradient and both factored recurrences were correct on the first attempt,
within the staged prompts and without a reported reference lookup.

### 3. Stability range and three learning rates

Both starting coordinates are nonzero. Repeated multiplication approaches
zero precisely when each multiplier has magnitude less than one:

$$
|1-\lambda|<1
\quad\Longleftrightarrow\quad
0<\lambda<2,
$$

$$
|1-10\lambda|<1
\quad\Longleftrightarrow\quad
0<\lambda<0.2.
$$

The common range is therefore

$$
\boxed{0<\lambda<0.2}.
$$

The learner correctly derived both inequalities, including the sign reversals.
The second coordinate imposes the stricter constraint.

| Learning rate | First multiplier | Second multiplier | Coordinate behavior |
| --- | --- | --- | --- |
| 0.05 | 0.95 | 0.5 | Both coordinates approach zero without changing sign |
| 0.15 | 0.85 | -0.5 | The first approaches zero without sign changes; the second alternates sign with shrinking magnitude |
| 0.25 | 0.75 | -1.5 | The first approaches zero; the second alternates sign with growing magnitude, so the iterate diverges |

All three classifications were correct. Review made the alternating-sign
behavior of the divergent case explicit. Oscillation by itself does not
imply divergence; the multiplier's magnitude determines whether it grows
or decays.

### 4. What the clipping experiment established

**Source:** the [Week 13 stability note](../notes/w13_training_stability_for_diffusion.md)
and its saved score-network experiment. This is separate from the quadratic
above. It used 20 plain-SGD updates at learning rate 0.1, paired initialization,
data splits, and training-noise draws, plus one fixed held-out noisy set.
The clipping-on threshold was a global parameter-gradient norm of 0.5.

| Condition | Clipped updates | Maximum applied gradient norm | Final held-out score MSE |
| --- | --- | --- | --- |
| Clipping off | 0/20 | 0.910351 | 1.240304 |
| Clipping on | 20/20 | 0.500000 | 1.345339 |

The learner correctly concluded that these results do not support improved
score accuracy from clipping in this run: the norm was bounded as intended,
but held-out MSE was higher with clipping.

Applied gradient norms assess the effect on parameter updates. Held-out
score MSE compares the network's predicted input-space vector field with
the analytical marginal score. These are different measurements, so
bounding the former does not guarantee improving the latter.

The comparison establishes the observed ordering under this setup and
budget. It does not establish a general advantage or disadvantage of clipping,
and the saved experiment did not demonstrate recovery from exploding gradients.

### 5. Proposed controlled follow-up — not run

The learner proposed extending training while keeping learning rate,
architecture, the clipping-on threshold, and other conditions fixed, and
comparing intermediate results as well as the final result.

The reviewed design is:

1. Extend both clipping-off and clipping-on runs to the same longer,
   predetermined update budget.
2. Keep the learning rate, architecture, initialization, data split, paired
   fresh-noise draws, fixed held-out set, and clipping-on threshold matched
   to the original comparison.
3. Compare held-out marginal-score MSE at the same update checkpoints and
   at the final update. As an optional refinement, predefine a common error
   level and compare updates needed to reach it, if either run reaches it.

This tests whether the clipped run catches up, overtakes, or remains behind
as the budget increases. A slower-progress explanation is a hypothesis,
not an established cause. No longer budget was selected and no new training
was run during this review.

### 6. What the toy still needs for diffusion generation

The learner identified multiple corruption timesteps and reverse sampling.
Review refined these into two ingredients:

1. Learn scores across a range of noise levels and tell the model the
   corresponding timestep or noise scale, rather than learning one fixed-noise
   score field.
2. Add a reverse sampling procedure that starts from a suitable, easily
   sampled high-noise distribution and uses those predictions to move
   through decreasing noise levels toward the data distribution.

For example, a noise-conditioned score model has the form

$$
s_\theta(x_t,t)\approx\nabla_{x_t}\log p_t(x_t).
$$

The learner also raised moving from analytical blobs to real data. This
would extend the application but is not a prerequisite for diffusion:
diffusion can be demonstrated on synthetic blobs. The analytical marginal
blob score was an evaluation reference. Training uses the known Gaussian
corruption conditional, whose score target can be computed from the clean
sample and chosen noise even when the real-data density is unknown.

The noise-conditioning detail and the training-versus-evaluation role of
analytical scores were clarified during review; they have not yet been
independently rechecked.

**Review outcome:** Problem 4, the score-target review, and clipping evidence
are reviewed on 2026-10-23. All four mixed problems are reviewed. Keep the
loss-floor and analytical-score clarification inside the existing Day 7
score questions; no additional Day 5 exercises or implementation are needed.
The checkpoint report and final recall review remain pending.

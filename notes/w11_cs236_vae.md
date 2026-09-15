# Week 11 — CS236 VAE Foundations

**Status:** Monday bridge and Tuesday Lecture 5 review completed on
2026-09-08. Wednesday Lecture 6 review and S1 consolidation completed on
2026-09-09. Thursday's general ELBO derivation is completed in the
[dedicated derivation note](./w11_elbo_derivation.md), now extended with the
scalar and diagonal Gaussian KL and reparameterization proof (2026-09-14).
The short code/reconstruction-loss checkpoint is complete. The minimal MNIST
VAE implementation and three observations were completed and reviewed on
2026-09-15. The [latent-diffusion bridge](./w11_why_latent_diffusion.md) was
reviewed and approved on the same date. Week 11 is complete.

**Source basis:** Stanford CS236 Fall 2023
[Lecture 5 slides: Latent Variable Models](https://deepgenerativemodels.github.io/assets/slides/cs236_lecture5.pdf),
especially slides 15–28, and the
[lecture recording studied](https://www.youtube.com/watch?v=MAGBUh77bNg).
The Monday bridge used MML §10.7, through the
[MML source catalog](../sources/mml/README.md), and the VAE segment of
[CS231n Generative Models 1](https://www.youtube.com/watch?v=zbHXQRUNlH0).
The CS236 slide content and MML passage were checked during study planning;
the video viewing was reported by the learner. These notes independently
consolidate the learner's explanations and our review, rather than transcribing
or quoting the lectures.

Wednesday's sections consolidate the discussion of
[Lecture 6: Latent Variable Models](https://deepgenerativemodels.github.io/assets/slides/cs236_lecture6.pdf),
especially slides 12–21 on optimization, reparameterization, amortized
inference, and the autoencoder interpretation. The slide text was inspected
earlier in this conversation; the learner reported completing the recording.
The scalar gradient example below is an independent explanation from our review.

## 1. The Distributions and Their Roles

Let $x\in\mathbb{R}^D$ denote an observed example and
$z\in\mathbb{R}^d$ a continuous latent vector. Throughout this review,
$x$ is fixed when we consider different latent explanations of it.

| Distribution | Role |
| --- | --- |
| $p(z)$ | The prior we choose over latent variables, often $\mathcal{N}(0,I_d)$. |
| $p_\theta(x\mid z)$ | The decoder's distribution over observations given a latent value. A neural network supplies its parameters. |
| $p_\theta(x)$ | The marginal distribution over observations defined by our model. |
| $p_\theta(z\mid x)$ | The exact posterior: the distribution over latent explanations of an observation under the current model. |
| $q_\phi(z\mid x)$ | A tractable approximation to that posterior, with adjustable parameters $\phi$. |

The real, unknown data distribution is $p_{\mathrm{data}}(x)$. We train
$p_\theta(x)$ to approximate it. The model distribution is specified by our
chosen prior and decoder, even when evaluating its density is difficult.

The generative direction is to sample $z\sim p(z)$ and then
$x\sim p_\theta(x\mid z)$. The decoder goes from latent values toward
observations. Inference asks the reverse question: given an observed $x$,
which values of $z$ could explain it?

For continuous variables, expressions such as $p_\theta(x\mid z)$ are
densities, not probabilities of individual exact images. The decoder can,
for example, output the mean and covariance of a Gaussian distribution over
observations; it does not merely assign one deterministic image to each $z$.

### The Exact Posterior Depends on the Decoder

Bayes' rule gives

$$
p_\theta(z\mid x)
=\frac{p_\theta(x\mid z)p(z)}{p_\theta(x)}.
$$

Changing $\theta$ can change which latent values explain the same observed
image well. If a latent value previously made our dog image likely but now
makes cat images likely, its posterior weight for that dog image can decrease.
The posterior is a distribution over candidate latent values, not one encoded
vector. A Gaussian prior does not guarantee a Gaussian posterior.

## 2. Why the Marginal Likelihood Is Difficult

The learner's starting explanation was that we must integrate over all
possible latent values:

$$
p_\theta(x)
=\int_{\mathbb{R}^d}p_\theta(x\mid z)p(z)\,dz.
$$

That is the correct marginalization. The symbol $dz$ simply identifies the
integration variable; it is not itself the source of difficulty. We must
combine every latent explanation's contribution, weighted by its prior
density. With a nonlinear neural decoder, this integral generally has no
convenient closed form, and numerical integration can be expensive.

The MML bridge shows why continuous latents alone are not the problem.
Probabilistic PCA uses independent Gaussian latent and observation noise:

$$
z\sim\mathcal{N}(0,I_d),\qquad
x=Bz+\mu+\epsilon,\qquad
\epsilon\sim\mathcal{N}(0,\sigma^2I_D),
\qquad B\in\mathbb{R}^{D\times d}.
$$

Its linear Gaussian structure yields an analytic marginal,
$x\sim\mathcal{N}(\mu,BB^\top+\sigma^2I_D)$, and an exact Gaussian posterior
by the conditioning rules studied in
[Week 10](./w10_mml_multivariate_gaussian.md).

## 3. Why Sampling from the Prior Can Be Inefficient

Because the marginal is an expectation under the prior, we can estimate it:

$$
z^{(1)},\ldots,z^{(K)}\overset{\mathrm{iid}}{\sim}p(z),
\qquad
\widehat p_\theta(x)
=\frac{1}{K}\sum_{k=1}^{K}p_\theta(x\mid z^{(k)}).
$$

For a particular observed image, most sampled latent vectors may explain it
poorly. A small sample can miss the regions that contribute substantially to
its marginal likelihood. Occasionally hitting those regions can change the
estimate considerably.

The estimator is unbiased, but its variance relative to the quantity being
estimated can be large. Many samples may be needed for a reliable result.
Taking the logarithm of this estimate does not generally give an unbiased
estimate of the log marginal likelihood.

## 4. Importance Sampling: Choose Plausible Explanations

We would prefer to sample from a distribution $q_\phi(z\mid x)$ that places
weight on plausible explanations of the particular observation. To preserve
the integral, we multiply and divide by the same density:

$$
\begin{aligned}
p_\theta(x)
&=\int q_\phi(z\mid x)
\frac{p_\theta(x\mid z)p(z)}{q_\phi(z\mid x)}\,dz\\
&=\mathbb{E}_{q_\phi(z\mid x)}
\left[\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right].
\end{aligned}
$$

For this identity, $q_\phi$ must be positive wherever the joint density
contributes, up to sets of measure zero. In this discussion, Gaussian
proposals with positive variances provide full support.

Drawing samples from $q_\phi$ gives the estimator

$$
z^{(k)}\overset{\mathrm{iid}}{\sim}q_\phi(z\mid x),
\qquad
\widehat p_\theta(x)
=\frac{1}{K}\sum_{k=1}^{K}
\frac{p_\theta(x,z^{(k)})}{q_\phi(z^{(k)}\mid x)}.
$$

There is no extra multiplication by $q_\phi$ in this sample average:
sampling from it already supplies that weighting. The ratio corrects for
the change in sampling distribution. A well-chosen proposal can improve
efficiency; an arbitrary proposal need not do so.

## 5. Jensen's Inequality Gives the ELBO

Training by maximum likelihood involves $\log p_\theta(x)$. We cannot
generally interchange a nonlinear function and an expectation. Because
$\log$ is concave, the average of the logs is at most the log of the average:

$$
\begin{aligned}
\log p_\theta(x)
&=\log\mathbb{E}_{q_\phi(z\mid x)}
\left[\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right]\\
&\geq\mathbb{E}_{q_\phi(z\mid x)}
\left[\log\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right]\\
&=: \mathcal{L}(x;\theta,\phi).
\end{aligned}
$$

$\mathcal{L}$ is the evidence lower bound, or ELBO. Here, evidence refers
to the marginal likelihood of the observed data. Moving the log inside
produces a bound, rather than a generally equal expression.

## 6. When the Bound Is Exact

If $q_\phi(z\mid x)=p_\theta(z\mid x)$, Bayes' rule simplifies the ratio:

$$
\frac{p_\theta(x,z)}{q_\phi(z\mid x)}
=\frac{p_\theta(x\mid z)p(z)}{p_\theta(z\mid x)}
=p_\theta(x).
$$

The learner obtained this by rearranging Bayes' rule. No further division
by $p(z)$ is needed. For fixed $x$ and $\theta$, the result is constant
with respect to $z$, so

$$
\mathcal{L}(x;\theta,\phi)
=\mathbb{E}_{p_\theta(z\mid x)}[\log p_\theta(x)]
=\log p_\theta(x).
$$

This explains tightness of the bound; it does not make the generally
intractable exact posterior available for computation.

## 7. The Posterior KL Gap and Its Direction

The gap has an exact expression:

$$
\begin{aligned}
\log p_\theta(x)-\mathcal{L}(x;\theta,\phi)
&=\mathbb{E}_{q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p_\theta(z\mid x)}\right]\\
&=D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)
\geq 0.
\end{aligned}
$$

The order matters: it is KL from the approximation to the exact posterior.
The expectation is under $q_\phi$, which appears first in the KL. Reversing
the arguments generally changes the divergence.

With $x$ and $\theta$ fixed, $\log p_\theta(x)$ is constant. Therefore,
maximizing the ELBO over $\phi$ is exactly equivalent to minimizing this
posterior KL. This is a consequence of the identity, not circular reasoning.

The ELBO need not reach $\log p_\theta(x)$. For example, a diagonal Gaussian
family cannot exactly represent every possible posterior. We seek a good
approximation within the chosen family, and numerical optimization may also
fall short of its best attainable value. If $\theta$ changes too, the model
likelihood and target posterior can both change; the fixed-model argument
must then be interpreted with that distinction in mind.

### What Is Omitted in Forming the Bound?

We omit the nonnegative posterior KL gap from the identity

$$
\log p_\theta(x)
=\mathcal{L}(x;\theta,\phi)
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)
$$

to obtain a lower bound. We do not discard $q_\phi$: it remains in the
ELBO's expectation and logarithmic ratio. The KL to the prior that appears
in the reconstruction/KL decomposition is a different term; Section 10
develops that distinction.

## 8. Tuesday Checkpoint

The completed review connects marginalization, inefficient prior sampling,
importance sampling, Jensen's inequality, ELBO tightness, and approximation
of the posterior. The main corrections were the distinction between model
and data distributions, the decoder's direction, the meaning of $dz$, and
the direction of the posterior KL.

## 9. Amortized Inference: A Shared Encoder

Without amortization, each training image can have its own variational
parameters $\lambda_i$, such as a Gaussian mean and variance. Finding a good
approximation requires optimizing those parameters for that image. As the
decoder changes, its posterior changes too, so existing approximations may
need updating. A new image requires another inference optimization.

The learner's explanation was: instead of solving for parameters separately
for every data point, learn a function that maps each image to good parameters.
This is amortized inference: one shared network learns to perform that mapping
across the dataset, making inference on a new image a forward pass.

We use $\lambda_i$ for the per-image parameters here and $\phi$ for the shared
encoder weights. The encoder outputs parameters of a distribution, not a
sampled latent vector directly:

$$
\operatorname{encoder}_\phi(x)
=\bigl(\mu_\phi(x),\log\sigma_\phi^2(x)\bigr),
\qquad
q_\phi(z\mid x)
=\mathcal N\!\left(\mu_\phi(x),
\operatorname{diag}(\sigma_\phi^2(x))\right).
$$

For $x\in\mathbb R^D$, each of the mean and log-variance outputs is in
$\mathbb R^d$. The covariance is $d\times d$. We then sample a latent vector
$z\in\mathbb R^d$ from the resulting Gaussian. The shared weights are the
same for every image, but their output depends on the image. This is a learned
approximation, not a guarantee of the exact or individually optimal posterior.

## 10. Two Equivalent Forms of the ELBO

The lecture's entropy expression and the reconstruction/KL expression are
equivalent. With all expectations below taken under $q_\phi(z\mid x)$,

$$
\begin{aligned}
\mathcal L(x;\theta,\phi)
&=\mathbb E_q[\log p_\theta(x,z)-\log q_\phi(z\mid x)]\\
&=\mathbb E_q[\log p_\theta(x,z)]+H(q_\phi(z\mid x))\\
&=\mathbb E_q[\log p_\theta(x\mid z)]
  +\mathbb E_q[\log p(z)-\log q_\phi(z\mid x)]\\
&=\mathbb E_q[\log p_\theta(x\mid z)]
  -D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right).
\end{aligned}
$$

For continuous latents, $H(q)=-\mathbb E_q[\log q]$ is differential entropy.
The correct pairings are joint log-density plus entropy, or reconstruction
log-likelihood minus KL. Reconstruction plus entropy alone would omit the
prior contribution.

The posterior KL in Section 7 measures the gap to the log marginal
likelihood. The prior KL here is part of the objective we optimize. Both
start from $q_\phi$, but they have different targets.

## 11. Why Encoder Gradients Need Special Care

Focus on the reconstruction term:

$$
R(\theta,\phi)
=\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x\mid z)].
$$

Changing decoder parameters $\theta$ changes the log-likelihood evaluated
at each latent sample, while the sampling distribution stays fixed. Under
the usual conditions for exchanging derivatives and expectations, we can
differentiate the decoder at sampled latent values and average the gradients.

Changing encoder parameters $\phi$ changes which latent values are sampled
and how often. For a fixed $z$, $\log p_\theta(x\mid z)$ has no explicit
$\phi$ dependence. If sampled latent values are treated as detached constants,
ordinary backpropagation through the decoder misses the effect of $\phi$
on their distribution. This does not mean the expected reconstruction term
is independent of $\phi$; its dependence comes through the sampling law.

The issue is therefore more specific than checking that the neural networks
are differentiable: we need a way to account for the parameter-dependent
sampling when estimating the gradient.

## 12. Reparameterization Exposes the Gradient Path

Draw noise from a fixed distribution and transform it using the encoder's
outputs:

$$
\epsilon\sim\mathcal N(0,I_d),\qquad
z=\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon.
$$

Here $\odot$ denotes elementwise multiplication. The mean, standard
deviation, noise, and sampled latent are all $d$-dimensional vectors.
This produces the same diagonal Gaussian distribution for $z$ as direct
sampling from $q_\phi(z\mid x)$.

The reconstruction expectation can now be written as

$$
R(\theta,\phi)
=\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}
\left[\log p_\theta\!\left(
x\mid\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon
\right)\right].
$$

The noise distribution does not depend on $\phi$. For a fixed noise draw,
the latent vector is a differentiable function of the encoder outputs.
The chain rule can carry reconstruction feedback through the decoder,
through $z$, and into the encoder. Under suitable regularity conditions,
these sampled gradients estimate the gradient of the expectation.

### Scalar Check from the Review

For $\mu=2$, $\sigma=1$, and a noise draw $\epsilon=0.5$, the sample is
$z=2.5$. Keeping the same noise draw and changing $\mu$ to $2.1$ changes
$z$ to $2.6$, which can change the decoder's reconstruction.

For a scalar reconstruction loss $\ell(z)$,

$$
\frac{\partial z}{\partial\mu}=1,
\qquad
\frac{\partial z}{\partial\sigma}=\epsilon,
\qquad
\frac{\partial\ell}{\partial\mu}=\frac{\partial\ell}{\partial z},
\qquad
\frac{\partial\ell}{\partial\sigma}
=\frac{\partial\ell}{\partial z}\epsilon.
$$

The encoder can learn both the center and spread of its Gaussian from
reconstruction feedback. Noise is held fixed while differentiating a
particular sampled computation; fresh noise can be drawn on the next pass.
Reparameterization preserves the distribution of $z$ while making this
gradient path explicit.

## 13. Reconstruction and Prior Compatibility

The reconstruction term encourages the decoder to assign high likelihood
to the original image using latent samples from that image's approximate
posterior. A particular handwritten nine might encode near $(0,2)$, and
decoding nearby samples should produce images resembling it. This coordinate
need not represent every nine or one interpretable feature.

The prior KL encourages each approximate posterior $q_\phi(z\mid x)$ to
remain close to the chosen prior, often $\mathcal N(0,I_d)$. It compares
distributions; an individual latent vector does not itself resemble or
follow a whole Gaussian density.

These objectives create a tradeoff. Image-dependent encodings can preserve
information useful for reconstruction. If every approximate posterior were
exactly the same prior, the sampled latent would carry no information about
which image was encoded. Training balances reconstruction with prior
compatibility rather than requiring every posterior to equal the prior.

### What If We Train with Reconstruction Alone?

Removing the KL term still allows reconstruction to train both the encoder
and decoder. The latents still have a distribution, but nothing in that
objective explicitly aligns it with our chosen prior.

For example, the encoder could put useful representations far from the
origin. In our two-dimensional example, a standard normal prior samples
mostly around the origin, potentially reaching regions where the decoder
has received little training. Reconstruction of encoded data can be good
while generation from prior samples is poor.

This resembles the sampling difficulty of an ordinary autoencoder, although
our encoder remains stochastic unless its sampling mechanism is also changed.
The KL term encourages compatibility between training encodings and the
prior used for generation; it does not guarantee that every prior sample
will decode into a good image.

## 14. Wednesday Checkpoint and Next Work

The completed review covered per-image variational optimization, amortized
inference, the encoder's Gaussian outputs, the two ELBO forms, the dependence
of the reconstruction expectation on $\phi$, reparameterization and its
gradient path, and the reconstruction–KL tradeoff.

S1 consolidation is complete. The subsequent Thursday review completed
[two derivations of the general ELBO](./w11_elbo_derivation.md).
The scalar and diagonal Gaussian KL and reparameterization proof were
completed on 2026-09-14 in that same note, followed by the three-question
checkpoint connecting these results to code and reconstruction loss.
The [minimal MNIST solved notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb)
was completed and reviewed on 2026-09-15, including sampling, loss reductions,
gradient checks, training, reconstructions, prior generation, and latent traversal.
The three observations distinguish approximate-posterior regularization from
reconstruction quality and input-conditioned reconstruction from prior generation.
Reconstruction does not guarantee a previously seen latent point; the displayed
inputs are held out. The [one-page latent-diffusion bridge](./w11_why_latent_diffusion.md)
was subsequently reviewed and approved on 2026-09-15, completing Week 11.
Next: Week 12 — normalizing flows and RealNVP on 2D data.

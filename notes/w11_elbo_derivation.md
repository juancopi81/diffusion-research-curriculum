# Week 11 — ELBO Derivation

**Status:** Thursday's general ELBO derivation and interpretation completed
on 2026-09-10. The scalar and diagonal Gaussian KL and mathematical
reparameterization proof were reviewed and consolidated on 2026-09-14.
The three-question code and reconstruction-loss checkpoint was completed
with a final explanation of additive constants on 2026-09-14. The planned
Friday theory and code map are complete. The minimal MNIST notebook and its
three observations were completed and reviewed on 2026-09-15; the separate
latent-diffusion bridge note remains pending.

**Basis:** Transcribed from the learner's two handwritten derivations supplied
on 2026-09-10, with reviewed notation and explanatory refinements. This is
the learner's derivation, not an official solution or a lecture transcript.
The conceptual background is consolidated in
[the CS236 VAE foundations note](./w11_cs236_vae.md).

The Gaussian sections below transcribe the learner's seven handwritten pages
supplied on 2026-09-14. They preserve the expanded algebra and marginalization
argument, with corrected logarithms and notation. The affine-Gaussian
justification and explicit shape annotations are review additions.

## Setup and Goal

Fix an observed example $x\in\mathbb R^D$ and let $z\in\mathbb R^d$ be a
continuous latent vector. The generative model has prior $p(z)$, decoder
$p_\theta(x\mid z)$, and joint density

$$
p_\theta(x,z)=p_\theta(x\mid z)p(z).
$$

We introduce a tractable approximate posterior $q_\phi(z\mid x)$. Throughout
the derivations, expectations are over $z$, with $x$, $\theta$, and $\phi$
held fixed. We assume $0<p_\theta(x)<\infty$, suitable support overlap, and
finite expectations for the manipulations below. In particular, the
importance-sampling identity requires $q_\phi(z\mid x)>0$ wherever
$p_\theta(x,z)$ contributes, up to sets of measure zero. Nondegenerate
Gaussian densities provide full support.

Our goal is to derive

$$
\log p_\theta(x)
\geq
\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right).
$$

The handwritten argument used sums, which apply to discrete latent variables.
Here we use integrals for continuous latents. Both versions follow the same
reasoning, and all distribution parameters and conditioning are kept explicit.

## Approach 1: Marginalization, Expectation, and Jensen

### Marginalize the Joint Density

Integrating out the latent variable gives

$$
p_\theta(x)=\int_{\mathbb R^d}p_\theta(x,z)\,dz.
$$

Multiply and divide the integrand by the approximate posterior:

$$
p_\theta(x)
=\int_{\mathbb R^d}
\frac{p_\theta(x,z)}{q_\phi(z\mid x)}q_\phi(z\mid x)\,dz.
$$

This is an exact rewrite. It is the basis of importance sampling: sample
latent values from a suitable proposal and correct for the sampling change
with the density ratio. We do not simply keep a few important latent values
and discard the rest of the integral.

### Why This Integral Is an Expectation: The LOTUS Connection

If $Z$ has density $q_\phi(z\mid x)$, the expected value of a function
$g(Z)$ is its density-weighted average:

$$
\mathbb E_{Z\sim q_\phi(z\mid x)}[g(Z)]
=\int_{\mathbb R^d}g(z)q_\phi(z\mid x)\,dz.
$$

This is the law of the unconscious statistician (LOTUS). It lets us compute
the expectation of a transformed random variable directly using the density
of $Z$, without first finding the distribution of $g(Z)$.

Here, choose

$$
g(z)=\frac{p_\theta(x,z)}{q_\phi(z\mid x)}.
$$

Our integral has exactly the form $g(z)q_\phi(z\mid x)$, so

$$
p_\theta(x)
=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right].
$$

For discrete latents, the same rule uses a probability-weighted sum instead
of an integral. If we approximate the expectation with samples drawn from
$q_\phi(z\mid x)$, we average the ratios without multiplying by that density
again: the sampling already supplies its weighting.

### Apply Jensen's Inequality

Taking logarithms gives

$$
\log p_\theta(x)
=\log\left(
\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right]
\right).
$$

The log of an average is not generally equal to the average of the logs.
Because $\log$ is concave, Jensen's inequality places the average of the
logs below the log of the average:

$$
\log p_\theta(x)
\geq
\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right]
=:\mathcal L(x;\theta,\phi).
$$

The expression on the right is the evidence lower bound, or ELBO.
The inequality allows equality; it is not a claim that moving the log
inside always changes the value strictly.

### Separate Reconstruction and KL

Factor the joint density and separate the logarithm:

$$
\begin{aligned}
\mathcal L(x;\theta,\phi)
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{p_\theta(x\mid z)p(z)}{q_\phi(z\mid x)}\right]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
+\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{p(z)}{q_\phi(z\mid x)}\right]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p(z)}\right]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right).
\end{aligned}
$$

The minus sign follows from reversing the ratio inside the logarithm.
The expectation is under $q_\phi(z\mid x)$, which is the first argument
of the KL divergence.

## Approach 2: Start from the Posterior KL

By definition,

$$
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)
=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p_\theta(z\mid x)}\right].
$$

Bayes' rule expresses the exact posterior as

$$
p_\theta(z\mid x)=\frac{p_\theta(x,z)}{p_\theta(x)}.
$$

Substitute this expression and separate the logarithm:

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)p_\theta(x)}{p_\theta(x,z)}\right]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p_\theta(x,z)}\right]
+\mathbb E_{z\sim q_\phi(z\mid x)}[\log p_\theta(x)]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p_\theta(x,z)}\right]
+\log p_\theta(x).
\end{aligned}
$$

The last step uses the fact that $\log p_\theta(x)$ is constant with
respect to $z$. Although observations can be modeled as random variables,
this particular observed $x$ is fixed in the expectation.

Rearrange and reverse the logarithmic ratio:

$$
\begin{aligned}
\log p_\theta(x)
&=-\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{q_\phi(z\mid x)}{p_\theta(x,z)}\right]
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\frac{p_\theta(x,z)}{q_\phi(z\mid x)}\right]
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right)\\
&=\mathcal L(x;\theta,\phi)
+D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p_\theta(z\mid x)\right).
\end{aligned}
$$

Since KL divergence is nonnegative,

$$
\log p_\theta(x)\geq\mathcal L(x;\theta,\phi).
$$

This recovers the same bound and identifies its gap. The gap vanishes when
the approximate posterior equals the exact posterior almost everywhere.
It is the KL to the exact posterior, not the KL to the prior.

## Interpretation of the Two Objective Terms

- **Reconstruction:** Increasing the expected conditional log-likelihood
  encourages the decoder to make the original $x$ likely using latent
  samples from $q_\phi(z\mid x)$. This is an average over the encoding
  distribution, not a guarantee that every latent sample reconstructs
  the image exactly.
- **Prior compatibility:** The subtracted KL penalizes divergence of the
  approximate posterior $q_\phi(z\mid x)$ from the chosen prior $p(z)$.
  It encourages compatibility with the latent distribution used for
  generation, while reconstruction rewards preserving information about $x$.

The prior KL is subtracted inside the ELBO. The posterior KL is added to
the ELBO to recover $\log p_\theta(x)$. Omitting the latter nonnegative
gap yields the bound; it does not remove $q_\phi(z\mid x)$ from training.

## Thursday Completion

Both handwritten approaches establish the general ELBO inequality, and
the reconstruction and prior-compatibility interpretations are clear.
Thursday's work is complete. The following sections record the subsequent
Gaussian derivations from the planned Friday work.

## Gaussian KL in One Dimension

Fix the observed $x$ and encoder parameters $\phi$. Let

$$
z\sim q_\phi(z\mid x)
=\mathcal N\!\left(z;\mu_\phi(x),\sigma_\phi^2(x)\right),
\qquad p(z)=\mathcal N(z;0,1),\qquad \sigma_\phi(x)>0.
$$

Here the normal notation on the right denotes a density evaluated at $z$;
the random variable $z$, rather than the density itself, is normally
distributed. All expectations in this section are under $q_\phi(z\mid x)$.
The outputs $\mu_\phi(x)$ and $\sigma_\phi(x)$ are constants with respect
to that expectation.

### Write and Subtract the Log Densities

Start from the definition:

$$
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log q_\phi(z\mid x)-\log p(z)\right].
$$

The approximate posterior density and its logarithm are

$$
q_\phi(z\mid x)
=\frac{1}{\sqrt{2\pi}\sigma_\phi(x)}
\exp\!\left(-\frac{(z-\mu_\phi(x))^2}{2\sigma_\phi^2(x)}\right),
$$

$$
\log q_\phi(z\mid x)
=\log\frac{1}{\sqrt{2\pi}\sigma_\phi(x)}
-\frac{(z-\mu_\phi(x))^2}{2\sigma_\phi^2(x)}.
$$

Similarly, the standard normal log density is

$$
\log p(z)=\log\frac{1}{\sqrt{2\pi}}-\frac{z^2}{2}.
$$

Work inside the expectation, retaining the signs when subtracting:

$$
\begin{aligned}
\log q_\phi(z\mid x)-\log p(z)
&=\log\frac{1}{\sqrt{2\pi}\sigma_\phi(x)}
-\frac{(z-\mu_\phi(x))^2}{2\sigma_\phi^2(x)}
-\log\frac{1}{\sqrt{2\pi}}+\frac{z^2}{2}\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac{z^2}{2}-\frac{(z-\mu_\phi(x))^2}{2\sigma_\phi^2(x)}.
\end{aligned}
$$

### Expand the Square and Apply Linearity

Pull the constants outside the expectation and expand the centered square:

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
&=\log\frac{1}{\sigma_\phi(x)}
+\frac12\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-\frac{1}{2\sigma_\phi^2(x)}
\mathbb E_{z\sim q_\phi(z\mid x)}[(z-\mu_\phi(x))^2]\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac12\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]\\
&\quad-\frac{1}{2\sigma_\phi^2(x)}
\left(\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-2\mu_\phi(x)\mathbb E_{z\sim q_\phi(z\mid x)}[z]
+\mu_\phi^2(x)\right)\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac12\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-\frac{\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]}{2\sigma_\phi^2(x)}\\
&\quad+\frac{\mu_\phi(x)\mathbb E_{z\sim q_\phi(z\mid x)}[z]}{\sigma_\phi^2(x)}
-\frac{\mu_\phi^2(x)}{2\sigma_\phi^2(x)}.
\end{aligned}
$$

The handwritten regrouping of the two second-moment terms is also valid:

$$
\frac12\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-\frac{\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]}{2\sigma_\phi^2(x)}
=\frac{\sigma_\phi^2(x)\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]}{2\sigma_\phi^2(x)}.
$$

### Evaluate the Moments

By the specified Gaussian distribution,

$$
\mathbb E_{z\sim q_\phi(z\mid x)}[z]=\mu_\phi(x).
$$

The variance identity gives

$$
\begin{aligned}
\sigma_\phi^2(x)
&=\operatorname{Var}_{z\sim q_\phi(z\mid x)}(z)\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
-\left(\mathbb E_{z\sim q_\phi(z\mid x)}[z]\right)^2,
\end{aligned}
$$

and hence

$$
\mathbb E_{z\sim q_\phi(z\mid x)}[z^2]
=\sigma_\phi^2(x)+\mu_\phi^2(x).
$$

### Substitute and Carry Out the Cancellations

Substituting these moments into the expanded KL gives

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
&=\log\frac{1}{\sigma_\phi(x)}
+\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2}
-\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2\sigma_\phi^2(x)}\\
&\quad+\frac{\mu_\phi^2(x)}{\sigma_\phi^2(x)}
-\frac{\mu_\phi^2(x)}{2\sigma_\phi^2(x)}\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2}
-\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2\sigma_\phi^2(x)}
+\frac{\mu_\phi^2(x)}{2\sigma_\phi^2(x)}\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2}
-\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)-\mu_\phi^2(x)}{2\sigma_\phi^2(x)}\\
&=\log\frac{1}{\sigma_\phi(x)}
+\frac{\sigma_\phi^2(x)+\mu_\phi^2(x)}{2}-\frac12.
\end{aligned}
$$

Since the standard deviation is positive,

$$
\log\frac{1}{\sigma_\phi(x)}
=-\log\sigma_\phi(x)
=-\frac12\log\sigma_\phi^2(x).
$$

Therefore,

$$
\boxed{
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
=\frac12\left[
\sigma_\phi^2(x)+\mu_\phi^2(x)-\log\sigma_\phi^2(x)-1
\right].
}
$$

### Check Against the Prior

Set $\sigma_\phi(x)=1$ and $\mu_\phi(x)=0$. Then

$$
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
=\frac12[1+0-\log 1-1]=0.
$$

For future reuse, the shorter route is to recognize
$\mathbb E_{z\sim q_\phi(z\mid x)}[(z-\mu_\phi(x))^2]=\sigma_\phi^2(x)$
immediately. The expanded calculation above is retained because it records
the actual handwritten reasoning and how the cancellations occur.

## Extension to Diagonal Gaussian Latents

Now let

$$
q_\phi(z\mid x)=\mathcal N\!\left(z;\mu_\phi(x),
\operatorname{diag}(\sigma_\phi^2(x))\right),
\qquad p(z)=\mathcal N(z;0,I_d).
$$

For fixed $x$, these are jointly Gaussian distributions with diagonal
covariance matrices. Their coordinates are therefore independent within
each distribution: uncorrelated coordinates of a jointly Gaussian vector
are independent. This does not assert that encoded coordinates remain
independent after mixing encodings from different observations.

The joint densities factor into their coordinate marginals:

$$
q_\phi(z\mid x)=\prod_{i=1}^d q_\phi(z_i\mid x),
\qquad p(z)=\prod_{i=1}^d p(z_i).
$$

Each $q_\phi(z_i\mid x)$ is the one-dimensional normal density with mean
$\mu_{\phi,i}(x)$ and variance $\sigma_{\phi,i}^2(x)$; each $p(z_i)$ is
standard normal.

### Products of Densities Become Sums of Log Densities

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\log\prod_{i=1}^d q_\phi(z_i\mid x)
-\log\prod_{i=1}^d p(z_i)\right]\\
&=\mathbb E_{z\sim q_\phi(z\mid x)}
\left[\sum_{i=1}^d\log q_\phi(z_i\mid x)
-\sum_{i=1}^d\log p(z_i)\right]\\
&=\sum_{i=1}^d\mathbb E_{z\sim q_\phi(z\mid x)}
[\log q_\phi(z_i\mid x)]
-\sum_{i=1}^d\mathbb E_{z\sim q_\phi(z\mid x)}[\log p(z_i)].
\end{aligned}
$$

Both products must be inside logarithms. In particular,
$\log\prod_i p(z_i)=\sum_i\log p(z_i)$, not $\prod_i\log p(z_i)$.
Linearity moves the finite sums outside the expectation.

### Why the Other Coordinates Integrate Out

Fix a coordinate $i$. Its expectation is initially over the whole vector:

$$
\begin{aligned}
\mathbb E_{z\sim q_\phi(z\mid x)}[\log q_\phi(z_i\mid x)]
&=\int_{\mathbb R}\cdots\int_{\mathbb R}
\log q_\phi(z_i\mid x)\,q_\phi(z\mid x)\,dz_1\cdots dz_d\\
&=\int_{\mathbb R}\cdots\int_{\mathbb R}
\log q_\phi(z_i\mid x)
\prod_{j=1}^d q_\phi(z_j\mid x)\,dz_1\cdots dz_d\\
&=\left[\int_{\mathbb R}\log q_\phi(z_i\mid x)
q_\phi(z_i\mid x)\,dz_i\right]
\prod_{\substack{j=1\\j\ne i}}^d
\left[\int_{\mathbb R}q_\phi(z_j\mid x)\,dz_j\right]\\
&=\left[\int_{\mathbb R}\log q_\phi(z_i\mid x)
q_\phi(z_i\mid x)\,dz_i\right](1\times\cdots\times1)\\
&=\mathbb E_{z_i\sim q_\phi(z_i\mid x)}[\log q_\phi(z_i\mid x)].
\end{aligned}
$$

Every other coordinate's marginal density integrates to one. The integrals
can be separated here because the Gaussian log-density terms are integrable.
The same calculation applies to the prior log density, but the weighting
distribution remains the approximate posterior:

$$
\begin{aligned}
\mathbb E_{z\sim q_\phi(z\mid x)}[\log p(z_i)]
&=\left[\int_{\mathbb R}\log p(z_i)q_\phi(z_i\mid x)\,dz_i\right]
\prod_{\substack{j=1\\j\ne i}}^d
\left[\int_{\mathbb R}q_\phi(z_j\mid x)\,dz_j\right]\\
&=\mathbb E_{z_i\sim q_\phi(z_i\mid x)}[\log p(z_i)].
\end{aligned}
$$

### Group the Terms Coordinatewise

$$
\begin{aligned}
D_{\mathrm{KL}}\!\left(q_\phi(z\mid x)\Vert p(z)\right)
&=\sum_{i=1}^d\mathbb E_{z_i\sim q_\phi(z_i\mid x)}
\left[\log q_\phi(z_i\mid x)-\log p(z_i)\right]\\
&=\sum_{i=1}^d D_{\mathrm{KL}}\!\left(q_\phi(z_i\mid x)\Vert p(z_i)\right)\\
&=\frac12\sum_{i=1}^d
\left[\sigma_{\phi,i}^2(x)+\mu_{\phi,i}^2(x)
-\log\sigma_{\phi,i}^2(x)-1\right].
\end{aligned}
$$

The total KL is the sum of the scalar KL contributions. For the handwritten
two-dimensional check, take

$$
\sigma_\phi^2(x)=\begin{bmatrix}1\\1\end{bmatrix},
\qquad\mu_\phi(x)=\begin{bmatrix}0\\0\end{bmatrix}.
$$

Each contribution is $\tfrac12[1+0-0-1]=0$, so the total is zero.
The variance vector has shape $d\times1$; applying $\operatorname{diag}$
to it gives the $d\times d$ covariance matrix.

## Reparameterization: Distribution, Mean, and Covariance

Fix $x$ and $\phi$, sample $\epsilon\sim\mathcal N(0,I_d)$, and define

$$
z=\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon.
$$

The mean, standard-deviation vector, noise, and resulting latent vector all
have shape $d\times1$. The multiplication is elementwise. The vector
$\sigma_\phi(x)$ contains standard deviations, not variances.

### Expected Value

Take the expectation over the sampled noise:

$$
\begin{aligned}
\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}[z]
&=\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}
[\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon]\\
&=\mu_\phi(x)+\sigma_\phi(x)\odot
\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}[\epsilon]\\
&=\mu_\phi(x)+\sigma_\phi(x)\odot0\\
&=\mu_\phi(x).
\end{aligned}
$$

### Covariance, Entry by Entry

The mean is a fixed shift, so

$$
\operatorname{Cov}_{\epsilon}(z)
=\operatorname{Cov}_{\epsilon}
(\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon)
=\operatorname{Cov}_{\epsilon}(\sigma_\phi(x)\odot\epsilon).
$$

For coordinates $i$ and $j$, expand the covariance definition:

$$
\begin{aligned}
\operatorname{Cov}_{\epsilon}(z_i,z_j)
&=\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}
[(z_i-\mathbb E_{\epsilon}[z_i])(z_j-\mathbb E_{\epsilon}[z_j])]\\
&=\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}
[(z_i-\mu_{\phi,i}(x))(z_j-\mu_{\phi,j}(x))]\\
&=\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}
[(\sigma_{\phi,i}(x)\epsilon_i)(\sigma_{\phi,j}(x)\epsilon_j)]\\
&=\sigma_{\phi,i}(x)\sigma_{\phi,j}(x)
\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}[\epsilon_i\epsilon_j].
\end{aligned}
$$

When $i=j$, each standard normal coordinate has zero mean and unit variance:

$$
\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}[\epsilon_i^2]
=\operatorname{Var}(\epsilon_i)+(\mathbb E[\epsilon_i])^2=1+0=1,
$$

so $\operatorname{Cov}_{\epsilon}(z_i,z_i)=\sigma_{\phi,i}^2(x)$.

When $i\ne j$, the standard normal coordinates are independent:

$$
\mathbb E_{\epsilon\sim\mathcal N(0,I_d)}[\epsilon_i\epsilon_j]
=\mathbb E[\epsilon_i]\mathbb E[\epsilon_j]=0\times0=0,
$$

so $\operatorname{Cov}_{\epsilon}(z_i,z_j)=0$. Therefore,

$$
\operatorname{Cov}_{\epsilon}(z)
=\operatorname{diag}(\sigma_\phi^2(x)).
$$

### Why the Result Is Gaussian

Matching a mean and covariance alone does not identify a distribution as
Gaussian. The additional justification is that, for fixed $x$ and $\phi$,

$$
z=\mu_\phi(x)+\operatorname{diag}(\sigma_\phi(x))\epsilon
$$

is an affine transformation of the jointly Gaussian vector $\epsilon$.
Affine transformations preserve joint Gaussianity. Together with the mean
and covariance just derived, this establishes

$$
\boxed{
z\sim\mathcal N\!\left(\mu_\phi(x),
\operatorname{diag}(\sigma_\phi^2(x))\right).
}
$$

Reparameterization therefore preserves the desired approximate posterior
distribution while exposing a differentiable dependence on encoder outputs
for each fixed noise draw.

## Session Boundary — 2026-09-14

The scalar KL, diagonal extension, zero-KL checks, and mathematical
reparameterization proof are complete. The full handwritten route is retained;
there is no need to repeat these proofs before starting the notebook.

The following three-question checkpoint closes the bridge to implementation.
The notebook and latent-diffusion note remain separate tasks.

## Three-Question Code and Loss Checkpoint

### 1. Log-Variance and Sampling Shapes

The learner correctly identified that exponentiating half the log-variance
produces the standard deviation:

$$
\exp\!\left(\tfrac12\log\sigma_{\phi,i}^2(x)\right)
=\sqrt{\sigma_{\phi,i}^2(x)}=\sigma_{\phi,i}(x).
$$

For a batch of $B$ images, `mu`, `logvar`, `std`, `epsilon`, and `z` all
have shape $(B,d)$. Here $d$ is the latent dimension, not the image
dimension $D$. With independent standard normal noise entries, the code map is

```python
std = (0.5 * logvar).exp()
z = mu + std * epsilon
```

These tensor expressions are implemented and checked in the
[minimal MNIST solved notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb).

### 2. KL Reduction and the Optimization Sign

The learner correctly explained the reduction: sum the KL contributions
over latent dimensions to obtain one KL per image, then average over images.

```python
kl_per_coordinate = 0.5 * (logvar.exp() + mu.square() - logvar - 1)
kl_per_image = kl_per_coordinate.sum(dim=1)
kl_loss = kl_per_image.mean()
```

The shapes are $(B,d)$, $(B,)$, and scalar, respectively. Minimizing the
negative ELBO adds the positive KL penalty to the reconstruction negative
log-likelihood. This is equivalent to maximizing the ELBO; minimization
simply matches the usual optimizer convention:

$$
\theta\leftarrow\theta-\eta\nabla_\theta(-\mathcal L)
=\theta+\eta\nabla_\theta\mathcal L.
$$

The same sign equivalence holds for the encoder parameters $\phi$.

### 3. Gaussian Reconstruction and Additive Constants

The learner recognized the squared-error form and connected the Gaussian
density to sampling around the decoder mean. Write the observation model as

$$
p_\theta(x\mid z)=\mathcal N(x;m_\theta(z),\tau^2I_D),
\qquad \tau>0\text{ fixed}.
$$

A fresh observation from this model can be sampled as
$\widetilde x=m_\theta(z)+\tau\eta$, with
$\eta\sim\mathcal N(0,I_D)$. During reconstruction training, however,
$x$ is the fixed observed target whose likelihood we evaluate. This decoder
noise is distinct from the encoder noise used to sample $z$.

From the Gaussian density,

$$
p_\theta(x\mid z)
=(2\pi\tau^2)^{-D/2}
\exp\!\left(-\frac{1}{2\tau^2}
\sum_{j=1}^D(x_j-m_{\theta,j}(z))^2\right),
$$

so

$$
-\log p_\theta(x\mid z)
=\frac{1}{2\tau^2}\sum_{j=1}^D(x_j-m_{\theta,j}(z))^2
+\frac D2\log(2\pi\tau^2).
$$

The additive term $C=\tfrac D2\log(2\pi\tau^2)$ has zero gradient with
respect to both trainable parameter sets because $D$ and $\tau$ are fixed.
It shifts the objective's value without changing its minimizer or gradients,
so we may omit it for training. Retain it when reporting the actual Gaussian
negative log-likelihood or numerical ELBO. If the variance is learned, this
term is no longer constant with respect to the trainable parameters.

The remaining term is scaled sum of squared errors. If MSE means the mean
over the $D$ observation coordinates, it equals $D/(2\tau^2)$ times MSE.
The multiplicative factor $1/(2\tau^2)$ must be preserved when combining
reconstruction and KL: dropping it changes their relative weighting.

For one reparameterized latent sample per image, the code map is

```python
# x and decoder_mean have shape (B, D); tau_squared is fixed and positive.
reconstruction_per_image = (
    (x - decoder_mean).square().sum(dim=1) / (2 * tau_squared)
)
loss = (reconstruction_per_image + kl_per_image).mean()
```

Here `decoder_mean` is evaluated at the sampled `z`. This estimates the
negative ELBO up to the omitted additive constant: reconstruction uses a
Monte Carlo sample, while the diagonal Gaussian KL is evaluated analytically.

The bounded checkpoint is complete. The subsequent minimal VAE notebook
was completed and reviewed on 2026-09-15 without repeating the handwritten
derivations.

## Implementation Review — 2026-09-15

The [solved notebook](../notebooks/w11_minimal_vae_mnist_solved.ipynb) implements
reparameterization, Gaussian reconstruction plus analytic KL, and a
one-coordinate traversal. Its checks cover sampling moments and gradients,
loss signs and reductions, agreement with PyTorch's Gaussian KL, and preservation
of the fixed traversal coordinate. The baseline notebook retains the exercises.

With 10,000 training images, 1,000 held-out images, two latent coordinates,
and five epochs, held-out reconstruction loss decreased from 267.43 to 214.83
between epochs 1 and 5; held-out KL decreased from 10.85 to 7.71. These are
per-image averages; reconstruction omits the fixed Gaussian normalization constant.
The results demonstrate learning, not an isolated test of bottleneck dimension
or a claim of high-quality generation.

The optional observation-noise comparison was also completed: it holds the
latent fixed, adds Gaussian observation noise to the decoder mean, and explicitly
reports that clipping to the display range is only a visualization step.

The final observations identify preserved and lost image details, distinguish
input-conditioned reconstruction from prior generation, and describe the effect
of increasing the second latent coordinate. The remaining Week 11 task is
the separate one-page explanation of why diffusion can operate in learned latents.

# Week 4 — Conditioning in Diffusion (Diffusion Contact)

> **Time**: 45-60 minutes  
> **Mode**: guided worksheet (no provided solutions)  
> **Goal**: understand where conditioning appears in diffusion, then derive the key pieces yourself.

---

## Deliverable for This Week

Complete this note with your own derivations and short explanations:

1. Derive conditional and marginal moments for a 1D forward noising model.
2. Derive the posterior form $q(x_0 \mid x_t)$ in the Gaussian case.
3. Explain why denoising is a conditional expectation problem.

---

## 1) Setup: One-Step Forward Noising

Work with the scalar model

$$
x_0 \sim \mathcal{N}(\mu_0, s_0^2), \qquad \epsilon \sim \mathcal{N}(0,1), \qquad \epsilon \perp x_0,
$$

and

$$
x_t = \alpha_t x_0 + \sigma_t \epsilon,
$$

with fixed $\alpha_t > 0$, $\sigma_t > 0$.

### Checkpoint 1.1 (independent derivation)

From

$$
x_t = \alpha_t x_0 + \sigma_t \epsilon,
$$

with fixed $\alpha_t,\sigma_t$ and $\epsilon \perp x_0$:

For $\mathbb{E}[x_t \mid x_0]$:

$$
\begin{aligned}
\mathbb{E}[x_t \mid x_0]
&= \mathbb{E}[\alpha_t x_0 + \sigma_t \epsilon \mid x_0] \\
&= \mathbb{E}[\alpha_t x_0 \mid x_0] + \mathbb{E}[\sigma_t \epsilon \mid x_0] \quad \text{(linearity)} \\
&= \alpha_t \mathbb{E}[x_0 \mid x_0] + \sigma_t \mathbb{E}[\epsilon \mid x_0] \quad \text{(constants out)} \\
&= \alpha_t x_0 + \sigma_t \mathbb{E}[\epsilon] \quad \text{(independence)} \\
&= \alpha_t x_0 \quad \text{(since } \mathbb{E}[\epsilon]=0 \text{).}
\end{aligned}
$$

For $\mathrm{Var}(x_t \mid x_0)$:

$$
\begin{aligned}
\mathrm{Var}(x_t \mid x_0)
&= \mathrm{Var}(\alpha_t x_0 + \sigma_t \epsilon \mid x_0) \\
&= \mathrm{Var}(\sigma_t \epsilon \mid x_0) \quad \text{(} \alpha_t x_0 \text{ is fixed given } x_0 \text{)} \\
&= \sigma_t^2 \mathrm{Var}(\epsilon \mid x_0) \\
&= \sigma_t^2 \mathrm{Var}(\epsilon) \quad \text{(independence)} \\
&= \sigma_t^2 \quad \text{(since } \epsilon \sim \mathcal{N}(0,1) \text{).}
\end{aligned}
$$

One-line results:

- $\mathbb{E}[x_t \mid x_0] = \alpha_t x_0$
- $\mathrm{Var}(x_t \mid x_0) = \sigma_t^2$

### Checkpoint 1.2 (independent derivation)

For $\mathbb{E}[x_t]$ (using LOTUS):

$$
\begin{aligned}
\mathbb{E}[x_t]
&= \mathbb{E}\!\left[\mathbb{E}[x_t \mid x_0]\right] \\
&= \mathbb{E}[\alpha_t x_0] \quad \text{(from Checkpoint 1.1)} \\
&= \alpha_t \mathbb{E}[x_0] \\
&= \alpha_t \mu_0.
\end{aligned}
$$

For $\mathrm{Var}(x_t)$ (linearity + independence):

$$
\begin{aligned}
\mathrm{Var}(x_t)
&= \mathrm{Var}(\alpha_t x_0 + \sigma_t \epsilon) \\
&= \alpha_t^2 \mathrm{Var}(x_0) + \sigma_t^2 \mathrm{Var}(\epsilon)
+ 2\alpha_t \sigma_t \mathrm{Cov}(x_0,\epsilon) \\
&= \alpha_t^2 s_0^2 + \sigma_t^2 \cdot 1 + 2\alpha_t \sigma_t \cdot 0 \quad \text{(independence)} \\
&= \alpha_t^2 s_0^2 + \sigma_t^2.
\end{aligned}
$$

One-line results:

- $\mathbb{E}[x_t] = \alpha_t \mu_0$
- $\mathrm{Var}(x_t) = \alpha_t^2 s_0^2 + \sigma_t^2$

### Checkpoint 1.3 (quick interpretation)

When $x_0$ is fixed, randomness in $x_t=\alpha_t x_0+\sigma_t\epsilon$ comes only from $\epsilon$.  
So $\sigma_t$ does not change the conditional mean $\mathbb{E}[x_t\mid x_0]=\alpha_t x_0$, it only changes spread.  
Specifically, $\mathrm{Var}(x_t\mid x_0)=\sigma_t^2$: larger $\sigma_t$ means wider noise around $\alpha_t x_0$ (not exponential growth).

---

## 2) Posterior View: $q(x_0 \mid x_t)$

Treat $x_t$ as observed. Start from:

$$
q(x_0 \mid x_t) \propto q(x_t \mid x_0)\,q(x_0).
$$

Using the setup above:

$$
q(x_0) \propto \exp\!\left(-\frac{(x_0-\mu_0)^2}{2s_0^2}\right),
\qquad
q(x_t \mid x_0) \propto \exp\!\left(-\frac{(x_t-\alpha_t x_0)^2}{2\sigma_t^2}\right).
$$

### Checkpoint 2.1 (complete derivation)

Start from

$$
q(x_0 \mid x_t) \propto q(x_t \mid x_0)\,q(x_0).
$$

Take logs:

$$
\log q(x_0 \mid x_t)=\log q(x_t \mid x_0)+\log q(x_0)+C_0(x_t),
$$

where $C_0(x_t)$ collects terms independent of $x_0$.

Substitute the Gaussian forms (dropping normalizing constants into $C_1(x_t)$):

$$
\log q(x_0 \mid x_t)
=-\frac{(x_t-\alpha_t x_0)^2}{2\sigma_t^2}
-\frac{(x_0-\mu_0)^2}{2s_0^2}
+C_1(x_t).
$$

Expand each square explicitly:

$$
(x_t-\alpha_t x_0)^2=x_t^2-2\alpha_t x_t x_0+\alpha_t^2 x_0^2,
$$

$$
(x_0-\mu_0)^2=x_0^2-2\mu_0 x_0+\mu_0^2.
$$

Plug back in:

$$
\log q(x_0 \mid x_t)
=-\frac{x_t^2-2\alpha_t x_t x_0+\alpha_t^2 x_0^2}{2\sigma_t^2}
-\frac{x_0^2-2\mu_0 x_0+\mu_0^2}{2s_0^2}
+C_1(x_t).
$$

Distribute the minus signs term-by-term:

$$
\log q(x_0 \mid x_t)
=-\frac{x_t^2}{2\sigma_t^2}
+\frac{\alpha_t x_t}{\sigma_t^2}x_0
-\frac{\alpha_t^2}{2\sigma_t^2}x_0^2
-\frac{1}{2s_0^2}x_0^2
+\frac{\mu_0}{s_0^2}x_0
-\frac{\mu_0^2}{2s_0^2}
+C_1(x_t).
$$

Now collect by powers of $x_0$:

$$
\log q(x_0 \mid x_t)
=-\frac12\left(\frac{\alpha_t^2}{\sigma_t^2}+\frac{1}{s_0^2}\right)x_0^2
+\left(\frac{\alpha_t x_t}{\sigma_t^2}+\frac{\mu_0}{s_0^2}\right)x_0
+C(x_t),
$$

where

$$
C(x_t)= -\frac{x_t^2}{2\sigma_t^2}-\frac{\mu_0^2}{2s_0^2}+C_1(x_t)
$$

contains all terms that do not depend on $x_0$.

### Checkpoint 2.2 (complete the square, step-by-step)

Start from the quadratic form obtained in Checkpoint 2.1:

$$
\log q(x_0 \mid x_t)
=-\frac12\left(\frac{\alpha_t^2}{\sigma_t^2}+\frac{1}{s_0^2}\right)x_0^2
+\left(\frac{\alpha_t x_t}{\sigma_t^2}+\frac{\mu_0}{s_0^2}\right)x_0
+C(x_t).
$$

Define

$$
A:=\left(\frac{\alpha_t^2}{\sigma_t^2}+\frac{1}{s_0^2}\right),
\qquad
B:=\left(\frac{\alpha_t x_t}{\sigma_t^2}+\frac{\mu_0}{s_0^2}\right).
$$

Then

$$
\log q(x_0 \mid x_t)= -\frac12 A x_0^2 + Bx_0 + C(x_t)
= -\frac12 A\left(x_0^2 - 2\frac{B}{A}x_0\right)+C(x_t).
$$

Now simplify $\frac{B}{A}$ explicitly:

$$
B=\frac{\alpha_t x_t s_0^2+\mu_0\sigma_t^2}{\sigma_t^2 s_0^2},
\qquad
A=\frac{\alpha_t^2 s_0^2+\sigma_t^2}{\sigma_t^2 s_0^2},
$$

so

$$
\frac{B}{A}
=\frac{\alpha_t x_t s_0^2+\mu_0\sigma_t^2}{\alpha_t^2 s_0^2+\sigma_t^2}
\,=: k_t(x_t).
$$

Substitute this back:

$$
\log q(x_0 \mid x_t)
= -\frac12 A\left(x_0^2-2k_t(x_t)x_0\right)+C(x_t).
$$

Use $x_0^2-2k x_0=(x_0-k)^2-k^2$:

$$
\log q(x_0 \mid x_t)
= -\frac12 A\left[(x_0-k_t(x_t))^2-k_t(x_t)^2\right]+C(x_t)
$$

$$
= -\frac12 A(x_0-k_t(x_t))^2
+\frac12 A\,k_t(x_t)^2
+C(x_t).
$$

Absorb the $x_0$-independent terms into a new constant $C_1(x_t)$:

$$
\log q(x_0 \mid x_t)
= -\frac12 A(x_0-k_t(x_t))^2 + C_1(x_t).
$$

Match with Gaussian log form

$$
\log q(x_0 \mid x_t)
=-\frac{(x_0-m_t(x_t))^2}{2v_t}+C_2(x_t).
$$

Therefore:

- posterior variance

$$
v_t=\frac{1}{A}
=\frac{1}{\frac{\alpha_t^2}{\sigma_t^2}+\frac{1}{s_0^2}}
=\frac{\sigma_t^2 s_0^2}{\alpha_t^2 s_0^2+\sigma_t^2}.
$$

- posterior mean

$$
m_t(x_t)=k_t(x_t)
=\frac{\alpha_t s_0^2\,x_t+\mu_0\sigma_t^2}{\alpha_t^2 s_0^2+\sigma_t^2}.
$$

Write $m_t(x_t)$ in affine form:

$$
m_t(x_t)=A_t x_t+b_t,
$$

with

$$
A_t=\frac{\alpha_t s_0^2}{\alpha_t^2 s_0^2+\sigma_t^2},
\qquad
b_t=\frac{\mu_0\sigma_t^2}{\alpha_t^2 s_0^2+\sigma_t^2}.
$$

### Checkpoint 2.3 (sanity checks)

1. As $\sigma_t \to 0$:

$$
A_t=\frac{\alpha_t s_0^2}{\alpha_t^2 s_0^2+\sigma_t^2}\to \frac{1}{\alpha_t},\qquad
b_t=\frac{\mu_0\sigma_t^2}{\alpha_t^2 s_0^2+\sigma_t^2}\to 0,\qquad
v_t=\frac{\sigma_t^2 s_0^2}{\alpha_t^2 s_0^2+\sigma_t^2}\to 0.
$$

So $m_t(x_t)=A_t x_t+b_t \to x_t/\alpha_t$, and $q(x_0\mid x_t)$ collapses around one value (almost deterministic).
Intuition (images): with almost no noise, the corrupted image still looks like the original image, so you can infer the clean image very confidently.

2. As $\sigma_t \to \infty$:

$$
A_t\to 0,\qquad b_t\to \mu_0,\qquad v_t\to s_0^2.
$$

So $m_t(x_t)\to \mu_0$, and

$$
q(x_0\mid x_t)\to \mathcal{N}(\mu_0,s_0^2)=q(x_0).
$$

The posterior becomes the prior: $x_t$ no longer adds useful information.
Intuition (images): if the observed image is mostly static, it does not tell you what the original image was, so you fall back to your general prior about likely images.

---

## 3) Denoising as Conditional Expectation

Let $g$ be any estimator of $x_0$ from $x_t$, with squared-error objective:

$$
\mathcal{L}(g)=\mathbb{E}\left[(x_0-g(x_t))^2\right].
$$

### Checkpoint 3.1

Condition first on $x_t$:

$$
\mathcal{L}(g)=\mathbb{E}\!\left[\mathbb{E}\!\left[(x_0-g(x_t))^2\mid x_t\right]\right].
$$

Define the posterior mean

$$
m(x_t):=\mathbb{E}[x_0\mid x_t].
$$

Add and subtract $m(x_t)$ inside the square:

$$
x_0-g(x_t)=\big(x_0-m(x_t)\big)+\big(m(x_t)-g(x_t)\big).
$$

Then

$$
\begin{aligned}
\mathbb{E}\!\left[(x_0-g(x_t))^2\mid x_t\right]
&= \mathbb{E}\!\left[(x_0-m(x_t))^2\mid x_t\right] \\
&\quad + 2\,\mathbb{E}\!\left[(x_0-m(x_t))(m(x_t)-g(x_t))\mid x_t\right] \\
&\quad + \mathbb{E}\!\left[(m(x_t)-g(x_t))^2\mid x_t\right].
\end{aligned}
$$

Now simplify term by term:

- First term:

  $$
  \mathbb{E}\!\left[(x_0-m(x_t))^2\mid x_t\right]=\mathrm{Var}(x_0\mid x_t).
  $$

  Why: by definition,

  $$
  \mathrm{Var}(X\mid Y)=\mathbb{E}\!\left[(X-\mathbb{E}[X\mid Y])^2\mid Y\right].
  $$

  Here $X=x_0$ and $Y=x_t$, and $\mathbb{E}[x_0\mid x_t]=m(x_t)$.

- Cross term:

  $$
  \begin{aligned}
  \mathbb{E}\!\left[(x_0-m)(m-g)\mid x_t\right]
  &=(m-g)\,\mathbb{E}[x_0-m\mid x_t] \\
  &=(m-g)\,\big(\mathbb{E}[x_0\mid x_t]-m\big)=0.
  \end{aligned}
  $$

  Why this is zero:

- $(m-g)$ is a function of $x_t$ only, so under conditioning on $x_t$ it is a constant and can be factored out.
- $\mathbb{E}[x_0-m\mid x_t]=0$ because $m(x_t)=\mathbb{E}[x_0\mid x_t]$.
- Therefore the product is zero.

- Last term (deterministic given $x_t$):
  $$
  \mathbb{E}\!\left[(m(x_t)-g(x_t))^2\mid x_t\right]=(m(x_t)-g(x_t))^2.
  $$
  Why: $(m(x_t)-g(x_t))^2$ depends only on $x_t$; once conditioned on $x_t$, it is non-random.

So the conditional decomposition is

$$
\mathbb{E}\!\left[(x_0-g(x_t))^2\mid x_t\right]
=\mathrm{Var}(x_0\mid x_t)+(m(x_t)-g(x_t))^2.
$$

Taking expectation over $x_t$:

$$
\mathcal{L}(g)
=\mathbb{E}\!\left[\mathrm{Var}(x_0\mid x_t)\right]
+\mathbb{E}\!\left[(m(x_t)-g(x_t))^2\right].
$$

Interpretation:

- $\mathbb{E}[\mathrm{Var}(x_0\mid x_t)]$ is irreducible uncertainty.
- $\mathbb{E}[(m(x_t)-g(x_t))^2]$ is estimator mismatch.

### Checkpoint 3.2

From Checkpoint 3.1:

$$
\mathcal{L}(g)
=\mathbb{E}\!\left[\mathrm{Var}(x_0\mid x_t)\right]
+\mathbb{E}\!\left[(m(x_t)-g(x_t))^2\right].
$$

The first term does not depend on $g$. The second term is always $\ge 0$, and it is minimized when it is zero almost surely, i.e.,

$$
g^\star(x_t)=m(x_t)=\mathbb{E}[x_0\mid x_t].
$$

Why: for any random variable $Z$, $Z^2\ge 0$, hence $\mathbb{E}[Z^2]\ge 0$. Here $Z=m(x_t)-g(x_t)$, so the minimum possible value is $0$, achieved when $g(x_t)=m(x_t)$ almost surely.

Therefore, under MSE, the optimal denoiser is the posterior conditional mean.

### Checkpoint 3.3 (connection to diffusion training)

In diffusion, we observe a noisy sample $x_t$ and want to recover the clean variable $x_0$.  
If our prediction function is $g(x_t)$ and we train with squared loss $\mathbb{E}[(x_0-g(x_t))^2]$, the unique optimal target is $g^\star(x_t)=\mathbb{E}[x_0\mid x_t]$.  
So denoising is not arbitrary inversion; it is estimation of a conditional expectation under the forward noising distribution $q(x_t\mid x_0)$.  
As noise level changes with $t$, the conditional distribution $q(x_0\mid x_t)$ changes, and so does its mean.  
This is why diffusion training can be interpreted as learning the best conditional estimator of the clean signal from noisy observations.

---

## 4) Optional Code Check (No Closed-Form Answers Needed Here)

Use `/notebooks/w04_normal_loc_scale_solved.ipynb` as a starting reference.

### Checkpoint 4.1

Simulate pairs $(x_0, x_t)$ from the setup in Section 1.

### Checkpoint 4.2

Estimate a linear predictor

$$
\hat{x}_0 = \hat{a}\,x_t + \hat{b}
$$

from simulated data and compare it qualitatively with your derived $m_t(x_t)=A_t x_t + b_t$.

### Checkpoint 4.3

Write 2-3 lines on whether the empirical trend agrees with your theory and why any mismatch appears.

The empirical trend agrees with theory: the fitted linear predictor is almost identical to the derived posterior mean, and its error is near the Bayes floor in this fixed-$t$ Gaussian setup. In particular, $\mathrm{MSE}_{\text{theory}}=0.6721$ and $\mathrm{MSE}_{\text{fit}}=0.6721$, both close to the theoretical floor $v_t=0.6736$, while the naive constant baseline is much worse ($1.4373$). The small gaps (for example, $\hat{a}=0.6658$ vs $A_t=0.6653$) are expected from finite-sample Monte Carlo and minor numerical estimation noise, not from a mismatch in the model.

---

## 5) Reflection (Short)

### Checkpoint 5.1

Write one paragraph (5-8 lines):

- Which step was hardest?
- What changed in your intuition about conditioning in diffusion?
- One question you want to revisit in Week 5.

The hardest step was the decomposition in Checkpoint 3.1 for $\mathcal{L}(g)$, especially adding and subtracting $m(x_t)=\mathbb{E}[x_0\mid x_t]$ inside the square and showing why the cross term is zero. Once that clicked, my intuition changed from "denoising as inversion" to "denoising as conditional estimation." In particular, I now see clearly that the MSE-optimal denoiser is the posterior mean $\mathbb{E}[x_0\mid x_t]$, and the best possible error is limited by irreducible uncertainty $\mathbb{E}[\mathrm{Var}(x_0\mid x_t)]$. The close match between empirical and theoretical results in this notebook reinforced that interpretation in the Gaussian case. For Week 5, I want to revisit SNR and connect it more deeply to joint distributions/covariance so I can explain how information about $x_0$ degrades as noise increases.

---

## Completion Checklist

- [x] I derived Section 1 moments without skipping steps.
- [x] I derived $q(x_0 \mid x_t)$ and checked limiting behavior.
- [x] I proved (for myself) the optimal denoiser under MSE.
- [x] I added one short empirical check or clearly noted why I skipped it.
- [x] I wrote the reflection paragraph.

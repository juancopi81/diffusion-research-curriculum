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

### TODO 1.1 (independent derivation)

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

### TODO 1.2 (independent derivation)

For $\mathbb{E}[x_t]$ (using LOTUS):

$$
\begin{aligned}
\mathbb{E}[x_t]
&= \mathbb{E}\!\left[\mathbb{E}[x_t \mid x_0]\right] \\
&= \mathbb{E}[\alpha_t x_0] \quad \text{(from TODO 1.1)} \\
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

### TODO 1.3 (quick interpretation)

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

### TODO 2.1 (complete derivation)

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

### TODO 2.2 (complete the square, step-by-step)

Start from the quadratic form obtained in TODO 2.1:

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

### TODO 2.3 (sanity checks)

Answer briefly:

1. What should happen to $q(x_0 \mid x_t)$ as $\sigma_t \to 0$?
2. What should happen as $\sigma_t \to \infty$?

---

## 3) Denoising as Conditional Expectation

Let $g$ be any estimator of $x_0$ from $x_t$, with squared-error objective:

$$
\mathcal{L}(g)=\mathbb{E}\left[(x_0-g(x_t))^2\right].
$$

### TODO 3.1

Condition on $x_t$ and derive the decomposition that separates:

- an irreducible uncertainty term, and
- a mismatch term involving $g(x_t)$.

### TODO 3.2

From your decomposition, show which function $g^\star(x_t)$ minimizes $\mathcal{L}(g)$.

### TODO 3.3 (connection to diffusion training)

Write 4-6 lines connecting your result to the sentence:

`"Denoising is estimating a conditional expectation."`

Do not use vague wording; name the random variables explicitly.

---

## 4) Optional Code Check (No Closed-Form Answers Needed Here)

Use `/Users/juanpineros/juancopi81/diffusion-research-curriculum/notebooks/w04_normal_loc_scale_solved.ipynb` as a starting reference.

### TODO 4.1

Simulate pairs $(x_0, x_t)$ from the setup in Section 1.

### TODO 4.2

Estimate a linear predictor

$$
\hat{x}_0 = \hat{a}\,x_t + \hat{b}
$$

from simulated data and compare it qualitatively with your derived $m_t(x_t)=A_t x_t + b_t$.

### TODO 4.3

Write 2-3 lines on whether the empirical trend agrees with your theory and why any mismatch appears.

---

## 5) Reflection (Short)

### TODO 5.1

Write one paragraph (5-8 lines):

- Which step was hardest?
- What changed in your intuition about conditioning in diffusion?
- One question you want to revisit in Week 5.

---

## Completion Checklist

- [ ] I derived Section 1 moments without skipping steps.
- [ ] I derived $q(x_0 \mid x_t)$ and checked limiting behavior.
- [ ] I proved (for myself) the optimal denoiser under MSE.
- [ ] I added one short empirical check or clearly noted why I skipped it.
- [ ] I wrote the reflection paragraph.

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

### TODO 1.1

Compute:

- $\mathbb{E}[x_t \mid x_0]$
- $\mathrm{Var}(x_t \mid x_0)$

Write each in one line.

### TODO 1.2

Compute:

- $\mathbb{E}[x_t]$
- $\mathrm{Var}(x_t)$

Use LOTUS/linearity and independence explicitly in your steps.

### TODO 1.3 (quick interpretation)

In 2-4 lines: explain how $\sigma_t$ changes uncertainty in $x_t$ when $x_0$ is fixed.

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

### TODO 2.1

Write $\log q(x_0 \mid x_t)$ up to additive constants and expand the quadratic terms in $x_0$.

### TODO 2.2

Complete the square and identify:

- posterior variance: $v_t$  
- posterior mean: $m_t(x_t)$

Use the affine form

$$
m_t(x_t)=A_t x_t + b_t
$$

and solve for $A_t$, $b_t$, and $v_t$.

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

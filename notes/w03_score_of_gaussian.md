# Week 3 — Score of a Gaussian (Diffusion Contact)

> **Time**: 45-60 minutes
> **Goal**: Derive and understand the score function of a Gaussian distribution

---

## 1. What is the Score Function?

The **score function** is the gradient of the log-density with respect to the input:

$$s(x) = \nabla_x \log p(x)$$

### Intuition

The score tells us the **direction toward higher probability**:

- Where $s(x) > 0$: moving right increases probability
- Where $s(x) < 0$: moving left increases probability
- Where $s(x) = 0$: we're at a mode (local maximum)

**Why this matters**: Score-based generative models learn to estimate $s(x)$ from data, then use it to generate new samples by "following the score" from noise toward high-probability regions.

---

## 2. Derivation for N(μ, σ²)

Derive the score function for a univariate Gaussian $X \sim N(\mu, \sigma^2)$.

### Step 1: Write the PDF

$$p(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### Step 2: Take the log

$$\log p(x) = \log\left(\frac{1}{\sigma\sqrt{2\pi}}\right) + \log e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$$= \log\left(\frac{1}{\sigma\sqrt{2\pi}}\right) - \frac{(x-\mu)^2}{2\sigma^2}$$

### Step 3: Differentiate with respect to x

$$s(x) = \frac{\partial}{\partial x} \log p(x) = 0 - \frac{2(x-\mu)}{2\sigma^2}$$

$$= \frac{\mu - x}{\sigma^2}$$

---

### Result

$$\boxed{s(x) = \frac{\mu - x}{\sigma^2} = -\frac{x - \mu}{\sigma^2}}$$

---

## 3. Interpretation

### Sign Analysis

| Condition | Score Sign | Interpretation           |
| --------- | ---------- | ------------------------ |
| $x > \mu$ | $s(x) < 0$ | Move **left** toward μ   |
| $x < \mu$ | $s(x) > 0$ | Move **right** toward μ  |
| $x = \mu$ | $s(x) = 0$ | At the mode (stationary) |

### Key Insight

> **The score always points toward the mean μ.**

This makes intuitive sense: the Gaussian has its peak at μ, so the "uphill" direction always points toward μ.

---

## 4. Code Verification

Verify your derivation by comparing the analytic score to a finite-difference approximation.

👉 **Notebook**: [`notebooks/w03_score_verification.ipynb`](../notebooks/w03_score_verification.ipynb)

### What You'll Implement

1. `gaussian_pdf(x, mu, sigma)` — the Gaussian PDF
2. `analytic_score(x, mu, sigma)` — your derived formula: $(μ - x) / σ²$
3. `numerical_score(x, mu, sigma)` — finite-difference approximation

### Verification Target

Max absolute error between analytic and numerical score should be < 1e-8.

---

## 5. Visualization

👉 **Notebook**: [`notebooks/w03_score_verification.ipynb`](../notebooks/w03_score_verification.ipynb) (Section 3)

### What You Should See

Arrows pointing:

- **Left** for $x > \mu$ (score is negative)
- **Right** for $x < \mu$ (score is positive)
- **No arrow** (zero length) at $x = \mu$

---

## 6. Why This Matters for Diffusion

### Score-Based Generative Models

Score-based models (including diffusion models) work by:

1. **Training**: Learn to estimate $s(x) = \nabla_x \log p_{\text{data}}(x)$ from samples
2. **Generation**: Start from noise $x_T \sim N(0, I)$ and follow the score:
   $$x_{t-1} = x_t + \eta \cdot s(x_t) + \text{noise}$$

This is called **Langevin dynamics**.

### The Gaussian Case is Special

For a Gaussian, we derived the score analytically:
$$s(x) = -\frac{x - \mu}{\sigma^2}$$

In general, we don't know $p(x)$, so we can't compute the score analytically. Instead:

- A neural network learns to approximate $s_\theta(x) \approx \nabla_x \log p(x)$
- This is exactly what the **denoising score matching** objective does

### Preview: Denoising Score Matching

The key insight (due to Vincent, 2011) is that we can learn the score by **denoising**:

$$\mathcal{L} = \mathbb{E}_{x \sim p_{\text{data}}, \epsilon \sim N(0, I)} \left[ \| s_\theta(x + \sigma\epsilon) - (-\epsilon/\sigma) \|^2 \right]$$

This connects to our derivation: the score of a Gaussian centered at $x$ is $-\epsilon/\sigma$!

---

## Summary

| Concept              | Formula/Value                           |
| -------------------- | --------------------------------------- |
| Score definition     | $s(x) = \nabla_x \log p(x)$             |
| Gaussian score       | $s(x) = -(x-\mu)/\sigma^2$              |
| Interpretation       | Points toward the mean                  |
| Diffusion connection | Neural nets learn to estimate the score |

---

## Next Steps

- Week 4+: See how score matching loss trains a neural network
- Weeks 17+: Implement DDPM and see the score in action

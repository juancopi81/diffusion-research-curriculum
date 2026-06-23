# Week 7 - Conditional Expectation in Diffusion

> Status: Complete. Reviewed as the Week 7 S3 diffusion contact on 2026-06-23.
> Goal: connect conditional expectation, denoising, and score functions using the diffusion artifacts you already built.

This note should stay short and conceptual. The purpose is not to rederive a full DDPM objective. The purpose is to connect the Week 7 Stat110 language to the diffusion idea:

$$
\text{noisy observation } x_t
\quad \Longrightarrow \quad
\text{best clean estimate } \mathbb{E}[x_0 \mid x_t].
$$

---

## 0. Source Map

Use these earlier artifacts as anchors:

- Week 2 forward moments: [`notebooks/w02_forward_moments_solved.ipynb`](../notebooks/w02_forward_moments_solved.ipynb)
  - Forward question: if $x_0$ is known, what are $\mathbb{E}[x_t \mid x_0]$ and $\mathrm{Var}(x_t \mid x_0)$?
- Week 2 expectation toolkit: [`notes/w02_expectation_toolkit.md`](w02_expectation_toolkit.md)
  - Tools: linearity, independence, and variance scaling.
- Week 4 conditioning in diffusion: [`notes/w04_conditioning_in_diffusion.md`](w04_conditioning_in_diffusion.md)
  - Posterior question: if $x_t$ is observed, what does $q(x_0 \mid x_t)$ look like?
  - Denoising question: why is the MSE-optimal denoiser $\mathbb{E}[x_0 \mid x_t]$?
- Week 7 lecture notes:
  - [`notes/w07_stat110_conditional_expectation.md`](w07_stat110_conditional_expectation.md)
  - [`notes/w07_stat110_conditional_expectation_given_rv.md`](w07_stat110_conditional_expectation_given_rv.md)
- Week 7 practice: [`proofs/w07_stat110_conditional_expectation.md`](../proofs/w07_stat110_conditional_expectation.md)
  - Main bridge: conditional expectation is a random variable, and taking expectation again is a separate step.

Source status: internal synthesis from existing repo notes and solved artifacts. No external paper/source is being quoted here.

---

## 1. The Direction Flip

In Week 2, the forward process was

$$
x_t = x_0 + \sigma(t)\epsilon,
\qquad
\epsilon \sim \mathcal{N}(0,I).
$$

There, the main question was:

$$
\mathbb{E}[x_t \mid x_0].
$$

That means: if the clean data point $x_0$ is known, where is the noisy point $x_t$ centered?

Week 7 asks the reverse kind of question:

$$
\mathbb{E}[x_0 \mid x_t].
$$

That means: if the noisy point $x_t$ is observed, what is the best average estimate of the clean point $x_0$?

### Checkpoint 1.1

Fill in this comparison table.

| Expression                 | What is observed?     | What is being predicted?      | Diffusion meaning                                 |
| -------------------------- | --------------------- | ----------------------------- | ------------------------------------------------- |
| $\mathbb{E}[x_t \mid x_0]$ | the clean point $x_0$ | the average noisy point $x_t$ | forward noising: where noisy samples are centered |
| $\mathbb{E}[x_0 \mid x_t]$ | the noisy point $x_t$ | the average clean point $x_0$ | denoising: best clean estimate from noisy data    |

Your notes:

- The first expression goes forward: given the clean data, average over the noise. The second expression goes backwards: given
  the noisy observation, estimate the clean data. The backward direction is harder because many possible $x_0$ values could have
  produced the same $x_t$.

### Checkpoint 1.2

Explain in your own words why the second question is harder.

Prompt:

- If $x_0$ is known, sampling $x_t$ is just adding noise.
- If $x_t$ is known, why might there be many possible clean $x_0$ values that could have produced it?

Your notes:

- There are many possible clean $x_0$ values that could plausibly explain the observed $x_t$ because the forward process adds random Gaussian noise. If we observe a noisy image, we do not know which clean image created it. For example, Image A plus one noise realization and Image B plus another noise realization could both be compatible with the same noisy-looking image:
  - Image A + Noise A = Image C
  - Image B + Noise B = Image C

  So $x_t$ gives information about $x_0$, but it does not identify $x_0$ exactly. The conditional expectation $\mathbb{E}[x_0 \mid x_t]$ summarizes the plausible clean images by taking their conditional average.

---

## 2. Setup: One-Step Forward Noising

Use the slightly more general scalar or vector setup from Week 4:

$$
x_t = \alpha_t x_0 + \sigma_t \epsilon,
\qquad
\epsilon \sim \mathcal{N}(0,I),
\qquad
\epsilon \perp x_0.
$$

Here:

- $x_0$ is the clean data variable.
- $x_t$ is the noisy observation at time $t$.
- $\alpha_t$ controls how much clean signal remains.
- $\sigma_t$ controls how much Gaussian noise is added.

### Checkpoint 2.1

Reuse the Week 2/Week 4 argument to compute the forward conditional mean:

$$
\mathbb{E}[x_t \mid x_0]
=
\mathbb{E}[\alpha_t x_0 + \sigma_t\epsilon \mid x_0].
$$

Fill in the steps:

$$
\begin{aligned}
\mathbb{E}[x_t \mid x_0]
&= \mathbb{E}[\alpha_t x_0 + \sigma_t\epsilon \mid x_0] \\
&= \mathbb{E}[\alpha_t x_0 \mid x_0]
 + \mathbb{E}[\sigma_t\epsilon \mid x_0]
 \quad \text{(linearity)} \\
&= \alpha_t x_0
 + \sigma_t\mathbb{E}[\epsilon \mid x_0]
 \quad \text{(given } x_0, \alpha_t x_0 \text{ and } \sigma_t \text{ are fixed)} \\
&= \alpha_t x_0
 + \sigma_t\mathbb{E}[\epsilon]
 \quad \text{(since } \epsilon \perp x_0 \text{)} \\
&= \alpha_t x_0
 \quad \text{(since } \mathbb{E}[\epsilon]=0 \text{)}.
\end{aligned}
$$

Final result:

$$
\mathbb{E}[x_t \mid x_0] = \alpha_t x_0.
$$

Your interpretation:

- Once $x_0$ is known, the only remaining randomness in $x_t$ comes from the Gaussian noise $\epsilon$. Since that noise has mean $0$, the conditional mean of $x_t$ is just the clean signal scaled by $\alpha_t$.

### Checkpoint 2.2

What changes when we condition the other way?

Compare:

$$
\mathbb{E}[x_t \mid x_0]
\qquad \text{versus} \qquad
\mathbb{E}[x_0 \mid x_t].
$$

Prompts:

- In the first expression, what becomes fixed?
- In the second expression, what becomes fixed?
- Why is $\mathbb{E}[x_0 \mid x_t]$ a function of $x_t$, not one fixed number?

Your notes:

- In the first expression, the clean point $x_0$ becomes fixed.
- In the second expression, the noisy point $x_t$ becomes fixed.
- $\mathbb{E}[x_0 \mid x_t]$ is a function of $x_t$ because the estimate changes depending on which noisy observation we see. It is not one fixed number. If $x_t$ is known, there might still be many possible clean $x_0$ values that could have plausibly produced it.

---

## 3. Tower Property: Averaging After Conditioning

Week 7 emphasized Adam's law:

$$
\mathbb{E}[\mathbb{E}(Y \mid X)] = \mathbb{E}(Y).
$$

For diffusion, one useful version is

$$
\mathbb{E}[\mathbb{E}(x_0 \mid x_t)] = \mathbb{E}(x_0).
$$

The inner object

$$
\mathbb{E}(x_0 \mid x_t)
$$

is the best clean estimate after observing $x_t$. It is a function of the noisy observation. Taking expectation again averages over all possible noisy observations.

### Checkpoint 3.1

Explain the tower property in this setting.

Prompts:

- What does $\mathbb{E}(x_0 \mid x_t)$ know that $\mathbb{E}(x_0)$ does not?
- Why does averaging $\mathbb{E}(x_0 \mid x_t)$ over all possible $x_t$ bring us back to $\mathbb{E}(x_0)$?
- How is this similar to the roommate problem distinction between $\mathbb{E}(X \mid N)$ and $\mathbb{E}[\mathbb{E}(X \mid N)]$?

Your notes:

- $\mathbb{E}(x_0 \mid x_t)$ has information about the noisy observation $x_t$, while $\mathbb{E}(x_0)$ does not use that observation.
- This is the intuition behind the tower property: $\mathbb{E}(x_0 \mid x_t)$ uses the observed value of $x_t$ to make an updated estimate of $x_0$. But if we then average those updated estimates over all possible values of $x_t$, we recover the original average $\mathbb{E}(x_0)$.
- This is the same situation as the roommate problem. Conditioning on $N$ gives a random variable $\mathbb{E}(X \mid N)$ whose value changes depending on the observed $N$. If we then average over all possible values of $N$, we recover $\mathbb{E}(X)$.

### Checkpoint 3.2

One-sentence summary:

> Conditional expectation lets us update our estimate after seeing noisy information, but Adam's law says that if we average those updated estimates over all possible observations, we recover the original average.

Rewrite that sentence in your own words:

- If we observe a specific noisy value $x_t$, we can update our estimate of the clean data point $x_0$ using $\mathbb{E}[x_0 \mid x_t]$. But if we average these updated estimates over all possible noisy observations $x_t$, we recover the original average $\mathbb{E}[x_0]$. This is Adam's law. For example, if we know a person's height, we can update our expected value of their weight. But if we average over all possible heights, we recover the general expected weight.

---

## 4. Denoising as Conditional Expectation

Suppose a model receives $x_t$ and outputs a guess $g(x_t)$ for the clean value $x_0$.

Use squared error:

$$
\mathcal{L}(g)
=
\mathbb{E}\left[\|x_0 - g(x_t)\|^2\right].
$$

The key fact from conditional expectation is:

$$
g^\star(x_t)
=
\mathbb{E}[x_0 \mid x_t].
$$

In words: under squared error, the best possible denoiser predicts the conditional mean of the clean data given the noisy observation.

### Checkpoint 4.1

Explain why this is not "undoing the noise exactly."

Prompts:

- If many clean $x_0$ values could have produced the same noisy $x_t$, can a denoiser know the true one exactly?
- What does the conditional mean do instead?
- How does this connect to Week 4's phrase "denoising as conditional estimation"?

Your notes:

- No, it cannot know the true clean value exactly. As we saw earlier, a specific noisy observation $x_t$ could be compatible with many possible clean values $x_0$, each paired with a different noise realization. So the denoiser cannot generally identify the exact $x_0$ that produced the observed $x_t$.
- The posterior conditional mean does not choose one guaranteed true clean value. Instead, it gives the MSE-optimal average estimate of $x_0$ under the posterior distribution $q(x_0 \mid x_t)$. In other words, it averages over the plausible clean values, weighted by how plausible they are after observing the fixed noisy value $x_t$.
- In Week 4 we saw that:

$$
\mathcal{L}(g)
=\mathbb{E}\!\left[\mathrm{Var}(x_0\mid x_t)\right]
+\mathbb{E}\!\left[(m(x_t)-g(x_t))^2\right].
$$

The first term is irreducible uncertainty: even the best estimator cannot remove the remaining posterior variance $\mathrm{Var}(x_0\mid x_t)$. The second term is estimator mismatch. Under this loss, the mismatch term is minimized when

$$
g(x_t)=m(x_t):=\mathbb{E}(x_0 \mid x_t).
$$

So denoising under squared error is not learning to undo the exact noise realization. It is learning the posterior average of the clean variable given the noisy observation.

### Checkpoint 4.2

Fill in the conceptual chain:

$$
x_t \text{ observed}
\quad \Longrightarrow \quad
q(x_0 \mid x_t)
\quad \Longrightarrow \quad
\mathbb{E}[x_0 \mid x_t]
\quad \Longrightarrow \quad
\text{MSE-optimal denoiser}.
$$

Explain each arrow in one sentence.

Your notes:

- First arrow: Based on the observed $x_t$, we form the posterior distribution $q(x_0 \mid x_t)$ over plausible clean values and their relative densities.
- Second arrow: We take the conditional average under that posterior distribution: the possible clean values are weighted by how plausible they are after observing $x_t$.
- Third arrow: This conditional average is the optimal denoiser for mean squared error loss; the optimal denoiser is $g^\star(x_t)=\mathbb{E}[x_0 \mid x_t]$.

---

## 5. Score Connection

The score of the noisy distribution is

$$
\nabla_{x_t}\log p_t(x_t).
$$

From Week 3 and Week 5, the score points in the direction of increasing log-density. In diffusion, we care about the score of the noisy distribution at each noise level $t$.

For the Gaussian corruption model

$$
p(x_t \mid x_0)
=
\mathcal{N}(\alpha_t x_0, \sigma_t^2 I),
$$

the key identity is

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{\alpha_t\mathbb{E}[x_0 \mid x_t] - x_t}{\sigma_t^2}.
$$

Equivalently, in the simpler additive-noise case where $\alpha_t=1$,

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{\mathbb{E}[x_0 \mid x_t] - x_t}{\sigma_t^2}.
$$

So the score points from the noisy point $x_t$ toward the $\alpha_t$-scaled conditional clean estimate, scaled by the noise variance. In the additive-noise case where $\alpha_t=1$, this is exactly the direction from $x_t$ toward $\mathbb{E}[x_0 \mid x_t]$.

### Checkpoint 5.1

Before looking at the derivation, explain the identity in words.

Prompts:

- What role does $\mathbb{E}[x_0 \mid x_t]$ play?
- Why does the vector $\mathbb{E}[x_0 \mid x_t] - x_t$ look like a denoising direction?
- Why should the scale depend on $\sigma_t^2$?

Your notes:

- $\mathbb{E}[x_0 \mid x_t]$ is the conditional mean of the clean data given the noisy observation. It plays the role of the best average clean estimate after seeing $x_t$.
- The vector $\mathbb{E}[x_0 \mid x_t]-x_t$ points from the noisy observation toward the conditional clean estimate. In 1D, for example, if $x_t$ is greater than the conditional mean, then $\mathbb{E}[x_0 \mid x_t]-x_t$ is negative, so the direction points left, back toward the mean.
- The scale depends on $\sigma_t^2$ because the noise variance controls how strong that denoising direction should be. If the variance is large, the same displacement is weaker evidence, so the score magnitude is smaller. If the variance is small, the same displacement is stronger evidence, so the score magnitude is larger.

### Checkpoint 5.2

Guided derivation of the identity. The main question is:

$$
\text{Why is the score of } p_t(x_t)
\text{ related to an average over } x_0?
$$

Start from the marginal noisy density. This density averages over all possible
clean values $x_0$ that could have produced the observed noisy value $x_t$:

$$
p_t(x_t)
=
\int p(x_t \mid x_0)p_{\text{data}}(x_0)\,dx_0.
$$

Differentiate the log-density using the vector version of $d\log f/dx=f'/f$:

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{1}{p_t(x_t)}\nabla_{x_t}p_t(x_t).
$$

Now substitute the definition of $p_t(x_t)$:

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{1}{p_t(x_t)}
\nabla_{x_t}
\int p(x_t \mid x_0)p_{\text{data}}(x_0)\,dx_0.
$$

Under the usual regularity assumptions, move the derivative inside the
integral. The data density $p_{\text{data}}(x_0)$ does not depend on $x_t$, so
it behaves like a constant:

$$
\begin{aligned}
\nabla_{x_t}\log p_t(x_t)
&=
\frac{1}{p_t(x_t)}
\int
\nabla_{x_t}
\left[
p(x_t \mid x_0)p_{\text{data}}(x_0)
\right]\,dx_0 \\
&=
\frac{1}{p_t(x_t)}
\int
\nabla_{x_t}p(x_t \mid x_0)
p_{\text{data}}(x_0)\,dx_0.
\end{aligned}
$$

Use the log-derivative identity $\nabla p=p\nabla\log p$ on the conditional
density:

$$
\nabla_{x_t}p(x_t \mid x_0)
=
p(x_t \mid x_0)\nabla_{x_t}\log p(x_t \mid x_0).
$$

Substitute that into the integral:

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{1}{p_t(x_t)}
\int
p(x_t \mid x_0)
\nabla_{x_t}\log p(x_t \mid x_0)
p_{\text{data}}(x_0)\,dx_0.
$$

Move the normalizing factor inside:

$$
\nabla_{x_t}\log p_t(x_t)
=
\int
\nabla_{x_t}\log p(x_t \mid x_0)
\frac{
p(x_t \mid x_0)p_{\text{data}}(x_0)
}{
p_t(x_t)
}\,dx_0.
$$

The fraction is Bayes' rule:

$$
p(x_0 \mid x_t)
=
\frac{
p(x_t \mid x_0)p_{\text{data}}(x_0)
}{
p_t(x_t)
}.
$$

So the marginal score becomes:

$$
\nabla_{x_t}\log p_t(x_t)
=
\int
\nabla_{x_t}\log p(x_t \mid x_0)
p(x_0 \mid x_t)\,dx_0.
$$

By the definition of conditional expectation:

$$
\nabla_{x_t}\log p_t(x_t)
=
\mathbb{E}\left[
\nabla_{x_t}\log p(x_t \mid x_0)
\mid x_t
\right].
$$

In words: the score of the marginal noisy density is the posterior average of
the conditional scores. The possible clean values $x_0$ are weighted by how
plausible they are after observing $x_t$.

Now use the Gaussian corruption model:

$$
p(x_t \mid x_0)
=
\mathcal{N}(\alpha_t x_0,\sigma_t^2 I).
$$

Its conditional score is:

$$
\nabla_{x_t}\log p(x_t \mid x_0)
=
-\frac{x_t-\alpha_t x_0}{\sigma_t^2}.
$$

Substitute the Gaussian score into the posterior-average identity:

$$
\begin{aligned}
\nabla_{x_t}\log p_t(x_t)
&=
\mathbb{E}\left[
-\frac{x_t-\alpha_t x_0}{\sigma_t^2}
\mid x_t
\right] \\
&=
-\frac{1}{\sigma_t^2}
\mathbb{E}\left[x_t-\alpha_t x_0 \mid x_t\right]
\quad \text{(pull out fixed } \sigma_t^2 \text{)} \\
&=
-\frac{1}{\sigma_t^2}
\left(
\mathbb{E}[x_t \mid x_t]
- \alpha_t\mathbb{E}[x_0 \mid x_t]
\right)
\quad \text{(linearity, and } \alpha_t \text{ is fixed)} \\
&=
-\frac{1}{\sigma_t^2}
\left(
x_t
- \alpha_t\mathbb{E}[x_0 \mid x_t]
\right)
\quad \text{(given } x_t\text{, }x_t\text{ is fixed)} \\
&=
\frac{\alpha_t\mathbb{E}[x_0 \mid x_t]-x_t}{\sigma_t^2}.
\end{aligned}
$$

Final result:

$$
\nabla_{x_t}\log p_t(x_t)
=
\frac{\alpha_t\mathbb{E}[x_0 \mid x_t]-x_t}{\sigma_t^2}.
$$

Your notes on the key step:

- The key step is not just algebra. First we prove that the marginal score
  $\nabla_{x_t}\log p_t(x_t)$ is the posterior average of the conditional
  scores $\nabla_{x_t}\log p(x_t \mid x_0)$. Only after that are we allowed to
  substitute the Gaussian conditional score and simplify with linearity.
- In the final simplification, $x_t$ is fixed because we are conditioning on
  $x_t$. The only remaining uncertain term is $x_0$, which becomes
  $\mathbb{E}[x_0 \mid x_t]$.

### Checkpoint 5.3

Connect this back to denoising score matching.

Prompts:

- If a model can estimate the score $\nabla_{x_t}\log p_t(x_t)$, what direction does it know?
- If a model can estimate $\mathbb{E}[x_0 \mid x_t]$, how can that be converted into a score estimate in the Gaussian corruption case?
- Why does this make conditional expectation relevant to score-based diffusion models?

Your notes:

- If a model estimates the score, it knows the direction of increasing log-density for the noisy marginal distribution $p_t(x_t)$. In other words, it knows which local direction moves $x_t$ toward more plausible noisy samples at time $t$.

- If a model estimates $\mathbb{E}[x_0 \mid x_t]$, then in the Gaussian corruption case we can plug that estimate into the identity

  $$
  \nabla_{x_t}\log p_t(x_t)
  =
  \frac{\alpha_t\mathbb{E}[x_0\mid x_t]-x_t}{\sigma_t^2}.
  $$

  This converts a denoiser estimate into a score estimate.

- This makes conditional expectation relevant because the posterior mean $\mathbb{E}[x_0\mid x_t]$ gives the clean-signal estimate needed to determine the score direction. When we cannot compute this conditional expectation analytically, we learn an approximation with a neural network.

---

## 6. Final Synthesis

Write a short paragraph answering:

> How does conditional expectation explain denoising in diffusion?

Your paragraph:

Conditional expectation explains denoising in diffusion because the posterior mean
$\mathbb{E}[x_0 \mid x_t]$ is the MSE-optimal estimate of the clean data after observing a noisy sample $x_t$. Given a noisy sample, this conditional expectation averages over the plausible clean values that could have produced it, weighted by their posterior plausibility. In the Gaussian corruption case, this denoiser estimate can be converted into a score estimate, which tells us the local direction that moves the noisy sample toward a more plausible region of the noisy marginal distribution.

---

## Memory Card

Completed memory card:

- Week 2 forward direction:

  $$
  \mathbb{E}[x_t \mid x_0] = \alpha_t x_0
  $$

- Week 7 reverse/denoising direction:

  $$
  \mathbb{E}[x_0 \mid x_t]
  =
  \text{posterior mean of the clean data given the noisy observation}
  $$

  In real diffusion models, this is usually approximated with a neural network rather than computed analytically.

- Tower property:

  $$
  \mathbb{E}[\mathbb{E}(x_0 \mid x_t)] = \mathbb{E}[x_0]
  $$

- MSE-optimal denoiser:

  $$
  g^\star(x_t) = \mathbb{E}[x_0 \mid x_t]
  $$

- Score connection:

  $$
  \nabla_{x_t}\log p_t(x_t)
  =
  \frac{\alpha_t\mathbb{E}[x_0 \mid x_t]-x_t}{\sigma_t^2}
  $$

## Completion Checklist

- [x] I explained the difference between $\mathbb{E}[x_t \mid x_0]$ and $\mathbb{E}[x_0 \mid x_t]$.
- [x] I connected Adam's law to $\mathbb{E}[\mathbb{E}(x_0 \mid x_t)] = \mathbb{E}(x_0)$.
- [x] I explained why denoising under squared error targets $\mathbb{E}[x_0 \mid x_t]$.
- [x] I derived or explained the score identity for Gaussian corruption.
- [x] I wrote a short final synthesis paragraph in my own words.

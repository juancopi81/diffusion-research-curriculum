# Week 6 - Where KL Appears in Diffusion

> Status: Complete. Finished after working through
> `notebooks/w06_kl_gaussians_solved.ipynb`.

## Goal

Connect the Week 6 KL notebook to the recurring generative modeling idea:

$$
\text{simple distribution} \longrightarrow \text{data distribution}.
$$

This note should stay short: about one page when finished.

---

## 1. KL as Distribution Mismatch

Start from the definition:

$$
D_{KL}(p\|q)
=
\mathbb{E}_{X\sim p}
\left[
\log p(X)-\log q(X)
\right].
$$

Prompts addressed:

- Explain in your own words what this expectation is averaging.
- Explain what it means if $D_{KL}(p\|q)=0$.
- Explain why this is a distribution-level comparison, not a pointwise comparison.

Your notes:

- The expectation averages the log-density ratio $\log(p(X)/q(X))$ over samples $X \sim p$. In words: we sample values from $p$, then compare how well $p$ explains those values versus how well $q$ explains them. Equivalently, it averages the extra surprise of using $q$ instead of $p$ to describe samples that actually came from $p$. In the continuous case this average is an integral weighted by $p(x)$; in the discrete case it is a sum over values weighted by $p(x)$.

- $D_{KL}(p\|q)=0$ means there is no distribution mismatch: $p$ and $q$ assign the same density/probability mass to values, up to sets that have zero probability under $p$. Intuitively, $p(x)/q(x)=1$, so $\log(p(x)/q(x))=0$, and the average log-ratio is zero.

- KL is a distribution-level comparison because it averages local log-ratio comparisons across the whole support of $p$. A single point can have a positive or negative log-ratio, but KL summarizes the expected mismatch over samples from the distribution, not the mismatch at one isolated value.

---

## 2. Direction Matters

Use your Gaussian notebook experiments.

Prompts addressed:

- Compare $D_{KL}(p\|q)$ and $D_{KL}(q\|p)$ for one pair of Gaussians.
- Write one sentence explaining why the direction changes the result.
- Connect this to the fact that the expectation is taken under the first distribution.

Your notes:

- As noticed in `notebooks/w06_kl_gaussians_solved.ipynb`, for the configured Gaussians, $D_{KL}(p\|q)=0.3467$ but $D_{KL}(q\|p)=0.6435$. The direction changes the result because KL always averages under the first distribution and compares against the second. In $D_{KL}(p\|q)$, we average $\log p(X)-\log q(X)$ over samples from $p$; in $D_{KL}(q\|p)$, we average $\log q(X)-\log p(X)$ over samples from $q$. These averages weight different regions of the line, so the two KL values are usually different.

---

## 3. Where KL Shows Up

Prompts addressed:

- Write a short paragraph on KL in variational objectives.
- Write a short paragraph on why "matching distributions" appears in diffusion and flow formulations.
- Keep this high-level. Do not attempt a full DDPM ELBO derivation yet.

Your notes:

- In variational objectives, KL is used to turn a hard distribution-matching problem into something we can optimize. The high-level idea is: if we cannot work directly with the true or desired distribution, we introduce a tractable approximation and use a KL term to measure how far that approximation is from the target. Later, this will show up in ELBO-style objectives, but for now the important point is that KL gives a mathematical penalty for distribution mismatch.

- In diffusion and flow formulations, the same broad theme appears: we want a learned process whose generated distribution matches the data distribution. We usually start from a simple distribution, such as Gaussian noise, and learn a transformation or reverse process that moves samples toward the data distribution. In high dimensions we usually cannot compare the full generated distribution and data distribution directly, so the training objective uses more tractable local or variational pieces that push the learned process in the right direction.

---

## 4. Connection to Week 6 Transformations

Week 6 change-of-variables work studied the tractable case:

$$
X\sim p,
\qquad
Y=g(X).
$$

Prompts addressed:

- Explain what is known in the tractable change-of-variables case.
- Explain what becomes unknown or intractable for real data distributions.
- Explain why a learned transformation path is a natural next idea.

Your notes:

- In the tractable change-of-variables case, we know the original distribution $p_X$ and we know the transformation $Y=g(X)$. If $g$ is well-behaved enough, for example one-to-one and differentiable in the 1D case, then we can use the inverse map $g^{-1}$ and the derivative/Jacobian factor to derive the density of $Y$ analytically.

- For real data distributions, the situation is different. We may have samples, such as images of cats, but we usually do not know the analytic density $p_{\text{data}}(x)$. We also do not know a closed-form transformation $g$ that maps simple noise into realistic data, and even if such a transformation exists, its inverse or Jacobian may be hard to compute.

- Because the analytic transformation is unknown or intractable, a learned transformation path becomes a natural idea. Instead of deriving $g$ by hand, we fit a model that gradually moves samples from a simple distribution, such as Gaussian noise, toward the data distribution. This is where distribution-matching objectives, including KL-based or KL-related ideas, become useful as a way to guide the learned process.

---

## 5. Personal Reflection

Prompt:

Write one paragraph answering:

> Why does matching distributions keep appearing in diffusion and flow matching?

Your paragraph:

Matching distributions keeps appearing because diffusion and flow matching models are trying to turn an easy distribution, such as Gaussian noise, into a complex real-data distribution, such as images of cats. The goal is not only to produce one good sample, but to make the whole generated distribution resemble the data distribution. Since the real data distribution is high-dimensional and not available in closed form, these models use tractable training objectives that push the learned process toward matching it.

---

## Memory Card

Final summary.

- KL measures: Distribution mismatch through the expected log-density ratio. In $D_{KL}(p\|q)$, we sample from $p$ and average how much better $p$ explains those samples compared with $q$.

- Direction matters because: KL averages under the first distribution. $D_{KL}(p\|q)$ weights regions where $p$ has mass, while $D_{KL}(q\|p)$ weights regions where $q$ has mass, so the two values are usually different.

- In diffusion, KL appears because: Diffusion models are ultimately trying to match a learned/generated distribution to the data distribution. Since the full data distribution is usually not available in closed form, KL appears in variational or tractable subproblems as a way to penalize distribution mismatch.

- Connection to transformations: In simple change-of-variables problems, the transformation is known and analytically tractable. In generative modeling, the transformation from simple noise to data is unknown, so we learn a transformation path or reverse process using objectives that push the learned distribution toward the data distribution.

## Main takeaways to remember

- KL measures expected log-density mismatch under the first distribution.
- Direction matters because $D_{KL}(p|q)$ weights regions where $p$ has mass, while $D_{KL}(q|p)$ weights regions where $q$ has mass.
- Diffusion/flow models are distribution-matching systems: they learn to move simple noise toward complex data.
- Week 6 transformations are the known analytic map case; generative modeling is the learned transformation path case.

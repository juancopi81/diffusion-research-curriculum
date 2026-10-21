# Week 14 — Generative Toolkit Mixed Problem Set

**Status:** In progress. Problem 1 reviewed on 2026-10-20; Problems 2–4
remain unattempted.

**Source basis:** Problem 1 consolidates the handwritten calculations and
explanation reviewed during Day 2. The Gaussian conditioning formulas were
looked up in the [Week 10 derivation](w10_multivariate_gaussian_score.md)
before applying them. This records a correct application with notes, not
unaided recall of those formulas. The prompts are in the
[Week 14 study plan](../notes/w14_study_plan.md#four-bounded-practice-problems).

| Problem | Status | Review evidence |
| --- | --- | --- |
| 1 — Gaussian score and conditioning | Reviewed 2026-10-20 | Score derivation and numerical evaluation correct; conditioning applied correctly with notes; marginal comparison explained correctly |
| 2 — ELBO, KL, and the implemented loss | Pending | Scheduled for Day 3 |
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

Pending Day 3 attempt and review. Use the prompt in the study plan.

## Problem 3 — Change of Variables and an Unchanged Coordinate

Pending Day 4 attempt and review. Use the prompt in the study plan.

## Problem 4 — Stability and What Clipping Actually Established

Pending Day 5 attempt and review. Use the prompt in the study plan.

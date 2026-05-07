# Week 5 - 2D Gaussian Score Field (Diffusion Contact)

> **Time**: 45-60 minutes  
> **Mode**: guided worksheet plus notebook visual check  
> **Companion notebook**: [`notebooks/w05_2d_gaussian_score_field.ipynb`](../notebooks/w05_2d_gaussian_score_field.ipynb)  
> **Goal**: extend the 1D Gaussian score to a 2D Gaussian and interpret the score as a vector field.

---

## Why This Fits Here

Week 3 introduced the 1D Gaussian score:

$$
s(x)=\nabla_x \log p(x)= -\frac{x-\mu}{\sigma^2}.
$$

Week 5 added joint Gaussians and covariance matrices. The diffusion contact for this week combines them:

$$
x \in \mathbb{R}^2,
\qquad
x \sim \mathcal{N}(\mu,\Sigma),
\qquad
s(x)=\nabla_x \log p(x).
$$

The target identity is

$$
\boxed{
\nabla_x \log \mathcal{N}(x;\mu,\Sigma)
=-\Sigma^{-1}(x-\mu).
}
$$

Do not treat this as a formula to memorize. The goal is to understand why the score is a vector and why the inverse covariance matrix controls its direction.

---

## 1. Start From the Multivariate Gaussian Log Density

For $x,\mu\in\mathbb{R}^2$ and positive definite $\Sigma\in\mathbb{R}^{2\times 2}$,

$$
p(x)=
\frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}
\exp\left(
-\frac12 (x-\mu)^T\Sigma^{-1}(x-\mu)
\right),
\qquad d=2.
$$

Taking logs gives

$$
\log p(x)
=
-\frac{d}{2}\log(2\pi)
-\frac12\log|\Sigma|
-\frac12 (x-\mu)^T\Sigma^{-1}(x-\mu).
$$

### Checkpoint 1.1 - Identify the only term that depends on $x$

In your own words, explain why the first two terms vanish when taking $\nabla_x$.

Write your answer here:

> The first two terms do not depend on $x$, so their gradient with respect to $x$ is zero. Moving $x$ a little changes only the quadratic term, not the normalizing constants.

---

## 2. Derive the Score

Let

$$
A=\Sigma^{-1},
\qquad
z=x-\mu.
$$

Then the $x$-dependent part of the log density is

$$
-\frac12 z^T A z.
$$

Because $\Sigma$ is symmetric positive definite, $A=\Sigma^{-1}$ is also symmetric.

### Checkpoint 2.1 - Differentiate the quadratic form

Use the fact that for symmetric $A$,

$$
\nabla_z(z^T A z)=2Az.
$$

Complete the derivation:

$$
\begin{aligned}
\nabla_x \log p(x)
&= \nabla_x \left[-\frac12 (x-\mu)^T\Sigma^{-1}(x-\mu)\right] \\
&= -\frac12 \nabla_x \left[z^T A z\right] \\
&= -\frac12 (2Az) \\
&= -Az \\
&= -\Sigma^{-1}(x-\mu).
\end{aligned}
$$

Final result:

$$
\boxed{
s(x)=-\Sigma^{-1}(x-\mu)
}
$$

---

## 3. Interpret the Formula

In 1D, the score points toward the mean and is scaled by $1/\sigma^2$.

In 2D, the same idea remains, but the scaling can depend on direction. The matrix

$$
\Lambda=\Sigma^{-1}
$$

is called the **precision matrix**.

### Checkpoint 3.1 - Special cases

Fill in the score formula for each covariance.

#### Isotropic covariance

If

$$
\Sigma=\sigma^2 I,
$$

then

$$
s(x)=-(\sigma^2 I)^{-1}(x-\mu)
=-\frac{1}{\sigma^2}(x-\mu).
$$

Question: how is this the same as the 1D score applied coordinate-by-coordinate?

> Each coordinate has the same variance $\sigma^2$, so each coordinate gets the same 1D score rule:
> $s_i(x)=-(x_i-\mu_i)/\sigma^2$.
> The score still points straight back toward the mean because both axes are scaled equally.

#### Diagonal covariance

If

$$
\Sigma=
\begin{bmatrix}
\sigma_1^2 & 0 \\
0 & \sigma_2^2
\end{bmatrix},
$$

then

$$
s(x)=-
\begin{bmatrix}
1/\sigma_1^2 & 0 \\
0 & 1/\sigma_2^2
\end{bmatrix}
\begin{bmatrix}
x_1-\mu_1 \\
x_2-\mu_2
\end{bmatrix}
=
\begin{bmatrix}
-(x_1-\mu_1)/\sigma_1^2 \\
-(x_2-\mu_2)/\sigma_2^2
\end{bmatrix}.
$$

Question: which coordinate gets a stronger pull when its variance is smaller?

> The coordinate with smaller variance gets the stronger pull, because its precision $1/\sigma_i^2$ is larger. For example, if $\sigma_1^2<\sigma_2^2$, then the $x_1$ direction is pulled back more strongly for the same displacement from the mean.

#### Correlated covariance

If

$$
\Sigma=
\begin{bmatrix}
\sigma_x^2 & \rho\sigma_x\sigma_y \\
\rho\sigma_x\sigma_y & \sigma_y^2
\end{bmatrix},
$$

then the score is still

$$
s(x)=-\Sigma^{-1}(x-\mu),
$$

but the arrows are not generally aimed straight at $\mu$ in Euclidean geometry.

Question: why can correlation rotate or shear the score field?

> With correlation, $\Sigma^{-1}$ has off-diagonal terms, so each score component depends on both $x_1-\mu_1$ and $x_2-\mu_2$. Applying the precision matrix is a linear transformation of the displacement vector: it can stretch, rotate, or shear the vector before the minus sign points it uphill toward higher log-density. Geometrically, the score arrows are normal to the elliptical density contours, not necessarily aimed straight at $\mu$ in the usual Euclidean sense.

---

## 4. Visual Check

Use the companion notebook to implement:

1. `score_2d(points, mean, cov)`
2. a finite-difference check of $\nabla_x\log p(x)$ at a few points
3. contour plus vector-field plots
4. a comparison between isotropic and correlated covariance

Notebook:

[`notebooks/w05_2d_gaussian_score_field.ipynb`](../notebooks/w05_2d_gaussian_score_field.ipynb)

Keep the main interpretation simple:

- density contours show level sets of $p(x)$
- score arrows point uphill in log-density
- at the mean, the score is zero
- covariance controls the shape of contours
- precision controls the local pull of the score

---

## 5. Diffusion Connection

Diffusion models repeatedly use scores of noisy distributions:

$$
s_t(x)=\nabla_x \log p_t(x).
$$

For a Gaussian, we can compute this exactly. For real data distributions, we usually cannot. So a neural network is trained to approximate the score:

$$
s_\theta(x,t)\approx \nabla_x \log p_t(x).
$$

### Checkpoint 5.1 - Short reflection

Write 4-6 lines:

- What changed from the 1D score to the 2D score?
- What does $\Sigma^{-1}$ do geometrically?
- Why is this a useful toy case before learning neural score models?

> In 1D, the score is a scalar that pulls $x$ back toward the mean.
> In 2D, the score is a vector that pulls each point through the precision matrix $\Sigma^{-1}$.
> The inverse covariance controls how strong the pull is in each direction, and with correlation it can mix the coordinates.
> Geometrically, $\Sigma$ shapes the density contours while $\Sigma^{-1}$ shapes the score arrows.
> This is a useful toy case because the exact score is known, so we can check what a neural score model is trying to approximate.

---

## Completion Checklist

- [x] I derived the 2D Gaussian score without skipping the log-density step.
- [x] I explained the role of the precision matrix.
- [x] I completed the notebook implementation.
- [x] I verified the analytic score against finite differences.
- [x] I interpreted the vector field in one short paragraph.

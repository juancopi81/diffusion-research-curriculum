# Gaussian Identities

This is a living reference for Gaussian calculations used throughout the
curriculum. Longer explanations and derivations remain in their corresponding
weekly notes and proofs.

## Conventions

- Vectors are columns unless stated otherwise.
- Gradients of scalar-valued functions are column vectors.
- Matrices in gradient identities are treated as constant unless another
  variable of differentiation is named.
- For $f:\mathbb{R}^n\to\mathbb{R}$,

$$
df=(\nabla_x f)^\top dx,
\qquad
\frac{\partial f}{\partial x}=(\nabla_x f)^\top.
$$

## Matrix Gradient Identities

For $x,a\in\mathbb{R}^n$ and $A\in\mathbb{R}^{n\times n}$,

$$
\boxed{
\nabla_x(x^\top a)=a
}
$$

and

$$
\boxed{
\nabla_x(x^\top A x)=(A+A^\top)x
}.
$$

If $A=A^\top$, this reduces to

$$
\boxed{
\nabla_x(x^\top A x)=2Ax
}.
$$

For

$$
g(s)=(x-As)^\top W(x-As),
\qquad
W=W^\top,
$$

the gradient with respect to $s$ is

$$
\boxed{
\nabla_s g(s)=-2A^\top W(x-As)
}.
$$

## Symmetric Positive-Definite Covariance

If $\Sigma$ is symmetric positive definite, then

$$
\Sigma^\top=\Sigma,
\qquad
\Sigma^{-1}\text{ exists},
\qquad
(\Sigma^{-1})^\top=\Sigma^{-1}.
$$

In general,

$$
\Sigma^{-1}\neq\Sigma^\top.
$$

## Affine Gaussian Transformation

If

$$
Z\sim\mathcal{N}(0,I),
\qquad
X=\mu+BZ,
$$

then

$$
\boxed{
\mathbb{E}[X]=\mu,
\qquad
\operatorname{Cov}(X)=BB^\top
}.
$$

More generally, for constant $A$ and $b$,

$$
X\sim\mathcal{N}(\mu,\Sigma)
\quad\Longrightarrow\quad
AX+b\sim\mathcal{N}(A\mu+b,A\Sigma A^\top).
$$

## Covariance Factorizations for Sampling

If

$$
\Sigma=Q\Lambda Q^\top,
$$

then one valid factor is

$$
\boxed{B=Q\Lambda^{1/2}},
\qquad
BB^\top=\Sigma.
$$

For symmetric positive-definite $\Sigma$, Cholesky factorization gives

$$
\boxed{\Sigma=LL^\top},
\qquad
X=\mu+LZ,
\qquad
Z\sim\mathcal{N}(0,I).
$$

## Mahalanobis Distance and Normalization

The squared Mahalanobis distance is

$$
\boxed{
d_\Sigma^2(x,\mu)
=(x-\mu)^\top\Sigma^{-1}(x-\mu)
}.
$$

For diagonal $\Sigma=\operatorname{diag}(\sigma_1^2,\ldots,\sigma_d^2)$,

$$
d_\Sigma^2(x,\mu)
=
\sum_{i=1}^d
\left(\frac{x_i-\mu_i}{\sigma_i}\right)^2.
$$

The Gaussian normalization uses

$$
\boxed{|\Sigma|^{1/2}}.
$$

For diagonal covariance,

$$
|\Sigma|^{1/2}=\prod_{i=1}^d\sigma_i.
$$

## Multivariate Gaussian Score

For

$$
x\sim\mathcal{N}(\mu,\Sigma),
$$

the log-density is

$$
\log p(x)
=
-\frac{d}{2}\log(2\pi)
-\frac12\log|\Sigma|
-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu).
$$

When $\mu$ and $\Sigma$ are fixed, only the quadratic term depends on $x$.
Therefore,

$$
\boxed{
\nabla_x\log p(x)
=
-\Sigma^{-1}(x-\mu)
}.
$$

Here $\Sigma^{-1}$ is the precision matrix.

## Conditional of a Joint Gaussian

Suppose

$$
\begin{bmatrix}
X_A\\
X_B
\end{bmatrix}
\sim
\mathcal{N}\left(
\begin{bmatrix}
\mu_A\\
\mu_B
\end{bmatrix},
\begin{bmatrix}
\Sigma_{AA} & \Sigma_{AB}\\
\Sigma_{BA} & \Sigma_{BB}
\end{bmatrix}
\right),
$$

where $\Sigma_{BB}$ is invertible. Then

$$
\boxed{
X_A\mid X_B=x_B
\sim
\mathcal{N}\left(
\mu_A+\Sigma_{AB}\Sigma_{BB}^{-1}(x_B-\mu_B),
\Sigma_{AA}-\Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA}
\right)
}.
$$

The observation $x_B$ changes the conditional mean but not the conditional
covariance. In numerical code, prefer linear solves to explicitly constructing
$\Sigma_{BB}^{-1}$.

## Diffusion Forward-Noising Kernel

The DDPM forward kernel can be written as

$$
q(x_t\mid x_0)
=
\mathcal{N}\left(
\sqrt{\bar{\alpha}_t}\,x_0,
(1-\bar{\alpha}_t)I
\right).
$$

Substituting this mean and covariance into the Gaussian score gives

$$
\boxed{
\nabla_{x_t}\log q(x_t\mid x_0)
=
-\frac{x_t-\sqrt{\bar{\alpha}_t}\,x_0}
{1-\bar{\alpha}_t}
}.
$$

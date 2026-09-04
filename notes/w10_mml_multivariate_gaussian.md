# Week 10 — MML Multivariate Gaussian

**Status:** Completed — gradient foundations, Gaussian geometry, affine
transformations, and sampling consolidated.

**Source basis:** Sections 5.2 and 5.5 of *Mathematics for Machine
Learning*, consolidated from handwritten study notes and checked against
identities 5.104, 5.107, and 5.108. See the
[MML source catalog](../sources/mml/README.md). The explanatory derivations
below are an independent consolidation, not quoted source text.

Tuesday's Gaussian geometry uses the Gaussian portion of Stanford's
[CS229 Probability Review](https://cs229.stanford.edu/notes2022fall/cs229-probability_review.pdf),
printed pages 20–33, together with the affine-transformation and sampling
material in MML §6.5. This pass consolidates the density, covariance geometry,
and sampling construction discussed in review. The score and block-conditioning
derivations, including the concrete 2D example, are completed in the
[Week 10 proof](../proofs/w10_multivariate_gaussian_score.md), with numerical
verification in the
[solved Week 10 notebook](../notebooks/w10_mv_gaussian_score_solved.ipynb).

The reusable formulas from this note are collected separately in the living
[Gaussian identities sheet](./gaussian_identities.md).

## Gradient Convention

Let $f:\mathbb{R}^n\to\mathbb{R}$ be scalar-valued and let
$x\in\mathbb{R}^n$ be a column vector. MML writes the derivative with
respect to $x$ as a row vector:

$$
\frac{\partial f}{\partial x}\in\mathbb{R}^{1\times n}.
$$

For diffusion work, this repository will use the column-gradient convention:

$$
\nabla_x f\in\mathbb{R}^{n\times 1}.
$$

The total differential connects the two conventions:

$$
df
=
\frac{\partial f}{\partial x}\,dx
=
(\nabla_x f)^\top dx.
$$

Therefore,

$$
\boxed{
\frac{\partial f}{\partial x}=(\nabla_x f)^\top
}.
$$

This is a transpose of the complete derivative expression. It does not allow
vectors and matrices to be reordered as if matrix multiplication were
commutative.

## Linear Form

For fixed $a\in\mathbb{R}^n$,

$$
f(x)=x^\top a
$$

has MML row derivative and column gradient

$$
\frac{\partial f}{\partial x}=a^\top,
\qquad
\boxed{\nabla_x f=a}.
$$

## Quadratic Form

Let

$$
f(x)=x^\top A x,
\qquad
A\in\mathbb{R}^{n\times n},
$$

where $A$ is constant with respect to $x$. Apply the product rule to the
scalar differential:

$$
\begin{aligned}
df
&=d(x^\top)Ax+x^\top A\,dx \\
&=(dx)^\top Ax+x^\top A\,dx.
\end{aligned}
$$

The first term is a scalar, so it equals its transpose:

$$
(dx)^\top Ax
=
\big((dx)^\top Ax\big)^\top
=
x^\top A^\top dx.
$$

Substituting this into the differential gives

$$
\begin{aligned}
df
&=x^\top A^\top dx+x^\top A\,dx \\
&=x^\top(A^\top+A)dx \\
&=\big((A+A^\top)x\big)^\top dx.
\end{aligned}
$$

Matching this expression with $df=(\nabla_x f)^\top dx$ yields

$$
\boxed{
\nabla_x(x^\top A x)=(A+A^\top)x
}.
$$

If $A$ is symmetric, then

$$
\boxed{
\nabla_x(x^\top A x)=2Ax
}.
$$

## Shifted Weighted Quadratic

Let

$$
g(s)=(x-As)^\top W(x-As),
$$

where $x$, $A$, and symmetric $W$ are constant with respect to $s$. MML's
row-vector identity is

$$
\frac{\partial g}{\partial s}
=
-2(x-As)^\top WA.
$$

Transposing the whole expression gives the column gradient

$$
\boxed{
\nabla_s g(s)=-2A^\top W(x-As)
}.
$$

The minus sign comes from differentiating the residual $x-As$ with respect
to $s$.

## Application to the Gaussian Exponent

For a symmetric positive-definite covariance matrix $\Sigma$,

$$
\Sigma^\top=\Sigma
$$

and $\Sigma$ is invertible. Its inverse is also symmetric because

$$
(\Sigma^{-1})^\top
=(\Sigma^\top)^{-1}
=\Sigma^{-1}.
$$

Symmetry does **not** mean that $\Sigma^{-1}=\Sigma^\top$ in general.

Define

$$
z=x-\mu,
\qquad
A=\Sigma^{-1}.
$$

The $x$-dependent part of a multivariate Gaussian log-density is

$$
-\frac12 z^\top A z.
$$

Since $A$ is symmetric,

$$
\begin{aligned}
\nabla_z\left(-\frac12z^\top Az\right)
&=-\frac12(A+A^\top)z \\
&=-Az.
\end{aligned}
$$

The translation $z=x-\mu$ has derivative $dz/dx=I$: subtracting the
constant $\mu$ shifts every point but does not change the local rate of
change. Therefore,

$$
\boxed{
\nabla_x\left[
-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)
\right]
=
-\Sigma^{-1}(x-\mu)
}.
$$

## Monday Takeaways

- A scalar differential can be written as a row derivative times $dx$ or as
  a column gradient transposed times $dx$.
- Matrix factors must remain in dimensionally valid order.
- A quadratic form depends only on the symmetric part of its matrix:
  $(A+A^\top)/2$.
- A symmetric positive-definite covariance has a symmetric inverse, but the
  inverse is not generally equal to the covariance or its transpose.
- Translating $x$ by a constant mean changes the location, not the derivative
  of the displacement with respect to $x$.

## Affine Construction of a Gaussian

Let

$$
Z\sim\mathcal{N}(0,I),
\qquad
X=\mu+BZ.
$$

Because $\mu$ is constant and $\mathbb{E}[Z]=0$,

$$
\boxed{\mathbb{E}[X]=\mu}.
$$

Subtracting the mean gives $X-\mu=BZ$. Therefore,

$$
\begin{aligned}
\operatorname{Cov}(X)
&=\mathbb{E}\left[(BZ)(BZ)^\top\right] \\
&=B\mathbb{E}[ZZ^\top]B^\top \\
&=BIB^\top,
\end{aligned}
$$

so

$$
\boxed{\operatorname{Cov}(X)=BB^\top}.
$$

This is the matrix generalization of
$\operatorname{Var}(cZ)=c^2\operatorname{Var}(Z)$. The matrix $B$ appears on
the left and $B^\top$ on the right; it is not squared element by element. In
addition to rescaling coordinates, $B$ may rotate them and mix several latent
coordinates into one output coordinate.

For example, if

$$
B=
\begin{bmatrix}
1&1\\
0&1
\end{bmatrix},
$$

then

$$
X_1=Z_1+Z_2,
\qquad
X_2=Z_2.
$$

The shared $Z_2$ term creates positive covariance:

$$
\operatorname{Cov}(X_1,X_2)
=\operatorname{Cov}(Z_1+Z_2,Z_2)
=0+1=1.
$$

Indeed,

$$
BB^\top=
\begin{bmatrix}
2&1\\
1&1
\end{bmatrix}.
$$

The positive off-diagonal entries tilt the Gaussian contours from lower left
to upper right. Negative off-diagonal entries would tilt them from upper left
to lower right. The contours extend in both directions along their major axis;
they do not point like a one-way arrow.

## Covariance Factors and Sampling

A covariance matrix is symmetric positive semidefinite and therefore has an
orthogonal eigendecomposition

$$
\Sigma=Q\Lambda Q^\top,
$$

where the columns of $Q$ are principal directions and the diagonal entries of
$\Lambda$ are variances along those directions. A valid sampling factor is

$$
\boxed{B=Q\Lambda^{1/2}}.
$$

It satisfies

$$
\begin{aligned}
BB^\top
&=Q\Lambda^{1/2}(Q\Lambda^{1/2})^\top \\
&=Q\Lambda^{1/2}\Lambda^{1/2}Q^\top \\
&=Q\Lambda Q^\top \\
&=\Sigma.
\end{aligned}
$$

The square root is applied to the eigenvalues because $B$ scales by standard
deviations, while $\Sigma$ records variances. When $\Sigma$ is positive
definite, a Cholesky factor $L$ is another common choice:

$$
\Sigma=LL^\top,
\qquad
X=\mu+LZ.
$$

The factor is not unique. The eigendecomposition and Cholesky factorization
can produce different $B$ matrices with the same product $BB^\top=\Sigma$ and
therefore the same Gaussian distribution.

## Density and Covariance-Adjusted Distance

For a full-rank $d$-dimensional Gaussian,

$$
p(x)
=
\frac{1}{(2\pi)^{d/2}|\Sigma|^{1/2}}
\exp\left(
-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)
\right).
$$

The quadratic form

$$
\boxed{
d_\Sigma^2(x,\mu)
=(x-\mu)^\top\Sigma^{-1}(x-\mu)
}
$$

is the squared Mahalanobis distance. It is the ordinary squared distance after
the coordinates have been standardized and, when correlated, rotated into the
covariance geometry. High-variance directions are penalized less than
low-variance directions.

For example, with

$$
\Sigma=
\begin{bmatrix}
9&0\\
0&1
\end{bmatrix},
$$

the displacements $(3,0)^\top$ and $(0,1)^\top$ both have squared
Mahalanobis distance $1$. Although the first is farther in Euclidean distance,
each displacement is one standard deviation along its corresponding axis.

For diagonal covariance, the squared Mahalanobis distance is the sum of the
squared standardized coordinate displacements. A point that is one standard
deviation away in two independent coordinates therefore has squared distance
$2$, not $1$. With correlated coordinates, the off-diagonal terms in
$\Sigma^{-1}$ also account for whether the point follows or cuts across the
population's usual direction of variation.

The factor $|\Sigma|^{1/2}$ measures the volume scaling of the Gaussian. For
diagonal covariance,

$$
|\Sigma|^{1/2}=\prod_{i=1}^d\sigma_i.
$$

Increasing the spread increases this denominator and lowers the density so
that its integral over $\mathbb{R}^d$ remains $1$. The density value itself
does not need to equal $1$. Rotating an ellipse without changing its
eigenvalues preserves the determinant, so it also preserves the peak density.

## Tuesday Takeaways

- The mean $\mu$ translates a Gaussian without changing its covariance.
- In $X=\mu+BZ$, the factor $B$ controls scaling, rotation, and coordinate
  mixing, while $BB^\top$ is the resulting covariance.
- Diagonal covariance gives axis-aligned contours. Off-diagonal covariance
  tilts them and records how coordinates vary together.
- $\Sigma^{-1}$ defines covariance-adjusted distance; it is the precision
  matrix, not another expression for $\Sigma$.
- $|\Sigma|^{1/2}$ records volume scaling and supplies the normalization needed
  to keep total probability equal to $1$.
- Eigendecomposition separates the Gaussian's principal directions from its
  variances. Taking square roots of those variances produces a sampling factor.

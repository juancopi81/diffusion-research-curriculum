# Week 12 — Change of Variables for Flows

**Status:** Session 3's first two derivations reviewed on 2026-09-22;
Session 4's coupling-transform derivation reviewed on 2026-09-23;
Session 5's two-layer composition reviewed on 2026-09-24.

**Source basis:** My handwritten Session 3 exercises, reviewed against the
change-of-variables rule in
[MML §6.7](https://mml-book.github.io/book/mml-book.pdf) and the
[MML source catalog](../sources/mml/README.md). The Gaussian check uses my
[Week 10 affine-Gaussian note](../notes/w10_mml_multivariate_gaussian.md).
These are independent derivations, not quotations or the book's solutions.
The coupling example below is based on the learner's Session 4 handwritten
work and conceptual review, checked against
[RealNVP §§3.1–3.3](https://arxiv.org/html/1605.08803v3).
The composition below also draws on the learner's Session 5 handwritten work
and [RealNVP §3.5](https://arxiv.org/html/1605.08803v3#S3.SS5).

## 1. One-Dimensional Monotone Transform: $X=e^Z$

Let $Z\sim\mathcal N(0,1)$ and $X=e^Z$. I start with the standard normal
density:

$$
p_Z(z)=\frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{z^2}{2}\right).
$$

The exponential is strictly increasing and invertible. For $x>0$,

$$
z=f^{-1}(x)=\ln x,
\qquad
\left|\frac{dz}{dx}\right|=\frac{1}{x}.
$$

I use the **inverse derivative** because I am calculating the density at a
target point $x$ from the density at its corresponding source point $z$:

$$
\begin{aligned}
p_X(x)
&=p_Z\!\left(f^{-1}(x)\right)
  \left|\frac{d f^{-1}(x)}{dx}\right| \\
&=\frac{1}{\sqrt{2\pi}}
  \exp\!\left(-\frac{(\ln x)^2}{2}\right)\frac{1}{x}.
\end{aligned}
$$

Since $e^z>0$ for every real $z$, the complete answer is

$$
\boxed{
p_X(x)=
\begin{cases}
\dfrac{1}{x\sqrt{2\pi}}
\exp\!\left(-\dfrac{(\ln x)^2}{2}\right), & x>0, \\
0, & x\leq 0.
\end{cases}
}
$$

The factor $1/x$ is the inverse length correction. It keeps probability mass
unchanged when a small interval in $z$ is mapped to an interval in $x$.

## 2. Multivariate Affine Transform: $X=AZ+b$

Let $Z\sim\mathcal N(0,I_n)$, let $A\in\mathbb R^{n\times n}$ be invertible,
and let $b\in\mathbb R^n$. Define

$$
X=f(Z)=AZ+b.
$$

The source density is

$$
p_Z(z)=\frac{1}{(2\pi)^{n/2}}
\exp\!\left(-\frac12 z^\top z\right).
$$

Solving for the unique source point and differentiating gives

$$
z=f^{-1}(x)=A^{-1}(x-b),
\qquad
J_{f^{-1}}(x)=A^{-1}.
$$

I use the **inverse Jacobian** $J_{f^{-1}}$, so its absolute determinant
multiplies the source density:

$$
\begin{aligned}
p_X(x)
&=p_Z\!\left(A^{-1}(x-b)\right)|\det A^{-1}| \\
&=\frac{1}{(2\pi)^{n/2}|\det A|}
\exp\!\left[
-\frac12
\bigl(A^{-1}(x-b)\bigr)^\top
\bigl(A^{-1}(x-b)\bigr)
\right] \\
&=\boxed{
\frac{1}{(2\pi)^{n/2}|\det A|}
\exp\!\left[
-\frac12(x-b)^\top A^{-\top}A^{-1}(x-b)
\right]
}.
\end{aligned}
$$

The density is defined for every $x\in\mathbb R^n$ because an invertible
affine map sends $\mathbb R^n$ onto $\mathbb R^n$.

### Check against the Week 10 Gaussian result

Using $\mathbb E[Z]=0$ and $\operatorname{Cov}(Z)=I_n$,

$$
\mathbb E[X]=A\mathbb E[Z]+b=b,
\qquad
\operatorname{Cov}(X)=A I_n A^\top=AA^\top.
$$

Thus Week 10 predicts $X\sim\mathcal N(b,\Sigma)$ with $\Sigma=AA^\top$.
Its density agrees with the result above because

$$
\Sigma^{-1}=(AA^\top)^{-1}=A^{-\top}A^{-1},
\qquad
\sqrt{\det\Sigma}
=\sqrt{\det A\,\det A^\top}
=|\det A|.
$$

Both the quadratic term and the normalization constant match the standard
multivariate-Gaussian density.

## 3. Determinant and Direction Checkpoint

The determinant measures signed volume change. Its sign indicates whether
the transformation reverses orientation; density depends on the magnitude
of the volume change, so the formula uses an absolute value.

For $x=f(z)=Az+b$, the forward Jacobian is $A$ and the inverse Jacobian is
$A^{-1}$. These are equivalent ways to write the correction:

$$
|\det J_{f^{-1}}(x)|
=|\det A^{-1}|
=\frac{1}{|\det A|}
=\frac{1}{|\det J_f(z)|},
\qquad z=f^{-1}(x).
$$

Therefore, I **multiply** by the inverse determinant or **divide** by the
forward determinant. A reflection may make $\det A$ negative, but it cannot
make the density negative.

## 4. Affine Coupling Transform in Two Dimensions

Let $s,t:\mathbb R\to\mathbb R$ be differentiable, and define $y=g(x)$ by

$$
y_1=x_1,
\qquad
y_2=x_2\exp(s(x_1))+t(x_1).
$$

Since $x_1=y_1$ and $\exp(s(y_1))>0$, solving for the second coordinate gives

$$
x_1=y_1,
\qquad
x_2=\frac{y_2-t(y_1)}{\exp(s(y_1))}
    =(y_2-t(y_1))\exp(-s(y_1)).
$$

Differentiating the forward map gives

$$
J_g(x)
=\begin{pmatrix}
\frac{\partial y_1}{\partial x_1} &
\frac{\partial y_1}{\partial x_2} \\
\frac{\partial y_2}{\partial x_1} &
\frac{\partial y_2}{\partial x_2}
\end{pmatrix}
=\begin{pmatrix}
1 & 0 \\
x_2\exp(s(x_1))s'(x_1)+t'(x_1) & \exp(s(x_1))
\end{pmatrix}.
$$

For a matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$, the determinant is
$ad-bc$. Here $b=0$, so the lower-left term cannot affect it:

$$
\det J_g(x)=1\cdot\exp(s(x_1))=\exp(s(x_1)),
\qquad
\log|\det J_g(x)|=s(x_1).
$$

This uses the **product** of diagonal entries, not their sum (the trace).
The inverse Jacobian is also lower triangular. Its diagonal entries are $1$
and

$$
\frac{\partial x_2}{\partial y_2}
=\frac{\partial}{\partial y_2}
\bigl[(y_2-t(y_1))\exp(-s(y_1))\bigr]
=\exp(-s(y_1)),
$$

where $y_1$ is held fixed. Hence

$$
\det J_{g^{-1}}(y)=\exp(-s(y_1)),
\qquad
\log|\det J_{g^{-1}}(y)|=-s(y_1).
$$

At corresponding points $x_1=y_1$, so the forward and inverse
log-determinants add to zero. As a numerical check, if $s(y_1)=\log 2$,
then $\partial x_2/\partial y_2=1/2$: increasing $y_2$ by $2$ while holding
$y_1$ fixed increases $x_2$ by $1$.

For a density, the direction must be stated. If $g$ maps data $x$ to a
base-distribution point $y$, then

$$
\log p_X(x)
=\log p_Y(g(x))+s(x_1).
$$

If $g$ maps a base-distribution point $x$ to data $y$, then

$$
\log p_Y(y)
=\log p_X(g^{-1}(y))-s(y_1).
$$

## 5. Two Alternating Coupling Layers

For the notebook, use data-to-latent layers $f_1:x\mapsto y$ and
$f_2:y\mapsto z$:

$$
\begin{aligned}
y_1&=x_1,
&y_2&=x_2\exp(s_1(x_1))+t_1(x_1),\\
z_1&=y_1\exp(s_2(y_2))+t_2(y_2),
&z_2&=y_2.
\end{aligned}
$$

The first layer updates coordinate 2 and has a lower-triangular Jacobian;
the second updates coordinate 1 and has an upper-triangular Jacobian. Their
determinants are $\exp(s_1(x_1))$ and $\exp(s_2(y_2))$, respectively. If the
same coordinate remained fixed in every layer, that output coordinate would
remain identical to its input throughout the stack.

For column-vector Jacobians, the chain rule follows by tracing a small
change through both layers:

$$
\delta y\approx J_{f_1}(x)\delta x,
\qquad
\delta z\approx J_{f_2}(y)\delta y
          \approx J_{f_2}(y)J_{f_1}(x)\delta x.
$$

Therefore, with $y=f_1(x)$,

$$
J_{f_2\circ f_1}(x)=J_{f_2}(y)J_{f_1}(x),
$$

and the determinant and logarithm rules yield

$$
\begin{aligned}
\log|\det J_{f_2\circ f_1}(x)|
&=\log|\det J_{f_2}(y)|+\log|\det J_{f_1}(x)|\\
&=s_2(y_2)+s_1(x_1).
\end{aligned}
$$

The matrix order matters in the chain rule; multiplication of the two scalar
determinants gives the same result in either order. The full density is

$$
\log p_\theta(x)
=\log p_Z(z)+s_1(x_1)+s_2(y_2),
\qquad z=f_2(f_1(x)).
$$

To generate a sample from $z$, first undo $f_2$ and then $f_1$:

$$
\begin{aligned}
y_2&=z_2,
&y_1&=(z_1-t_2(z_2))\exp(-s_2(z_2)),\\
x_1&=y_1,
&x_2&=(y_2-t_1(y_1))\exp(-s_1(y_1)).
\end{aligned}
$$

This makes $f^{-1}=f_1^{-1}\circ f_2^{-1}$ explicit. A notebook's
`forward(x)` should return $z$ and the sum of the forward log-determinants;
`log_prob(x)` adds the base log density, and `sample(n)` draws $z$ from the
base distribution before calling `inverse(z)`.

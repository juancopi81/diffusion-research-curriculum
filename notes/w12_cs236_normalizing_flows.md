# Week 12 — CS236 Normalizing Flows Foundations

**Status:** Sessions 1 and 2 reviewed and consolidated on 2026-09-21;
Session 4's affine-coupling derivation reviewed on 2026-09-23; Session 5's
composition and code map reviewed on 2026-09-24. The CS236 lecture coverage
below extends only through slide 12 of 19. The later coupling and composition
sections come from the learner's handwritten work and the RealNVP paper,
rather than an assumed continuation of that recording.

**Source basis:** Stanford CS236 Fall 2023
[Lecture 7 slides: Normalizing Flow Models](https://deepgenerativemodels.github.io/assets/slides/cs236_lecture7.pdf),
slides 1–12, and the
[lecture recording studied](https://www.youtube.com/watch?v=m6dKKRsZwBQ&list=PL14_CPAN5yShN6x139pvSwLS4o6QaI5rJ&index=7&t=1s).
The learner reported watching the recording through slide 12. These
AI-assisted notes synthesize the inspected slides, the learner's handwritten
affine-transformation example, and the subsequent conceptual review. A video
transcript and lecture frames were not available in this session, so claims
about the recording are limited to the learner's report rather than presented
as independently verified transcription.

**Session 4 source basis:** The learner's two handwritten pages and conceptual
review, checked against [RealNVP §§3.1–3.3](https://arxiv.org/html/1605.08803v3).

**Session 5 source basis:** The learner's two handwritten pages and conceptual
review, checked against [RealNVP §§3.1 and 3.5](https://arxiv.org/html/1605.08803v3).

## 1. Why the VAE Recap Motivates Flows

The VAE defines its marginal density by integrating over possible latent
explanations:

$$
p_\theta(x)
=
\int p_\theta(x\mid z)p(z)\,dz.
$$

Its latent representation can be useful, but the nonlinear decoder generally
makes this marginal-likelihood integral intractable. Multiple latent values
can contribute density to the same observation.

The lecture asks whether a model can preserve two desirable properties at
once:

- a simple base density that is easy to evaluate and sample;
- a flexible data density that is also exactly evaluable and easy to sample.

The proposed change is to make the relationship between latent and observed
variables deterministic and invertible:

$$
x=f_\theta(z),
\qquad
z=f_\theta^{-1}(x).
$$

For each observed $x$, invertibility gives one unique corresponding latent
value $z$. There is therefore no collection of latent explanations to
marginalize over. Evaluating the density of $x$ instead requires:

1. mapping $x$ back to $z=f_\theta^{-1}(x)$;
2. evaluating the known base density $p_Z(z)$;
3. correcting for how the transformation changes local volume.

## 2. Probability Mass Is Preserved, Density Compensates

For a continuous variable, density at a point is not the probability of that
point. Probabilities are obtained by integrating density over regions.

Suppose

$$
Z\sim\operatorname{Uniform}(0,2),
\qquad
X=4Z.
$$

The source interval has length $2$ and density $1/2$. The transformation maps
it to $[0,8]$, which is four times as long. Corresponding source and target
regions must contain the same probability mass.

For a small interval around $z=1$ and its image around $x=4$,

$$
p_Z(1)\,\Delta z
\approx
p_X(4)\,\Delta x.
$$

Because $\Delta x=4\Delta z$,

$$
p_X(4)
=
p_Z(1)\frac{\Delta z}{\Delta x}
=
\frac12\cdot\frac14
=
\frac18.
$$

The central intuition is:

> When a transformation expands space, density contracts by the reciprocal
> factor so corresponding regions retain the same probability mass.

## 3. One-Dimensional Change of Variables

Let $X=f(Z)$, where $f$ is differentiable and monotone, with inverse
$Z=f^{-1}(X)$. Then

$$
\boxed{
p_X(x)
=
p_Z\!\left(f^{-1}(x)\right)
\left|
\frac{d f^{-1}(x)}{dx}
\right|.
}
$$

The inverse derivative converts density per unit of $z$ into density per unit
of $x$:

$$
\left|\frac{dz}{dx}\right|
=
\frac{\text{small source length}}
{\text{corresponding transformed length}}.
$$

Equivalently, if $z=f^{-1}(x)$ and it is easier to use the forward derivative,

$$
p_X(x)
=
p_Z(z)
\frac{1}{|f'(z)|}.
$$

The absolute value is necessary because density responds to the magnitude of
length change, not whether the transformation reverses orientation.

## 4. Determinants Measure Multidimensional Volume Change

For an invertible affine transformation

$$
y=Au+b,
$$

the matrix $A$ transforms edge vectors. Its determinant records the signed
volume scale:

- $|\det A|>1$ expands volume;
- $0<|\det A|<1$ contracts volume;
- $|\det A|=1$ preserves volume;
- the sign records whether orientation is preserved or reversed.

Probability density uses $|\det A|$ because a reflection may reverse
orientation without producing negative volume or negative density. Translation
does not affect volume because

$$
\frac{\partial(Au+b)}{\partial u}=A.
$$

The affine change-of-variables formula is

$$
\boxed{
p_Y(y)
=
p_U\!\left(f^{-1}(y)\right)
\frac{1}{|\det A|}.
}
$$

Equivalently,

$$
p_Y(y)
=
p_U\!\left(f^{-1}(y)\right)|\det A^{-1}|.
$$

When using the inverse determinant, multiply by it directly. When using the
forward determinant, divide by it.

## 5. Worked Affine Example from Session 1

The learner studied

$$
f(u_1,u_2)
=
\begin{pmatrix}
2u_1+u_2\\
u_2+1
\end{pmatrix}
=
\begin{pmatrix}
2&1\\
0&1
\end{pmatrix}
\begin{pmatrix}
u_1\\
u_2
\end{pmatrix}
+
\begin{pmatrix}
0\\
1
\end{pmatrix}.
$$

The Jacobian is constant:

$$
J_f(u_1,u_2)
=
\begin{pmatrix}
\frac{\partial f_1}{\partial u_1}
&
\frac{\partial f_1}{\partial u_2}\\
\frac{\partial f_2}{\partial u_1}
&
\frac{\partial f_2}{\partial u_2}
\end{pmatrix}
=
\begin{pmatrix}
2&1\\
0&1
\end{pmatrix},
\qquad
\det J_f=2.
$$

The unit-square edge vectors transform as

$$
f(1,0)-f(0,0)
=
\begin{pmatrix}2\\0\end{pmatrix},
\qquad
f(0,1)-f(0,0)
=
\begin{pmatrix}1\\1\end{pmatrix}.
$$

They span a parallelogram of area $2$. If $U$ is uniform on the unit square,
then $p_U(u)=1$ there. The transformed density is therefore

$$
p_Y(y)=1\cdot\frac{1}{2}=\frac12
$$

inside the parallelogram and $0$ outside. Its integral is still one:

$$
\int_{\text{parallelogram}}\frac12\,dy
=
\frac12\times2
=
1.
$$

The translation vector $(0,1)$ moves the parallelogram but does not change its
area or density.

## 6. Jacobians Give Local Linear Approximations

An affine transformation uses the same matrix everywhere. A nonlinear
transformation can stretch different regions by different amounts. Near a
particular source point $z$, its Jacobian

$$
J_f(z)
=
\frac{\partial f(z)}{\partial z}
$$

is the best local linear approximation. For a sufficiently small region
around $z$,

$$
\text{transformed volume}
\approx
|\det J_f(z)|
\times
\text{source volume}.
$$

Thus $|\det J_f(z)|$ is the local volume-expansion factor. Unlike the affine
case, it can vary with position.

## 7. Multivariate Change of Variables

Let

$$
x=f(z),
\qquad
f:\mathbb{R}^n\to\mathbb{R}^n,
$$

where $f$ is differentiable and invertible. For a given $x$, set

$$
z=f^{-1}(x).
$$

Using the forward Jacobian,

$$
\boxed{
p_X(x)
=
p_Z\!\left(f^{-1}(x)\right)
\frac{1}{
\left|
\det J_f\!\left(f^{-1}(x)\right)
\right|}.
}
$$

Equivalently, using the inverse Jacobian,

$$
\boxed{
p_X(x)
=
p_Z\!\left(f^{-1}(x)\right)
\left|
\det J_{f^{-1}}(x)
\right|.
}
$$

The two expressions agree because the Jacobian matrices of inverse mappings
are inverses at corresponding points.

## 8. Why Ordinary Flows Preserve Dimension

The construction in this lecture requires $x$ and $z$ to have the same
dimension. If a continuous differentiable map compresses
$x\in\mathbb{R}^n$ into $z\in\mathbb{R}^d$ with $d<n$, multiple inputs must
generally share the same lower-dimensional representation. The latent value
then does not contain enough information to recover one unique original input,
and the Jacobian is rectangular rather than having the determinant required by
the ordinary formula.

This differs from a VAE, which may deliberately learn a lower-dimensional,
lossy representation and use a stochastic decoder. Lossless compression can
exist for discrete structured data or data restricted to a lower-dimensional
set, but a standard flow representing a full-dimensional continuous density
uses an equal-dimensional invertible map.

## 9. Two-Dimensional Affine Coupling Layer

The Session 4 transform keeps one coordinate fixed and uses it to scale and
shift the other:

$$
y_1=x_1,
\qquad
y_2=x_2\exp(s(x_1))+t(x_1).
$$

Here $s$ and $t$ may be nonlinear functions. Their values depend on $x_1$,
but the factor $\exp(s(x_1))$ is always positive, so the transform can be
inverted for any $x_2$:

$$
x_1=y_1,
\qquad
x_2=(y_2-t(y_1))\exp(-s(y_1)).
$$

The transform is not a matrix multiplication with $t(x_1)$ as a coefficient:
$t(x_1)$ is an added shift. Its local linear behavior is described by the
Jacobian:

$$
J_{x\to y}(x)
=
\begin{pmatrix}
1 & 0 \\
x_2\exp(s(x_1))s'(x_1)+t'(x_1) & \exp(s(x_1))
\end{pmatrix}.
$$

Because the upper-right entry is zero, this matrix is lower triangular. For a
$2\times2$ matrix, $\det\begin{pmatrix}a&0\\c&d\end{pmatrix}=ad$;
the lower-left entry does not contribute. Thus

$$
\det J_{x\to y}(x)=\exp(s(x_1)),
\qquad
\log|\det J_{x\to y}(x)|=s(x_1).
$$

The determinant is the **product** of the diagonal entries; the trace is
their **sum**. Taking the logarithm cancels the exponential.

For the inverse, the diagonal derivatives are
$\partial x_1/\partial y_1=1$ and
$\partial x_2/\partial y_2=\exp(-s(y_1))$. The latter includes the scale
factor even though $\partial(y_2-t(y_1))/\partial y_2=1$. Therefore

$$
\log|\det J_{y\to x}(y)|=-s(y_1).
$$

The two log-determinants cancel at corresponding points because $x_1=y_1$.
If this layer maps data $x$ to latent $y$, its contribution to
$\log p_X(x)=\log p_Y(y)+\log|\det J_{x\to y}(x)|$ is $+s(x_1)$.
If it maps latent $x$ to data $y$, evaluating the data density instead uses
the inverse Jacobian and contributes $-s(y_1)$.

## 10. Compose Layers and Add Their Log-Determinants

Use the data-to-latent convention $z=f_\theta(x)$ for the Week 12 notebook.
For two successive layers, let

$$
y=f_1(x),
\qquad
z=f_2(y)=f_2(f_1(x)).
$$

With column-vector inputs, a small change passes through the layers as
$\delta y\approx J_1(x)\delta x$ and
$\delta z\approx J_2(y)\delta y$. Substitution gives the Jacobian chain rule:

$$
J_f(x)=J_2(f_1(x))J_1(x).
$$

The order of these matrices matters for the Jacobian itself. For the
determinant, $\det(AB)=\det(A)\det(B)$, so

$$
\log|\det J_f(x)|
=\log|\det J_1(x)|
 +\log|\det J_2(f_1(x))|.
$$

Each layer's contribution is evaluated at that layer's **input**, then added
to the running log-determinant. The absolute value makes this rule valid even
if a layer reverses orientation.

## 11. Why Alternate the Transformed Coordinate?

In a two-dimensional coupling layer, one coordinate stays unchanged while it
controls the scale and shift of the other. If every layer preserves the first
coordinate, that coordinate remains unchanged by the complete composition.
Alternating the choice lets both coordinates be updated:

$$
\begin{aligned}
y_1&=x_1,
&y_2&=x_2\exp(s_1(x_1))+t_1(x_1),\\
z_1&=y_1\exp(s_2(y_2))+t_2(y_2),
&z_2&=y_2.
\end{aligned}
$$

Layer 1 updates the second coordinate; layer 2 updates the first. For this
example their log-determinants are $s_1(x_1)$ and $s_2(y_2)$, respectively.
Alternating is a way to mix which coordinates change across layers, not a
condition for each individual layer to be invertible.

## 12. Map the Convention to Notebook Operations

Under the chosen data-to-latent convention:

- `forward(x)` applies the coupling layers in order and returns the final
  latent point $z$ and the sum of their forward log-determinants.
- `log_prob(x)` calls `forward(x)`, evaluates $\log p_Z(z)$, and adds the
  returned log-determinant:

$$
\log p_\theta(x)
=\log p_Z(f_\theta(x))
 +\log|\det J_{f_\theta}(x)|.
$$

- `inverse(z)` applies the layer inverses in reverse order and returns $x$.
  For two layers, $f^{-1}=f_1^{-1}\circ f_2^{-1}$: undo $f_2$ first.
- `sample(n)` draws $z\sim p_Z$ and passes it through `inverse(z)`.

Keeping `forward` as data-to-latent and `inverse` as latent-to-data fixes the
sign convention for the training likelihood and for generation.

## Main Takeaways

- Invertibility assigns one latent point to each observation and removes the
  VAE-style marginalization over latent explanations.
- Probability mass is preserved across corresponding regions; density changes
  inversely with length, area, or volume.
- A determinant gives the volume scale of a linear transformation, while a
  Jacobian determinant gives the local scale of a nonlinear transformation.
- The absolute value discards orientation and retains the nonnegative volume
  factor needed by a density.
- Using the inverse Jacobian means multiplying by its determinant; using the
  forward Jacobian means dividing by its determinant.
- Ordinary normalizing flows require deterministic, invertible mappings
  between continuous spaces of equal dimension.
- An affine coupling layer is invertible without inverting its scale and shift
  functions; its triangular Jacobian makes the log-determinant cheap to compute.
- The forward and inverse log-determinants have opposite signs. State which
  direction a layer uses before adding its contribution to a log density.
- For a composition, evaluate each layer's log-determinant at its own input
  and add the results; undo layers in reverse order to generate samples.

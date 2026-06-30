# Stat 110 (Blitzstein) - Lecture 30

**Lecture 30:** [Chi-Square, Student-t, Multivariate Normal](https://www.youtube.com/watch?v=MF-XSJOsGqw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=30)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** Transcribed from user-provided notebook photos. Notation is cleaned up and a few explanatory bridges are added where the surrounding derivation is clear; this is not labeled as an official solution.

---

## 1) Chi-Square Distribution

Let

$$
Z_1,Z_2,\dots,Z_n
$$

be i.i.d. standard normal random variables:

$$
Z_j\sim N(0,1).
$$

Define

$$
V=Z_1^2+Z_2^2+\cdots+Z_n^2.
$$

Then, by definition,

$$
\boxed{
V\sim \chi_n^2.
}
$$

The parameter $n$ is called the degrees of freedom.

### Gamma Connection

A useful fact is

$$
\chi_1^2\sim \mathrm{Gamma}\!\left(\frac{1}{2},\frac{1}{2}\right),
$$

using the Stat 110 Gamma(shape, rate) convention.

Since sums of independent Gamma random variables with the same rate are again Gamma, we get

$$
\boxed{
\chi_n^2\sim \mathrm{Gamma}\!\left(\frac{n}{2},\frac{1}{2}\right).
}
$$

So a chi-square random variable is a Gamma random variable with shape $n/2$ and rate $1/2$.

---

## 2) Even Moments of a Standard Normal

For

$$
Z\sim N(0,1),
$$

the first few even moments are

$$
\mathbb{E}(Z^2)=1,
\qquad
\mathbb{E}(Z^4)=3,
\qquad
\mathbb{E}(Z^6)=3\cdot 5=15.
$$

In general,

$$
\boxed{
\mathbb{E}(Z^{2m})=(2m-1)!!=1\cdot 3\cdot 5\cdots (2m-1).
}
$$

One way to get these moments is from the MGF of $Z$. Another way is to use

$$
Z^2\sim \chi_1^2\sim \mathrm{Gamma}\!\left(\frac{1}{2},\frac{1}{2}\right)
$$

and then compute

$$
\mathbb{E}(Z^{2m})
=
\mathbb{E}\!\left((Z^2)^m\right)
$$

using LOTUS or the Gamma moment formula.

---

## 3) Student-t Distribution

The Student-t distribution was introduced by William Gosset, who published under the name "Student" around 1908.

Let

$$
Z\sim N(0,1),
\qquad
V\sim \chi_n^2,
$$

with $Z$ and $V$ independent. Define

$$
T=
\frac{Z}{\sqrt{V/n}}.
$$

Then

$$
\boxed{
T\sim t_n.
}
$$

The parameter $n$ is again the degrees of freedom.

### Basic Properties

The Student-t distribution is symmetric:

$$
T\sim t_n
\quad\Longrightarrow\quad
-T\sim t_n.
$$

For $n=1$,

$$
t_1
$$

is the Cauchy distribution. In this case the mean does not exist.

For $n\ge 2$, the mean exists and equals $0$. Using the independence of $Z$ and $V$,

$$
\begin{aligned}
\mathbb{E}(T)
&=
\mathbb{E}\!\left(
Z\frac{1}{\sqrt{V/n}}
\right) \\
&=
\mathbb{E}(Z)\,
\mathbb{E}\!\left(\frac{1}{\sqrt{V/n}}\right) \\
&=
0.
\end{aligned}
$$

The Student-t distribution has heavier tails than the normal distribution. Intuitively, the denominator $\sqrt{V/n}$ is random, and when it is small, the ratio can be large in magnitude.

For $n>2$, its variance exists and is

$$
\mathrm{Var}(T)=\frac{n}{n-2}.
$$

This variance approaches $1$ as $n\to\infty$, matching the standard normal limit.

---

## 4) Large Degrees of Freedom Limit

For large $n$, the $t_n$ distribution looks very much like $N(0,1)$.

To see why, construct

$$
T_n=\frac{Z}{\sqrt{V_n/n}},
$$

where

$$
Z\sim N(0,1),
$$

and

$$
V_n=Z_1^2+\cdots+Z_n^2,
$$

with

$$
Z_1,Z_2,\dots
$$

i.i.d. $N(0,1)$ and independent of $Z$.

Since

$$
\mathbb{E}(Z_j^2)=1,
$$

the law of large numbers gives

$$
\frac{V_n}{n}
=
\frac{Z_1^2+\cdots+Z_n^2}{n}
\to 1
\quad
\text{with probability }1.
$$

Therefore,

$$
\sqrt{\frac{V_n}{n}}\to 1
\quad
\text{with probability }1.
$$

So

$$
T_n=\frac{Z}{\sqrt{V_n/n}}\to Z
\quad
\text{with probability }1.
$$

Since $Z\sim N(0,1)$, this gives the distributional limit

$$
\boxed{
t_n\to N(0,1)
\quad
\text{as }n\to\infty.
}
$$

---

## 5) Multivariate Normal Definition

A random vector

$$
\mathbf{X}=(X_1,\dots,X_k)
$$

is multivariate normal (MVN) if every linear combination of its components is normal.

That is, for every choice of constants $t_1,\dots,t_k$,

$$
\boxed{
t_1X_1+\cdots+t_kX_k
\text{ is normal.}
}
$$

This definition includes degenerate normal random variables, such as constants, so that zero-variance linear combinations are allowed.

---

## 6) MVN Example

Let

$$
Z,W
$$

be independent $N(0,1)$ random variables.

Then

$$
(Z,2W,3Z,5W)
$$

is multivariate normal.

To check this, take an arbitrary linear combination:

$$
a_1Z+a_2(2W)+a_3(3Z)+a_4(5W).
$$

Collect terms:

$$
a_1Z+2a_2W+3a_3Z+5a_4W
=
(a_1+3a_3)Z+(2a_2+5a_4)W.
$$

This is a linear combination of independent normal random variables, so it is normal. Therefore the vector is MVN.

---

## 7) Marginal Normals Are Not Enough

It is not enough for each component to be marginally normal.

Let

$$
Z\sim N(0,1),
$$

and let $S$ be a random sign independent of $Z$:

$$
\mathbb{P}(S=1)=\mathbb{P}(S=-1)=\frac{1}{2}.
$$

Then both

$$
Z
\qquad
\text{and}
\qquad
SZ
$$

are marginally $N(0,1)$.

But the vector

$$
(Z,SZ)
$$

is not MVN. To see this, look at the linear combination

$$
Z+SZ=(1+S)Z.
$$

If $S=1$, then

$$
Z+SZ=2Z.
$$

If $S=-1$, then

$$
Z+SZ=0.
$$

So $Z+SZ$ has a point mass at $0$ with probability $1/2$, and therefore is not normal. Hence $(Z,SZ)$ is not multivariate normal.

---

## 8) MGF of a Multivariate Normal

Let

$$
\mathbf{X}=(X_1,\dots,X_k)
$$

be MVN with mean vector

$$
\boldsymbol{\mu}
=
(\mu_1,\dots,\mu_k)
$$

and covariance matrix $\Sigma$.

For

$$
\mathbf{t}=(t_1,\dots,t_k),
$$

the MGF of $\mathbf{X}$ is

$$
M_{\mathbf{X}}(\mathbf{t})
=
\mathbb{E}\!\left(e^{\mathbf{t}^\top\mathbf{X}}\right).
$$

Now

$$
\mathbf{t}^\top\mathbf{X}
=
t_1X_1+\cdots+t_kX_k
$$

is normal by the MVN definition.

Its mean is

$$
\mathbb{E}(\mathbf{t}^\top\mathbf{X})
=
\mathbf{t}^\top\boldsymbol{\mu},
$$

and its variance is

$$
\mathrm{Var}(\mathbf{t}^\top\mathbf{X})
=
\mathbf{t}^\top\Sigma\mathbf{t}.
$$

Using the one-dimensional normal MGF,

$$
\boxed{
M_{\mathbf{X}}(\mathbf{t})
=
\exp\!\left(
\mathbf{t}^\top\boldsymbol{\mu}
+
\frac{1}{2}\mathbf{t}^\top\Sigma\mathbf{t}
\right).
}
$$

This shows that an MVN distribution is determined by its mean vector and covariance matrix.

---

## 9) Within MVN: Uncorrelated Implies Independent

For general random variables, uncorrelated does not imply independent.

Inside the multivariate normal family, it does.

If

$$
\mathbf{X}
=
(\mathbf{X}_1,\mathbf{X}_2)
$$

is jointly MVN, and every component of $\mathbf{X}_1$ is uncorrelated with every component of $\mathbf{X}_2$, then

$$
\boxed{
\mathbf{X}_1\perp\!\!\!\perp \mathbf{X}_2.
}
$$

The reason is visible from the MVN MGF. If the cross-covariance terms are all $0$, then the quadratic form

$$
\mathbf{t}^\top\Sigma\mathbf{t}
$$

splits into one part involving only $\mathbf{X}_1$ and another part involving only $\mathbf{X}_2$. The joint MGF then factors into the product of the two marginal MGFs, which implies independence.

---

## 10) Example: Independent Sum and Difference

Let

$$
X,Y
$$

be i.i.d. $N(0,1)$ random variables.

The vector

$$
(X+Y,\ X-Y)
$$

is MVN because it is a linear transformation of the MVN vector $(X,Y)$.

Compute the covariance:

$$
\begin{aligned}
\mathrm{Cov}(X+Y,\ X-Y)
&=
\mathrm{Cov}(X,X)
-
\mathrm{Cov}(X,Y)
+
\mathrm{Cov}(Y,X)
-
\mathrm{Cov}(Y,Y) \\
&=
\mathrm{Var}(X)-\mathrm{Var}(Y) \\
&=
1-1 \\
&=
0.
\end{aligned}
$$

Since the pair is MVN and the two components are uncorrelated, they are independent:

$$
\boxed{
X+Y\perp\!\!\!\perp X-Y.
}
$$

---

## Main Takeaways

- $\chi_n^2$ is the distribution of a sum of $n$ squared independent standard normals.
- $\chi_n^2$ is the same as $\mathrm{Gamma}(n/2,1/2)$ under the shape-rate convention.
- Student-t is $Z/\sqrt{V/n}$, where $Z\sim N(0,1)$ and $V\sim \chi_n^2$ are independent.
- The $t_n$ distribution is symmetric, heavy-tailed, and approaches $N(0,1)$ as $n$ grows.
- A vector is MVN if every linear combination of its components is normal.
- Marginal normality alone does not imply joint multivariate normality.
- Within the MVN family, uncorrelated components or blocks are independent.

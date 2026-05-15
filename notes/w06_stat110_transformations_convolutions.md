# Stat 110 (Blitzstein) — Lecture 22

**Lecture 22:** [Transformations and Convolutions](https://www.youtube.com/watch?v=yXwPUAIvFyg)
**Course:** Statistics 110 (Harvard) — Prof. Joe Blitzstein

---

## 1) Quick recap: variance of the Hypergeometric

Let

$$
X\sim \mathrm{HGeom}(w,b,n),
\qquad
N=w+b,
\qquad
p=\frac{w}{w+b}.
$$

Write $X$ as a sum of indicators:

$$
X=X_1+\cdots+X_n,
$$

where $X_j=1$ if the $j$th sampled ball is white and $0$ otherwise.

From the variance-of-sums formula,

$$
\mathrm{Var}\left(\sum_{j=1}^{n}X_j\right)
=
\sum_{j=1}^{n}\mathrm{Var}(X_j)
+
2\sum_{i<j}\mathrm{Cov}(X_i,X_j).
$$

By symmetry,

$$
\mathrm{Var}(X)
=
n\,\mathrm{Var}(X_1)
+
2\binom{n}{2}\mathrm{Cov}(X_1,X_2).
$$

Now

$$
\mathrm{Var}(X_1)=p(1-p),
$$

and

$$
\begin{aligned}
\mathrm{Cov}(X_1,X_2)
&=
\mathbb{E}[X_1X_2]-\mathbb{E}[X_1]\mathbb{E}[X_2] \\
&=
\frac{w}{w+b}\cdot \frac{w-1}{w+b-1}
-
p^2.
\end{aligned}
$$

Therefore,

$$
\begin{aligned}
\mathrm{Var}(X)
&=
n p(1-p)
+
2\binom{n}{2}
\left(
\frac{w}{w+b}\cdot \frac{w-1}{w+b-1}
-
p^2
\right) \\
&=
\boxed{
\frac{N-n}{N-1}\,n p(1-p).
}
\end{aligned}
$$

The factor

$$
\boxed{\frac{N-n}{N-1}}
$$

is the **finite population correction**. It measures the variance reduction from sampling without replacement.

Sanity checks:

- If $n=1$, then the correction is $1$, so the variance is just the Bernoulli variance $p(1-p)$.
- If $N$ is much larger than $n$, then the correction is close to $1$, so the Hypergeometric variance is close to the Binomial variance $np(1-p)$.

---

## 2) Reminder: covariance formula

For two random variables $X_1,X_2$,

$$
\boxed{
\mathrm{Cov}(X_1,X_2)
=
\mathbb{E}[X_1X_2]
-
\mathbb{E}[X_1]\mathbb{E}[X_2].
}
$$

This is the expanded form of

$$
\mathrm{Cov}(X_1,X_2)
=
\mathbb{E}\!\left[
(X_1-\mathbb{E}[X_1])(X_2-\mathbb{E}[X_2])
\right].
$$

---

## 3) Transformations of one continuous random variable

Let $X$ be a continuous random variable with PDF $f_X$, and let

$$
Y=g(X),
$$

where $g$ is differentiable and one-to-one. If $x=g^{-1}(y)$, then the PDF of $Y$ is

$$
\boxed{
f_Y(y)
=
f_X(x)\left|\frac{dx}{dy}\right|
=
f_X(g^{-1}(y))
\left|
\frac{d}{dy}g^{-1}(y)
\right|.
}
$$

The absolute value is needed because densities must be nonnegative. If $g$ is strictly increasing, then $dx/dy>0$, so the absolute value does not change the result.

Also,

$$
\frac{dx}{dy}
=
\left(\frac{dy}{dx}\right)^{-1},
$$

when the derivative is nonzero.

### CDF proof for the increasing case

Assume $g$ is strictly increasing. Then

$$
\begin{aligned}
F_Y(y)
&=
\mathbb{P}(Y\le y) \\
&=
\mathbb{P}(g(X)\le y) \\
&=
\mathbb{P}(X\le g^{-1}(y)) \\
&=
F_X(g^{-1}(y)).
\end{aligned}
$$

Let $x=g^{-1}(y)$. Differentiate with respect to $y$:

$$
f_Y(y)
=
f_X(x)\frac{dx}{dy}.
$$

For decreasing transformations, the inequality reverses in the CDF step, and the final PDF formula uses the absolute value.

---

## 4) Example: LogNormal distribution

Let

$$
Z\sim N(0,1),
\qquad
Y=e^Z.
$$

Then $Y$ is **LogNormal**. Since

$$
z=\log y,
\qquad
\frac{dz}{dy}=\frac{1}{y},
$$

we get, for $y>0$,

$$
\begin{aligned}
f_Y(y)
&=
f_Z(\log y)\left|\frac{dz}{dy}\right| \\
&=
\frac{1}{\sqrt{2\pi}}
\exp\left(-\frac{(\log y)^2}{2}\right)
\cdot \frac{1}{y}.
\end{aligned}
$$

So

$$
\boxed{
f_Y(y)
=
\frac{1}{y\sqrt{2\pi}}
\exp\left(-\frac{(\log y)^2}{2}\right),
\qquad y>0.
}
$$

For $y\le 0$, $f_Y(y)=0$.

---

## 5) Transformations in $\mathbb{R}^n$

Let

$$
\vec{Y}=g(\vec{X}),
\qquad
g:\mathbb{R}^n\to\mathbb{R}^n,
$$

where $g$ is invertible and differentiable. Write

$$
\vec{x}=g^{-1}(\vec{y}).
$$

Then the joint PDF of $\vec{Y}$ is

$$
\boxed{
f_{\vec{Y}}(\vec{y})
=
f_{\vec{X}}(\vec{x})
\left|
\det\left(\frac{\partial \vec{x}}{\partial \vec{y}}\right)
\right|.
}
$$

The matrix

$$
\frac{\partial \vec{x}}{\partial \vec{y}}
=
\begin{pmatrix}
\frac{\partial x_1}{\partial y_1} & \frac{\partial x_1}{\partial y_2} & \cdots & \frac{\partial x_1}{\partial y_n} \\
\frac{\partial x_2}{\partial y_1} & \frac{\partial x_2}{\partial y_2} & \cdots & \frac{\partial x_2}{\partial y_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial x_n}{\partial y_1} & \frac{\partial x_n}{\partial y_2} & \cdots & \frac{\partial x_n}{\partial y_n}
\end{pmatrix}
$$

is the Jacobian matrix of the inverse transformation. The PDF uses the absolute value of its determinant.

Equivalently, if the easier Jacobian is $\partial \vec{y}/\partial \vec{x}$, then

$$
\left|
\det\left(\frac{\partial \vec{x}}{\partial \vec{y}}\right)
\right|
=
\frac{1}{
\left|
\det\left(\frac{\partial \vec{y}}{\partial \vec{x}}\right)
\right|
}.
$$

---

## 6) Convolution: distribution of a sum

Let

$$
T=X+Y,
$$

where $X$ and $Y$ are independent.

### Discrete case

If $X,Y$ are discrete, then the PMF of $T$ is

$$
\boxed{
\mathbb{P}(T=t)
=
\sum_x \mathbb{P}(X=x)\mathbb{P}(Y=t-x).
}
$$

This is the discrete convolution formula.

### Continuous case

If $X,Y$ are continuous, then the PDF of $T$ is

$$
\boxed{
f_T(t)
=
\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx.
}
$$

This is the continuous convolution formula.

One way to derive it is to start with the CDF:

$$
\begin{aligned}
F_T(t)
&=
\mathbb{P}(T\le t) \\
&=
\int_{-\infty}^{\infty}
\mathbb{P}(X+Y\le t\mid X=x) f_X(x)\,dx \\
&=
\int_{-\infty}^{\infty}
\mathbb{P}(Y\le t-x) f_X(x)\,dx \\
&=
\int_{-\infty}^{\infty}
F_Y(t-x) f_X(x)\,dx.
\end{aligned}
$$

Differentiate both sides with respect to $t$:

$$
f_T(t)
=
\int_{-\infty}^{\infty}
f_Y(t-x)f_X(x)\,dx.
$$

---

## 7) The probabilistic method

The probabilistic method is a way to prove that an object with a desired property exists, even if we do not explicitly construct it.

Two common strategies:

1. Define a random object and show that the probability of the desired event $A$ is positive:

$$
\mathbb{P}(A)>0.
$$

Then at least one object with property $A$ must exist.

2. Define a score $S$ on objects and compute its expectation. At least one object has score at least the average:

$$
\text{some object has score } \ge \mathbb{E}[S].
$$

Otherwise all scores would be below the average, which is impossible.

This idea is useful in information theory, including Shannon-style existence arguments.

---

## 8) Example: committee overlaps

Suppose there are:

- 100 people,
- 15 committees,
- 20 people on each committee,
- each person is on 3 committees.

Show that there exist two committees with overlap at least 3.

Choose two distinct committees uniformly at random. Let $S$ be their overlap size.

For person $j$, define the indicator

$$
I_j=
\begin{cases}
1, & \text{if person }j\text{ is on both chosen committees},\\
0, & \text{otherwise.}
\end{cases}
$$

Then

$$
S=I_1+\cdots+I_{100}.
$$

For any fixed person, the person belongs to 3 committees, so the number of committee pairs containing that person is $\binom{3}{2}$. The total number of committee pairs is $\binom{15}{2}$. Therefore,

$$
\mathbb{P}(I_j=1)
=
\frac{\binom{3}{2}}{\binom{15}{2}}.
$$

By linearity of expectation,

$$
\begin{aligned}
\mathbb{E}[S]
&=
\sum_{j=1}^{100}\mathbb{E}[I_j] \\
&=
100\cdot \frac{\binom{3}{2}}{\binom{15}{2}} \\
&=
100\cdot \frac{3}{105} \\
&=
\frac{20}{7}.
\end{aligned}
$$

So the average overlap of two committees is $20/7$. Therefore, at least one pair of committees has overlap at least $20/7$.

Since overlap size is an integer,

$$
\boxed{
\text{there exist two committees with overlap at least }3.
}
$$

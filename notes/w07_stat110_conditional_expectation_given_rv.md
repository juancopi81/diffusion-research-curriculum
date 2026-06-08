# Stat 110 (Blitzstein) - Lecture 27

**Lecture 27:** [Conditional Expectation Given an R.V.](https://www.youtube.com/watch?v=gjBvCiRt8QA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=27)

**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** Transcribed from user-provided notebook photos. Notation is cleaned up where the surrounding derivation is clear; this is not labeled as an official solution.

---

## 1) Conditional Expectation as a Random Variable

The object

$$
\mathbb{E}(Y \mid X)
$$

is itself a random variable. More precisely, it is a function of $X$.

### Example: $Y=X^2$

Let

$$
X\sim N(0,1),
\qquad
Y=X^2.
$$

Then

$$
\mathbb{E}(Y \mid X)
=
\mathbb{E}(X^2 \mid X)
=
X^2
=
Y.
$$

But if we condition in the other direction, then observing $Y=X^2$ only tells us the magnitude of $X$, not its sign. By symmetry, if $Y=a$, then $X=\sqrt{a}$ and $X=-\sqrt{a}$ are equally likely.

So

$$
\mathbb{E}(X \mid Y)
=
\mathbb{E}(X \mid X^2)
=
0.
$$

The key point is that conditional expectation depends on what information is being observed.

---

## 2) Stick-Breaking Example

Start with a stick of length $1$.

1. Break off a random piece with length $X$.
2. From that piece, break off another random piece with length $Y$.

Model this as

$$
X\sim \mathrm{Unif}(0,1),
\qquad
Y \mid X=x \sim \mathrm{Unif}(0,x).
$$

Given $X=x$, the average value of $Y$ is the midpoint of $[0,x]$:

$$
\mathbb{E}(Y \mid X=x)=\frac{x}{2}.
$$

Therefore,

$$
\mathbb{E}(Y \mid X)=\frac{X}{2}.
$$

Taking expectation again gives

$$
\mathbb{E}\!\left(\mathbb{E}(Y \mid X)\right)
=
\mathbb{E}\!\left(\frac{X}{2}\right)
=
\frac{1}{4}
=
\mathbb{E}(Y).
$$

This is the tower property in a concrete example.

---

## 3) Core Properties

### 1. Taking Out What Is Known

If $h(X)$ is a function of the information being conditioned on, then it can be pulled out:

$$
\boxed{
\mathbb{E}(h(X)Y \mid X)
=
h(X)\mathbb{E}(Y \mid X).
}
$$

Given $X$, the value $h(X)$ is already known.

### 2. Independence

If $X$ and $Y$ are independent, then conditioning on $X$ does not change the expectation of $Y$:

$$
\boxed{
\mathbb{E}(Y \mid X)=\mathbb{E}(Y).
}
$$

### 3. Adam's Law

The iterated expectation law says

$$
\boxed{
\mathbb{E}\!\left(\mathbb{E}(Y \mid X)\right)
=
\mathbb{E}(Y).
}
$$

This is also called Adam's law.

### 4. Orthogonality of the Residual

For any function $h(X)$,

$$
\boxed{
\mathbb{E}\!\left[
\left(Y-\mathbb{E}(Y \mid X)\right)h(X)
\right]
=
0.
}
$$

In words, the residual

$$
Y-\mathbb{E}(Y \mid X)
$$

is uncorrelated with every function of $X$.

Equivalently, conditional expectation acts like a projection: $\mathbb{E}(Y \mid X)$ is the best $X$-measurable summary of $Y$, and the leftover residual is orthogonal to all functions of $X$.

Since

$$
\mathbb{E}\!\left[Y-\mathbb{E}(Y \mid X)\right]=0,
$$

the covariance with any $h(X)$ is

$$
\mathrm{Cov}\!\left(Y-\mathbb{E}(Y \mid X), h(X)\right)
=
\mathbb{E}\!\left[
\left(Y-\mathbb{E}(Y \mid X)\right)h(X)
\right]
-
0\cdot \mathbb{E}(h(X))
=
0.
$$

---

## 4) Proof of the Orthogonality Property

Start from

$$
\mathbb{E}\!\left[
\left(Y-\mathbb{E}(Y \mid X)\right)h(X)
\right].
$$

Expand:

$$
\mathbb{E}(Yh(X))
-
\mathbb{E}(\mathbb{E}(Y \mid X)h(X)).
$$

Using the "taking out what is known" property,

$$
\mathbb{E}(Y \mid X)h(X)
=
\mathbb{E}(Yh(X) \mid X).
$$

Therefore,

$$
\begin{aligned}
\mathbb{E}\!\left[
\left(Y-\mathbb{E}(Y \mid X)\right)h(X)
\right]
&=
\mathbb{E}(Yh(X))
-
\mathbb{E}\!\left(\mathbb{E}(Yh(X) \mid X)\right) \\
&=
\mathbb{E}(Yh(X))
-
\mathbb{E}(Yh(X)) \\
&=
0.
\end{aligned}
$$

---

## 5) Proof of Adam's Law in the Discrete Case

Let

$$
g(X)=\mathbb{E}(Y \mid X).
$$

Then

$$
\begin{aligned}
\mathbb{E}(g(X))
&=
\sum_x g(x)\mathbb{P}(X=x) \\
&=
\sum_x \mathbb{E}(Y \mid X=x)\mathbb{P}(X=x) \\
&=
\sum_x
\left(
\sum_y y\,\mathbb{P}(Y=y \mid X=x)
\right)
\mathbb{P}(X=x) \\
&=
\sum_x\sum_y
y\,\mathbb{P}(Y=y, X=x) \\
&=
\sum_y
y
\sum_x\mathbb{P}(Y=y, X=x) \\
&=
\sum_y y\,\mathbb{P}(Y=y) \\
&=
\mathbb{E}(Y).
\end{aligned}
$$

The middle step uses the joint PMF identity

$$
\mathbb{P}(Y=y \mid X=x)\mathbb{P}(X=x)
=
\mathbb{P}(Y=y, X=x).
$$

---

## 6) Conditional Variance and Eve's Law

Define conditional variance by

$$
\boxed{
\mathrm{Var}(Y \mid X)
=
\mathbb{E}(Y^2 \mid X)
-
\left[\mathbb{E}(Y \mid X)\right]^2.
}
$$

Equivalently,

$$
\mathrm{Var}(Y \mid X)
=
\mathbb{E}\!\left[
\left(Y-\mathbb{E}(Y \mid X)\right)^2
\mid X
\right].
$$

Eve's law, or the law of total variance, is

$$
\boxed{
\mathrm{Var}(Y)
=
\mathbb{E}(\mathrm{Var}(Y \mid X))
+
\mathrm{Var}(\mathbb{E}(Y \mid X)).
}
$$

Interpretation:

- $\mathbb{E}(\mathrm{Var}(Y \mid X))$ is the average within-group variance.
- $\mathrm{Var}(\mathbb{E}(Y \mid X))$ is the between-group variance.

---

## 7) Beta-Binomial Example

Pick a random city, then pick a random sample of $n$ people in that city.

Let

$$
X=\text{number of sampled people with the disease},
$$

and let

$$
Q=\text{proportion of people in the random city with the disease}.
$$

Assume

$$
Q\sim \mathrm{Beta}(a,b),
\qquad
X \mid Q=q \sim \mathrm{Bin}(n,q).
$$

We want $\mathbb{E}(X)$ and $\mathrm{Var}(X)$.

Given $Q=q$,

$$
\mathbb{E}(X \mid Q=q)=nq,
\qquad
\mathrm{Var}(X \mid Q=q)=nq(1-q).
$$

Therefore,

$$
\begin{aligned}
\mathbb{E}(X)
&=
\mathbb{E}\!\left(\mathbb{E}(X \mid Q)\right) \\
&=
\mathbb{E}(nQ) \\
&=
n\mathbb{E}(Q) \\
&=
\boxed{\frac{na}{a+b}}.
\end{aligned}
$$

For the variance, apply Eve's law:

$$
\begin{aligned}
\mathrm{Var}(X)
&=
\mathbb{E}(\mathrm{Var}(X \mid Q))
+
\mathrm{Var}(\mathbb{E}(X \mid Q)) \\
&=
n\mathbb{E}(Q(1-Q))
+
n^2\mathrm{Var}(Q).
\end{aligned}
$$

For $Q\sim \mathrm{Beta}(a,b)$,

$$
\begin{aligned}
\mathbb{E}(Q(1-Q))
&=
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}
\int_0^1 q^a(1-q)^b\,dq \\
&=
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}
\cdot
\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+2)} \\
&=
\frac{ab}{(a+b)(a+b+1)}.
\end{aligned}
$$

Also,

$$
\mathrm{Var}(Q)
=
\frac{\mu(1-\mu)}{a+b+1},
\qquad
\mu=\frac{a}{a+b},
$$

so

$$
\mathrm{Var}(Q)
=
\frac{ab}{(a+b)^2(a+b+1)}.
$$

Thus

$$
\boxed{
\mathrm{Var}(X)
=
\frac{nab}{(a+b)(a+b+1)}
+
\frac{n^2ab}{(a+b)^2(a+b+1)}.
}
$$

Equivalently,

$$
\boxed{
\mathrm{Var}(X)
=
\frac{nab(a+b+n)}{(a+b)^2(a+b+1)}.
}
$$

The first term is the average binomial variance within a city. The second term is the extra variance from city-to-city variation in the disease rate $Q$.

---

## Main Takeaways

- $\mathbb{E}(Y \mid X)$ is a function of $X$, not a fixed number.
- Adam's law: $\mathbb{E}(\mathbb{E}(Y \mid X))=\mathbb{E}(Y)$.
- The residual $Y-\mathbb{E}(Y \mid X)$ is orthogonal to every function of $X$.
- Eve's law decomposes total variance into average conditional variance plus variance of conditional means.
- The beta-binomial example uses both laws: Adam's law for $\mathbb{E}(X)$ and Eve's law for $\mathrm{Var}(X)$.

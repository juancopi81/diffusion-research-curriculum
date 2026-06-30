# Stat 110 (Blitzstein) - Lecture 28

**Lecture 28:** [Inequalities](https://www.youtube.com/watch?v=UtXK_EQ3Pow&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=28)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** Transcribed from user-provided notebook photos. Notation is cleaned up and a few explanatory bridges are added where the surrounding derivation is clear; this is not labeled as an official solution.

---

## 1) Conditional Expectation Review: Random Customer Total

Suppose a store has a random number of customers. Let

$$
N=\text{number of customers},
$$

and let $X_j$ be the amount spent by the $j$th customer.

Assume

$$
\mathbb{E}(X_j)=\mu,
\qquad
\mathrm{Var}(X_j)=\sigma^2,
$$

and that $X_1,X_2,\dots$ are independent of each other and independent of $N$.

Let the total amount spent be

$$
X=\sum_{j=1}^{N}X_j.
$$

The goal is to find the mean and variance of $X$.

### Mean

A tempting but wrong shortcut is to write

$$
\mathbb{E}(X)=N\mu.
$$

This is a category error: $\mathbb{E}(X)$ is a number, while $N\mu$ is still a random variable.

Condition on the value of $N$:

$$
\begin{aligned}
\mathbb{E}(X)
&=
\sum_{n=0}^{\infty}\mathbb{E}(X\mid N=n)\mathbb{P}(N=n) \\
&=
\sum_{n=0}^{\infty} n\mu\,\mathbb{P}(N=n) \\
&=
\mu\sum_{n=0}^{\infty}n\mathbb{P}(N=n) \\
&=
\boxed{\mu\,\mathbb{E}(N).}
\end{aligned}
$$

Equivalently, by Adam's law,

$$
\mathbb{E}(X)
=
\mathbb{E}\!\left(\mathbb{E}(X\mid N)\right)
=
\mathbb{E}(\mu N)
=
\mu\mathbb{E}(N).
$$

### Variance

Use Eve's law:

$$
\mathrm{Var}(X)
=
\mathbb{E}(\mathrm{Var}(X\mid N))
+
\mathrm{Var}(\mathbb{E}(X\mid N)).
$$

Given $N=n$, the total is a sum of $n$ independent customer amounts, so

$$
\mathbb{E}(X\mid N=n)=n\mu,
\qquad
\mathrm{Var}(X\mid N=n)=n\sigma^2.
$$

Therefore,

$$
\begin{aligned}
\mathrm{Var}(X)
&=
\mathbb{E}(N\sigma^2)
+
\mathrm{Var}(\mu N) \\
&=
\boxed{\sigma^2\mathbb{E}(N)+\mu^2\mathrm{Var}(N).}
\end{aligned}
$$

Interpretation:

- $\sigma^2\mathbb{E}(N)$ is the average within-customer spending variance.
- $\mu^2\mathrm{Var}(N)$ is the extra variance from the random number of customers.

---

## 2) Cauchy-Schwarz Inequality

For random variables with finite second moments,

$$
\boxed{
\left|\mathbb{E}(XY)\right|
\le
\sqrt{\mathbb{E}(X^2)\mathbb{E}(Y^2)}.
}
$$

This is one of the main inequalities for controlling expectations of products.

If $X$ and $Y$ are uncorrelated, then

$$
\mathbb{E}(XY)=\mathbb{E}(X)\mathbb{E}(Y).
$$

In particular, if both have mean $0$, then uncorrelated means

$$
\mathbb{E}(XY)=0.
$$

For correlation, apply Cauchy-Schwarz to the centered variables

$$
X-\mathbb{E}(X),
\qquad
Y-\mathbb{E}(Y).
$$

Then

$$
\left|\mathrm{Cov}(X,Y)\right|
\le
\sqrt{\mathrm{Var}(X)\mathrm{Var}(Y)}.
$$

So, as long as both variances are positive,

$$
\boxed{
\left|\mathrm{Corr}(X,Y)\right|
=
\left|
\frac{\mathrm{Cov}(X,Y)}
{\sqrt{\mathrm{Var}(X)\mathrm{Var}(Y)}}
\right|
\le 1.
}
$$

In the mean-zero version from the notes,

$$
\left|
\frac{\mathbb{E}(XY)}
{\sqrt{\mathbb{E}(X^2)\mathbb{E}(Y^2)}}
\right|
\le 1.
$$

---

## 3) Jensen's Inequality

If $g$ is convex, then

$$
\boxed{
\mathbb{E}(g(X))\ge g(\mathbb{E}(X)).
}
$$

For example, $g(x)=x^2$ is convex because

$$
g''(x)=2\ge 0.
$$

So Jensen gives

$$
\boxed{\mathbb{E}(X^2)\ge (\mathbb{E}(X))^2.}
$$

If $h$ is concave, the inequality reverses:

$$
\boxed{
\mathbb{E}(h(X))\le h(\mathbb{E}(X)).
}
$$

For $X>0$, this gives two useful examples:

$$
\mathbb{E}\!\left(\frac{1}{X}\right)
\ge
\frac{1}{\mathbb{E}(X)}
$$

because $1/x$ is convex on $x>0$, and

$$
\mathbb{E}(\log X)
\le
\log \mathbb{E}(X)
$$

because $\log x$ is concave on $x>0$.

### Proof Idea

For a convex function, every tangent line lies below the curve.

Let

$$
\mu=\mathbb{E}(X).
$$

Take the tangent line to $g$ at $\mu$:

$$
y=a+bx.
$$

Since the tangent line is below the convex curve,

$$
g(x)\ge a+bx
$$

for all $x$. Therefore,

$$
g(X)\ge a+bX.
$$

Taking expectations,

$$
\begin{aligned}
\mathbb{E}(g(X))
&\ge
\mathbb{E}(a+bX) \\
&=
a+b\mathbb{E}(X) \\
&=
a+b\mu \\
&=
g(\mu) \\
&=
g(\mathbb{E}(X)).
\end{aligned}
$$

That proves Jensen's inequality for convex $g$.

---

## 4) Markov's Inequality

For a nonnegative random variable $X$ and any $a>0$,

$$
\boxed{
\mathbb{P}(X\ge a)\le \frac{\mathbb{E}(X)}{a}.
}
$$

Applying this to $|X|$ gives the version in the notes:

$$
\boxed{
\mathbb{P}(|X|\ge a)\le \frac{\mathbb{E}(|X|)}{a}.
}
$$

### Indicator Bridge Proof

The key observation is

$$
aI_{\{|X|\ge a\}}\le |X|.
$$

If $|X|\ge a$, then the left side is $a$, which is at most $|X|$. If $|X|<a$, then the left side is $0$.

Taking expectations,

$$
\begin{aligned}
a\mathbb{P}(|X|\ge a)
&=
a\mathbb{E}(I_{\{|X|\ge a\}}) \\
&=
\mathbb{E}\!\left(aI_{\{|X|\ge a\}}\right) \\
&\le
\mathbb{E}(|X|).
\end{aligned}
$$

Divide by $a$:

$$
\mathbb{P}(|X|\ge a)
\le
\frac{\mathbb{E}(|X|)}{a}.
$$

### Age Example

Suppose there are $100$ people in a group.

It is possible that at least $95\%$ of them are younger than the average age. For example, one very old person can pull the average upward.

But it is not possible that at least $95\%$ of them are older than twice the average age.

Let $X$ be the age of a randomly chosen person from the group. Since ages are nonnegative, Markov gives

$$
\mathbb{P}(X\ge 2\mathbb{E}(X))
\le
\frac{\mathbb{E}(X)}{2\mathbb{E}(X)}
=
\frac{1}{2}.
$$

So at most $50\%$ of the group can have age at least twice the average.

---

## 5) Chebyshev's Inequality

Let

$$
\mu=\mathbb{E}(X).
$$

For any $a>0$,

$$
\boxed{
\mathbb{P}(|X-\mu|\ge a)
\le
\frac{\mathrm{Var}(X)}{a^2}.
}
$$

This is Markov's inequality applied to the nonnegative random variable

$$
(X-\mu)^2.
$$

Indeed,

$$
\begin{aligned}
\mathbb{P}(|X-\mu|\ge a)
&=
\mathbb{P}((X-\mu)^2\ge a^2) \\
&\le
\frac{\mathbb{E}((X-\mu)^2)}{a^2} \\
&=
\boxed{\frac{\mathrm{Var}(X)}{a^2}.}
\end{aligned}
$$

In standard-deviation units, if $c>0$ and $\mathrm{SD}(X)>0$, then

$$
\boxed{
\mathbb{P}(|X-\mu|\ge c\,\mathrm{SD}(X))
\le
\frac{1}{c^2}.
}
$$

This is distribution-free: it does not assume normality.

---

## 6) Why These Inequalities Matter

These inequalities are general tools for controlling random variables when the full distribution is unknown or inconvenient.

- Cauchy-Schwarz controls expectations of products and proves $|\mathrm{Corr}(X,Y)|\le 1$.
- Jensen controls the direction of expectation through nonlinear functions.
- Markov turns an expected size into a tail bound.
- Chebyshev turns mean and variance into a two-sided concentration bound.

Chebyshev is especially important for the next topic, the law of large numbers. If $X_1,\dots,X_n$ are independent with mean $\mu$ and variance $\sigma^2$, then

$$
\bar X_n=\frac{1}{n}\sum_{j=1}^{n}X_j
$$

has

$$
\mathbb{E}(\bar X_n)=\mu,
\qquad
\mathrm{Var}(\bar X_n)=\frac{\sigma^2}{n}.
$$

So Chebyshev gives

$$
\mathbb{P}(|\bar X_n-\mu|\ge \epsilon)
\le
\frac{\sigma^2}{n\epsilon^2}.
$$

As $n$ grows, this bound goes to $0$, which is the core shape of the weak law of large numbers.

---

## Main Takeaways

- Random sums should be handled by conditioning on the random count $N$.
- $\mathbb{E}(X)=\mu\mathbb{E}(N)$ for the random customer total, not $N\mu$.
- $\mathrm{Var}(X)=\sigma^2\mathbb{E}(N)+\mu^2\mathrm{Var}(N)$ separates spending variability from customer-count variability.
- Cauchy-Schwarz, Jensen, Markov, and Chebyshev are reusable inequalities that turn limited information into useful bounds.
- Chebyshev is the bridge from variance calculations to LLN-style concentration.

# Week 8 — S2 Warm-up: Inequalities, LLN/CLT, and Multivariate Normal

**Sources:**

- `/Users/juanpineros/Downloads/strategic_practice_and_homework_10.pdf`
- `/Users/juanpineros/Downloads/strategic_practice_and_homework_11.pdf`

---

## Strategic Practice 10 — Inequalities Problem 3

**Prompt.**
For i.i.d. r.v.s $X_1,\ldots,X_n$ with mean $\mu$ and variance $\sigma^2$, give a value of $n$ (as a specific number) that will ensure that there is at least a $99\%$ chance that the sample mean will be within $2$ standard deviations of the true mean $\mu$.

### My solution

Let

$$
\bar X_n=\frac{1}{n}\sum_{j=1}^n X_j.
$$

Since the $X_j$ are i.i.d. with variance $\sigma^2$,

$$
\begin{aligned}
\operatorname{Var}(\bar X_n)
&=\operatorname{Var}\left(\frac{1}{n}\sum_{j=1}^n X_j\right)\\
&=\frac{1}{n^2}\sum_{j=1}^n \operatorname{Var}(X_j)\\
&=\frac{1}{n^2}n\sigma^2\\
&=\frac{\sigma^2}{n}.
\end{aligned}
$$

Therefore,

$$
\operatorname{SD}(\bar X_n)=\frac{\sigma}{\sqrt n}.
$$

The problem asks for the sample mean to be within $2$ standard deviations of the true mean $\mu$. Here the standard deviation is the population standard deviation $\sigma$, so the target event is

$$
|\bar X_n-\mu|<2\sigma.
$$

By Chebyshev's inequality,

$$
P(|\bar X_n-\mu|\ge 2\sigma)
\le
\frac{\operatorname{Var}(\bar X_n)}{(2\sigma)^2}.
$$

Substituting $\operatorname{Var}(\bar X_n)=\sigma^2/n$,

$$
\begin{aligned}
P(|\bar X_n-\mu|\ge 2\sigma)
&\le
\frac{\sigma^2/n}{4\sigma^2}\\
&=\frac{1}{4n}.
\end{aligned}
$$

We want the outside probability to be at most $0.01$, so

$$
\frac{1}{4n}\le 0.01.
$$

Equivalently,

$$
4n\ge 100,
$$

so

$$
n\ge 25.
$$

Thus a specific value that works is

$$
\boxed{n=25.}
$$

### What I initially missed / corrected

The confusing point was the phrase "within $2$ standard deviations of the true mean." In this problem, that means within $2\sigma$, where $\sigma$ is the population standard deviation of each $X_j$.

It does not mean within $2$ standard errors of the sample mean. The standard error of $\bar X_n$ is

$$
\frac{\sigma}{\sqrt n}.
$$

So $2\sigma$ is equal to $2\sqrt n$ standard errors:

$$
2\sigma
=2\sqrt n\left(\frac{\sigma}{\sqrt n}\right).
$$

The event stays

$$
|\bar X_n-\mu|\ge 2\sigma.
$$

The $n$ enters through

$$
\operatorname{Var}(\bar X_n)=\frac{\sigma^2}{n},
$$

not by changing the event to use $2\sigma/\sqrt n$.

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

The book sets up the required probability as

$$
P(|\bar X_n-\mu|>2\sigma)\le 0.01.
$$

Then it applies Chebyshev's inequality to $Y=\bar X_n$ with $c=2\sigma$:

$$
P(|\bar X_n-\mu|>2\sigma)
\le
\frac{\operatorname{Var}(\bar X_n)}{(2\sigma)^2}.
$$

Since

$$
\operatorname{Var}(\bar X_n)=\frac{\sigma^2}{n},
$$

we get

$$
\frac{\operatorname{Var}(\bar X_n)}{(2\sigma)^2}
=
\frac{\sigma^2/n}{4\sigma^2}
=
\frac{1}{4n}.
$$

Therefore the desired inequality holds if

$$
\frac{1}{4n}\le 0.01,
$$

which gives

$$
\boxed{n\ge 25.}
$$

### Intuition

Averaging reduces variance. Each individual $X_j$ has standard deviation $\sigma$, but the sample mean has standard deviation

$$
\frac{\sigma}{\sqrt n}.
$$

The problem asks whether $\bar X_n$ lands within a fixed population-scale window around $\mu$, namely $2\sigma$. As $n$ grows, the sample mean gets more concentrated, so that fixed window becomes easier to hit.

Chebyshev gives a conservative guarantee:

$$
P(|\bar X_n-\mu|\ge 2\sigma)\le \frac{1}{4n}.
$$

To make the failure probability at most $1\%$, we need $n\ge 25$.

### Memory card (quick review)

- Population SD of each observation: $\sigma$.
- Standard error of the sample mean: $\sigma/\sqrt n$.
- The event in this problem is population-scale:

  $$
  |\bar X_n-\mu|\ge 2\sigma.
  $$

- Chebyshev applied to $\bar X_n$ gives:

  $$
  P(|\bar X_n-\mu|\ge 2\sigma)
  \le
  \frac{\sigma^2/n}{4\sigma^2}
  =
  \frac{1}{4n}.
  $$

- To get at least $99\%$ inside the window, require:

  $$
  \frac{1}{4n}\le 0.01,
  \qquad n\ge 25.
  $$

---

## Strategic Practice 11 — Law of Large Numbers / Central Limit Theorem Problem 5

**Prompt.**
Let $f$ be a complicated function whose integral $\int_a^b f(x)\,dx$ we want to approximate. Assume that $0\le f(x)\le c$. Let $A$ be the rectangle in the $(x,y)$-plane given by $a\le x\le b$ and $0\le y\le c$. Pick i.i.d. uniform points $(X_1,Y_1),(X_2,Y_2),\ldots,(X_n,Y_n)$ in the rectangle $A$.

How would you use these random points to approximate the integral? This is an example of a Monte Carlo method. Show that the estimate converges to the true value of the integral as $n\to\infty$.

Hint: look at whether each point is in the area below the curve $y=f(x)$.

---

## Strategic Practice 11 — Multivariate Normal Problem 3

**Prompt.**
Let $(X,Y)$ be Bivariate Normal, with $X,Y\sim \mathcal{N}(0,1)$ marginally and correlation $\rho$, where $-1<\rho<1$. Find $a,b,c,d$ in terms of $\rho$ such that

$$
Z=aX+bY
$$

and

$$
W=cX+dY
$$

are independent $\mathcal{N}(0,1)$ random variables.

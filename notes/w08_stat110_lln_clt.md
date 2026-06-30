# Stat 110 (Blitzstein) - Lecture 29

**Lecture 29:** [Law of Large Numbers and Central Limit Theorem](https://www.youtube.com/watch?v=OprNqnHsVIA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=29)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** Transcribed from user-provided notebook photos. Notation is cleaned up and a few explanatory bridges are added where the surrounding derivation is clear; this is not labeled as an official solution.

---

## 1) Setup: Sample Mean

Let

$$
X_1,X_2,\dots
$$

be i.i.d. random variables with

$$
\mathbb{E}(X_j)=\mu,
\qquad
\mathrm{Var}(X_j)=\sigma^2.
$$

The sample mean is

$$
\bar X_n
=
\frac{1}{n}\sum_{j=1}^{n}X_j.
$$

The law of large numbers says that the sample mean gets close to the true mean $\mu$ as $n$ becomes large.

---

## 2) Strong Law of Large Numbers

The strong law of large numbers says

$$
\boxed{
\bar X_n \to \mu
\quad
\text{as } n\to\infty
\text{ with probability }1.
}
$$

In words: the sample mean converges to the true mean almost surely.

### Bernoulli Example

If

$$
X_j\sim \mathrm{Bern}(p),
$$

then

$$
\bar X_n
=
\frac{X_1+\cdots+X_n}{n}
$$

is the sample proportion of successes. Since $\mathbb{E}(X_j)=p$, the strong law gives

$$
\boxed{
\frac{X_1+\cdots+X_n}{n}
\to p
\quad
\text{with probability }1.
}
$$

So the empirical frequency of success converges to the true success probability.

---

## 3) Weak Law of Large Numbers

The weak law says that for any fixed $c>0$,

$$
\boxed{
\mathbb{P}(|\bar X_n-\mu|>c)\to 0
\quad
\text{as }n\to\infty.
}
$$

This is convergence in probability. It says that the probability of being more than $c$ away from the true mean goes to zero.

### Proof Using Chebyshev

First compute the variance of the sample mean. Since the $X_j$ are independent,

$$
\mathrm{Var}(\bar X_n)
=
\mathrm{Var}\!\left(
\frac{1}{n}\sum_{j=1}^{n}X_j
\right)
=
\frac{1}{n^2}\sum_{j=1}^{n}\mathrm{Var}(X_j)
=
\frac{1}{n^2}n\sigma^2
=
\frac{\sigma^2}{n}.
$$

By Chebyshev's inequality,

$$
\begin{aligned}
\mathbb{P}(|\bar X_n-\mu|>c)
&\le
\frac{\mathrm{Var}(\bar X_n)}{c^2} \\
&=
\frac{\sigma^2}{nc^2}.
\end{aligned}
$$

As $n\to\infty$,

$$
\frac{\sigma^2}{nc^2}\to 0.
$$

Therefore,

$$
\boxed{
\mathbb{P}(|\bar X_n-\mu|>c)\to 0.
}
$$

This proves the weak law under the finite-variance assumption.

---

## 4) From LLN to CLT

The law of large numbers says

$$
\bar X_n-\mu\to 0.
$$

But it does not describe the shape of the distribution around $\mu$.

The central limit theorem answers the next question:

> What does the distribution of the error $\bar X_n-\mu$ look like after the right rescaling?

Since

$$
\mathrm{Var}(\bar X_n)=\frac{\sigma^2}{n},
$$

the typical size of $\bar X_n-\mu$ is about $\sigma/\sqrt n$. So the right standardized quantity is

$$
\frac{\sqrt n(\bar X_n-\mu)}{\sigma}.
$$

---

## 5) Central Limit Theorem

If $X_1,X_2,\dots$ are i.i.d. with mean $\mu$ and variance $\sigma^2>0$, then

$$
\boxed{
\frac{\sqrt n(\bar X_n-\mu)}{\sigma}
\to N(0,1)
\quad
\text{in distribution.}
}
$$

Equivalently,

$$
\boxed{
\frac{\sum_{j=1}^{n}X_j-n\mu}{\sqrt n\,\sigma}
\to N(0,1)
\quad
\text{in distribution.}
}
$$

The LLN says the sample mean gets close to $\mu$. The CLT says the fluctuations around $\mu$, after multiplying by $\sqrt n$, look approximately normal.

---

## 6) MGF Proof Sketch of the CLT

This proof assumes the moment generating function of $X_j$ exists in a neighborhood of $0$. That assumption is stronger than the CLT needs, but it gives a clean proof.

By standardizing each variable, we may assume

$$
\mu=0,
\qquad
\sigma=1.
$$

Indeed, the general case is handled by applying the proof to

$$
\frac{X_j-\mu}{\sigma}.
$$

Let

$$
S_n=\sum_{j=1}^{n}X_j,
$$

where now each $X_j$ has mean $0$ and variance $1$. We want to show

$$
\frac{S_n}{\sqrt n}
\to N(0,1)
\quad
\text{in distribution.}
$$

It is enough, in this MGF proof, to show that the MGF of $S_n/\sqrt n$ converges to the MGF of $N(0,1)$:

$$
e^{t^2/2}.
$$

Let

$$
M(t)=\mathbb{E}(e^{tX_1})
$$

be the common MGF of the $X_j$.

Using independence,

$$
\begin{aligned}
\mathbb{E}\!\left(e^{tS_n/\sqrt n}\right)
&=
\mathbb{E}\!\left(e^{t(X_1+\cdots+X_n)/\sqrt n}\right) \\
&=
\mathbb{E}\!\left(e^{tX_1/\sqrt n}\cdots e^{tX_n/\sqrt n}\right) \\
&=
\prod_{j=1}^{n}\mathbb{E}\!\left(e^{tX_j/\sqrt n}\right) \\
&=
\left(M\!\left(\frac{t}{\sqrt n}\right)\right)^n.
\end{aligned}
$$

Take logs:

$$
\log \mathbb{E}\!\left(e^{tS_n/\sqrt n}\right)
=
n\log M\!\left(\frac{t}{\sqrt n}\right).
$$

Let

$$
y=\frac{1}{\sqrt n}.
$$

Then $n=1/y^2$, and as $n\to\infty$, $y\to 0$. So

$$
n\log M\!\left(\frac{t}{\sqrt n}\right)
=
\frac{\log M(yt)}{y^2}.
$$

Now use the facts

$$
M(0)=1,
\qquad
M'(0)=\mathbb{E}(X_1)=0,
\qquad
M''(0)=\mathbb{E}(X_1^2)=1.
$$

Applying l'Hopital's rule twice,

$$
\begin{aligned}
\lim_{y\to 0}\frac{\log M(yt)}{y^2}
&=
\lim_{y\to 0}
\frac{tM'(yt)/M(yt)}{2y} \\
&=
\frac{t}{2}
\lim_{y\to 0}
\frac{M'(yt)}{yM(yt)} \\
&=
\frac{t}{2}
\lim_{y\to 0}
\frac{tM''(yt)}{M(yt)+ytM'(yt)} \\
&=
\frac{t}{2}
\cdot
\frac{tM''(0)}{M(0)} \\
&=
\frac{t^2}{2}.
\end{aligned}
$$

Therefore,

$$
\log \mathbb{E}\!\left(e^{tS_n/\sqrt n}\right)
\to
\frac{t^2}{2},
$$

so

$$
\mathbb{E}\!\left(e^{tS_n/\sqrt n}\right)
\to
e^{t^2/2}.
$$

This is the MGF of a standard normal random variable. Hence

$$
\frac{S_n}{\sqrt n}\to N(0,1)
\quad
\text{in distribution.}
$$

---

## 7) Normal Approximation to the Binomial

Let

$$
X\sim \mathrm{Bin}(n,p),
\qquad
q=1-p.
$$

Think of $X$ as a sum of independent Bernoulli variables:

$$
X=\sum_{j=1}^{n}X_j,
\qquad
X_j\sim \mathrm{Bern}(p).
$$

Then

$$
\mathbb{E}(X)=np,
\qquad
\mathrm{Var}(X)=npq.
$$

By the CLT,

$$
\frac{X-np}{\sqrt{npq}}
\approx
N(0,1)
$$

for large $n$.

Therefore,

$$
\begin{aligned}
\mathbb{P}(a\le X\le b)
&=
\mathbb{P}\!\left(
\frac{a-np}{\sqrt{npq}}
\le
\frac{X-np}{\sqrt{npq}}
\le
\frac{b-np}{\sqrt{npq}}
\right) \\
&\approx
\Phi\!\left(\frac{b-np}{\sqrt{npq}}\right)
-
\Phi\!\left(\frac{a-np}{\sqrt{npq}}\right),
\end{aligned}
$$

where $\Phi$ is the standard normal CDF.

### Continuity Correction

The binomial is discrete, while the normal approximation is continuous. For an integer $a$,

$$
\mathbb{P}(X=a)
$$

is approximated more accurately by assigning the integer value $a$ the interval around it:

$$
\mathbb{P}(X=a)
\approx
\mathbb{P}\!\left(a-\frac{1}{2}<Y<a+\frac{1}{2}\right),
$$

where

$$
Y\sim N(np,npq).
$$

Similarly,

$$
\mathbb{P}(a\le X\le b)
\approx
\mathbb{P}\!\left(a-\frac{1}{2}<Y<b+\frac{1}{2}\right).
$$

So the corrected normal approximation is

$$
\boxed{
\mathbb{P}(a\le X\le b)
\approx
\Phi\!\left(\frac{b+\frac{1}{2}-np}{\sqrt{npq}}\right)
-
\Phi\!\left(\frac{a-\frac{1}{2}-np}{\sqrt{npq}}\right).
}
$$

---

## 8) Contrast with the Poisson Approximation

For a binomial random variable $X\sim \mathrm{Bin}(n,p)$:

- The Poisson approximation is useful when $n$ is large, $p$ is small, and $\lambda=np$ is moderate.
- The normal approximation is useful when $n$ is large and the binomial is not too skewed, often summarized by requiring both $np$ and $nq$ to be reasonably large.

The notes phrase the normal case as $p$ close to $1/2$, which is the cleanest symmetric case. More generally, the approximation improves when the binomial mass is not concentrated near $0$ or $n$.

When $\lambda=np$ is also large, a Poisson distribution can itself look approximately normal.

---

## Main Takeaways

- The strong law says $\bar X_n\to\mu$ almost surely.
- The weak law says $\bar X_n\to\mu$ in probability.
- Chebyshev proves the weak law because $\mathrm{Var}(\bar X_n)=\sigma^2/n$.
- The CLT describes the scaled fluctuations: $\sqrt n(\bar X_n-\mu)/\sigma\to N(0,1)$ in distribution.
- The MGF proof reduces the standardized sum to $\left(M(t/\sqrt n)\right)^n$ and shows its log converges to $t^2/2$.
- The binomial normal approximation comes from viewing a binomial as a sum of Bernoulli random variables.
- The continuity correction adjusts for approximating a discrete distribution by a continuous one.

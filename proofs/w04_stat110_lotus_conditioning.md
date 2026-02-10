# Week 4 — S2 (Stat110 Practice): LOTUS + Conditioning

**Topics:** LOTUS, Normal expectation practice, conditional probability review  
**Resources:**

- [Stat110 Strategic Practice and Homework 5](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_5.pdf)
- [Stat110 Strategic Practice and Homework 3](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_3.pdf)

---

## Section 4 — LOTUS

## Problem 1

**Statement.**  
For $X \sim \mathrm{Pois}(\lambda)$, find $E(X!)$ (the average factorial of $X$), if it is finite.

### My attempt (to complete)

Using LOTUS for a discrete random variable:

$$
E[g(X)] = \sum_{k=0}^{\infty} g(k)\,P(X=k).
$$

Here, $g(k)=k!$ and $X\sim\mathrm{Pois}(\lambda)$, so

$$
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
$$

Therefore,

$$
E(X!)=\sum_{k=0}^{\infty} k!\,e^{-\lambda}\frac{\lambda^k}{k!}
=e^{-\lambda}\sum_{k=0}^{\infty}\lambda^k.
$$

Now we identify the series:

$$
\sum_{k=0}^{\infty}\lambda^k = 1+\lambda+\lambda^2+\cdots
$$

which is a geometric series with ratio $\lambda$.

To justify the formula carefully, first use the finite partial sum:

$$
S_n=\sum_{k=0}^{n}\lambda^k=\frac{1-\lambda^{n+1}}{1-\lambda}\quad(\lambda\neq1).
$$

Then take $n\to\infty$:

- If $0\le\lambda<1$, then $\lambda^{n+1}\to0$, so

  $$
  \sum_{k=0}^{\infty}\lambda^k=\frac{1}{1-\lambda}.
  $$

  Hence

  $$
  E(X!)=\frac{e^{-\lambda}}{1-\lambda}.
  $$

- If $\lambda=1$, then

  $$
  \sum_{k=0}^{\infty}1^k=1+1+1+\cdots
  $$

  diverges, so $E(X!)=\infty$.

- If $\lambda>1$, terms $\lambda^k$ do not go to $0$, so the series diverges and $E(X!)=\infty$.

Edge case: when $\lambda=0$, $X=0$ almost surely, so $X!=0!=1$ and $E(X!)=1$ (finite).

### What I initially missed / corrected

- I originally treated $\sum_{k=0}^{\infty}\lambda^k$ like a finite sum too early.
- The key fix was to work with partial sums $S_n=\sum_{k=0}^{n}\lambda^k$ first, then take the limit $n\to\infty$.
- I also clarified that divergence at $\lambda=1$ should be shown directly from $1+1+1+\cdots$, not only from a denominator issue in the finite-sum formula.
- Final condition: finite for $0\le\lambda<1$, infinite for $\lambda\ge1$.

### Book's solution (for comparison)

The book writes:

$$
E(X!)=e^{-\lambda}\sum_{k=0}^{\infty}\lambda^k=\frac{e^{-\lambda}}{1-\lambda},
$$

for $0<\lambda<1$, and states $E(X!)=\infty$ for $\lambda\ge1$.

This matches the derivation above. I added the explicit edge case $\lambda=0$:
$E(X!)=1$.

### Memory card (quick review)

- LOTUS: to compute $E[g(X)]$, apply $g$ inside the expectation:
  $$
  E[g(X)] = \sum_x g(x)P(X=x) \quad \text{or} \quad E[g(X)] = \int g(x)f_X(x)\,dx.
  $$
  You do not need to find the distribution of $g(X)$ first.
- Poisson intuition: $X\sim\mathrm{Pois}(\lambda)$ is a count of arrivals/events in a fixed interval, with average rate $\lambda$.
- In this problem:
  $$
  E(X!)=e^{-\lambda}\sum_{k=0}^{\infty}\lambda^k.
  $$
  The factorial in $X!$ cancels the factorial in the Poisson pmf, so the problem becomes a geometric-series convergence check.
- Final condition: $E(X!)$ is finite for $0\le\lambda<1$, and infinite for $\lambda\ge1$.

## Problem 2

**Statement.**  
Let $Z \sim \mathcal{N}(0,1)$. Find $E|Z|$.

### My attempt (to complete)

Using LOTUS with the standard normal PDF $\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}$:

$$
E|Z|=\int_{-\infty}^{\infty}|z|\phi(z)\,dz
=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}|z|e^{-z^2/2}\,dz.
$$

Since $|z|e^{-z^2/2}$ is even:

$$
E|Z|
=\frac{2}{\sqrt{2\pi}}\int_{0}^{\infty}ze^{-z^2/2}\,dz.
$$

Let $u=z^2/2$, so $du=z\,dz$:

$$
\int_{0}^{\infty}ze^{-z^2/2}\,dz
=\int_{0}^{\infty}e^{-u}\,du
=1.
$$

Therefore,

$$
E|Z|=\frac{2}{\sqrt{2\pi}}=\sqrt{\frac{2}{\pi}}.
$$

### What I initially missed / corrected

I initially mixed up $E|Z|$ with $E(Z)$.  
The symmetry argument that gives zero applies to $E(Z)$ (signed values cancel), not to $E|Z|$.

Key correction: interpret $E|Z|$ as the average distance from 0. Distances do not cancel, and the even-function rewrite to $2\int_0^\infty$ is the right way to use symmetry here.

### Book's solution (for comparison)

Matches my final result exactly:

$$
E|Z|=\sqrt{\frac{2}{\pi}}.
$$

The book uses the same ideas: LOTUS, even symmetry, and a substitution to turn the integral into an exponential integral.

---

## Section 3

## Problem 3

**Statement.**  
Let $Z \sim \mathcal{N}(0,1)$. Find $E(\Phi(Z))$ without using LOTUS, where $\Phi$ is the CDF of $Z$.

### My attempt

Use the **Probability Integral Transform** (a.k.a. _Universality of the Uniform_).

Let $X$ be a continuous r.v. with CDF $F$. Define $U=F(X)$. Claim: $U\sim \text{Unif}(0,1)$.

Compute the CDF of $U$. For $0\le u\le 1$:

$$
F_U(u)=P(U\le u)
=P(F(X)\le u)
=P(X\le F^{-1}(u))
=F(F^{-1}(u))
=u.
$$

Thus $F_U(u)=u$ on $[0,1]$, so $U\sim \text{Unif}(0,1)$.

Now apply it with $X=Z$ and $F=\Phi$. Since $Z$ is continuous,

$$
\Phi(Z)\sim \text{Unif}(0,1).
$$

Therefore,

$$
E(\Phi(Z))=E(U)=\frac{1}{2}.
$$

### What I initially missed / corrected

- I first tried to treat $\Phi(Z)$ as if it were a normal random variable and use the standard normal PDF for it. But $X=\Phi(Z)$ is **not** normal: it takes values only in $[0,1]$.
- The right viewpoint is that $\Phi(Z)$ is the **CDF-value** (percentile) of the draw $Z$ under its own distribution, and by the probability integral transform this must be Uniform.

### Book's solution (for comparison)

By Universality of the Uniform, for any continuous r.v. $X$ with CDF $F$, we have $F(X)\sim \text{Unif}(0,1)$. Taking $X=Z$ and $F=\Phi$ gives

$$
\Phi(Z)\sim \text{Unif}(0,1),
$$

so

$$
E(\Phi(Z))=\frac{1}{2}.
$$

---

## Continuing with Conditioning (Strategic Practice and Homework 3)

## Strategic Practice — Section 1

## Problem 1

**Statement.**  
Consider the Monty Hall problem, except that Monty enjoys opening Door 2 more than he enjoys opening Door 3, and if he has a choice between opening these two doors, he opens Door 2 with probability $p$, where $\frac{1}{2} \le p \le 1$.

To recap: there are three doors, behind one of which there is a car (which you want), and behind the other two of which there are goats (which you don't want). Initially, all possibilities are equally likely for where the car is. You choose a door, which for concreteness we assume is Door 1. Monty Hall then opens a door to reveal a goat, and offers you the option of switching. Assume that Monty Hall knows which door has the car, will always open a goat door and offer the option of switching, and as above assume that if Monty Hall has a choice between opening Door 2 and Door 3, he chooses Door 2 with probability $p$ (with $\frac{1}{2} \le p \le 1$).

(a) Find the unconditional probability that the strategy of always switching succeeds (unconditional in the sense that we do not condition on which of Doors 2,3 Monty opens).

(b) Find the probability that the strategy of always switching succeeds, given that Monty opens Door 2.

(c) Find the probability that the strategy of always switching succeeds, given that Monty opens Door 3.

### My attempt (to complete)

_Pending._

### What I initially missed / corrected

_Pending._

### Book's solution (for comparison)

_Pending._

## Homework

## Problem 2

**Statement.**  
The odds of an event with probability $p$ are defined to be $\frac{p}{1-p}$, e.g., an event with probability $\frac{3}{4}$ is said to have odds of 3 to 1 in favor (or 1 to 3 against). We are interested in a hypothesis $H$ (which we think of as a event), and we gather new data as evidence (expressed as an event $D$) to study the hypothesis. The prior probability of $H$ is our probability for $H$ being true before we gather the new data; the posterior probability of $H$ is our probability for it after we gather the new data. The likelihood ratio is defined as $\frac{P(D \mid H)}{P(D \mid H^c)}$.

(a) Show that Bayes' rule can be expressed in terms of odds as follows: the posterior odds of a hypothesis $H$ are the prior odds of $H$ times the likelihood ratio.

(b) As in the example from class, suppose that a patient tests positive for a disease afflicting 1% of the population. For a patient who has the disease, there is a 95% chance of testing positive (in medical statistics, this is called the sensitivity of the test); for a patient who doesn't have the disease, there is a 95% chance of testing negative test (in medical statistics, this is called the specificity of the test).

The patient gets a second, independent test done (with the same sensitivity and specificity), and again tests positive. Use the odds form of Bayes' rule to find the probability that the patient has the disease, given the evidence, in two ways: in one step, conditioning on both test results simultaneously, and in two steps, first updating the probabilities based on the first test result, and then updating again based on the second test result.

### My attempt (to complete)

_Pending._

### What I initially missed / corrected

_Pending._

### Book's solution (for comparison)

_Pending._

## Problem 4

**Statement.**  
Calvin and Hobbes play a match consisting of a series of games, where Calvin has probability $p$ of winning each game (independently). They play with a "win by two" rule: the first player to win two games more than his opponent wins the match. Find the probability that Calvin wins the match (in terms of $p$), in two different ways:

(a) by conditioning, using the law of total probability.

(b) by interpreting the problem as a gambler's ruin problem.

### My attempt (to complete)

_Pending._

### What I initially missed / corrected

_Pending._

### Book's solution (for comparison)

_Pending._

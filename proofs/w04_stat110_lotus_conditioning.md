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

Let:

- $C_j$: car is behind Door $j$.
- $D_i$: Monty opens Door $i$.
- $W$: always-switch strategy wins.

We choose Door 1 first.

Useful conditional probabilities:

- If $C_1$: Monty chooses between Doors 2 and 3, so
  $P(D_2\mid C_1)=p$, $P(D_3\mid C_1)=1-p$.
- If $C_2$: Monty must open Door 3, so
  $P(D_2\mid C_2)=0$, $P(D_3\mid C_2)=1$.
- If $C_3$: Monty must open Door 2, so
  $P(D_2\mid C_3)=1$, $P(D_3\mid C_3)=0$.

Also, $P(C_1)=P(C_2)=P(C_3)=\frac{1}{3}$.

For part (a), switching wins exactly when our first pick (Door 1) is wrong, i.e., when $C_2$ or $C_3$ happens:

$$
P(W)=P(C_2)+P(C_3)=\frac{1}{3}+\frac{1}{3}=\frac{2}{3}.
$$

For part (b), given Monty opens Door 2, switching means we move to Door 3, so we win iff $C_3$:

$$
P(W\mid D_2)=P(C_3\mid D_2)
=\frac{P(D_2\mid C_3)P(C_3)}{P(D_2)}.
$$

By total probability:

$$
P(D_2)=P(D_2\mid C_1)P(C_1)+P(D_2\mid C_2)P(C_2)+P(D_2\mid C_3)P(C_3)
=p\cdot\frac{1}{3}+0\cdot\frac{1}{3}+1\cdot\frac{1}{3}
=\frac{1+p}{3}.
$$

Hence:

$$
P(W\mid D_2)=\frac{1\cdot\frac{1}{3}}{\frac{1+p}{3}}=\frac{1}{1+p}.
$$

For part (c), given Monty opens Door 3, switching means we move to Door 2, so we win iff $C_2$:

$$
P(W\mid D_3)=P(C_2\mid D_3)
=\frac{P(D_3\mid C_2)P(C_2)}{P(D_3)}.
$$

And

$$
P(D_3)=P(D_3\mid C_1)P(C_1)+P(D_3\mid C_2)P(C_2)+P(D_3\mid C_3)P(C_3)
=(1-p)\cdot\frac{1}{3}+1\cdot\frac{1}{3}+0\cdot\frac{1}{3}
=\frac{2-p}{3}.
$$

Therefore:

$$
P(W\mid D_3)=\frac{1\cdot\frac{1}{3}}{\frac{2-p}{3}}=\frac{1}{2-p}.
$$

### What I initially missed / corrected

- I initially treated $P(D_2)=p$ and $P(D_3)=1-p$ as unconditional probabilities.  
  Correction: those are only true conditional on $C_1$.
- The unconditional values are:
  $$
  P(D_2)=\frac{1+p}{3},\qquad P(D_3)=\frac{2-p}{3}.
  $$
- I also initially combined the conditional answers incorrectly for part (a).  
  Correct unconditional switching success is always:
  $$
  P(W)=\frac{2}{3},
  $$
  independent of $p$.

### Book's solution (for comparison)

For part (a), the book uses the law of total probability:

$$
P(W)=P(W\mid C_1)P(C_1)+P(W\mid C_2)P(C_2)+P(W\mid C_3)P(C_3)
$$

$$
=0\cdot\frac{1}{3}+1\cdot\frac{1}{3}+1\cdot\frac{1}{3}
=\frac{2}{3}.
$$

For part (b), with $D_i=$ "Monty opens Door $i$", the book notes
$P(W\mid D_2)=P(C_3\mid D_2)$ and applies Bayes + total probability:

$$
P(C_3\mid D_2)=\frac{P(D_2\mid C_3)P(C_3)}
{P(D_2\mid C_1)P(C_1)+P(D_2\mid C_2)P(C_2)+P(D_2\mid C_3)P(C_3)}
$$

$$
=\frac{1\cdot\frac{1}{3}}{p\cdot\frac{1}{3}+0\cdot\frac{1}{3}+1\cdot\frac{1}{3}}
=\frac{1}{1+p}.
$$

For part (c), the book uses the symmetric argument from part (b), replacing $p$ by $1-p$:

$$
P(C_2\mid D_3)=\frac{1}{1+(1-p)}=\frac{1}{2-p}.
$$

## Homework

## Problem 2

**Statement.**  
The odds of an event with probability $p$ are defined to be $\frac{p}{1-p}$, e.g., an event with probability $\frac{3}{4}$ is said to have odds of 3 to 1 in favor (or 1 to 3 against). We are interested in a hypothesis $H$ (which we think of as a event), and we gather new data as evidence (expressed as an event $D$) to study the hypothesis. The prior probability of $H$ is our probability for $H$ being true before we gather the new data; the posterior probability of $H$ is our probability for it after we gather the new data. The likelihood ratio is defined as $\frac{P(D \mid H)}{P(D \mid H^c)}$.

(a) Show that Bayes' rule can be expressed in terms of odds as follows: the posterior odds of a hypothesis $H$ are the prior odds of $H$ times the likelihood ratio.

(b) As in the example from class, suppose that a patient tests positive for a disease afflicting 1% of the population. For a patient who has the disease, there is a 95% chance of testing positive (in medical statistics, this is called the sensitivity of the test); for a patient who doesn't have the disease, there is a 95% chance of testing negative test (in medical statistics, this is called the specificity of the test).

The patient gets a second, independent test done (with the same sensitivity and specificity), and again tests positive. Use the odds form of Bayes' rule to find the probability that the patient has the disease, given the evidence, in two ways: in one step, conditioning on both test results simultaneously, and in two steps, first updating the probabilities based on the first test result, and then updating again based on the second test result.

### My attempt (to complete)

For part (a), define:

- prior odds: $\frac{P(H)}{1-P(H)}=\frac{P(H)}{P(H^c)}$
- posterior odds: $\frac{P(H\mid D)}{1-P(H\mid D)}=\frac{P(H\mid D)}{P(H^c\mid D)}$
- likelihood ratio: $\frac{P(D\mid H)}{P(D\mid H^c)}$

Goal:

$$
\frac{P(H)}{P(H^c)}\cdot\frac{P(D\mid H)}{P(D\mid H^c)}
=\frac{P(H\mid D)}{P(H^c\mid D)}.
$$

Using Bayes on both $H$ and $H^c$:

$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)},
\qquad
P(H^c\mid D)=\frac{P(D\mid H^c)P(H^c)}{P(D)}.
$$

Take the ratio:

$$
\frac{P(H\mid D)}{P(H^c\mid D)}
=
\frac{\frac{P(D\mid H)P(H)}{P(D)}}{\frac{P(D\mid H^c)P(H^c)}{P(D)}}
=
\frac{P(H)}{P(H^c)}\cdot\frac{P(D\mid H)}{P(D\mid H^c)}.
$$

Therefore, posterior odds $=$ prior odds $\times$ likelihood ratio, as required.

For part (b), let:

- $H$: patient has disease, so $P(H)=0.01$, $P(H^c)=0.99$.
- $D_1$: first test is positive.
- $D_2$: second test is positive.

Given sensitivity/specificity:

$$
P(D_i\mid H)=0.95,\qquad
P(D_i\mid H^c)=0.05,\quad i\in\{1,2\}.
$$

Prior odds:

$$
\frac{P(H)}{P(H^c)}=\frac{0.01}{0.99}=\frac{1}{99}.
$$

For one positive test, likelihood ratio is:

$$
\frac{P(D_i\mid H)}{P(D_i\mid H^c)}=\frac{0.95}{0.05}=19.
$$

**One-step update (condition on both positives simultaneously).**  
Using conditional independence of tests given disease status:

$$
\frac{P(D_1\cap D_2\mid H)}{P(D_1\cap D_2\mid H^c)}
=\frac{0.95^2}{0.05^2}=361.
$$

So posterior odds are:

$$
\frac{P(H\mid D_1\cap D_2)}{P(H^c\mid D_1\cap D_2)}
=\frac{1}{99}\cdot 361=\frac{361}{99}\approx 3.6464.
$$

Convert odds $O=\frac{p}{1-p}$ to probability $p=\frac{O}{1+O}$:

$$
P(H\mid D_1\cap D_2)
=\frac{\frac{361}{99}}{1+\frac{361}{99}}
=\frac{361}{460}
\approx 0.7848.
$$

So the probability the patient has the disease after two positive tests is about $78.48\%$.

**Two-step update (sequential Bayes updates).**

After first positive:

$$
\text{odds}_1=\frac{1}{99}\cdot 19=\frac{19}{99}.
$$

After second positive:

$$
\text{odds}_2=\frac{19}{99}\cdot 19=\frac{361}{99}.
$$

This matches the one-step posterior odds, so

$$
P(H\mid D_1\cap D_2)=\frac{361}{460}\approx 0.7848.
$$

### What I initially missed / corrected

- I initially had an algebra slip in part (a) when simplifying stacked fractions.
- In part (b), the main bookkeeping point is that specificity $0.95$ implies
  $P(\text{positive}\mid H^c)=0.05$ (false-positive rate), which goes in the denominator of the likelihood ratio.
- I also clarified that odds $\frac{361}{99}\approx 3.6464$ must be converted to a probability:
  $$
  p=\frac{O}{1+O}.
  $$

### Reference solution (with source note)

Source note: part (b) below is verified from your provided screenshot on February 13, 2026. Part (a) below is an inferred standard derivation unless you share the corresponding page.

For part (a), the standard target identity is:

$$
\frac{P(H\mid D)}{P(H^c\mid D)}
=
\frac{P(H)}{P(H^c)}\cdot\frac{P(D\mid H)}{P(D\mid H^c)}.
$$

Then, by Bayes' rule:

$$
P(H\mid D)=\frac{P(D\mid H)P(H)}{P(D)},
\qquad
P(H^c\mid D)=\frac{P(D\mid H^c)P(H^c)}{P(D)}.
$$

Dividing the first equation by the second immediately gives the target odds-form equation.

For part (b), matching your provided screenshot:

$$
\text{prior odds}=\frac{0.01}{0.99}=\frac{1}{99},\qquad
\text{LR for one positive}=\frac{0.95}{0.05}=19.
$$

Hence two independent positives multiply the odds by $19^2$:

$$
\text{posterior odds}=\frac{1}{99}\cdot 19^2=\frac{361}{99}.
$$

Convert to posterior probability:

$$
P(H\mid D_1\cap D_2)=\frac{361}{361+99}=\frac{361}{460}\approx 0.7848.
$$

## Problem 4

**Statement.**  
Calvin and Hobbes play a match consisting of a series of games, where Calvin has probability $p$ of winning each game (independently). They play with a "win by two" rule: the first player to win two games more than his opponent wins the match. Find the probability that Calvin wins the match (in terms of $p$), in two different ways:

(a) by conditioning, using the law of total probability.

(b) by interpreting the problem as a gambler's ruin problem.

### My attempt

For part (a), use first-step analysis (conditioning on the first 2 games).

Let:

- $C$: Calvin wins the match.
- $x=P(C)$ starting from a tied score (initially $0$-$0$).
- $q=1-p$.

Condition on outcomes of the first 2 games:

- Calvin wins both (`WW`), probability $p^2$: match ends and Calvin wins.
- Calvin loses both (`LL`), probability $q^2$: match ends and Calvin loses.
- They split (`WL` or `LW`), probability $2pq$: score difference returns to $0$, so by independence and the memoryless reset of state, win probability is again $x$.

So:

$$
x = 1\cdot p^2 + 0\cdot q^2 + x\cdot 2pq
= p^2 + 2pq\,x.
$$

Rearrange:

$$
x(1-2pq)=p^2
\quad\Rightarrow\quad
x=\frac{p^2}{1-2pq}.
$$

Using $p+q=1$:

$$
1-2pq=p^2+q^2,
$$

so equivalent forms are:

$$
P(C)=x=\frac{p^2}{1-2pq}
=\frac{p^2}{p^2+q^2}
=\frac{p^2}{2p^2-2p+1}.
$$

### What I initially missed / corrected

- The key step to justify clearly is the split case:
  $$
  P(C\mid WL\ \text{or}\ LW)=P(C),
  $$
  because after one win and one loss the process is back to a tied state.
- The final answer can look different algebraically, but
  $$
  \frac{p^2}{1-2p(1-p)}=\frac{p^2}{p^2+(1-p)^2}
  $$
  is the same quantity.

### Book's solution (for comparison)

Source note: part (a) below is verified from your provided screenshot on February 16, 2026.

For part (a), the book defines $X\sim\mathrm{Bin}(2,p)$ as Calvin's number of wins in the first 2 games, with $q=1-p$, and conditions on $X\in\{0,1,2\}$:

$$
P(C)=P(C\mid X=0)q^2+P(C\mid X=1)(2pq)+P(C\mid X=2)p^2.
$$

Then:

$$
P(C\mid X=0)=0,\quad P(C\mid X=2)=1,\quad P(C\mid X=1)=P(C),
$$

so:

$$
P(C)=2pq\,P(C)+p^2
\quad\Rightarrow\quad
P(C)=\frac{p^2}{1-2pq}
=\frac{p^2}{p^2+q^2}.
$$

This matches the result from my first-step conditioning derivation.

Part (b): _Pending._

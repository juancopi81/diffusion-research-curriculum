# Distributions & Expected Values (Discrete RVs) — Strategic Practice (Lec 9–10)

## Problem 1
**Question.**
Find an example of two discrete random variables $X$ and $Y$ (on the same sample space) such that $X$ and $Y$ have the same distribution (same PMF/CDF), but the event $X=Y$ never occurs.

### My attempt (what I wrote / idea)
- Use **one coin flip** as the sample space.
- Define:
  - $X = 1\{\text{Head}\}$
  - $Y = 1\{\text{Tail}\}$
- Then $(X,Y)$ is always either $(1,0)$ or $(0,1)$, so **$X=Y$ never happens**.

### What I initially missed / corrected
- The key check for "same distribution" is:
  $P(X=1) = P(Y=1)$ and $P(X=0) = P(Y=0)$.
  This holds **only if the coin is fair**.

### Book's solution (for comparison)
- Let $X \sim \text{Bernoulli}(1/2)$, and define $Y = 1 - X$.
- Then $Y$ is also $\text{Bernoulli}(1/2)$ by symmetry, but $X=Y$ is impossible.
- Generalization: $X \sim \text{Binomial}(n,1/2)$, $Y=n-X$ with $n$ odd.

---

## Problem 2
**Question.**
Let $X$ be a random day of the week coded as $1,\dots,7$ with equal probabilities.
Let $Y$ be the *next day after* $X$ (also coded $1,\dots,7$).
Do $X$ and $Y$ have the same distribution? What is $P(X<Y)$?

### My initial thought (and the correction)
- I initially mixed up unconditional vs conditional:
  - I wrote something like: $P(X=x)=1/7$ while $P(Y \mid X=x)=1$, so "not same distribution."
- Correction:
  - "Same distribution" is about $P(Y=y)$, not $P(Y \mid X=x)$.
  - With wrap-around (after 7 comes 1), the map $x \mapsto y$ is a one-to-one shift mod 7, so $Y$ is also uniform on $\{1,\dots,7\}$.
  ✅ So **they have the same distribution**.

### $P(X<Y)$: where I slipped
- I initially thought "if 7 comes before 1 in the cycle, then 7 < 1," which would make it 1.
- But the inequality $X<Y$ uses **normal integer order** $1<2<\dots<7$. Wrap-around changes the definition of $Y$, not the meaning of "<".
- So $X<Y$ fails only when $X=7$ (since then $Y=1$ and $7<1$ is false).
  - Favorable cases: $X=1,2,3,4,5,6$ (6 cases out of 7)
  - So $P(X<Y)=6/7$.

### Book's solution (for comparison)
- Same distribution since $Y$ is equally likely to be any day.
- $P(X<Y) = P(X\ne 7) = 6/7$.

---

## Problem 3
**Question.**
A coin is tossed repeatedly until it lands Heads for the first time.
Let $X$ be the number of tosses required (including the first Head), and $p=P(\text{Head})$.
Find the CDF of $X$, and for $p=1/2$ sketch its graph.

### My attempt (what I wrote / where it went wrong)
- I tried to shift to a "failures before first success" variable:
  - Let $Y = X-1$, so $Y$ counts the number of Tails before the first Head.
- The idea was correct, but I made two main mistakes at first:
  1) I wrote extra "$+1$" terms in PMF/CDF lines (which can push probabilities above 1).
  2) I mixed up PMF values and CDF values:
     - I listed $1/2, 1/4, 1/8,\dots$ and sketched a **decreasing curve** — that's the PMF (or tail), **not** a CDF.
     - A CDF must be **nondecreasing** and approach 1.

### Corrected direction (still in my "shift + sum" style)
- Since $Y=X-1$ and $Y\in\{0,1,2,\dots\}$:
  - $P(X=k)=P(Y=k-1)$ for $k\in\{1,2,3,\dots\}$
  - For integer $x\ge 1$:

$$
F(x)=P(X\le x)=P(Y\le x-1)=\sum_{k=0}^{x-1}(1-p)^k\,p
$$

- For a fair coin $p=1/2$, the PMF terms are:
  - $P(X=1)=1/2$, $P(X=2)=1/4$, $P(X=3)=1/8$, ...
- The *CDF* values are cumulative:
  - $F(1)=1/2$
  - $F(2)=1/2+1/4=3/4$
  - $F(3)=1/2+1/4+1/8=7/8$
  - ... so the CDF is a **step function** jumping at integers.

### Sketch
![w02_proof_CDF](/notes/figures/w02_proof_CDF.png)

### Book's solution (for comparison)
- Uses the Geometric story: $X-1 \sim \text{Geometric}(p)$ (in the "# failures before first success" convention).
- PMF: $P(X=k)=p(1-p)^{k-1}$ for $k=1,2,3,\dots$
- CDF for real $x$:

$$
F(x)=P(X\le x)=
\begin{cases}
0, & x<1\\
1-(1-p)^{\lfloor x\rfloor}, & x\ge 1
\end{cases}
$$

- For $p=1/2$: $F(x)=1-2^{-\lfloor x\rfloor}$ for $x\ge 1$.

### How my result matches the book (what was "different" at first)
- My sum form is the same as the book's closed form:
  - $\sum_{k=0}^{x-1}(1-p)^k p = 1-(1-p)^x$ for integer $x\ge 1$.
- The book writes it with $\lfloor x\rfloor$ to define it for **non-integer** $x$ (flat between integers).

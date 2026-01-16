# Week 1 — S2 (Stat110 Practice): Discrete RVs, Conditioning, Binomial

**Topics:** Bernoulli trials, Binomial RVs, conditioning, independence, (Hypergeometric via conditioning)
**Resource:** [Stat110-Text] + [Stat110-Practice]

---

## Problem 1 — Bernoulli trials: conditioning on the number of successes

**Statement.**
A sequence of $n$ independent experiments is performed. Each experiment is a success with probability $p$ and a failure with probability $q=1-p$.
Show that **conditional on the number of successes**, all outcome sequences with that many successes are **equally likely**.

### Solution (clean proof)

Let $X_i \in \{0,1\}$ indicate whether trial $i$ is a success, and let

$$
X = \sum_{i=1}^n X_i
$$

be the total number of successes.

Fix $k$ and any $(a_1,\dots,a_n)\in\{0,1\}^n$ such that $\sum_{i=1}^n a_i = k$. Then

$$
\mathbb{P}(X_1=a_1,\dots,X_n=a_n \mid X=k)
= \frac{\mathbb{P}(X_1=a_1,\dots,X_n=a_n,\;X=k)}{\mathbb{P}(X=k)}.
$$

Since $\{X_1=a_1,\dots,X_n=a_n\}$ already implies $\{X=k\}$ (because $\sum a_i = k$),

$$
\mathbb{P}(X_1=a_1,\dots,X_n=a_n,\;X=k)
=\mathbb{P}(X_1=a_1,\dots,X_n=a_n).
$$

By independence, the probability of this specific sequence is

$$
\mathbb{P}(X_1=a_1,\dots,X_n=a_n)=p^k q^{n-k}.
$$

Also, $X\sim\mathrm{Bin}(n,p)$, so

$$
\mathbb{P}(X=k)=\binom{n}{k}p^k q^{n-k}.
$$

Therefore,

$$
\mathbb{P}(X_1=a_1,\dots,X_n=a_n \mid X=k)
=\frac{p^k q^{n-k}}{\binom{n}{k}p^k q^{n-k}}
=\frac{1}{\binom{n}{k}}.
$$

This does not depend on $(a_1,\dots,a_n)$. Hence, given exactly $k$ successes, the $\binom{n}{k}$ valid sequences are all equally likely.

**Key takeaway:** conditioning on the total number of successes makes the sequence **uniform** over all placements of the $k$ successes.

---

## Problem 2 — Let $X\sim\mathrm{Bin}(n,p)$, $Y\sim\mathrm{Bin}(m,p)$, independent

### (a) Show that $X+Y \sim \mathrm{Bin}(n+m,p)$ (story proof)

Interpret $X$ as the number of successes in $n$ Bernoulli($p$) trials, and $Y$ as the number of successes in **another** $m$ Bernoulli($p$) trials, independent of the first $n$. Then $X+Y$ counts successes across all $n+m$ independent trials, so

$$
X+Y \sim \mathrm{Bin}(n+m,p).
$$

---

### (b) Show that $X-Y$ is not Binomial

A Binomial random variable cannot be negative (its support is $\{0,1,\dots,N\}$). But $X-Y$ can be negative with positive probability when $0<p<1$. For instance,

$$
\mathbb{P}(X-Y=-1)\ge \mathbb{P}(X=0,\;Y=1)
= \mathbb{P}(X=0)\mathbb{P}(Y=1)
= q^n \cdot \binom{m}{1}p q^{m-1} > 0.
$$

Thus $X-Y$ takes negative values with positive probability, so it cannot be Binomial.

---

### (c) Find $\mathbb{P}(X=k \mid X+Y=j)$. Relation to the elk problem (HW1)

Start from the definition:

$$
\mathbb{P}(X=k \mid X+Y=j)
= \frac{\mathbb{P}(X=k,\;X+Y=j)}{\mathbb{P}(X+Y=j)}
= \frac{\mathbb{P}(X=k,\;Y=j-k)}{\mathbb{P}(X+Y=j)}.
$$

Using independence:

$$
\mathbb{P}(X=k,\;Y=j-k) = \mathbb{P}(X=k)\mathbb{P}(Y=j-k).
$$

Plug in binomial pmfs:

$$
\mathbb{P}(X=k)=\binom{n}{k}p^k q^{n-k},\qquad
\mathbb{P}(Y=j-k)=\binom{m}{j-k}p^{j-k}q^{m-(j-k)}.
$$

Also $X+Y\sim\mathrm{Bin}(n+m,p)$, so

$$
\mathbb{P}(X+Y=j)=\binom{n+m}{j}p^j q^{n+m-j}.
$$

Therefore,

$$
\mathbb{P}(X=k \mid X+Y=j)
=\frac{\binom{n}{k}\binom{m}{j-k}}{\binom{n+m}{j}}.
$$

**Valid range of $k$:**

$$
\max(0,\;j-m) \le k \le \min(n,\;j),
$$

equivalently $0\le k\le n$ and $0\le j-k\le m$.

**Key takeaway:** the $p$ cancels — the conditional distribution depends only on combinatorics.

#### Relation to the elk problem (Hypergeometric intuition)

Interpret there being two groups (e.g., $n$ male elk and $m$ female elk). Each elk is "tagged" independently with probability $p$. Given that **a total of $j$** elk are tagged, the conditional distribution of **how many tagged are male** is

$$
\mathbb{P}(X=k \mid X+Y=j)=\frac{\binom{n}{k}\binom{m}{j-k}}{\binom{n+m}{j}},
$$

which is the **Hypergeometric** distribution form (same structure as "sampling $j$ from $n+m$" and counting how many came from the first group).

---

## Notes / Next

- ✅ Conditioning-on-success-count ⇒ uniform over sequences (Problem 1)
- ✅ Binomial sum/difference + conditional (Problem 2a–c)

## Problem 3 — Gambler’s Ruin with unfavorable odds (p ≠ q)

**Statement.**  
A gambler repeatedly plays a game where in each round he wins \$1 with probability
$p=\tfrac13$ and loses \$1 with probability $q=\tfrac23$. He starts with \$1,000,000
and plans to quit if he is ever **ahead by \$2**.  
Show that the probability that he is ever ahead by \$2 is **less than $1/4$**.

---

### Solution (via Gambler’s Ruin formula)

Model the gambler’s fortune as a biased random walk with
+1 w.p. $p=\tfrac13$ and −1 w.p. $q=\tfrac23$.

Define the target as reaching **\$2 above the starting point**, and ruin as reaching \$0.
Shift the process so the state space is

$$
\{0,1,\dots,N\}, \qquad N=1{,}000{,}002,
$$

where the gambler starts at $i=1{,}000{,}000$.

For gambler’s ruin with $p\neq q$, the probability of hitting $N$ before $0$ is

$$
\mathbb{P}(\text{hit }N\text{ before }0)
= \frac{1-(q/p)^i}{1-(q/p)^N}.
$$

Here, $q/p = 2$, so

$$
\mathbb{P}(\text{ahead by \$2})
= \frac{1-2^{\,1{,}000{,}000}}{1-2^{\,1{,}000{,}002}}
= \frac{2^{1{,}000{,}000}-1}{4\cdot 2^{1{,}000{,}000}-1}.
$$

Since

$$
\frac{2^{1{,}000{,}000}-1}{4\cdot 2^{1{,}000{,}000}-1}
\;<\;
\frac{2^{1{,}000{,}000}}{4\cdot 2^{1{,}000{,}000}}
=\frac14,
$$

the desired probability is strictly less than $1/4$.

---

### Alternative viewpoint (book’s approach — recurrence)

Let $a_i$ be the probability of ever being ahead by \$2 before ruin, starting with fortune $i$.

Conditioning on the first step gives

$$
a_i=\tfrac13 a_{i+1}+\tfrac23 a_{i-1},
$$

with boundary conditions

$$
a_0=0,\qquad a_{i+2}=1.
$$

Solving this difference equation (or using gambler’s ruin) yields

$$
a_i=\frac{2^i-1}{2^{i+2}-1},
$$

which matches the expression obtained above and is always $<\tfrac14$.

---

**Key takeaway:**  
With unfavorable odds ($p<q$), even starting with an enormous bankroll does **not**
make short-term profit events likely; the success probability is controlled by the bias,
not by the initial capital.

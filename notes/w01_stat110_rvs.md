# Notes for Lectures 7 (Gambler's Ruin and Random Variables) and 8 (Random Variables and Their Distribution)

## [Lecture 8](https://www.youtube.com/watch?v=k2BB0p8byGA&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=8): Random Variables and Their Distribution

### Two Main Aspects of Statistics

1. **Conditioning**: The soul of statistics
2. **Random variables and their distributions**

### What's a Random Variable?

Not a variable but a **function**. It is a function from the sample space $S$ to the real line.

- **Input**: $s$, a specific outcome of $S$
- **Output**: a number in the real line

---

## Distributions

### Bernoulli Distribution

A r.v. $X$ is said to have the $\text{Bern}(p)$ distribution if $X$ has only 2 possible values (0 and 1), and $P(X=1) = p$ and $P(X=0) = 1-p$.

### Binomial Distribution

**Story**: The distribution of # of successes in $n$ independent $\text{Bern}(p)$ trials is called $\text{Bin}(n, p)$. For example, flip a coin $n$ times.

**PMF (Probability Mass Function)**:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Alternative view** — sum of indicator r.v.'s:

$$X = X_1 + X_2 + \dots + X_n$$

$$X_j = \begin{cases} 1, & \text{if } j\text{-th trial is a success} \\ 0, & \text{otherwise} \end{cases}$$

where $X_1, \dots, X_n$ are i.i.d. (independent and identically distributed) $\text{Bern}(p)$.

---

## PMF and CDF

### CDF (Cumulative Distribution Function)

- $X = 7$ is an event
- $X \leq x$ is also an event
- $F(x) = P(X \leq x)$, then $F$ is the CDF of $X$
- CDF is a way to describe the distribution

### PMF (Probability Mass Function)

Only for discrete r.v.'s. **Discrete**: possible values can be listed.

$$P(X = a_j) = p_j \quad \text{for all } j$$

**Two conditions**:
1. $p_j \geq 0$
2. $\sum p_j = 1$

**Checking Binomial satisfies both conditions**:

$$\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + q)^n = 1^n = 1$$

by the binomial theorem.

> **Recall — Binomial Theorem**: $(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$
>
> Here we use $x = p$ and $y = (1-p) = q$, so $(p + q)^n = 1^n = 1$.

---

## Common Mistake: Thinking Something is Binomial When It's Not

**Example**: 5-card hand, find distribution of # aces.

Let $X$ = # of aces. We need to find $P(X = k)$.

This is 0, except if $k \in \{0, 1, 2, 3, 4\}$.

**Not binomial** since trials are not independent.

By naive definition:

$$P(X=k) = \frac{\binom{4}{k}\binom{48}{5 - k}}{\binom{52}{5}} \quad \text{for } k \in \{0, 1, 2, 3, 4\}$$

---

## Hypergeometric Distribution

**Generalization**: Have $b$ black and $w$ white marbles. Pick a simple random sample of size $n$. Find distribution of $X$ = # of white marbles in the sample.

$$P(X=k) = \frac{\binom{w}{k}\binom{b}{n - k}}{\binom{w+b}{n}}$$

where $0 \leq k \leq w$ and $0 \leq n - k \leq b$.

This is the **Hypergeometric distribution** — sampling without replacement (if you replace, it becomes binomial).

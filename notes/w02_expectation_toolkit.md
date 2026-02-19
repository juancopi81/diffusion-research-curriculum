# Expectation Toolkit (Week 2)

A one-page reference for expectation patterns and discrete distributions.

---

## 1. Key Rules

### Linearity of Expectation

$$E[X + Y] = E[X] + E[Y]$$
$$E[cX] = c \cdot E[X]$$

**Key insight:** Works even when X and Y are **dependent**.

### Variance Scaling

$$\text{Var}(aX + b) = a^2 \text{Var}(X)$$

Adding a constant doesn't change variance; scaling by $a$ squares it.

---

## 2. Expectation Patterns

### Indicator Method

**When to use:** Counting something (# of successes, matches, events).

**Steps:**

1. Define indicator $X_j = 1\text{event } j \text{ occurs}$
2. Write total as sum: $X = \sum_j X_j$
3. Apply linearity: $E[X] = \sum_j E[X_j] = \sum_j P(\text{event } j)$

**Why powerful:** Works even when indicators are dependent.

### Symmetry Argument

**When to use:** All indicators have the same probability of success.

If $E[X_j]$ is the same for all $j$, then:
$$E[X] = n \cdot E[X_1]$$

Compute one, multiply by count.

**Examples:** Birthday pairs, Hypergeometric (aces in hand), Haribo bags.

### Conditioning Trick ("First Step Analysis")

**When to use:** Problems with recursive structure (e.g., waiting times).

**Pattern:**

1. Let $c = E[X]$
2. Condition on "first thing that happens"
3. Get equation where $c$ appears on both sides
4. Solve for $c$

**Example (Geometric):**

- With prob $p$: succeed immediately, $X = 0$
- With prob $q$: fail once, then "back where we started" with expected $c$ remaining

$$c = 0 \cdot p + (1 + c) \cdot q \implies c = \frac{q}{p}$$

---

## 3. Discrete Distributions Reference


| Distribution         | Story                                                                                          | PMF                                                   | E[X]           |
| -------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------- |
| **Bern(p)**          | Single trial, success (1) or failure (0)                                                       | $P(X=1)=p$, $P(X=0)=1-p$                              | $p$            |
| **Bin(n,p)**         | # of successes in $n$ indep. Bern($p$) trials                                                  | $\binom{n}{k}p^k(1-p)^{n-k}$                          | $np$           |
| **Hypergeom(N,K,n)** | # of "success" items when sampling $n$ from population $N$ with $K$ successes (no replacement) | $\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$   | $\frac{nK}{N}$ |
| **Geom(p)**          | # of failures before 1st success                                                               | $p \cdot q^k$, $k=0,1,2,\ldots$                       | $\frac{q}{p}$  |
| **FS(p)**            | # of trials until 1st success (incl.)                                                          | $p \cdot q^{k-1}$, $k=1,2,3,\ldots$                   | $\frac{1}{p}$  |
| **NegBin(r,p)**      | # of failures before $r$-th success                                                            | $\binom{n+r-1}{r-1}p^r q^n$                           | $\frac{rq}{p}$ |
| **Pois(λ)**          | # of rare events (limit of Bin(n,p) as n→∞, p→0, np→λ)                                         | $\frac{\lambda^k e^{-\lambda}}{k!}$, $k=0,1,2,\ldots$ | $\lambda$      |


Where $q = 1 - p$ throughout.

---

## 4. Diffusion Application (Week 2 Contact)

For forward noising $x_t = x_0 + \sigma(t) \cdot \varepsilon$ where $\varepsilon \sim N(0,1)$:

$$E[x_t \mid x_0] = x_0$$
$$\text{Var}(x_t \mid x_0) = \sigma^2(t)$$

**Derivation uses:**

- Linearity: $E[x_0 + \sigma(t)\varepsilon \mid x_0] = x_0 + \sigma(t) E[\varepsilon]$
- Independence: $\varepsilon$ independent of $x_0$, so $E[\varepsilon \mid x_0] = E[\varepsilon] = 0$
- Variance scaling: $\text{Var}(\sigma(t)\varepsilon) = \sigma^2(t) \cdot \text{Var}(\varepsilon) = \sigma^2(t)$


# Checkpoint 01 (Week 4 S3): Conditioning in Code

## Problem Choice

This project uses the **Monty Hall with biased host choice** problem:

- You pick Door 1.
- The car is equally likely behind Door 1, 2, or 3.
- Monty always opens a goat door.
- If Monty has a choice (when car is behind Door 1), he opens Door 2 with probability $p$ and Door 3 with probability $1-p$, where $\frac{1}{2} \le p \le 1$.

You want:

1. $P(W)$: probability that "always switch" wins (unconditional).
2. $P(W \mid D_2)$: probability "always switch" wins given Monty opens Door 2.
3. $P(W \mid D_3)$: probability "always switch" wins given Monty opens Door 3.

---

## Notation (Use This Consistently)

- $C_j$: event that the car is behind Door $j$.
- $D_i$: event that Monty opens Door $i$.
- $W$: event that always-switch wins.

Given setup:

$$
P(C_1) = P(C_2) = P(C_3) = \frac{1}{3}.
$$

And:

$$
P(D_2 \mid C_1) = p, \quad P(D_3 \mid C_1) = 1-p,
$$
$$
P(D_2 \mid C_2) = 0, \quad P(D_3 \mid C_2) = 1,
$$
$$
P(D_2 \mid C_3) = 1, \quad P(D_3 \mid C_3) = 0.
$$

---

## Derivation Worksheet

### Part (a): Unconditional switching success

Switching wins exactly when your first pick (Door 1) is wrong.

So:

$$
P(W) = P(C_2) + P(C_3) = \frac{2}{3}.
$$

TODO:
- Write this same argument in your own words in 2 to 4 lines.
- Add one sentence on why this does **not** depend on $p$.

---

### Part (b): Conditional switching success given Monty opens Door 2

If Monty opens Door 2, switching means you move to Door 3. So:

$$
P(W \mid D_2) = P(C_3 \mid D_2).
$$

Apply Bayes:

$$
P(C_3 \mid D_2) = \frac{P(D_2 \mid C_3)P(C_3)}{P(D_2)}.
$$

Use LOTP for denominator:

$$
P(D_2) = \sum_{j=1}^3 P(D_2 \mid C_j)P(C_j)
= p\cdot\frac{1}{3} + 0\cdot\frac{1}{3} + 1\cdot\frac{1}{3}
= \frac{1+p}{3}.
$$

Hence:

$$
P(W \mid D_2)
= \frac{1\cdot\frac{1}{3}}{(1+p)/3}
= \frac{1}{1+p}.
$$

TODO:
- Explicitly write the Bayes numerator before simplification.
- Briefly explain why $P(D_2 \mid C_3)=1$.

---

### Part (c): Conditional switching success given Monty opens Door 3

If Monty opens Door 3, switching means you move to Door 2. So:

$$
P(W \mid D_3) = P(C_2 \mid D_3).
$$

Apply Bayes:

$$
P(C_2 \mid D_3) = \frac{P(D_3 \mid C_2)P(C_2)}{P(D_3)}.
$$

Use LOTP:

$$
P(D_3) = \sum_{j=1}^3 P(D_3 \mid C_j)P(C_j)
= (1-p)\cdot\frac{1}{3} + 1\cdot\frac{1}{3} + 0\cdot\frac{1}{3}
= \frac{2-p}{3}.
$$

Hence:

$$
P(W \mid D_3)
= \frac{1\cdot\frac{1}{3}}{(2-p)/3}
= \frac{1}{2-p}.
$$

TODO:
- Add one sentence comparing $P(W \mid D_2)$ and $P(W \mid D_3)$ when $p$ is large.
- Explain intuitively why these two conditionals are different.

---

## Final Theoretical Results (Self-Check)

$$
P(W) = \frac{2}{3}, \quad
P(W \mid D_2) = \frac{1}{1+p}, \quad
P(W \mid D_3) = \frac{1}{2-p}.
$$

---

## Bridge to Code

`simulate.py` and `results.ipynb` estimate the same three probabilities by Monte Carlo.

You should verify:

1. Empirical estimates approach theory as trials increase.
2. Conditional estimates depend on $p$ in the expected direction.
3. Unconditional estimate stays near $\frac{2}{3}$ regardless of $p$.

TODO:
- After running the notebook, copy one short paragraph here summarizing what matched theory and what differed due to finite-sample noise.

---

## S3 Completion Checklist (Project-Only)

- [ ] Derivation is clean and self-contained.
- [ ] Monte Carlo outputs are reported for at least 3 values of $p$.
- [ ] At least one plot compares empirical vs theoretical probabilities.
- [ ] You wrote a short interpretation paragraph about conditional probabilities.

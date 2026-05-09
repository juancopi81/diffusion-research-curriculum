# Checkpoint 01 (Week 4 S3): Conditioning in Code

## Portfolio Summary

This checkpoint shows how conditioning changes a probability problem. In a biased Monty Hall variant, the unconditional switch win rate remains $2/3$, but the conditional win rate depends on which door Monty opens.

**What I learned:** Conditioning is not just filtering data after the fact. It changes the probability model by using the observed event as evidence.

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

Completed explanation:
- At the start, the car is equally likely behind each door: $P(C_1)=P(C_2)=P(C_3)=\frac{1}{3}$.
- If the car is behind Door 1 (my initial pick), switching loses.
- If the car is behind Door 2 or Door 3, Monty opens the only goat door left, so switching wins.
- Hence $P(W)=P(C_2)+P(C_3)=\frac{2}{3}$.
- This does not depend on $p$ because $p$ only affects which goat door Monty opens when he has a choice, not whether my initial pick was right or wrong.

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

Completed explanation:
- Bayes numerator before simplification:
  $$
  P(D_2 \mid C_3)P(C_3) = 1 \cdot \frac{1}{3}.
  $$
- Denominator by LOTP:
  $$
  P(D_2)=P(D_2 \mid C_1)P(C_1)+P(D_2 \mid C_2)P(C_2)+P(D_2 \mid C_3)P(C_3)
  = p\cdot\frac{1}{3}+0\cdot\frac{1}{3}+1\cdot\frac{1}{3}
  = \frac{1+p}{3}.
  $$
- Why $P(D_2 \mid C_3)=1$:
  if the car is behind Door 3 and the player chose Door 1, Monty cannot open Door 1 (player's door) or Door 3 (car door), so he must open Door 2.

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

Completed explanation:
- When $p$ is large, $P(W \mid D_2)=\frac{1}{1+p}$ is close to $\frac{1}{2}$, while $P(W \mid D_3)=\frac{1}{2-p}$ is close to $1$. So seeing Door 3 opened is much stronger evidence that switching will win.
- Intuitively, if Monty strongly prefers Door 2, then opening Door 3 usually means he was forced (car in Door 2), which favors switching. Opening Door 2 is less informative because it can occur both when switching wins and when switching loses.

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

The code verifies:

1. Empirical estimates approach theory as trials increase.
2. Conditional estimates depend on $p$ in the expected direction.
3. Unconditional estimate stays near $\frac{2}{3}$ regardless of $p$.

Summary:
- Monte Carlo matches theory closely across the grid $p\in\{0.5,0.7,0.9,1.0\}$ with $200{,}000$ trials per value. In all cases, the unconditional estimate stayed near $\frac{2}{3}$ (absolute errors about $2\times 10^{-4}$ to $8\times 10^{-4}$), while the conditional estimates followed the expected trend: $P(W\mid D_2)$ decreased as $p$ increased and $P(W\mid D_3)$ increased as $p$ increased, reaching $P(W\mid D_3)=1$ at $p=1$. Small differences from theory are consistent with finite-sample Monte Carlo noise.

---

## S3 Completion Checklist (Project-Only)

- [x] Derivation is clean and self-contained.
- [x] Monte Carlo outputs are reported for at least 3 values of $p$.
- [x] At least one plot compares empirical vs theoretical probabilities.
- [x] You wrote a short interpretation paragraph about conditional probabilities.

# Stat 110 (Blitzstein) - Lecture 31

**Lecture 31:** [Markov Chains](https://www.youtube.com/watch?v=8AJPs3gvNlY&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=31)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** Synthesized from the full lecture video (audio transcript + blackboard frames, retrieved via Video Moment Finder), not from a written solution set. The board work (state diagram, transition matrix, stationary-distribution equation) is source-verified against captured frames; the surrounding prose is a paraphrased summary of the lecture, not a transcript reproduction.

---

## 1) Setup: Stochastic Processes and the Markov Property

A **stochastic process** is a sequence of random variables evolving over time,

$$
X_0, X_1, X_2, \dots
$$

Earlier in the course (LLN, CLT) this sequence was assumed i.i.d. A **Markov chain** goes one step beyond i.i.d.: the variables are allowed to depend on each other, but only through the *most recent* value. Think of $X_n$ as the state of a system at (discrete) time $n$, wandering randomly among finitely many states, conventionally labeled $1,\dots,M$.

**Markov property.** For any states $i,i_{n-1},\dots,i_0$ and any $j$,

$$
\mathbb{P}(X_{n+1}=j \mid X_n=i, X_{n-1}=i_{n-1},\dots,X_0=i_0)
=
\mathbb{P}(X_{n+1}=j\mid X_n=i).
$$

In words: **the past and future are conditionally independent given the present.** Once $X_n$ is known, everything further back is redundant information — it doesn't matter *how* the chain reached state $i$, only that it is there now.

A chain is **homogeneous** (time-homogeneous) if this conditional probability does not depend on $n$. Writing

$$
q_{ij} = \mathbb{P}(X_{n+1}=j\mid X_n=i)
$$

for a homogeneous chain, $q_{ij}$ is called a **transition probability**. This course only considers homogeneous, finite-state, discrete-time chains.

---

## 2) Transition Matrices

Collecting the $q_{ij}$ into an $M\times M$ matrix gives the **transition matrix**

$$
Q = (q_{ij}).
$$

Since row $i$ of $Q$ is the conditional PMF of $X_{n+1}$ given $X_n = i$,

$$
\boxed{
\text{every row of } Q \text{ is non-negative and sums to } 1.
}
$$

Conversely, any square matrix with non-negative entries and rows summing to $1$ is a valid transition matrix — it can always be drawn as a state diagram with arrows carrying the corresponding probabilities.

---

## 3) A Worked Example (Four States)

The lecture works with a hand-drawn 4-state chain, states $1,2,3,4$:

- From $1$: stay at $1$ w.p. $1/3$, move to $2$ w.p. $2/3$.
- From $2$: move to $1$ or to $3$, each w.p. $1/2$.
- From $3$: move to $4$ w.p. $1$ (deterministic).
- From $4$: move to $1$ w.p. $1/2$, to $3$ w.p. $1/4$, stay at $4$ w.p. $1/4$.

which gives the transition matrix

$$
Q =
\begin{pmatrix}
1/3 & 2/3 & 0 & 0 \\
1/2 & 0 & 1/2 & 0 \\
0 & 0 & 0 & 1 \\
1/2 & 0 & 1/4 & 1/4
\end{pmatrix}.
$$

Each row sums to $1$, as required. Note that not every state can be reached from every other in one step (e.g. $1\to 3$ is impossible in a single step) — that's expected and does not violate the row-sum condition.

---

## 4) Multi-Step Transitions: Powers of $Q$

Let $X_n$ have distribution written as a row vector

$$
s = (s_1,\dots,s_M), \qquad s_i = \mathbb{P}(X_n=i),
$$

a $1\times M$ matrix with non-negative entries summing to $1$.

**One step forward.** Condition on the current state and apply the Markov property:

$$
\begin{aligned}
\mathbb{P}(X_{n+1}=j)
&=
\sum_{i} \mathbb{P}(X_{n+1}=j\mid X_n=i)\,\mathbb{P}(X_n=i) \\
&=
\sum_i s_i\, q_{ij}.
\end{aligned}
$$

This sum is exactly the $j$-th entry of the matrix product $sQ$ (a $1\times M$ times an $M\times M$ matrix, valid since the inner dimensions match). Hence

$$
\boxed{
X_n \sim s \implies X_{n+1}\sim sQ.
}
$$

**Iterating.** Since $sQ$ is itself a valid distribution, the same argument applied again gives $X_{n+2}\sim (sQ)Q = sQ^2$, and inductively

$$
\boxed{
X_{n+m} \sim s\,Q^{m}.
}
$$

So the entire future evolution of the distribution is obtained just by taking powers of $Q$ — no need to redo the conditioning argument at each step.

**Two-step transition probabilities.** The same idea applies entrywise. Condition on the intermediate state $X_{n+1}=k$:

$$
\begin{aligned}
\mathbb{P}(X_{n+2}=j\mid X_n=i)
&=
\sum_k \mathbb{P}(X_{n+2}=j\mid X_{n+1}=k, X_n=i)\,\mathbb{P}(X_{n+1}=k\mid X_n=i) \\
&=
\sum_k \mathbb{P}(X_{n+2}=j\mid X_{n+1}=k)\,\mathbb{P}(X_{n+1}=k\mid X_n=i)
&&\text{(Markov property drops the extra conditioning)}\\
&=
\sum_k q_{ik}\,q_{kj}.
\end{aligned}
$$

This sum is precisely the $(i,j)$ entry of $Q^2$ (row $i$ of $Q$ dotted with column $j$ of $Q$). More generally,

$$
\boxed{
\mathbb{P}(X_{n+m}=j\mid X_n=i) = \left(Q^{m}\right)_{ij}.
}
$$

---

## 5) Stationary Distributions (introduced, not yet solved)

A row vector $s$ (non-negative entries, $1\times M$, summing to $1$) is a **stationary distribution** for the chain if

$$
\boxed{
sQ = s.
}
$$

(For readers who know linear algebra: this is an eigenvector equation for $Q^\top$ with eigenvalue $1$, just written with the vector on the left.)

**Why "stationary."** By the result of Section 4, if $X_n\sim s$ and $sQ=s$, then $X_{n+1}\sim sQ = s$ too — and by induction $X_{n+m}\sim s$ for every $m$. Once the chain's distribution equals $s$, it stays $s$ forever.

The lecture poses, without yet resolving, the natural follow-up questions:

1. **Existence** — does a solution to $sQ=s$ with non-negative entries summing to $1$ exist?
2. **Uniqueness** — if it exists, is it the only one?
3. **Convergence** — does the chain's distribution actually approach $s$ in the long run, starting from an arbitrary initial distribution (not just from $s$ itself)?
4. **Computability** — solving $sQ=s$ directly is a linear system that can become intractable by hand (or even by brute-force computation) as $M$ grows; are there efficient ways to find $s$?

The lecture states that under mild conditions (to be made precise later in the course) the answers to (1)–(3) are yes: a stationary distribution exists, is unique, and the chain converges to it — so it does capture the long-run/steady-state behavior of the chain. Question (4) is left open here, with a preview that certain special classes of chains admit fast, matrix-free formulas for $s$ (upcoming material).

---

## 6) Context: Where Markov Chains Come From and Why They Matter

A few historical/motivational points from the lecture, kept brief since they're not derivations:

- Markov introduced these chains (~1906) partly to settle a philosophical dispute: some worried the Law of Large Numbers threatened free will, and a rival of Markov's argued human behavior escapes this because it isn't i.i.d. Markov's response was to prove a version of the LLN for a strictly more general, "one step beyond i.i.d." dependence structure — i.e. Markov chains — showing i.i.d. was never the essential ingredient.
- Markov's original worked example was a simple two-state chain: classifying successive letters of a Russian-novel text as vowel or consonant, and empirically estimating the transition probabilities between the two states.
- Markov chains now serve two quite different modern purposes:
  - **Direct modeling**: treating a real evolving system (physical, biological, social, financial, ...) as approximately Markovian — an empirical modeling choice to be judged case by case.
  - **Markov Chain Monte Carlo (MCMC)**: *constructing* a synthetic chain engineered so that its stationary distribution is some target distribution of interest, then simulating the chain on a computer to study that target distribution. This sidesteps any debate about whether the real-world process is Markovian, since the chain is built, not observed — and it underlies a huge share of modern computational statistics.

---

## Main Takeaways

- A Markov chain generalizes i.i.d. sequences by allowing dependence, but restricted to conditional independence of past and future given the present (the Markov property).
- All one-step behavior is packaged in the transition matrix $Q=(q_{ij})$, whose rows are non-negative and sum to $1$.
- Distributions propagate by right-multiplication: $X_n\sim s \implies X_{n+m}\sim sQ^m$; equivalently $\mathbb{P}(X_{n+m}=j\mid X_n=i) = (Q^m)_{ij}$.
- A stationary distribution satisfies $sQ=s$; under mild conditions it exists, is unique, and is the chain's long-run limiting distribution — but solving for it directly can be computationally hard in general.
- Transition matrix and stationary distribution are flagged as the two central concepts of the Markov chain unit.
- Markov chains support both descriptive modeling of dependent real-world systems and constructive use via MCMC, where the chain is engineered rather than observed.

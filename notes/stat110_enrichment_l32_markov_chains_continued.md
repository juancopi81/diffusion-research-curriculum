# Stat 110 (Blitzstein) - Lecture 32

**Lecture 32:** [Markov Chains Continued](https://www.youtube.com/watch?v=aBGOyZv2pZE&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=32)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** AI-assisted notes synthesized from the full lecture video (audio transcript + high-resolution blackboard frames, retrieved via Video Moment Finder). The state diagrams, theorem statements, detailed-balance proof, and network example were checked against captured frames; the prose below paraphrases the lecture rather than reproducing its transcript.

---

## 1) Recap: The Markov Property

A Markov chain is a stochastic process that moves among states and satisfies a conditional-independence property: given the present state, the past provides no further information about the future.

For a time-homogeneous chain $(X_n)$,

$$
\mathbb{P}(X_{n+1}=j\mid X_n=i,X_{n-1},\dots,X_0)
=
\mathbb{P}(X_{n+1}=j\mid X_n=i).
$$

Thus the transition matrix

$$
Q=(q_{ij}),
\qquad
q_{ij}=\mathbb{P}(X_{n+1}=j\mid X_n=i),
$$

contains all the information needed to propagate the chain. Throughout the lecture, the state space is finite.

---

## 2) Reading Long-Run Behavior from State Diagrams

The lecture begins with four diagrams that illustrate the main qualitative obstructions.

### Irreducibility

A chain is **irreducible** if every state can reach every other state with positive probability in some finite number of steps:

$$
\boxed{
\text{For every } i,j,\text{ there is an } n\ge 0\text{ such that }(Q^n)_{ij}>0.
}
$$

This does not require a direct one-step arrow from $i$ to $j$; a path of several transitions is enough.

A diagram consisting of two disconnected groups of states is reducible. It can often be studied by splitting it into irreducible components. If an arrow connects an upper component to a lower one but no path returns upward, the upper states may eventually be abandoned forever.

### Recurrent and transient states

A state $i$ is **recurrent** if a chain started at $i$ returns to $i$ with probability $1$. Otherwise it is **transient**.

Writing

$$
T_i^+=\inf\{n\ge 1:X_n=i\},
$$

the definitions are

$$
\mathbb{P}_i(T_i^+<\infty)=1
\quad\text{(recurrent)},
$$

and

$$
\mathbb{P}_i(T_i^+<\infty)<1
\quad\text{(transient)}.
$$

For a recurrent state, the Markov property lets the return argument restart each time the chain reaches $i$. Consequently, the chain returns to $i$ infinitely often with probability $1$.

For a finite irreducible chain, every state is recurrent. Intuitively, any route that has positive probability eventually gets repeated often enough to occur.

### Absorbing states and gambler's ruin

A state $i$ is **absorbing** when

$$
q_{ii}=1.
$$

Once entered, it can never be left. In the lecture's diagram the interior
states can step toward either absorbing endpoint, and each endpoint loops on
itself:

$$
0 \longleftarrow 1 \longleftrightarrow 2 \longrightarrow 3,
\qquad
0\to 0,
\qquad
3\to 3.
$$

The endpoints $0$ and $3$ are absorbing, and the interior states $1$ and $2$ are transient because the chain eventually reaches an endpoint and remains there. This is the gambler's ruin process viewed as a Markov chain: the endpoints represent one gambler or the other becoming bankrupt.

### Periodicity

In the deterministic three-cycle

$$
1\to 2\to 3\to 1,
$$

the chain is irreducible and every state is recurrent, but its position cycles predictably. If it starts at state $1$, it can return to state $1$ only after $3,6,9,\dots$ steps.

This is a **periodicity** obstruction. Irreducibility alone does not guarantee that the distribution at time $n$ converges as $n\to\infty$.

---

## 3) Stationary Distributions

A probability row vector

$$
s=(s_1,\dots,s_M)
$$

is a **stationary distribution** for a chain with transition matrix $Q$ if

$$
\boxed{
sQ=s.
}
$$

If $X_0\sim s$, then

$$
X_n\sim sQ^n=s
$$

for every $n$. This invariance explains the word *stationary*. Algebraically, $s$ is a left eigenvector of $Q$ with eigenvalue $1$, normalized to be a probability vector.

### The finite irreducible-chain theorem

For any irreducible Markov chain with finitely many states, the lecture states:

1. A stationary distribution $s$ exists.
2. The stationary distribution is unique.
3. Its entries satisfy

$$
\boxed{
s_i=\frac{1}{r_i},
}
$$

where

$$
r_i=\mathbb{E}_i(T_i^+)
$$

is the expected return time to state $i$ when the chain starts at $i$.

The reciprocal formula matches the long-run intuition: states visited frequently have short average return times. For example, if a chain spends a long-run fraction $1/10$ of its time at $i$, its average return time to $i$ is $10$ steps.

### When distributions converge to stationarity

The preceding three statements still hold for an irreducible periodic chain. To ensure convergence of the distribution from an arbitrary initial condition, periodicity must also be ruled out.

The lecture gives a convenient sufficient condition: if there is some $m$ such that every entry of $Q^m$ is strictly positive, then

$$
\boxed{
\mathbb{P}(X_n=i)\longrightarrow s_i
\quad\text{for every state }i,
}
$$

regardless of the initial distribution. In row-vector form, for any initial probability vector $t$,

$$
\boxed{
tQ^n\longrightarrow s.
}
$$

The positivity condition says that, after exactly $m$ steps, every state can reach every other state with positive probability. It is stronger than irreducibility and excludes the oscillating-zero pattern produced by a periodic chain.

---

## 4) Reversible Markov Chains

Directly solving $sQ=s$ can require a large linear system. Reversibility provides a more structural route.

A Markov chain with transition matrix $Q=(q_{ij})$ is **reversible with respect to** a probability vector $s$ if, for all states $i,j$,

$$
\boxed{
s_iq_{ij}=s_jq_{ji}.
}
$$

These are the **detailed-balance equations**. Each side represents stationary probability flow across the edge between $i$ and $j$: flow from $i$ to $j$ equals flow from $j$ to $i$.

### Time-reversal intuition

Suppose the chain starts with distribution $s$ and its trajectory is recorded. Reversibility means that the recorded process has the same probabilistic behavior when played backward. An observer could not infer the direction of time from the sequence of states alone.

### Detailed balance implies stationarity

Fix $j$ and sum the detailed-balance equation over all $i$:

$$
\begin{aligned}
\sum_i s_iq_{ij}
&=\sum_i s_jq_{ji} \\
&=s_j\sum_i q_{ji} \\
&=s_j.
\end{aligned}
$$

The final equality holds because row $j$ of $Q$ sums to $1$. The left side is the $j$-th entry of $sQ$, so this is true for every $j$ and therefore

$$
\boxed{
sQ=s.
}
$$

Hence any probability vector satisfying detailed balance is stationary. Reversibility is a stronger property than stationarity: detailed balance is sufficient, but a stationary chain need not be reversible.

---

## 5) Random Walk on an Undirected Network

Consider a connected undirected graph. At each step, the walker chooses uniformly among the edges incident to its current node. Let $d_i$ be the degree of node $i$.

For adjacent nodes $i$ and $j$,

$$
q_{ij}=\frac{1}{d_i},
\qquad
q_{ji}=\frac{1}{d_j}.
$$

Therefore

$$
d_iq_{ij}=1=d_jq_{ji}.
$$

If $i$ and $j$ are not adjacent, both transition probabilities are $0$, so the same equality still holds. Thus the degree vector satisfies the detailed-balance equations up to normalization.

The stationary distribution is

$$
\boxed{
s_i=\frac{d_i}{\sum_{j=1}^M d_j}.
}
$$

Since the sum of all degrees equals twice the number of edges,

$$
s_i=\frac{d_i}{2|E|}.
$$

This result requires no transition-matrix elimination and works for a graph of any finite size.

### Four-node lecture example

The board example has edges

$$
\{1,2\},\quad \{1,3\},\quad \{2,3\},\quad \{3,4\}.
$$

Its degrees are

$$
(d_1,d_2,d_3,d_4)=(2,2,3,1),
$$

so

$$
\sum_j d_j=8
$$

and

$$
\boxed{
s=\left(\frac14,\frac14,\frac38,\frac18\right).
}
$$

The higher-degree node $3$ receives the largest stationary mass because the random walk has more routes leading into and out of it.

---

## Main Takeaways

- Irreducibility means every state can reach every other state in finitely many steps with positive probability.
- Recurrent states are revisited with probability $1$; transient states are eventually left behind. In a finite irreducible chain, all states are recurrent.
- Absorbing states trap the chain, while periodicity can prevent the time-$n$ distribution from converging even when the chain is irreducible.
- Every finite irreducible chain has a unique stationary distribution, and $s_i=1/r_i$ links stationary mass to expected return time.
- If some power $Q^m$ is strictly positive, then every initial distribution converges to the stationary distribution.
- Detailed balance, $s_iq_{ij}=s_jq_{ji}$, implies stationarity and gives the time-reversal interpretation of reversible chains.
- For a simple random walk on a connected undirected graph, stationary probabilities are proportional to node degrees: $s_i=d_i/(2|E|)$.

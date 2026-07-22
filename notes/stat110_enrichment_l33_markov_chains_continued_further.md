# Stat 110 (Blitzstein) - Lecture 33

**Lecture 33:** [Markov Chains Continued Further](https://www.youtube.com/watch?v=Q-pCzTpwPBU&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=33)  
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source status:** AI-assisted notes synthesized from the full lecture video (audio transcript + high-resolution blackboard frames, retrieved via Video Moment Finder). The weighted-network derivation, reversible-chain representation, PageRank example, transition matrices, teleportation formula, and iterative computation were checked against captured frames; the prose below paraphrases the lecture rather than reproducing its transcript.

---

## 1) Weighted Random Walks on Undirected Networks

Lecture 32 showed that a simple random walk on a finite, connected, undirected graph has stationary probability proportional to node degree. Lecture 33 begins by allowing different edges to have different strengths.

Assign a nonnegative weight $w_{ij}$ to the edge between states $i$ and $j$, with

$$
w_{ij}=0 \quad \text{if there is no edge between }i\text{ and }j,
$$

and impose the symmetry condition

$$
\boxed{w_{ij}=w_{ji}.}
$$

From state $i$, choose the next state with probability proportional to the available edge weights. If

$$
w_i=\sum_k w_{ik}
$$

is the total weight incident to $i$, then

$$
\boxed{q_{ij}=\frac{w_{ij}}{w_i}=\frac{w_{ij}}{\sum_k w_{ik}}.}
$$

The unweighted walk is the special case in which every present edge has weight $1$. Then $w_i$ is the ordinary degree of node $i$.

### Stationary distribution

The weighted degree replaces ordinary degree. Let

$$
W=\sum_\ell w_\ell=\sum_\ell\sum_k w_{\ell k}.
$$

Define

$$
s_i=\frac{w_i}{W}.
$$

Then

$$
s_iq_{ij}
=\frac{w_i}{W}\frac{w_{ij}}{w_i}
=\frac{w_{ij}}{W}
=\frac{w_{ji}}{W}
=s_jq_{ji}.
$$

Thus detailed balance holds, so the chain is reversible and $s$ is stationary:

$$
\boxed{
s_i=\frac{\sum_k w_{ik}}{\sum_\ell\sum_k w_{\ell k}}
\propto \sum_k w_{ik}.
}
$$

The calculation avoids solving the linear system $sQ=s$ directly.

---

## 2) Every Reversible Chain Is a Weighted Undirected Walk

The weighted-network construction is not merely one example. Any reversible Markov chain with a positive stationary distribution can be represented this way.

Suppose $Q=(q_{ij})$ is reversible with respect to $s$, so

$$
s_iq_{ij}=s_jq_{ji}.
$$

Define edge weights by the stationary flow

$$
\boxed{w_{ij}=s_iq_{ij}.}
$$

Detailed balance gives

$$
w_{ij}=s_iq_{ij}=s_jq_{ji}=w_{ji},
$$

so the weights are symmetric. Moreover,

$$
\sum_k w_{ik}
=\sum_k s_iq_{ik}
=s_i\sum_k q_{ik}
=s_i.
$$

The weighted random walk therefore recovers the original transition probabilities:

$$
\frac{w_{ij}}{\sum_k w_{ik}}
=\frac{s_iq_{ij}}{s_i}
=q_{ij}.
$$

This gives a concrete interpretation of reversibility: the symmetric weights describe equilibrium traffic across undirected edges.

---

## 3) A Non-Reversible Example: The Web as a Directed Network

The lecture then turns to Google PageRank as an important non-reversible Markov chain. Web pages are states and hyperlinks are directed edges. Since page $i$ may link to page $j$ without $j$ linking back, the resulting graph generally cannot satisfy the symmetric-edge picture above.

The board example uses four pages with links

$$
1\to 2,\qquad 1\to 3,\qquad
2\to 1,\qquad 2\to 3,\qquad
3\to 4,
$$

while page $4$ has no outgoing links.

The basic random-surfer transition rule is:

- From a page with outgoing links, choose one uniformly.
- From a page with no outgoing links, called a **dangling page**, jump uniformly to any page so the row still sums to $1$.

For the four-page example,

$$
Q=
\begin{pmatrix}
0 & \tfrac12 & \tfrac12 & 0 \\
\tfrac12 & 0 & \tfrac12 & 0 \\
0 & 0 & 0 & 1 \\
\tfrac14 & \tfrac14 & \tfrac14 & \tfrac14
\end{pmatrix}.
$$

This matrix is not reversible: its directed transitions include one-way flows such as $3\to4$.

---

## 4) PageRank as Recursive Importance

Counting incoming links treats every recommendation as equally valuable. PageRank instead uses two ideas:

1. A link from an important page should contribute more than a link from an unimportant page.
2. A page's recommendation should be diluted across all of its outgoing links.

Let $s_j$ be the importance score of page $j$. The recursive definition is

$$
\boxed{s_j=\sum_i s_iq_{ij}.}
$$

In row-vector notation,

$$
\boxed{s=sQ.}
$$

After normalization, the PageRank score vector is therefore a stationary distribution of the random web-surfing chain.

This resolves the apparent circularity in defining importance using the importance of linking pages: the scores are determined simultaneously as a left eigenvector of $Q$ with eigenvalue $1$.

### Random-surfer interpretation

If the chain has suitable long-run behavior, $s_j$ is the long-run fraction of time a random surfer spends on page $j$. Pages that receive more stationary traffic receive larger ranks.

The probability interpretation is more than a metaphor. It suggests a computational method that scales better than directly solving an enormous linear system.

---

## 5) Teleportation and the Google Matrix

The raw link-following chain $Q$ can be reducible or periodic. Some groups of pages may be unreachable from others, and the chain need not converge to a unique stationary distribution from every starting point.

PageRank repairs this by mixing link-following with **teleportation**. Let

- $M$ be the number of pages,
- $J$ be the $M\times M$ all-ones matrix,
- $0<\alpha<1$ be the probability of following a link.

The Google transition matrix is

$$
\boxed{
G=\alpha Q+(1-\alpha)\frac{J}{M}.
}
$$

At each step, the surfer:

- follows the $Q$ transition with probability $\alpha$;
- jumps to a uniformly random page with probability $1-\alpha$.

The original PageRank proposal discussed in the lecture suggested

$$
\alpha=0.85,
$$

so the model follows a link $85\%$ of the time and teleports $15\%$ of the time.

Every entry of $G$ is strictly positive because

$$
g_{ij}\ge \frac{1-\alpha}{M}>0.
$$

Consequently, the finite chain is irreducible and aperiodic. It has a unique stationary distribution, and the distribution converges to it from any initial distribution. Each individual teleportation probability can be tiny when $M$ is large, yet the term gives strong theoretical guarantees.

---

## 6) Computing PageRank by Running the Chain

For $M$ pages, direct Gaussian elimination on $s=sG$ has cubic-order cost in $M$, which is impractical at web scale. The Markov-chain convergence theorem suggests **power iteration** instead.

Let $t$ be any initial probability row vector. After $n$ steps, the distribution is

$$
tG^n.
$$

One update has the form

$$
tG
=\alpha tQ+(1-\alpha)\frac{tJ}{M}.
$$

Since the entries of $t$ sum to $1$,

$$
tJ=(1,1,\dots,1),
$$

and therefore

$$
\boxed{
tG=\alpha tQ+(1-\alpha)u,
}
$$

where

$$
u=\left(\frac1M,\dots,\frac1M\right)
$$

is the uniform distribution.

Repeatedly use the new probability vector as the next input:

$$
t,\quad tG,\quad tG^2,\quad \dots,\quad tG^n.
$$

Because $G$ is strictly positive,

$$
\boxed{
tG^n\longrightarrow s
\quad\text{as }n\to\infty,
}
$$

where $s$ is the PageRank vector.

### Why the multiplication is feasible

Although $Q$ is enormous, it is sparse: a typical page links to only a tiny fraction of all pages. A sparse representation stores and multiplies only the nonzero link probabilities. The teleportation term is also cheap because it reduces to adding a multiple of the uniform vector.

In practice, the iteration is run until the rank vector appears stable enough for the required approximation. Determining exact convergence rates for a web-scale chain is a separate and difficult question.

---

## 7) Reversible and Non-Reversible Chains in Perspective

The two halves of the lecture highlight different advantages:

- **Reversibility** converts global stationarity into local flow balance. For weighted undirected walks, the stationary distribution follows immediately from weighted degrees.
- **Non-reversible chains** may lack a closed-form stationary distribution, but convergence can still turn the probabilistic process into an algorithm.
- **Model design matters.** The teleportation term is not merely computational decoration; it changes the chain so existence, uniqueness, and convergence are guaranteed.

PageRank is therefore both a modeling example and a computational one: a recursive ranking problem becomes a stationary-distribution problem, and repeated Markov transitions approximate its solution.

---

## Main Takeaways

- A weighted random walk on an undirected graph uses $q_{ij}=w_{ij}/\sum_k w_{ik}$ with symmetric weights $w_{ij}=w_{ji}$.
- Its stationary distribution is proportional to weighted degree: $s_i\propto\sum_k w_{ik}$.
- Every reversible chain can be represented as a weighted undirected walk by setting $w_{ij}=s_iq_{ij}$.
- PageRank models web pages as states and hyperlinks as directed transitions; its score equation $s=sQ$ is a stationarity equation.
- Dangling pages are handled by replacing their transition row with a uniform distribution.
- The Google matrix $G=\alpha Q+(1-\alpha)J/M$ mixes link-following with uniform teleportation.
- Teleportation makes every entry of $G$ positive, guaranteeing a unique stationary distribution and convergence from any start.
- Sparse power iteration computes PageRank through $tG^n\to s$, avoiding direct solution of a web-scale linear system.

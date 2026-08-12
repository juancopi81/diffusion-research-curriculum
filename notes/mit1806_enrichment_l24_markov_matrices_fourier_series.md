# MIT 18.06 (Strang) - Lecture 24

**Lecture 24:** [Markov Matrices; Fourier Series](https://www.youtube.com/watch?v=8MF3pz-oYHo)

**Course:** 18.06 Linear Algebra (MIT OpenCourseWare) - Prof. Gilbert Strang

**Related enrichment:** [Stat 110 Lecture 31](./stat110_enrichment_l31_markov_chains.md), [Lecture 32](./stat110_enrichment_l32_markov_chains_continued.md), and [Lecture 33](./stat110_enrichment_l33_markov_chains_continued_further.md)

**Source status:** AI-assisted notes synthesized from the full lecture video (audio transcript + 13 high-resolution blackboard frames, retrieved via Video Moment Finder). The Markov matrices, eigenvector calculations, population model, orthonormal-expansion identities, and Fourier coefficient derivation were checked against captured frames; the prose below paraphrases the lecture rather than reproducing its transcript.

---

## 1) Markov Matrices in the Column-Vector Convention

Strang calls a square matrix $A$ a **Markov matrix** when it has two properties:

1. Every entry is nonnegative: $a_{ij}\ge 0$.
2. Every column sums to $1$.

The lecture's first example is

$$
A=
\begin{pmatrix}
0.1 & 0.01 & 0.3 \\
0.2 & 0.99 & 0.3 \\
0.7 & 0 & 0.4
\end{pmatrix}.
$$

Each column is a probability distribution describing where the members of one current state go next. If $u_k$ is a column vector of populations or probabilities at time $k$, the evolution rule is

$$
\boxed{u_{k+1}=Au_k.}
$$

Nonnegativity ensures that $u_{k+1}$ remains nonnegative. The column-sum condition conserves total mass:

$$
\mathbf{1}^{\mathsf T}u_{k+1}
=\mathbf{1}^{\mathsf T}Au_k
=\mathbf{1}^{\mathsf T}u_k,
$$

where $\mathbf{1}=(1,\dots,1)^{\mathsf T}$. Products and powers of Markov matrices are therefore Markov matrices too.

---

## 2) Why $\lambda=1$ Is Always an Eigenvalue

Because the columns of $A$ sum to $1$,

$$
\mathbf{1}^{\mathsf T}A=\mathbf{1}^{\mathsf T}.
$$

Equivalently,

$$
\mathbf{1}^{\mathsf T}(A-I)=0.
$$

Thus the rows of $A-I$ are linearly dependent: $\mathbf{1}$ lies in the left nullspace of $A-I$. Hence $A-I$ is singular, so

$$
\boxed{\lambda=1\text{ is an eigenvalue of }A.}
$$

The board demonstrates this with

$$
A-I=
\begin{pmatrix}
-0.9 & 0.01 & 0.3 \\
0.2 & -0.01 & 0.3 \\
0.7 & 0 & -0.6
\end{pmatrix},
$$

whose columns all sum to zero.

Another way to express the same argument is

$$
A^{\mathsf T}\mathbf{1}=\mathbf{1}.
$$

So $1$ is visibly an eigenvalue of $A^{\mathsf T}$. Since a matrix and its transpose have the same characteristic polynomial,

$$
\det(A-\lambda I)
=\det\big((A-\lambda I)^{\mathsf T}\big)
=\det(A^{\mathsf T}-\lambda I),
$$

it is also an eigenvalue of $A$.

### Why no eigenvalue can have magnitude greater than $1$

For a column-stochastic matrix,

$$
\|A\|_1
=\max_j\sum_i |a_{ij}|
=1.
$$

If $Ax=\lambda x$, then

$$
|\lambda|\,\|x\|_1
=\|Ax\|_1
\le \|A\|_1\|x\|_1
=\|x\|_1,
$$

so

$$
\boxed{|\lambda|\le 1\text{ for every eigenvalue of }A.}
$$

The inequality need not be strict for every eigenvalue. Additional eigenvalues on the unit circle can produce periodic behavior instead of convergence.

---

## 3) Matrix Powers and the Steady State

Assume for the moment that $A$ has a complete set of eigenvectors and write the initial state as

$$
u_0=c_1x_1+c_2x_2+\cdots+c_nx_n,
$$

where $Ax_i=\lambda_i x_i$. Then

$$
u_k=A^ku_0
=c_1\lambda_1^k x_1
+c_2\lambda_2^k x_2
+\cdots
+c_n\lambda_n^k x_n.
$$

Take $\lambda_1=1$. If all other eigenvalues satisfy $|\lambda_i|<1$, then their contributions vanish:

$$
\lambda_i^k\longrightarrow 0
\qquad (i\ge 2).
$$

Therefore

$$
\boxed{u_k\longrightarrow c_1x_1,}
$$

where $x_1$ satisfies

$$
Ax_1=x_1.
$$

This eigenvector is the **steady state**. For a Markov matrix it can be chosen nonnegative; under stronger connectivity assumptions it is strictly positive and, after normalization, gives the unique stationary distribution.

The convergence qualifications matter:

- Multiple independent eigenvectors with $\lambda=1$ can make the steady state nonunique.
- Another eigenvalue with $|\lambda|=1$, such as $\lambda=-1$, can make the state oscillate.
- The displayed eigenvector expansion assumes enough eigenvectors to diagonalize $A$.

These are the linear-algebra versions of reducibility and periodicity in the Stat 110 treatment.

---

## 4) The Three-State Steady Vector

For the lecture's first matrix, solving

$$
(A-I)x_1=0
$$

gives the positive eigenvector

$$
x_1=
\begin{pmatrix}
0.6 \\
33 \\
0.7
\end{pmatrix}.
$$

The unusually large middle component is consistent with the $0.99$ probability of remaining in state $2$. To turn the eigenvector into a probability vector, scale it so its entries sum to $1$. Multiplying by $10$ first gives $(6,330,7)^{\mathsf T}$, whose entries sum to $343$. Thus

$$
\boxed{
\pi=
\begin{pmatrix}
6/343 \\
330/343 \\
7/343
\end{pmatrix},
\qquad
A\pi=\pi.
}
$$

---

## 5) Population Migration: California and Massachusetts

The main application models a fixed population moving between two states. Let

$$
u_k=
\begin{pmatrix}
u_{\mathrm{Cal},k} \\
u_{\mathrm{Mass},k}
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
0.9 & 0.2 \\
0.1 & 0.8
\end{pmatrix}.
$$

The first column says that each year $90\%$ of California's population stays and $10\%$ moves to Massachusetts. The second says that $80\%$ of Massachusetts's population stays and $20\%$ moves to California. Because both columns sum to $1$, the model loses or creates no people.

Starting with all $1000$ people in Massachusetts,

$$
u_0=
\begin{pmatrix}
0 \\
1000
\end{pmatrix},
\qquad
u_1=Au_0=
\begin{pmatrix}
200 \\
800
\end{pmatrix}.
$$

The eigenvalues and eigenvectors are

$$
\lambda_1=1,
\qquad
x_1=
\begin{pmatrix}
2 \\
1
\end{pmatrix},
$$

and

$$
\lambda_2=0.7,
\qquad
x_2=
\begin{pmatrix}
-1 \\
1
\end{pmatrix}.
$$

Expanding the initial state in this eigenbasis gives

$$
u_0
=\frac{1000}{3}
\begin{pmatrix}
2 \\
1
\end{pmatrix}
+\frac{2000}{3}
\begin{pmatrix}
-1 \\
1
\end{pmatrix}.
$$

After $k$ years,

$$
\boxed{
u_k
=\frac{1000}{3}
\begin{pmatrix}
2 \\
1
\end{pmatrix}
+\frac{2000}{3}(0.7)^k
\begin{pmatrix}
-1 \\
1
\end{pmatrix}.
}
$$

The second term is the transient part. Since $(0.7)^k\to0$,

$$
\boxed{
u_k\longrightarrow
\begin{pmatrix}
2000/3 \\
1000/3
\end{pmatrix}.
}
$$

The total remains $1000$, while the long-run split approaches two-thirds in California and one-third in Massachusetts.

---

## 6) Connecting the MIT and Stat 110 Conventions

The MIT and Stat 110 notes describe the same process with transposed bookkeeping:

| Object | MIT 18.06 convention | Stat 110 convention |
|---|---|---|
| State distribution | Column vector $u_k$ | Row vector $s_k$ |
| Transition matrix | Columns of $A$ sum to $1$ | Rows of $Q$ sum to $1$ |
| Evolution | $u_{k+1}=Au_k$ | $s_{k+1}=s_kQ$ |
| Steady state | $Ax=x$ | $sQ=s$ |
| Conversion | $Q=A^{\mathsf T}$ | $s=x^{\mathsf T}$ |

Thus the right eigenvector in the MIT notes and the left eigenvector in the Stat 110 notes are the same stationary distribution after transposition and normalization. The probability course emphasizes Markov dependence, recurrence, periodicity, and long-run interpretation; this lecture exposes the eigenvalue mechanism that drives the same convergence.

---

## 7) Orthonormal Bases Make Projection Coefficients Easy

The lecture then changes topics from Markov matrices to projections. Suppose $q_1,\dots,q_n$ form an orthonormal basis and

$$
v=x_1q_1+x_2q_2+\cdots+x_nq_n.
$$

Taking the inner product with $q_i$ eliminates all other terms:

$$
q_i^{\mathsf T}v
=x_iq_i^{\mathsf T}q_i
+\sum_{j\ne i}x_jq_i^{\mathsf T}q_j
=x_i.
$$

Therefore

$$
\boxed{x_i=q_i^{\mathsf T}v.}
$$

In matrix form, let

$$
Q=
\begin{pmatrix}
q_1 & q_2 & \cdots & q_n
\end{pmatrix}.
$$

Then

$$
Qx=v,
\qquad
Q^{-1}=Q^{\mathsf T},
$$

so

$$
\boxed{x=Q^{\mathsf T}v.}
$$

This finite-dimensional expansion is the template for Fourier series.

---

## 8) Fourier Series as Projection in Function Space

For a $2\pi$-periodic function, the Fourier expansion has the form

$$
f(x)
=a_0
+\sum_{n=1}^{\infty}
\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$

The vectors are now functions, so the vector dot product becomes a function inner product:

$$
\boxed{
\langle f,g\rangle
=\int_0^{2\pi}f(x)g(x)\,dx.
}
$$

Under this inner product, the functions

$$
1,\ \cos x,\ \sin x,\ \cos 2x,\ \sin 2x,\dots
$$

are mutually orthogonal. For example,

$$
\int_0^{2\pi}\sin x\cos x\,dx
=\left.\frac12\sin^2x\right|_0^{2\pi}
=0.
$$

The unscaled trigonometric functions are **orthogonal**, but not normalized:

$$
\langle 1,1\rangle=2\pi,
$$

and, for $n\ge1$,

$$
\langle \cos(nx),\cos(nx)\rangle
=\langle \sin(nx),\sin(nx)\rangle
=\pi.
$$

They become orthonormal after scaling $1$ by $1/\sqrt{2\pi}$ and the sine and cosine functions by $1/\sqrt{\pi}$.

### Extracting the coefficients

To isolate $a_1$, take the inner product of the whole series with $\cos x$. Orthogonality removes every term except $a_1\cos x$:

$$
\int_0^{2\pi}f(x)\cos x\,dx
=a_1\int_0^{2\pi}\cos^2x\,dx
=a_1\pi.
$$

Hence

$$
\boxed{
a_1=\frac1\pi\int_0^{2\pi}f(x)\cos x\,dx.
}
$$

The same projection argument gives the general formulas

$$
\boxed{
a_0=\frac{1}{2\pi}\int_0^{2\pi}f(x)\,dx,
}
$$

$$
\boxed{
a_n=\frac1\pi\int_0^{2\pi}f(x)\cos(nx)\,dx,
\qquad
b_n=\frac1\pi\int_0^{2\pi}f(x)\sin(nx)\,dx
\quad (n\ge1).
}
$$

So a Fourier coefficient is not a new kind of object: it is the projection coefficient of a function onto an orthogonal basis direction, divided by that direction's squared norm.

---

## Main Takeaways

- A column-stochastic Markov matrix has nonnegative entries and columns summing to $1$; it propagates column states by $u_{k+1}=Au_k$ while conserving total mass.
- The column-sum condition gives $\mathbf{1}^{\mathsf T}A=\mathbf{1}^{\mathsf T}$, forcing $\lambda=1$ to be an eigenvalue.
- Every eigenvalue satisfies $|\lambda|\le1$. When $1$ is the only non-decaying eigenvalue, powers $A^ku_0$ approach the eigenvector component associated with $\lambda=1$.
- In the migration example, the transient mode decays as $(0.7)^k$ and the population approaches a two-thirds/one-third steady split.
- MIT's column-stochastic/right-eigenvector convention is the transpose of Stat 110's row-stochastic/left-eigenvector convention.
- An orthonormal basis makes expansion coefficients simple inner products: $x_i=q_i^{\mathsf T}v$.
- Fourier series carry the same projection idea into an infinite-dimensional function space, replacing finite sums with integrals.
- The Fourier coefficient formulas follow directly from the orthogonality of $1$, $\cos(nx)$, and $\sin(nx)$ on $[0,2\pi]$.

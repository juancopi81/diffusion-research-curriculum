# Week 5 — S2 (Stat110 Practice): Joint/Conditional/Marginal + Covariance/Correlation

**Topics:** joint distributions, marginal distributions, conditional distributions, independence, covariance, correlation  
**Resources:**

- [Stat110 Strategic Practice and Homework 7](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_7.pdf)
- [Stat110 Strategic Practice and Homework 8](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_8.pdf)

---

## Strategic Practice 7 — Joint, Conditional, and Marginal Distributions

## Practice 7 — Problem 1

**Prompt.**  
A random point $(X, Y, Z)$ is chosen uniformly in the ball

$$
B=\{(x,y,z): x^2+y^2+z^2\le 1\}.
$$

1. Find the joint PDF of $X, Y, Z$.
2. Find the joint PDF of $X, Y$.
3. Find an expression for the marginal PDF of $X$, as an integral.

### My attempt

Since the point is chosen **uniformly** in the ball, the density must be **constant inside the ball** and $0$ outside. So let

$$
f_{X,Y,Z}(x,y,z)=
\begin{cases}
c, & (x,y,z)\in B,\\
0, & \text{otherwise}.
\end{cases}
$$

To determine $c$, use that the total probability must be $1$:

$$
\iiint_{\mathbb{R}^3} f_{X,Y,Z}(x,y,z)\,dV = 1.
$$

Because the density is constant on the ball,

$$
c\cdot \mathrm{Vol}(B)=1.
$$

The ball has radius $1$, so

$$
\mathrm{Vol}(B)=\frac{4}{3}\pi.
$$

Hence

$$
c=\frac{1}{\frac{4}{3}\pi}=\frac{3}{4\pi}.
$$

Therefore,

$$
f_{X,Y,Z}(x,y,z)=
\begin{cases}
\dfrac{3}{4\pi}, & x^2+y^2+z^2\le 1,\\[6pt]
0, & \text{otherwise}.
\end{cases}
$$

For part (b), we integrate out $z$:

$$
f_{X,Y}(x,y)=\int_{-\infty}^{\infty} f_{X,Y,Z}(x,y,z)\,dz.
$$

For fixed $(x,y)$, the allowed values of $z$ must satisfy

$$
x^2+y^2+z^2\le 1,
$$

so

$$
z^2\le 1-x^2-y^2.
$$

Thus, real $z$ exist only when

$$
x^2+y^2\le 1,
$$

and then

$$
-\sqrt{1-x^2-y^2}\le z\le \sqrt{1-x^2-y^2}.
$$

So

$$
f_{X,Y}(x,y)
=\int_{-\sqrt{1-x^2-y^2}}^{\sqrt{1-x^2-y^2}} \frac{3}{4\pi}\,dz
=\frac{3}{2\pi}\sqrt{1-x^2-y^2},
$$

for $x^2+y^2\le 1$, and $0$ otherwise. Hence

$$
f_{X,Y}(x,y)=
\begin{cases}
\dfrac{3}{2\pi}\sqrt{1-x^2-y^2}, & x^2+y^2\le 1,\\[6pt]
0, & \text{otherwise}.
\end{cases}
$$

For part (c), we integrate out $y$ from the joint PDF of $X,Y$:

$$
f_X(x)=\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy.
$$

For fixed $x$, the support condition is

$$
x^2+y^2\le 1,
$$

so

$$
-\sqrt{1-x^2}\le y\le \sqrt{1-x^2},
\qquad -1\le x\le 1.
$$

Therefore,

$$
f_X(x)=\frac{3}{2\pi}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \sqrt{1-x^2-y^2}\,dy,
\qquad -1\le x\le 1,
$$

and $f_X(x)=0$ otherwise.

### What I initially missed / corrected

- I first wrote separate bounds like $0\le x,y,z\le 1$, but that describes part of a **cube**, not the ball.
  The correct support is

  $$
  x^2+y^2+z^2\le 1.
  $$

- For the marginal $f_{X,Y}(x,y)$, I needed to understand why

  $$
  x^2+y^2\le 1.
  $$

  This is because for fixed $(x,y)$, there must exist at least one real $z$ such that

  $$
  x^2+y^2+z^2\le 1.
  $$

  That is only possible when

  $$
  1-x^2-y^2\ge 0.
  $$

- For the marginal $f_X(x)$, my bounds got mixed because I was trying to let the $y$-bounds depend on $z$ and the $z$-bounds depend on $y$ at the same time.
  In an iterated integral, I must choose one order and keep the outer limits independent of the inner variable.

- A cleaner route is:
  $$
  f_{X,Y,Z}\to f_{X,Y}\to f_X.
  $$

### Book's solution (for comparison)

The book gives:

$$
f_{X,Y,Z}(x,y,z)=
\begin{cases}
\dfrac{3}{4\pi}, & x^2+y^2+z^2\le 1,\\[6pt]
0, & \text{otherwise},
\end{cases}
$$

and then

$$
f_{X,Y}(x,y)
=\int_{-\sqrt{1-x^2-y^2}}^{\sqrt{1-x^2-y^2}} \frac{3}{4\pi}\,dz
=\frac{3}{2\pi}\sqrt{1-x^2-y^2},
$$

for $x^2+y^2\le 1$.

Finally, it writes the marginal of $X$ as

$$
f_X(x)=\frac{3}{2\pi}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \sqrt{1-x^2-y^2}\,dy,
\qquad -1\le x\le 1.
$$

This matches the derivation above.

### Memory card (quick review)

- **Uniform in a region** means density is constant on that region and $0$ outside.
- In 1D:
  $$
  \text{density}=\frac{1}{\text{length}}.
  $$
- In 2D:
  $$
  \text{density}=\frac{1}{\text{area}}.
  $$
- In 3D:

  $$
  \text{density}=\frac{1}{\text{volume}}.
  $$

- For this problem, the unit ball has volume

  $$
  \frac{4}{3}\pi,
  $$

  so the constant density is

  $$
  \frac{3}{4\pi}.
  $$

- To get a marginal, integrate out the unwanted variable(s):

  $$
  f_{X,Y}(x,y)=\int f_{X,Y,Z}(x,y,z)\,dz,
  \qquad
  f_X(x)=\int f_{X,Y}(x,y)\,dy.
  $$

- Support matters:
  - $(x,y,z)$ lives in the ball:
    $$
    x^2+y^2+z^2\le 1.
    $$
  - $(x,y)$ lives in the disk:
    $$
    x^2+y^2\le 1.
    $$
  - $x$ lives in the interval:
    $$
    -1\le x\le 1.
    $$

- Final answers:
  $$
  f_{X,Y,Z}(x,y,z)=
  \begin{cases}
  \dfrac{3}{4\pi}, & x^2+y^2+z^2\le 1,\\[6pt]
  0, & \text{otherwise},
  \end{cases}
  $$
  $$
  f_{X,Y}(x,y)=
  \begin{cases}
  \dfrac{3}{2\pi}\sqrt{1-x^2-y^2}, & x^2+y^2\le 1,\\[6pt]
  0, & \text{otherwise},
  \end{cases}
  $$
  $$
  f_X(x)=\frac{3}{2\pi}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \sqrt{1-x^2-y^2}\,dy,
  \qquad -1\le x\le 1,
  $$
  and $f_X(x)=0$ otherwise.

## Practice 7 — Problem 3

**Prompt.**  
Let $U_1, U_2, U_3$ be i.i.d. $\mathrm{Unif}(0,1)$, and let

$$
L=\min(U_1,U_2,U_3), \qquad M=\max(U_1,U_2,U_3).
$$

1. Find the marginal CDF and marginal PDF of $M$, and the joint CDF and joint PDF of $L, M$.
2. Find the conditional PDF of $M$ given $L$.

### My attempt

The easiest place to start is the maximum:

$$
M=\max(U_1,U_2,U_3).
$$

To get its CDF, write the event directly:

$$
F_M(m)=P(M\le m).
$$

But $M\le m$ means that **all three** uniforms are at most $m$, so

$$
P(M\le m)=P(U_1\le m,\;U_2\le m,\;U_3\le m).
$$

Since the $U_i$ are independent and each is $\mathrm{Unif}(0,1)$,

$$
P(U_i\le m)=m \qquad \text{for } 0\le m\le 1.
$$

Therefore,

$$
F_M(m)=
\begin{cases}
0, & m<0,\\[4pt]
m^3, & 0\le m\le 1,\\[4pt]
1, & m>1.
\end{cases}
$$

Differentiating on the interior gives the marginal PDF of $M$:

$$
f_M(m)=
\begin{cases}
3m^2, & 0<m<1,\\[4pt]
0, & \text{otherwise}.
\end{cases}
$$

Now consider the joint CDF

$$
F_{L,M}(l,m)=P(L\le l,\;M\le m).
$$

On the main region $0\le l\le m\le 1$, it is convenient to subtract the complementary part inside $\{M\le m\}$:

$$
P(L\le l,\;M\le m)=P(M\le m)-P(L>l,\;M\le m).
$$

The event $L>l$ means all three uniforms are greater than $l$, while $M\le m$ means all three are at most $m$. So together this means all three fall in $(l,m]$, and hence

$$
P(L>l,\;M\le m)=P(l<U_1\le m,\;l<U_2\le m,\;l<U_3\le m)=(m-l)^3.
$$

Thus, for $0\le l\le m\le 1$,

$$
F_{L,M}(l,m)=m^3-(m-l)^3.
$$

To write the full joint CDF, we also need the other regions:

$$
F_{L,M}(l,m)=
\begin{cases}
0, & l<0 \text{ or } m<0,\\[4pt]
m^3-(m-l)^3, & 0\le l\le m\le 1,\\[4pt]
m^3, & 0\le m\le 1,\; l\ge m,\\[4pt]
1-(1-l)^3, & m>1,\; 0\le l\le 1,\\[4pt]
1, & l>1,\; m>1.
\end{cases}
$$

The joint PDF comes from differentiating on the interior of the support:

$$
0<l<m<1.
$$

There,

$$
f_{L,M}(l,m)=\frac{\partial^2}{\partial l\,\partial m}\big[m^3-(m-l)^3\big]=6(m-l).
$$

So

$$
f_{L,M}(l,m)=
\begin{cases}
6(m-l), & 0<l<m<1,\\[4pt]
0, & \text{otherwise}.
\end{cases}
$$

For the conditional PDF of $M$ given $L$, first find the marginal PDF of $L$. Since

$$
P(L>l)=P(U_1>l,\;U_2>l,\;U_3>l)=(1-l)^3
\qquad \text{for } 0\le l\le 1,
$$

we get

$$
F_L(l)=P(L\le l)=1-(1-l)^3,
$$

and hence

$$
f_L(l)=
\begin{cases}
3(1-l)^2, & 0<l<1,\\[4pt]
0, & \text{otherwise}.
\end{cases}
$$

Therefore,

$$
f_{M\mid L}(m\mid l)=\frac{f_{L,M}(l,m)}{f_L(l)}
=\frac{6(m-l)}{3(1-l)^2}
=\frac{2(m-l)}{(1-l)^2},
$$

for $0<l<1$ and $l<m<1$, and $0$ otherwise.

### What I initially missed / corrected

- For max/min problems, the first job is to translate the event correctly:
  - $M\le m$ means **all three** $U_i$ are at most $m$.
  - $L>l$ means **all three** $U_i$ are greater than $l$.

- The CDF route is the cleanest starting point for extrema.
  Trying to think about the density of $\max(U_1,U_2,U_3)$ directly is much harder than first writing $P(M\le m)$.

- The pair $(L,M)$ does not live on the whole square $[0,1]^2$.
  Its support is the triangular region

  $$
  0\le l\le m\le 1,
  $$

  because a minimum cannot exceed a maximum.

- The formula

  $$
  m^3-(m-l)^3
  $$

  is only the joint CDF on the main region $0\le l\le m\le 1$.
  Outside that region, the logic changes:
  - if $l\ge m$, then $M\le m$ already forces $L\le l$;
  - if $m>1$, then $M\le m$ is automatic;
  - if $l<0$ or $m<0$, the event is impossible.

- For the conditional density, use **density over density**:

  $$
  f_{M\mid L}(m\mid l)=\frac{f_{L,M}(l,m)}{f_L(l)}.
  $$

  The conditional PDF uses the joint PDF in the numerator, not the joint CDF.

### Book's solution (for comparison)

Source status: partial. The book excerpt you shared verifies the core formulas below.

The book's solution follows the same event-translation strategy:

- Since $M\le m$ means all three $U_j$ are at most $m$,

  $$
  F_M(m)=m^3
  \qquad \text{for } 0\le m\le 1,
  $$

  so

  $$
  f_M(m)=3m^2.
  $$

- Since $L>l$ and $M\le m$ means all three $U_j$ fall between $l$ and $m$,

  $$
  P(L>l,\;M\le m)=(m-l)^3
  \qquad \text{for } 0\le l\le m\le 1.
  $$

- Therefore,

  $$
  F_{L,M}(l,m)=P(L\le l,\;M\le m)=m^3-(m-l)^3
  \qquad \text{for } 0\le l\le m\le 1,
  $$

  and differentiating gives

  $$
  f_{L,M}(l,m)=6(m-l)
  \qquad \text{for } 0<l<m<1.
  $$

- For the conditional part, the marginal density of $L$ is

  $$
  f_L(l)=3(1-l)^2,
  $$

  so

  $$
  f_{M\mid L}(m\mid l)=\frac{2(m-l)}{(1-l)^2}
  \qquad \text{for } 0<l<1,\; l<m<1.
  $$

### Memory card (quick review)

- For a maximum:
  $$
  P(\max\le m)=P(\text{all are }\le m).
  $$

- For a minimum:
  $$
  P(\min>l)=P(\text{all are }>l).
  $$

- For i.i.d. $\mathrm{Unif}(0,1)$ variables, interval probabilities are lengths:
  $$
  P(l<U\le m)=m-l.
  $$

- The support of $(L,M)$ is
  $$
  0\le l\le m\le 1.
  $$

- Joint PDF:
  $$
  f_{L,M}(l,m)=6(m-l)
  \quad \text{on } 0<l<m<1.
  $$

- Conditional PDF:
  $$
  f_{M\mid L}(m\mid l)=\frac{2(m-l)}{(1-l)^2}
  \quad \text{for } 0<l<1,\; l<m<1.
  $$

## Practice 7 — Problem 5

**Prompt.**  
A chicken lays $n$ eggs. Each egg independently hatches with probability $p$. For each egg that hatches, the chick independently survives with probability $s$.

Let

$$
N \sim \mathrm{Bin}(n,p)
$$

be the number of eggs that hatch, let $X$ be the number of chicks that survive, and let $Y$ be the number of chicks that hatch but do not survive, so that $X+Y=N$.

Find the marginal PMF of $X$, and the joint PMF of $X$ and $Y$. Are they independent?

---

## Strategic Practice 8 — Covariance and Correlation

## Practice 8 — Problem 1

**Prompt.**  
Two fair six-sided dice are rolled, one green and one orange, with outcomes $X$ and $Y$ respectively.

1. Compute the covariance of $X+Y$ and $X-Y$.
2. Are $X+Y$ and $X-Y$ independent? Show that they are, or that they are not.

## Practice 8 — Problem 2

**Prompt.**  
A chicken lays a $\mathrm{Poisson}(\lambda)$ number $N$ of eggs. Each egg, independently, hatches a chick with probability $p$. Let $X$ be the number that hatch, so

$$
X \mid N \sim \mathrm{Bin}(N,p).
$$

Find the correlation between $N$ and $X$. Simplify your final answer to a function of $p$.

## Practice 8 — Problem 4

**Prompt.**  
Let $(X_1,\dots,X_k)$ be Multinomial with parameters $n$ and $(p_1,\dots,p_k)$.

Use indicator random variables to show that

$$
\mathrm{Cov}(X_i,X_j)=-n p_i p_j \qquad \text{for } i\ne j.
$$

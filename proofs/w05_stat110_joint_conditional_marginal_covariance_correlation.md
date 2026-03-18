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

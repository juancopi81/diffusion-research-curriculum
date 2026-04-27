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

### My attempt

For the marginal PMF of $X$, I condition on the number of eggs that hatch.

We are given

$$
N\sim \mathrm{Bin}(n,p),
$$

and once $N=k$ eggs have hatched, each of those $k$ chicks survives independently with probability $s$. Therefore,

$$
X\mid N=k \sim \mathrm{Bin}(k,s).
$$

So for any integer $i$ with $0\le i\le n$,

$$
P(X=i)=\sum_{k=i}^n P(X=i\mid N=k)\,P(N=k).
$$

Using the two binomial PMFs,

$$
P(X=i\mid N=k)=\binom{k}{i}s^i(1-s)^{k-i},
\qquad
P(N=k)=\binom{n}{k}p^k(1-p)^{n-k},
$$

we get

$$
P(X=i)=\sum_{k=i}^n \binom{k}{i}s^i(1-s)^{k-i}\binom{n}{k}p^k(1-p)^{n-k}.
$$

Now use the combinatorial identity

$$
\binom{n}{k}\binom{k}{i}=\binom{n}{i}\binom{n-i}{k-i}.
$$

Then

$$
P(X=i)
=
\sum_{k=i}^n
\binom{n}{i}\binom{n-i}{k-i}s^i(1-s)^{k-i}p^k(1-p)^{n-k}.
$$

Factor out the terms that do not depend on $k$:

$$
P(X=i)
=
\binom{n}{i}s^ip^i
\sum_{k=i}^n
\binom{n-i}{k-i}(1-s)^{k-i}p^{k-i}(1-p)^{n-k}.
$$

Let $j=k-i$. Then as $k$ goes from $i$ to $n$, $j$ goes from $0$ to $n-i$. Also,

$$
n-k=n-i-j.
$$

So

$$
P(X=i)
=
\binom{n}{i}(ps)^i
\sum_{j=0}^{n-i}
\binom{n-i}{j}[p(1-s)]^j(1-p)^{n-i-j}.
$$

This sum is a binomial expansion:

$$
\sum_{j=0}^{n-i}
\binom{n-i}{j}[p(1-s)]^j(1-p)^{n-i-j}
=
\big(p(1-s)+(1-p)\big)^{n-i}
=
(1-ps)^{n-i}.
$$

Therefore,

$$
P(X=i)=\binom{n}{i}(ps)^i(1-ps)^{n-i},
\qquad i=0,1,\dots,n.
$$

So the marginal distribution of $X$ is

$$
X\sim \mathrm{Bin}(n,ps).
$$

This also makes sense from a story proof: each egg independently produces a surviving chick with probability

$$
p\cdot s=ps,
$$

so $X$ is just the number of successes in $n$ independent Bernoulli trials with success probability $ps$.

For the joint PMF of $X$ and $Y$, note that if $X=i$ and $Y=j$, then necessarily

$$
N=X+Y=i+j.
$$

So only the value $N=i+j$ contributes, and for integers $i,j\ge 0$ with $i+j\le n$,

$$
P(X=i,Y=j)=P(X=i,Y=j\mid N=i+j)\,P(N=i+j).
$$

Now

$$
P(N=i+j)=\binom{n}{i+j}p^{i+j}(1-p)^{n-i-j}.
$$

Also, given that exactly $i+j$ eggs hatched, we want exactly $i$ of those chicks to survive and $j$ to not survive. Since each hatched chick survives independently with probability $s$,

$$
P(X=i,Y=j\mid N=i+j)=\binom{i+j}{i}s^i(1-s)^j.
$$

Hence

$$
P(X=i,Y=j)
=
\binom{i+j}{i}s^i(1-s)^j
\binom{n}{i+j}p^{i+j}(1-p)^{n-i-j}.
$$

Using

$$
\binom{n}{i+j}\binom{i+j}{i}
=
\frac{n!}{i!\,j!\,(n-i-j)!},
$$

we obtain

$$
P(X=i,Y=j)
=
\frac{n!}{i!\,j!\,(n-i-j)!}\,
p^{i+j}(1-p)^{n-i-j}s^i(1-s)^j.
$$

Now regroup the powers:

$$
p^{i+j}s^i(1-s)^j
=
(ps)^i\big(p(1-s)\big)^j.
$$

So the joint PMF is

$$
P(X=i,Y=j)
=
\frac{n!}{i!\,j!\,(n-i-j)!}\,
(ps)^i\big(p(1-s)\big)^j(1-p)^{n-i-j},
$$

for

$$
i\ge 0,\qquad j\ge 0,\qquad i+j\le n,
$$

and $0$ otherwise.

This has the Multinomial form. If we let

$$
Z=n-X-Y
$$

be the number of eggs that do not hatch, then each egg independently falls into one of three categories:

- hatch and survive, with probability $ps$,
- hatch and do not survive, with probability $p(1-s)$,
- do not hatch, with probability $1-p$.

Therefore,

$$
(X,Y,Z)\sim \mathrm{Multinomial}\bigl(n;\,ps,\;p(1-s),\;1-p\bigr).
$$

Finally, $X$ and $Y$ are **not independent**.

A very clean way to see this is to look at an extreme case: if $X=n$, then every egg produced a surviving chick, so necessarily

$$
Y=0.
$$

Thus

$$
P(Y=0\mid X=n)=1.
$$

But in general,

$$
P(Y=0)<1,
$$

so $X$ and $Y$ cannot be independent.

Equivalently, the support of $(X,Y)$ is

$$
\{(i,j): i\ge 0,\ j\ge 0,\ i+j\le n\},
$$

which already shows that the pair cannot behave like two independent binomial counts on all of $\{0,\dots,n\}^2$.

### What I initially missed / corrected

- For the marginal of $X$, the right conditioning idea is

  $$
  P(X=i)=\sum_{k=i}^n P(X=i\mid N=k)P(N=k).
  $$

  The conditional distribution is

  $$
  X\mid N=k\sim \mathrm{Bin}(k,s),
  $$

  not $\mathrm{Bin}(n,s)$.

- The key combinatorial identity is

  $$
  \binom{n}{k}\binom{k}{i}=\binom{n}{i}\binom{n-i}{k-i}.
  $$

  After the change of variable $j=k-i$, the sum becomes a binomial expansion.

- For the joint PMF, the important observation is that if $X=i$ and $Y=j$, then automatically

  $$
  N=i+j.
  $$

  So only one conditioning term survives.

- Given $N=i+j$, the event $\{X=i,Y=j\}$ is the same as saying that among the $i+j$ hatched chicks, exactly $i$ survive and $j$ do not. That is why

  $$
  P(X=i,Y=j\mid N=i+j)=\binom{i+j}{i}s^i(1-s)^j.
  $$

- Once the joint PMF is simplified, the pattern is clearly Multinomial with three categories:
  survive, hatch-but-don't-survive, and don't-hatch.

- For independence, the cleanest argument is the extreme case:
  if $X=n$, then $Y=0$ for sure, so $X$ and $Y$ cannot be independent.

### Book's solution (for comparison)

The book first notes that marginally

$$
X\sim \mathrm{Bin}(n,ps),
$$

which matches the result above.

For the dependence question, it uses the same extreme-case idea: if

$$
X=n,
$$

then necessarily

$$
Y=0,
$$

so

$$
P(Y=0\mid X=n)=1,
$$

while

$$
P(Y=0)<1.
$$

Hence $X$ and $Y$ are not independent.

For the joint PMF, the book conditions on $N$ and observes that for nonnegative integers $i,j$ with $i+j\le n$,

$$
P(X=i,Y=j)=P(X=i,Y=j\mid N=i+j)\,P(N=i+j).
$$

Then it writes

$$
P(X=i,Y=j\mid N=i+j)=\binom{i+j}{i}s^i(1-s)^j
$$

and

$$
P(N=i+j)=\binom{n}{i+j}p^{i+j}(1-p)^{n-i-j},
$$

so

$$
P(X=i,Y=j)
=
\binom{i+j}{i}\binom{n}{i+j}s^i(1-s)^j p^{i+j}(1-p)^{n-i-j}.
$$

Simplifying gives

$$
P(X=i,Y=j)
=
\frac{n!}{i!\,j!\,(n-i-j)!}(ps)^i\bigl(p(1-s)\bigr)^j(1-p)^{n-i-j}.
$$

Finally, if $Z$ is the number of eggs that do not hatch, then the book recognizes that

$$
(X,Y,Z)\sim \mathrm{Multinomial}\bigl(n;\,ps,\;p(1-s),\;1-p\bigr),
$$

which matches the derivation above.

### Memory card (quick review)

- If each egg must both **hatch** and then **survive**, the overall success probability is

  $$
  ps.
  $$

- Therefore,

  $$
  X\sim \mathrm{Bin}(n,ps).
  $$

- Conditioning idea for the marginal:

  $$
  P(X=i)=\sum_{k=i}^n P(X=i\mid N=k)P(N=k),
  \qquad
  X\mid N=k\sim \mathrm{Bin}(k,s).
  $$

- Joint PMF:

  $$
  P(X=i,Y=j)
  =
  \frac{n!}{i!\,j!\,(n-i-j)!}(ps)^i\bigl(p(1-s)\bigr)^j(1-p)^{n-i-j},
  $$

  for

  $$
  i\ge 0,\quad j\ge 0,\quad i+j\le n.
  $$

- Multinomial viewpoint:
  each egg independently falls into one of three categories:

  $$
  ps,\qquad p(1-s),\qquad 1-p.
  $$

- So

  $$
  (X,Y,n-X-Y)\sim \mathrm{Multinomial}\bigl(n;\,ps,\;p(1-s),\;1-p\bigr).
  $$

- $X$ and $Y$ are **not independent**.
  A quick check:
  $$
  X=n \implies Y=0,
  $$
  so
  $$
  P(Y=0\mid X=n)=1 \neq P(Y=0).
  $$

---

## Strategic Practice 8 — Covariance and Correlation

## Practice 8 — Problem 1

**Prompt.**  
Two fair six-sided dice are rolled, one green and one orange, with outcomes $X$ and $Y$ respectively.

1. Compute the covariance of $X+Y$ and $X-Y$.
2. Are $X+Y$ and $X-Y$ independent? Show that they are, or that they are not.

### My attempt

For part (a), I used bilinearity of covariance:

$$
\mathrm{Cov}(X+Y,\;X-Y)
=\mathrm{Cov}(X,X)+\mathrm{Cov}(X,-Y)+\mathrm{Cov}(Y,X)+\mathrm{Cov}(Y,-Y).
$$

Now simplify each term:

$$
\mathrm{Cov}(X,X)=\mathrm{Var}(X),
\qquad
\mathrm{Cov}(Y,-Y)=-\mathrm{Cov}(Y,Y)=-\mathrm{Var}(Y),
$$

and also

$$
\mathrm{Cov}(X,-Y)=-\mathrm{Cov}(X,Y).
$$

So

$$
\mathrm{Cov}(X+Y,\;X-Y)
=\mathrm{Var}(X)-\mathrm{Cov}(X,Y)+\mathrm{Cov}(Y,X)-\mathrm{Var}(Y).
$$

Since covariance is symmetric,

$$
\mathrm{Cov}(Y,X)=\mathrm{Cov}(X,Y),
$$

the middle terms cancel, and I get

$$
\mathrm{Cov}(X+Y,\;X-Y)=\mathrm{Var}(X)-\mathrm{Var}(Y).
$$

Because $X$ and $Y$ are outcomes of fair dice, they have the same distribution, so

$$
\mathrm{Var}(X)=\mathrm{Var}(Y).
$$

Therefore,

$$
\mathrm{Cov}(X+Y,\;X-Y)=0.
$$

For part (b), let

$$
U=X+Y, \qquad V=X-Y.
$$

If $U$ and $V$ were independent, then for all possible values $u,v$ we would need

$$
P(U=u,\;V=v)=P(U=u)\,P(V=v).
$$

I used a counterexample. Take

$$
U=12,\qquad V=3.
$$

This is impossible, because $U=12$ means

$$
X=6,\qquad Y=6,
$$

so then

$$
V=X-Y=0,
$$

not $3$. Hence

$$
P(U=12,\;V=3)=0.
$$

But both marginal events are possible:

$$
P(U=12)>0
\qquad\text{and}\qquad
P(V=3)>0.
$$

So

$$
P(U=12,\;V=3)\ne P(U=12)\,P(V=3),
$$

which shows that $U$ and $V$ are not independent.

Therefore, $X+Y$ and $X-Y$ are not independent.

### What I initially missed / corrected

- For part (a), the clean way is to use **bilinearity of covariance** and keep the minus signs attached carefully:

  $$
  \mathrm{Cov}(X,-Y)=-\mathrm{Cov}(X,Y),\qquad
  \mathrm{Cov}(Y,-Y)=-\mathrm{Var}(Y).
  $$

- The symmetry property

  $$
  \mathrm{Cov}(Y,X)=\mathrm{Cov}(X,Y)
  $$

  is what makes the middle terms cancel.

- For part (b), I first tried to use covariance / expected value to test independence.
  But the lecture fact only goes one way:

  $$
  \text{independent} \implies \text{covariance } 0,
  $$

  not the reverse.

- So the right setup for part (b) is to use the **definition of independence** for random variables:

  $$
  P(U=u,\;V=v)=P(U=u)P(V=v).
  $$

  To disprove independence, it is enough to find one pair $(u,v)$ where this fails.

- A very convenient trick is to choose an **impossible pair** like $(U,V)=(12,3)$:
  the joint probability is $0$, while each marginal probability is positive.

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

For part (a), the book writes

$$
\mathrm{Cov}(X+Y,\;X-Y)
=\mathrm{Cov}(X,X)-\mathrm{Cov}(X,Y)+\mathrm{Cov}(Y,X)-\mathrm{Cov}(Y,Y)=0.
$$

This is the same covariance expansion as above, just written in a more compressed form.

For part (b), the book uses an extreme conditional example:
if

$$
X+Y=12,
$$

then necessarily

$$
X=Y=6,
$$

so

$$
X-Y=0.
$$

Therefore,

$$
P(X-Y=0\mid X+Y=12)=1\ne P(X-Y=0),
$$

which shows that $X+Y$ and $X-Y$ are not independent.

It also notes a parity check:
$X+Y$ and $X-Y$ must always have the same parity, since

$$
(X+Y)-(X-Y)=2Y,
$$

which is always even.

### Memory card (quick review)

- Bilinearity:

  $$
  \mathrm{Cov}(A+B,\;C+D)
  =
  \mathrm{Cov}(A,C)+\mathrm{Cov}(A,D)+\mathrm{Cov}(B,C)+\mathrm{Cov}(B,D).
  $$

- Pull out constants:

  $$
  \mathrm{Cov}(A,\;cB)=c\,\mathrm{Cov}(A,B).
  $$

- Symmetry:

  $$
  \mathrm{Cov}(A,B)=\mathrm{Cov}(B,A).
  $$

- Zero covariance does **not** prove independence.

- To disprove independence, it is enough to find one pair of values where

  $$
  P(U=u,\;V=v)\ne P(U=u)P(V=v).
  $$

## Practice 8 — Problem 2

**Prompt.**  
A chicken lays a $\mathrm{Poisson}(\lambda)$ number $N$ of eggs. Each egg, independently, hatches a chick with probability $p$. Let $X$ be the number that hatch, so

$$
X \mid N \sim \mathrm{Bin}(N,p).
$$

Find the correlation between $N$ and $X$. Simplify your final answer to a function of $p$.

### My attempt

Start from

$$
\mathrm{Corr}(N,X)=\frac{\mathrm{Cov}(N,X)}{\mathrm{SD}(N)\mathrm{SD}(X)}.
$$

So I first compute the covariance.

By definition,

$$
\mathrm{Cov}(N,X)=E[NX]-E[N]E[X].
$$

Since

$$
N \sim \mathrm{Pois}(\lambda),
$$

we know

$$
E[N]=\lambda,
\qquad
\mathrm{Var}(N)=\lambda,
\qquad
\mathrm{SD}(N)=\sqrt{\lambda}.
$$

Now compute $E[X]$ using total expectation:

$$
E[X]=E(E[X \mid N]).
$$

Because

$$
X \mid N \sim \mathrm{Bin}(N,p),
$$

we have

$$
E[X \mid N]=Np.
$$

Therefore,

$$
E[X]=E[Np]=pE[N]=\lambda p.
$$

Next, compute $E[NX]$ by conditioning on $N$ again:

$$
E[NX]=E(E[NX \mid N]).
$$

Given $N$, the quantity $N$ is fixed, so

$$
E[NX \mid N]=N E[X \mid N]=N(Np)=N^2p.
$$

Hence

$$
E[NX]=pE[N^2].
$$

Now use

$$
\mathrm{Var}(N)=E[N^2]-(E[N])^2,
$$

so

$$
E[N^2]=\mathrm{Var}(N)+(E[N])^2=\lambda+\lambda^2.
$$

Thus

$$
E[NX]=p(\lambda+\lambda^2).
$$

Plugging into the covariance formula,

$$
\mathrm{Cov}(N,X)=p(\lambda+\lambda^2)-(\lambda)(\lambda p)=\lambda p.
$$

Now I compute $\mathrm{Var}(X)$ using total variance:

$$
\mathrm{Var}(X)=E[\mathrm{Var}(X \mid N)] + \mathrm{Var}(E[X \mid N]).
$$

Again, since

$$
X \mid N \sim \mathrm{Bin}(N,p),
$$

we know

$$
\mathrm{Var}(X \mid N)=Np(1-p),
\qquad
E[X \mid N]=Np.
$$

Therefore,

$$
E[\mathrm{Var}(X \mid N)]=E[Np(1-p)]=p(1-p)E[N]=\lambda p(1-p),
$$

and

$$
\mathrm{Var}(E[X \mid N])=\mathrm{Var}(Np)=p^2 \mathrm{Var}(N)=p^2 \lambda.
$$

So

$$
\mathrm{Var}(X)=\lambda p(1-p)+p^2\lambda=\lambda p.
$$

Hence

$$
\mathrm{SD}(X)=\sqrt{\lambda p}.
$$

Finally,

$$
\mathrm{Corr}(N,X)=\frac{\mathrm{Cov}(N,X)}{\mathrm{SD}(N)\mathrm{SD}(X)}=\frac{\lambda p}{\sqrt{\lambda}\sqrt{\lambda p}}=\frac{\lambda p}{\lambda\sqrt{p}}=\sqrt{p}.
$$

So the final answer is

$$
\mathrm{Corr}(N,X)=\sqrt{p}.
$$

### What I initially missed / corrected

- I started correctly from

  $$
  \mathrm{Corr}(N,X)=\frac{\mathrm{Cov}(N,X)}{\mathrm{SD}(N)\mathrm{SD}(X)},
  $$

  but it helped to split the problem into smaller parts:

  $$
  E[X], \qquad E[NX], \qquad \mathrm{Var}(X).
  $$

- For

  $$
  E[X]=E(E[X \mid N]),
  $$

  I had to remember that after writing

  $$
  E[X \mid N]=Np,
  $$

  the quantity $Np$ is still random because it depends on $N$.

- In the $E[NX]$ step, the key move was

  $$
  E[NX]=E(E[NX \mid N]).
  $$

  Given $N$, the factor $N$ is fixed, so

  $$
  E[NX \mid N]=N E[X \mid N].
  $$

- My main correction was with variance scaling. The correct rule is

  $$
  \mathrm{Var}(cY)=c^2 \mathrm{Var}(Y),
  $$

  so here

  $$
  \mathrm{Var}(Np)=p^2 \mathrm{Var}(N),
  $$

  not $p \mathrm{Var}(N)$.

- It was useful to keep the distinction clear:

  $$
  E[cY]=cE[Y],
  \qquad
  \mathrm{Var}(cY)=c^2 \mathrm{Var}(Y).
  $$

- Once I found

  $$
  \mathrm{Var}(X)=\lambda p,
  $$

  the denominator simplified cleanly and the $\lambda$ canceled.

### Book's solution (for comparison)

The book uses the Poisson splitting idea.

Let

$$
Y=N-X
$$

be the number of eggs that do not hatch. Then

$$
N=X+Y.
$$

By Poisson thinning,

$$
X \sim \mathrm{Pois}(\lambda p),
\qquad
Y \sim \mathrm{Pois}(\lambda(1-p)),
$$

and $X$ and $Y$ are independent.

Therefore,

$$
\mathrm{Cov}(N,X)=\mathrm{Cov}(X+Y,X)=\mathrm{Cov}(X,X)+\mathrm{Cov}(Y,X).
$$

Since $X$ and $Y$ are independent,

$$
\mathrm{Cov}(Y,X)=0,
$$

so

$$
\mathrm{Cov}(N,X)=\mathrm{Var}(X)=\lambda p.
$$

Also,

$$
\mathrm{SD}(N)=\sqrt{\lambda},
\qquad
\mathrm{SD}(X)=\sqrt{\lambda p}.
$$

Hence

$$
\mathrm{Corr}(N,X)=\frac{\lambda p}{\sqrt{\lambda}\sqrt{\lambda p}}=\sqrt{p}.
$$

This is shorter than the conditioning route, but it uses the extra thinning fact.

### Memory card (quick review)

- Start from

  $$
  \mathrm{Corr}(N,X)=\frac{\mathrm{Cov}(N,X)}{\mathrm{SD}(N)\mathrm{SD}(X)}.
  $$

- Since

  $$
  N \sim \mathrm{Pois}(\lambda),
  $$

  we know

  $$
  E[N]=\lambda,
  \qquad
  \mathrm{Var}(N)=\lambda.
  $$

- If

  $$
  X \mid N \sim \mathrm{Bin}(N,p),
  $$

  then

  $$
  E[X \mid N]=Np,
  \qquad
  \mathrm{Var}(X \mid N)=Np(1-p).
  $$

- Total expectation:

  $$
  E[X]=E(E[X \mid N])=\lambda p.
  $$

- Total variance:

  $$
  \mathrm{Var}(X)=E[\mathrm{Var}(X \mid N)] + \mathrm{Var}(E[X \mid N]).
  $$

- Be careful with constants:

  $$
  E[cY]=cE[Y],
  \qquad
  \mathrm{Var}(cY)=c^2 \mathrm{Var}(Y).
  $$

- In this problem,

  $$
  \mathrm{Cov}(N,X)=\lambda p,
  \qquad
  \mathrm{Var}(X)=\lambda p.
  $$

- Therefore,

  $$
  \mathrm{Corr}(N,X)=\sqrt{p}.
  $$

- Intuition:

  $X$ is the thinned part of $N$. If $p=1$, then $X=N$ and the correlation is $1$. If $p$ is small, $X$ is only a small noisy fraction of $N$, so the correlation is smaller. The final answer depends only on $p$, not on $\lambda$.

---

## Practice 8 — Problem 4

**Prompt.**  
Let $(X_1,\dots,X_k)$ be Multinomial with parameters $n$ and $(p_1,\dots,p_k)$.

Use indicator random variables to show that

$$
\mathrm{Cov}(X_i,X_j)=-n p_i p_j \qquad \text{for } i\ne j.
$$

### My attempt

For each trial or object, define the indicator

$$
I_{t,r}=
\begin{cases}
1, & \text{if trial } t \text{ lands in category } r,\\[4pt]
0, & \text{otherwise}.
\end{cases}
$$

Then $X_i$ counts how many of the $n$ trials landed in category $i$, so

$$
X_i=\sum_{t=1}^n I_{t,i}.
$$

Similarly,

$$
X_j=\sum_{s=1}^n I_{s,j}.
$$

Now use bilinearity of covariance:

$$
\mathrm{Cov}(X_i,X_j)
=
\mathrm{Cov}\left(\sum_{t=1}^n I_{t,i},\sum_{s=1}^n I_{s,j}\right).
$$

Therefore,

$$
\mathrm{Cov}(X_i,X_j)
=
\sum_{t=1}^n\sum_{s=1}^n
\mathrm{Cov}(I_{t,i},I_{s,j}).
$$

Now split the double sum into two cases.

First, suppose

$$
t\ne s.
$$

Then the indicators refer to different trials. Since different trials are independent,

$$
I_{t,i} \text{ and } I_{s,j}
$$

are independent, so

$$
\mathrm{Cov}(I_{t,i},I_{s,j})=0.
$$

Now suppose

$$
t=s.
$$

Then both indicators refer to the same trial. Since

$$
i\ne j,
$$

the same trial cannot land in both category $i$ and category $j$. Therefore,

$$
I_{t,i}I_{t,j}=0.
$$

So

$$
E[I_{t,i}I_{t,j}]=0.
$$

Also,

$$
E[I_{t,i}]=p_i
$$

and

$$
E[I_{t,j}]=p_j.
$$

Thus,

$$
\mathrm{Cov}(I_{t,i},I_{t,j})
=
E[I_{t,i}I_{t,j}]-E[I_{t,i}]E[I_{t,j}].
$$

So

$$
\mathrm{Cov}(I_{t,i},I_{t,j})
=
0-p_ip_j
=
-p_ip_j.
$$

Only the same-trial terms contribute to the covariance. There are $n$ of those terms, one for each trial, so

$$
\mathrm{Cov}(X_i,X_j)
=
\sum_{t=1}^n \mathrm{Cov}(I_{t,i},I_{t,j}).
$$

Therefore,

$$
\mathrm{Cov}(X_i,X_j)
=
\sum_{t=1}^n (-p_ip_j)
=
-np_ip_j.
$$

So for $i\ne j$,

$$
\mathrm{Cov}(X_i,X_j)=-np_ip_j.
$$

### What I initially missed / corrected

The main subtlety is that the double sum

$$
\sum_{t=1}^n\sum_{s=1}^n
$$

contains $n^2$ terms, not just $n$ terms.

The terms with

$$
t\ne s
$$

compare different trials, so their covariance is $0$ by independence.

The terms with

$$
t=s
$$

compare two categories within the same trial. These are not independent, because one trial cannot be in two different categories at once.

For the same trial,

$$
I_{t,i}I_{t,j}=0
$$

because $i\ne j$.

This is why

$$
\mathrm{Cov}(I_{t,i},I_{t,j})=-p_ip_j.
$$

Then there are exactly $n$ same-trial terms, so the final answer is

$$
-np_ip_j.
$$

### Book's solution (for comparison)

The book first proves the result for $X_1$ and $X_2$.

It defines $I_i$ as the indicator that object $i$ is in category $1$, and $J_j$ as the indicator that object $j$ is in category $2$. Then

$$
X_1=\sum_{i=1}^n I_i
$$

and

$$
X_2=\sum_{j=1}^n J_j.
$$

Therefore,

$$
\mathrm{Cov}(X_1,X_2)
=
\mathrm{Cov}\left(\sum_{i=1}^n I_i,\sum_{j=1}^n J_j\right)
=
\sum_{i,j}\mathrm{Cov}(I_i,J_j).
$$

When

$$
i\ne j,
$$

the indicators refer to different objects, so the covariance is $0$.

When

$$
i=j,
$$

the indicators refer to the same object. The same object cannot be in both category $1$ and category $2$, so

$$
I_iJ_i=0.
$$

Thus,

$$
\mathrm{Cov}(I_i,J_i)
=
E[I_iJ_i]-E[I_i]E[J_i]
=
0-p_1p_2
=
-p_1p_2.
$$

There are $n$ such same-object terms, so

$$
\mathrm{Cov}(X_1,X_2)
=
\sum_{i=1}^n \mathrm{Cov}(I_i,J_i)
=
n(-p_1p_2)
=
-np_1p_2.
$$

By the same argument, replacing categories $1$ and $2$ by any two different categories $i$ and $j$ gives

$$
\mathrm{Cov}(X_i,X_j)=-np_ip_j
\qquad \text{for } i\ne j.
$$

### Memory card (quick review)

For a Multinomial random vector,

$$
(X_1,\dots,X_k)\sim \mathrm{Multinomial}(n;p_1,\dots,p_k),
$$

each $X_i$ counts how many trials landed in category $i$.

Write the count as a sum of indicators:

$$
X_i=\sum_{t=1}^n I_{t,i}.
$$

For two different categories,

$$
X_j=\sum_{s=1}^n I_{s,j}.
$$

Then

$$
\mathrm{Cov}(X_i,X_j)
=
\sum_{t=1}^n\sum_{s=1}^n
\mathrm{Cov}(I_{t,i},I_{s,j}).
$$

Different trials are independent:

$$
t\ne s
\implies
\mathrm{Cov}(I_{t,i},I_{s,j})=0.
$$

Same trial, different categories are mutually exclusive:

$$
t=s,\quad i\ne j
\implies
I_{t,i}I_{t,j}=0.
$$

So

$$
\mathrm{Cov}(I_{t,i},I_{t,j})
=
0-p_ip_j
=
-p_ip_j.
$$

There are $n$ same-trial terms, hence

$$
\mathrm{Cov}(X_i,X_j)=-np_ip_j.
$$

The intuition is negative dependence: if one trial lands in category $i$, that same trial cannot land in category $j$.

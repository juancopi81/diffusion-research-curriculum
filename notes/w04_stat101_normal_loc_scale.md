# Stat 110 (Blitzstein) — Lecture 14

**Lecture 14:** [Location, Scale, and LOTUS](https://www.youtube.com/watch?v=9vp1Ll2NpRw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo&index=14)  
**Course:** Statistics 110 (Harvard) — Prof. Joe Blitzstein

---

## 1) Standard Normal recap + symmetry

Let

$$
Z \sim N(0,1),
$$

with CDF $\Phi$.

Key facts:

$$
\mathbb{E}[Z]=0,
\qquad
\mathrm{Var}(Z)=\mathbb{E}[Z^2]=1.
$$

### Odd-moment symmetry trick (example: $\mathbb{E}[Z^3]$)

By LOTUS (continuous form),

$$
\mathbb{E}[Z^3]
=
\int_{-\infty}^{\infty} z^3 \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\,dz.
$$

The integrand

$$
z^3 \frac{1}{\sqrt{2\pi}} e^{-z^2/2}
$$

is an **odd function**, so the integral over $(-\infty,\infty)$ is $0$:

$$
\boxed{\mathbb{E}[Z^3]=0.}
$$

Also, by symmetry,

$$
-Z \sim N(0,1).
$$

---

## 2) Location + scale transform (build any Normal from $Z$)

Let

$$
X = \mu + \sigma Z,
\qquad
\mu \in \mathbb{R}\ \text{(mean/location)},\quad \sigma>0\ \text{(sd/scale)}.
$$

Then

$$
\boxed{X \sim N(\mu,\sigma^2).}
$$

Mean and variance:

$$
\mathbb{E}[X] = \mu,
\qquad
\mathrm{Var}(X)=\mathrm{Var}(\mu+\sigma Z)=\sigma^2\mathrm{Var}(Z)=\sigma^2.
$$

### Standardization (go back to $N(0,1)$)

If $X \sim N(\mu,\sigma^2)$, then

$$
\boxed{Z=\frac{X-\mu}{\sigma} \sim N(0,1).}
$$

---

## 3) Variance identities (quick toolkit)

Definition:

$$
\mathrm{Var}(X)=\mathbb{E}\big[(X-\mathbb{E}[X])^2\big]
=
\mathbb{E}[X^2]-\big(\mathbb{E}[X]\big)^2.
$$

Shifts don’t change variance:

$$
\mathrm{Var}(X+c)=\mathrm{Var}(X).
$$

Scaling:

$$
\mathrm{Var}(cX)=c^2\mathrm{Var}(X)\ge 0.
$$

Degenerate case:

$$
\mathrm{Var}(X)=0
\iff
\exists a\ \text{s.t.}\ \mathbb{P}(X=a)=1.
$$

Sum of RVs (important bridge):

$$
\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y).
$$

So in general,

$$
\mathrm{Var}(X+Y)\ne \mathrm{Var}(X)+\mathrm{Var}(Y),
$$

but **if $X$ and $Y$ are independent**, then $\mathrm{Cov}(X,Y)=0$ and

$$
\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y).
$$

Special case:

$$
\mathrm{Var}(X+X)=\mathrm{Var}(2X)=4\mathrm{Var}(X).
$$

---

## 4) CDF + PDF of $N(\mu,\sigma^2)$ from standardization

Start from the CDF:

$$
\mathbb{P}(X\le x)
=
\mathbb{P}\left(\frac{X-\mu}{\sigma}\le \frac{x-\mu}{\sigma}\right)
=
\Phi\left(\frac{x-\mu}{\sigma}\right).
$$

So,

$$
\boxed{F_X(x)=\Phi\left(\frac{x-\mu}{\sigma}\right).}
$$

Differentiate to get the PDF:

$$
\boxed{
f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\!\left(-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2\right).
}
$$

### Negation

If $X\sim N(\mu,\sigma^2)$, then

$$
-X = -\mu + \sigma(-Z) \sim N(-\mu,\sigma^2).
$$

---

## 5) Sums / differences of independent Normals

If

$$
X_1\sim N(\mu_1,\sigma_1^2),\quad X_2\sim N(\mu_2,\sigma_2^2),
\quad \text{and } X_1 \perp X_2,
$$

then

$$
\boxed{X_1+X_2 \sim N(\mu_1+\mu_2,\ \sigma_1^2+\sigma_2^2)}
$$

and

$$
\boxed{X_1-X_2 \sim N(\mu_1-\mu_2,\ \sigma_1^2+\sigma_2^2)}.
$$

---

## 6) 68–95–99.7 rule (Normal rule of thumb)

If $X\sim N(\mu,\sigma^2)$, then approximately:

$$
\mathbb{P}(|X-\mu|\le \sigma)\approx 0.68,
$$

$$
\mathbb{P}(|X-\mu|\le 2\sigma)\approx 0.95,
$$

$$
\mathbb{P}(|X-\mu|\le 3\sigma)\approx 0.997.
$$

---

## 7) LOTUS (Law of the Unconscious Statistician)

### Discrete LOTUS statement

For discrete $X$,

$$
\boxed{\mathbb{E}[g(X)] = \sum_x g(x)\,\mathbb{P}(X=x).}
$$

### “Grouped” vs “ungrouped” (discrete sample space proof idea)

Let the sample space be $S$ (discrete), and $X:S\to \mathbb{R}$.

Ungrouped expectation (sum over outcomes):

$$
\mathbb{E}[g(X)]
=
\sum_{s\in S} g(X(s))\,\mathbb{P}(\{s\}).
$$

Group outcomes by the value $x$ that $X(s)$ takes:

$$
\sum_{s\in S} g(X(s))\,\mathbb{P}(\{s\})
=
\sum_x \sum_{s:\,X(s)=x} g(X(s))\,\mathbb{P}(\{s\}).
$$

But if $X(s)=x$, then $g(X(s))=g(x)$, so:

$$
=
\sum_x g(x)\sum_{s:\,X(s)=x}\mathbb{P}(\{s\})
=
\sum_x g(x)\,\mathbb{P}(X=x).
$$

So the grouped form is exactly:

$$
\boxed{\mathbb{E}[g(X)] = \sum_x g(x)\,\mathbb{P}(X=x).}
$$

_(Continuous LOTUS reminder: $\mathbb{E}[g(X)] = \int g(x) f_X(x)\,dx$.)_

### Intuition + tiny example (same sum, just reorganized)

**Intuition.** The ungrouped sum is "sum over outcomes." The grouped sum is "collect outcomes that give the same value of $X$." Nothing changes except the order of adding terms, so the total is the same.

**Example (fair die).** Let $S=\{1,2,3,4,5,6\}$, $X=$ die outcome, and let

$$
g(x)=\mathbf{1}\{x\ \text{is even}\}.
$$

Ungrouped (sum over outcomes):

$$
\mathbb{E}[g(X)]
=
\sum_{s\in S} g(X(s))\,\mathbb{P}(\{s\})
$$

Write it term by term (each outcome has probability $1/6$):

$$
= g(1)\cdot \frac{1}{6}
 + g(2)\cdot \frac{1}{6}
 + g(3)\cdot \frac{1}{6}
 + g(4)\cdot \frac{1}{6}
 + g(5)\cdot \frac{1}{6}
 + g(6)\cdot \frac{1}{6}
$$

Now plug in the values of $g$:

$$
= 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
 + 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
 + 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
$$

Combine:

$$
= \frac{0+1+0+1+0+1}{6}
= \frac{3}{6}
= \frac{1}{2}.
$$

Grouped (sum over values of $X$):

$$
\mathbb{E}[g(X)]
=
\sum_x g(x)\,\mathbb{P}(X=x)
$$

Since $X$ is the die outcome,

$$
\mathbb{P}(X=x)=\frac{1}{6},\quad x=1,2,3,4,5,6.
$$

So

$$
= \sum_{x=1}^6 g(x)\cdot \frac{1}{6}
$$

Write out the sum:

$$
= g(1)\cdot \frac{1}{6}
 + g(2)\cdot \frac{1}{6}
 + g(3)\cdot \frac{1}{6}
 + g(4)\cdot \frac{1}{6}
 + g(5)\cdot \frac{1}{6}
 + g(6)\cdot \frac{1}{6}
$$

Now plug in $g(1)=0,\ g(2)=1,\ g(3)=0,\ g(4)=1,\ g(5)=0,\ g(6)=1$:

$$
= 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
 + 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
 + 0\cdot \frac{1}{6}
 + 1\cdot \frac{1}{6}
= \frac{3}{6}
= \frac{1}{2}.
$$

Same terms, same total; the grouped form just adds together equal $g(x)$ values in one block.

---

## 8) Example: Poisson variance via LOTUS + Taylor series

Let $X\sim \mathrm{Pois}(\lambda)$. Then

$$
\mathbb{E}[X^2] = \sum_{k=0}^\infty k^2\,\mathbb{P}(X=k)
=
\sum_{k=0}^\infty k^2\,e^{-\lambda}\frac{\lambda^k}{k!}.
$$

Use the Taylor series:

$$
\sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^\lambda.
$$

Differentiate:

$$
\sum_{k=1}^\infty \frac{k\lambda^{k-1}}{k!} = e^\lambda.
$$

Multiply by $\lambda$:

$$
\sum_{k=1}^\infty \frac{k\lambda^{k}}{k!} = \lambda e^\lambda.
$$

Differentiate again:

$$
\sum_{k=1}^\infty \frac{k^2\lambda^{k-1}}{k!} = \lambda e^\lambda + e^\lambda = e^\lambda(\lambda+1).
$$

Multiply by $\lambda e^{-\lambda}$:

$$
\sum_{k=1}^\infty k^2 e^{-\lambda}\frac{\lambda^k}{k!}
=
\lambda(\lambda+1)
=
\lambda^2+\lambda.
$$

So

$$
\mathbb{E}[X^2]=\lambda^2+\lambda,
\qquad
\mathbb{E}[X]=\lambda,
$$

and therefore

$$
\boxed{\mathrm{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2=(\lambda^2+\lambda)-\lambda^2=\lambda.}
$$

---

## 9) Example: Binomial variance via indicators

Let $X\sim \mathrm{Bin}(n,p)$ and write

$$
X = I_1+\cdots+I_n,
\qquad
I_i \ \text{i.i.d. } \mathrm{Bern}(p).
$$

Compute $X^2$:

$$
X^2
=
\sum_{i=1}^n I_i^2
+
2\sum_{1\le i<j\le n} I_i I_j.
$$

Take expectations:

- For indicators, $I_i^2=I_i$, so $\mathbb{E}[I_i^2]=\mathbb{E}[I_i]=p$.
- By independence, $\mathbb{E}[I_i I_j]=\mathbb{P}(I_i=1, I_j=1)=p^2$ for $i\ne j$.

Thus

$$
\mathbb{E}[X^2]
=
n\,p + 2\binom{n}{2}p^2
=
np + n(n-1)p^2.
$$

Also,

$$
\mathbb{E}[X]=np
\quad\Rightarrow\quad
(\mathbb{E}[X])^2=n^2p^2.
$$

So

$$
\mathrm{Var}(X)
=
\mathbb{E}[X^2]-(\mathbb{E}[X])^2
=
\big(np+n(n-1)p^2\big)-n^2p^2
=
np-np^2
=
np(1-p).
$$

Let $q=1-p$, then

$$
\boxed{\mathrm{Var}(X)=npq,\qquad q=1-p.}
$$

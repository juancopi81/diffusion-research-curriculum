# Week 3 — S2 (Stat110 Practice): Continuous Distributions & the Normal

**Topics:** PDF/CDF relationships, computing probabilities by integration, Normal distribution properties, standardization
**Resource:** [Stat110-Practice] + [Stat110-Text]

---

## Poisson: Problem 1

**Question.**
Raindrops are falling at an average rate of 20 drops per square inch per minute.
What would be a reasonable distribution to use for the number of raindrops
hitting a particular region measuring $5\text{ in}^2$ in $t$ minutes? Why? Using your
chosen distribution, compute the probability that the region has no rain drops
in a given 3 second time interval.

### My attempt (what I wrote / idea)

- Use a **Poisson** model for the number of drops hitting the region in a time interval.
- Convert the rate:
  - $20 \text{ drops}/(\text{in}^2\cdot\text{min}) = \dfrac{20}{60}=\dfrac{1}{3} \text{ drops}/(\text{in}^2\cdot\text{sec})$
- For a $5\text{ in}^2$ region over $3$ seconds the expected values is given by:

  $$
  \lambda = \underbrace{5}_{\text{area (in}^2\text{)}} \cdot \underbrace{\frac{1}{3}}_{\text{rate (drops/in}^2\text{/sec)}} \cdot \underbrace{3}_{\text{time (sec)}} = 5.
  $$

- Then: $P(X=0)=e^{-\lambda}=e^{-5}$.

### What I initially missed / corrected

- The phrase “each region is unlikely to be hit” is **not** about the whole $5\text{ in}^2$ region.
  It’s about imagining **splitting** space/time into many **tiny** pieces so that each tiny piece has
  a very small chance of a drop, which motivates the Poisson model.
- Also, it helps to write the mean explicitly for $t$ minutes:
  $$
  \lambda(t) = (20\ \text{drops}/(\text{in}^2\cdot\text{min}))\cdot(5\ \text{in}^2)\cdot(t\ \text{min}) = 100t.
  $$
  Then for $3$ seconds, $t=\frac{1}{20}$ minute, so $\lambda=100\cdot\frac{1}{20}=5$.

### Book's solution (for comparison)

- Compute the region’s rate per minute:
  $$
  20\cdot 5 = 100 \ \text{drops/min}.
  $$
- Use $X(t)\sim \text{Poisson}(\lambda(t))$ with $\lambda(t)=100t$.
- For $3$ seconds ($t=1/20$ minute):
  $$
  P(\text{no drops in }3\text{ sec}) = P(X=0)=e^{-100/20}=e^{-5}.
  $$
  (Note: the Poisson formula gives $e^{-\lambda}$, i.e. the exponent is negative.)

---

## Symmetry: Problem 1

**Question.**
Let $Z \sim N(0,1)$ and let $S$ be a “random sign” independent of $Z$, i.e.

$$
P(S=1)=\frac12,\qquad P(S=-1)=\frac12.
$$

Show that $SZ \sim N(0,1)$.

### My attempt (what I wrote / idea)

- The pdf of $Z\sim N(0,1)$ is
  $$
  f_Z(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}.
  $$
- Since the exponent depends on $z^2$, the pdf is symmetric:
  $$
  f_Z(z)=f_Z(-z).
  $$
- Since $S$ is $+1$ half the time and $-1$ half the time, $SZ$ is $Z$ half the time and $-Z$ half the time, so (mixing the two cases):
  $$
  f_{SZ}(z)=\frac12 f_Z(z)+\frac12 f_Z(-z)
  =\frac12 f_Z(z)+\frac12 f_Z(z)
  =f_Z(z).
  $$
- Therefore $SZ$ has the same pdf as $Z$, so $SZ \sim N(0,1)$.

### What I initially missed / corrected

- The “half the time $Z$, half the time $-Z$” step is made rigorous by **conditioning on $S$** (law of total probability):
  $$
  f_{SZ}(z)=P(S=1)\,f_{SZ\mid S=1}(z)+P(S=-1)\,f_{SZ\mid S=-1}(z)
  =\frac12 f_Z(z)+\frac12 f_{-Z}(z).
  $$
- Then use the transformation fact
  $$
  f_{-Z}(z)=f_Z(-z),
  $$
  and finally symmetry $f_Z(-z)=f_Z(z)$.

### Book's solution (for comparison)

- Condition on $S$ to compute the CDF of $SZ$:
  $$
  P(SZ\le x)
  =P(SZ\le x\mid S=1)\frac12 + P(SZ\le x\mid S=-1)\frac12.
  $$
- Simplify each conditional term:
  - If $S=1$, then $SZ=Z$, so $P(SZ\le x\mid S=1)=P(Z\le x)$.
  - If $S=-1$, then $SZ=-Z$, so
    $$
    P(SZ\le x\mid S=-1)=P(-Z\le x)=P(Z\ge -x).
    $$
- So:
  $$
  P(SZ\le x)=\frac12 P(Z\le x)+\frac12 P(Z\ge -x).
  $$
- By symmetry of the standard normal,
  $$
  P(Z\ge -x)=P(Z\le x),
  $$
  hence
  $$
  P(SZ\le x)=\frac12 \Phi(x)+\frac12 \Phi(x)=\Phi(x),
  $$
  which is the CDF of $N(0,1)$. Therefore $SZ\sim N(0,1)$.

---

## Continuous Distributions: Problem 1

**Question.**
Let $Y=e^X$, where $X\sim N(\mu,\sigma^2)$. Then $Y$ is said to have a LogNormal distribution.
Find the **CDF** and **PDF** of $Y$ (the CDF should be in terms of $\Phi$).

### My attempt (what I wrote / idea)

- Start from the definition of the CDF:
  $$
  F_Y(y)=P(Y\le y)=P(e^X\le y).
  $$
- Since $e^X>0$ always, if $y\le 0$ then the event $\{e^X\le y\}$ is impossible:
  $$
  F_Y(y)=0,\qquad y\le 0.
  $$
- For $y>0$, apply $\log(\cdot)$ (monotone increasing) to both sides:
  $$
  P(e^X\le y)=P(X\le \log y).
  $$
  Therefore
  $$
  F_Y(y)=P(X\le \log y)=F_X(\log y),\qquad y>0.
  $$
- Since $X\sim N(\mu,\sigma^2)$,
  $$
  F_X(x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right),
  $$
  so substituting $x=\log y$:
  $$
  F_Y(y)=\Phi\!\left(\frac{\log y-\mu}{\sigma}\right),\qquad y>0.
  $$

### What I initially missed / corrected

- **Uppercase vs lowercase:** $\Phi$ is a **CDF** (an integral / area), while $\phi$ is the **PDF** (the curve height):
  $$
  \Phi(z)=\int_{-\infty}^{z}\phi(t)\,dt,
  \qquad
  \phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}.
  $$
  So $\dfrac{d}{dz}\Phi(z)=\phi(z)$.
- When differentiating the CDF to get the PDF, I must use the **chain rule**.
  Let
  $$
  g(y)=\frac{\log y-\mu}{\sigma}.
  $$
  Then
  $$
  g'(y)=\frac{1}{\sigma}\cdot\frac{1}{y}=\frac{1}{\sigma y}.
  $$
- Therefore, for $y>0$:
  $$
  f_Y(y)=\frac{d}{dy}F_Y(y)
  =\frac{d}{dy}\Phi(g(y))
  =\phi(g(y))\cdot g'(y)
  =\phi\!\left(\frac{\log y-\mu}{\sigma}\right)\cdot\frac{1}{\sigma y}.
  $$
  And $f_Y(y)=0$ for $y\le 0$.

### Book's solution (for comparison)

- The book often writes $\log$ as $\ln$ (natural log), but it’s the same thing here.
- It presents the PDF by expanding $\phi(\cdot)$:
  $$
  f_Y(y)=\frac{1}{\sigma y}\,\phi\!\left(\frac{\ln y-\mu}{\sigma}\right)
  =\frac{1}{\sigma y\sqrt{2\pi}}
    \exp\!\left(-\frac{(\ln y-\mu)^2}{2\sigma^2}\right),
  \qquad y>0,
  $$
  and $f_Y(y)=0$ for $y\le 0$.
- CDF (same as ours):
  $$
  F_Y(y)=
  \begin{cases}
  0, & y\le 0,\\[6pt]
  \Phi\!\left(\dfrac{\ln y-\mu}{\sigma}\right), & y>0.
  \end{cases}
  $$

---

## Continuous Distributions: Problem 2

**Question.** Let $U \sim \text{Unif}(0,1)$. Using $U$, construct a r.v. $X$ whose PDF is $\lambda e^{-\lambda x}$ for $x > 0$ (and 0 otherwise), where $\lambda > 0$ is a constant. Then $X$ is said to have an _Exponential_ distribution; this distribution is of great importance in engineering, chemistry, survival analysis, and elsewhere.

---

### My attempt (what I wrote / idea)

#### 1) Compute the CDF from the PDF

- For $x\le 0$:
  $$
  F(x)=P(X\le x)=0.
  $$
- For $x>0$:
  $$
  F(x)=\int_0^x \lambda e^{-\lambda t}\,dt
  = \left[-e^{-\lambda t}\right]_0^x
  = 1-e^{-\lambda x}.
  $$
  So the CDF is
  $$
  F(x)=
  \begin{cases}
  0, & x\le 0,\\
  1-e^{-\lambda x}, & x>0.
  \end{cases}
  $$

#### 2) Invert the CDF

For $x>0$ set $u=F(x)=1-e^{-\lambda x}$ and solve for $x$:

$$
u = 1-e^{-\lambda x}
\Rightarrow 1-u=e^{-\lambda x}
\Rightarrow \ln(1-u)=-\lambda x
\Rightarrow x=-\frac{1}{\lambda}\ln(1-u).
$$

So

$$
F^{-1}(u)=-\frac{1}{\lambda}\ln(1-u),\qquad 0<u<1.
$$

---

### Using the inverse transform to get the CDF/PDF of $X$

Define

$$
X=F^{-1}(U)=-\frac{1}{\lambda}\ln(1-U).
$$

#### CDF derivation

For $x\le 0$:

$$
F_X(x)=P(X\le x)=0
$$

(since $X\ge 0$ always).

For $x>0$:

$$
\begin{aligned}
F_X(x)
&=P\!\left(-\frac{1}{\lambda}\ln(1-U)\le x\right)\\
&=P\!\left(\ln(1-U)\ge -\lambda x\right) \quad\text{(multiply by $-\lambda$ flips inequality)}\\
&=P\!\left(1-U\ge e^{-\lambda x}\right)\quad\text{(apply $\exp$)}\\
&=P\!\left(U\le 1-e^{-\lambda x}\right).
\end{aligned}
$$

Since $U\sim \text{Unif}(0,1)$, $P(U\le a)=a$ for $0\le a\le 1$. Here $a=1-e^{-\lambda x}\in(0,1)$, so

$$
F_X(x)=1-e^{-\lambda x},\qquad x>0.
$$

Thus

$$
F_X(x)=
\begin{cases}
0, & x\le 0,\\
1-e^{-\lambda x}, & x>0,
\end{cases}
$$

which matches the Exponential$(\lambda)$ CDF.

#### PDF derivation (differentiate the CDF)

For $x>0$:

$$
f_X(x)=\frac{d}{dx}\left(1-e^{-\lambda x}\right)=\lambda e^{-\lambda x}.
$$

And $f_X(x)=0$ for $x\le 0$.

---

### Book’s solution (for comparison / key idea)

- Compute $F(x)$, invert it to get $F^{-1}(u)$, then apply the **inverse transform sampling theorem**:
  if $U\sim\text{Unif}(0,1)$ and $X=F^{-1}(U)$, then $X$ has CDF $F$.
- So the generator for Exponential$(\lambda)$ is:
  $$
  X=-\frac{1}{\lambda}\ln(1-U).
  $$
- Often it’s also written as:
  $$
  X=-\frac{1}{\lambda}\ln U,
  $$
  because $1-U\sim \text{Unif}(0,1)$ as well (uniform symmetry).

---

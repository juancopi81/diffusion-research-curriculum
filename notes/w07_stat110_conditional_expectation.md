# Stat 110 (Blitzstein) - Lecture 26

**Lecture 25 preview:** [Order Statistics and Conditional Expectation](https://www.youtube.com/watch?v=2LR5JYbhyjg)
**Lecture 26:** [Conditional Expectation Continued](https://www.youtube.com/watch?v=PgawcWisb0I)
**Course:** Statistics 110 (Harvard) - Prof. Joe Blitzstein

**Source note:** cleaned transcription from handwritten notes; lecture links are included for navigation.

This note starts with the conditional-expectation preview at the end of Lecture 25 and then continues with Lecture 26.

---

## 1) Conditional expectation given an event

For an event $A$, the conditional expectation of $X$ given $A$ is written

$$
\mathbb{E}[X\mid A].
$$

The ordinary expectation can be decomposed using the partition $A,A^c$:

$$
\boxed{
\mathbb{E}[X]
=
\mathbb{E}[X\mid A]\mathbb{P}(A)
+
\mathbb{E}[X\mid A^c]\mathbb{P}(A^c).
}
$$

For a discrete random variable, this comes directly from the definition of expectation and the law of total probability:

$$
\begin{aligned}
\mathbb{E}[X]
&=
\sum_x x\,\mathbb{P}(X=x) \\
&=
\sum_x x\left(
\mathbb{P}(X=x\mid A)\mathbb{P}(A)
+
\mathbb{P}(X=x\mid A^c)\mathbb{P}(A^c)
\right) \\
&=
\mathbb{P}(A)\sum_x x\,\mathbb{P}(X=x\mid A)
+
\mathbb{P}(A^c)\sum_x x\,\mathbb{P}(X=x\mid A^c) \\
&=
\mathbb{E}[X\mid A]\mathbb{P}(A)
+
\mathbb{E}[X\mid A^c]\mathbb{P}(A^c).
\end{aligned}
$$

The key idea is: **expectations can be expanded by conditioning on cases**, just like probabilities can be expanded by LOTP.

---

## 2) Two-envelope paradox

There are two envelopes. One contains twice as much money as the other.

Suppose one envelope contains $X$ and the other contains $Y$. By symmetry,

$$
\boxed{\mathbb{E}[Y]=\mathbb{E}[X].}
$$

The tempting wrong argument says:

$$
\begin{aligned}
\mathbb{E}[Y]
&=
\mathbb{E}[Y\mid Y=2X]\mathbb{P}(Y=2X)
+
\mathbb{E}[Y\mid Y=X/2]\mathbb{P}(Y=X/2) \\
&\stackrel{\text{wrong}}{=}
\mathbb{E}[2X]\cdot \frac{1}{2}
+
\mathbb{E}[X/2]\cdot \frac{1}{2} \\
&=
\frac{5}{4}\mathbb{E}[X].
\end{aligned}
$$

This contradicts the symmetry result, so something went wrong.

The correct conditioning is

$$
\boxed{
\mathbb{E}[Y]
=
\mathbb{E}[2X\mid Y=2X]\cdot \frac{1}{2}
+
\mathbb{E}[X/2\mid Y=X/2]\cdot \frac{1}{2}.
}
$$

The mistake was replacing a conditional expectation by an unconditional one:

$$
\mathbb{E}[2X\mid Y=2X]
\ne
\mathbb{E}[2X]
$$

in general.

Let

$$
I=\mathbf{1}_{\{Y=2X\}}.
$$

Then $X$ and $I$ are **not independent**. If $Y=2X$, then $X$ must be the smaller amount. If $Y=X/2$, then $X$ must be the larger amount. So conditioning on which envelope is larger changes the distribution of $X$.

For example, if you see $\$100$, the naive calculation says the other envelope is either $\$50$ or $\$200$, giving average

$$
\frac{50+200}{2}=125.
$$

But that calculation quietly assumes the two cases are equally likely after observing $\$100$. The paradox is a warning that the conditioning information matters.

---

## 3) Waiting for coin-flip patterns

Repeatedly flip a fair coin. Let

$$
W_{HT}
=
\text{waiting time until the first occurrence of }HT,
$$

and

$$
W_{HH}
=
\text{waiting time until the first occurrence of }HH.
$$

By symmetry,

$$
\mathbb{E}[W_{HT}]=\mathbb{E}[W_{TH}],
\qquad
\mathbb{E}[W_{HH}]=\mathbb{E}[W_{TT}].
$$

But there is no symmetry between $HT$ and $HH$.

### Waiting for $HT$

To get $HT$, first wait for an $H$, then wait for a $T$ after an $H$.

Let $G$ be a geometric random variable with success probability $1/2$, counting the number of flips until success. Then

$$
\mathbb{E}[G]=\frac{1}{1/2}=2.
$$

The waiting time decomposes into two geometric pieces:

$$
W_{HT}=W_1+W_2,
$$

where $W_1$ is the wait for the first $H$ and $W_2$ is the wait for the next $T$ after an $H$ has appeared.

Therefore,

$$
\boxed{
\mathbb{E}[W_{HT}]
=
\mathbb{E}[W_1]+\mathbb{E}[W_2]
=
2+2
=4.
}
$$

Extra $H$'s do not destroy progress toward $HT$: after seeing another $H$, the last flip is still $H$, so we are still one $T$ away.

### Waiting for $HH$

Let

$$
e=\mathbb{E}[W_{HH}].
$$

Condition on the first toss.

If the first toss is $T$, then we used one toss and reset:

$$
1+e.
$$

If the first toss is $H$, then condition on the second toss:

- If the second toss is $H$, we are done in $2$ tosses.
- If the second toss is $T$, we used $2$ tosses and reset, so the remaining expected time is $e$.

Thus

$$
\begin{aligned}
e
&=
\frac{1}{2}(1+e)
+
\frac{1}{2}\left(
\frac{1}{2}\cdot 2
+
\frac{1}{2}(2+e)
\right).
\end{aligned}
$$

Solving,

$$
\begin{aligned}
e
&=
\frac{1}{2}+\frac{e}{2}
+
\frac{1}{2}\left(1+1+\frac{e}{2}\right) \\
&=
\frac{3}{2}+\frac{3e}{4},
\end{aligned}
$$

so

$$
\boxed{\mathbb{E}[W_{HH}]=6.}
$$

Intuition: $HH$ can reset more easily than $HT$. After seeing $HT$, we are done. But while trying to see $HH$, the partial progress $H$ is destroyed by a following $T$.

---

## 4) Conditional expectation given $X=x$

For discrete $Y$,

$$
\boxed{
\mathbb{E}[Y\mid X=x]
=
\sum_y y\,\mathbb{P}(Y=y\mid X=x).
}
$$

For continuous $Y$,

$$
\boxed{
\mathbb{E}[Y\mid X=x]
=
\int_{-\infty}^{\infty} y\,f_{Y\mid X}(y\mid x)\,dy.
}
$$

If $X$ and $Y$ are jointly continuous and $f_X(x)>0$, then

$$
f_{Y\mid X}(y\mid x)
=
\frac{f_{X,Y}(x,y)}{f_X(x)}.
$$

Therefore,

$$
\boxed{
\mathbb{E}[Y\mid X=x]
=
\int_{-\infty}^{\infty}
y\,\frac{f_{X,Y}(x,y)}{f_X(x)}\,dy.
}
$$

This is the expectation of $Y$ after freezing $X$ at the value $x$.

---

## 5) Conditional expectation as a random variable

Define

$$
g(x)=\mathbb{E}[Y\mid X=x].
$$

Then

$$
\boxed{
\mathbb{E}[Y\mid X]=g(X).
}
$$

So $\mathbb{E}[Y\mid X]$ is itself a random variable. It is a function of $X$.

For example, if

$$
g(x)=x^2,
$$

then

$$
\mathbb{E}[Y\mid X]=g(X)=X^2.
$$

This is an important shift:

- $\mathbb{E}[Y\mid X=x]$ is a number depending on the fixed value $x$.
- $\mathbb{E}[Y\mid X]$ is a random variable, because $X$ is random.

---

## 6) Useful rules

### Linearity

Conditional expectation is linear:

$$
\boxed{
\mathbb{E}[Y+Z\mid X]
=
\mathbb{E}[Y\mid X]+\mathbb{E}[Z\mid X].
}
$$

More generally,

$$
\mathbb{E}[aY+bZ\mid X]
=
a\mathbb{E}[Y\mid X]+b\mathbb{E}[Z\mid X].
$$

### Functions of the conditioning variable

If $h(X)$ is already known once $X$ is known, then

$$
\boxed{
\mathbb{E}[h(X)\mid X]=h(X).
}
$$

In particular,

$$
\mathbb{E}[X\mid X]=X.
$$

### Independence

If $Y$ is independent of $X$, then knowing $X$ gives no information about $Y$:

$$
\boxed{
\mathbb{E}[Y\mid X]=\mathbb{E}[Y].
}
$$

---

## 7) Example: independent Poisson variables

Let

$$
X,Y\overset{\text{iid}}{\sim}\mathrm{Pois}(\lambda).
$$

### Compute $\mathbb{E}[X+Y\mid X]$

By linearity,

$$
\mathbb{E}[X+Y\mid X]
=
\mathbb{E}[X\mid X]+\mathbb{E}[Y\mid X].
$$

Since $X$ is known given $X$,

$$
\mathbb{E}[X\mid X]=X.
$$

Since $Y$ is independent of $X$,

$$
\mathbb{E}[Y\mid X]=\mathbb{E}[Y]=\lambda.
$$

Therefore,

$$
\boxed{
\mathbb{E}[X+Y\mid X]=X+\lambda.
}
$$

### Compute $\mathbb{E}[X\mid X+Y]$

Let

$$
T=X+Y.
$$

For $k=0,1,\dots,n$,

$$
\begin{aligned}
\mathbb{P}(X=k\mid T=n)
&=
\frac{\mathbb{P}(T=n\mid X=k)\mathbb{P}(X=k)}
{\mathbb{P}(T=n)} \\
&=
\frac{\mathbb{P}(Y=n-k)\mathbb{P}(X=k)}
{\mathbb{P}(T=n)}.
\end{aligned}
$$

Now

$$
\mathbb{P}(Y=n-k)
=
e^{-\lambda}\frac{\lambda^{n-k}}{(n-k)!},
\qquad
\mathbb{P}(X=k)
=
e^{-\lambda}\frac{\lambda^k}{k!}.
$$

Also,

$$
T=X+Y\sim \mathrm{Pois}(2\lambda),
$$

so

$$
\mathbb{P}(T=n)
=
e^{-2\lambda}\frac{(2\lambda)^n}{n!}.
$$

Therefore,

$$
\begin{aligned}
\mathbb{P}(X=k\mid T=n)
&=
\frac{
e^{-\lambda}\frac{\lambda^{n-k}}{(n-k)!}
e^{-\lambda}\frac{\lambda^k}{k!}
}{
e^{-2\lambda}\frac{(2\lambda)^n}{n!}
} \\
&=
\frac{n!}{k!(n-k)!}\frac{1}{2^n} \\
&=
\binom{n}{k}\left(\frac{1}{2}\right)^n.
\end{aligned}
$$

Thus

$$
\boxed{
X\mid (T=n)\sim \mathrm{Bin}\left(n,\frac{1}{2}\right).
}
$$

So

$$
\mathbb{E}[X\mid T=n]=\frac{n}{2}.
$$

Turning this back into a random variable,

$$
\boxed{
\mathbb{E}[X\mid T]=\frac{T}{2}
=
\frac{X+Y}{2}.
}
$$

The same result follows by symmetry. Since $X$ and $Y$ are iid,

$$
\mathbb{E}[X\mid T]=\mathbb{E}[Y\mid T].
$$

But

$$
\mathbb{E}[X\mid T]+\mathbb{E}[Y\mid T]
=
\mathbb{E}[X+Y\mid T]
=
\mathbb{E}[T\mid T]
=
T.
$$

Therefore each one must be $T/2$.

---

## 8) Takeaways

1. Conditional expectation is an average computed after conditioning on information.
2. Conditioning on an event can change the distribution of the random variable being averaged.
3. $\mathbb{E}[Y\mid X=x]$ is a function of $x$.
4. $\mathbb{E}[Y\mid X]$ is a random variable and a function of $X$.
5. If something is already known from $X$, it stays fixed inside $\mathbb{E}[\cdot\mid X]$.
6. If something is independent of $X$, conditioning on $X$ does not change its expectation.

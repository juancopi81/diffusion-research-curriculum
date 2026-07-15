# Week 8 - Phase 1 Mini-Exam

**Purpose:** Check whether the Phase 1 probability tools are becoming usable for
diffusion theory. These are approachable Strategic Practice problems selected for
conceptual coverage, not for maximum difficulty.

**Sources:**

- [Stat 110 source catalog](../../sources/stat110/strategic-practice/)
- [Strategic Practice and Homework 2 - official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_2.pdf)
- [Strategic Practice and Homework 7 - official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_7.pdf)
- [Strategic Practice and Homework 8 - official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_8.pdf)
- [Strategic Practice and Homework 10 - official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_10.pdf)
- [Strategic Practice and Homework 11 - official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_11.pdf)

The selected problems are from the **Strategic Practice** sections. The three
Week 8 warm-up problems are intentionally not repeated here.

## Attempt protocol

- Suggested total time: **2 hours**.
- Aim for roughly **15-20 minutes per problem**; do not spend more than 25 minutes on one problem on the first pass.
- Start without notes or AI if possible. The goal is to test tool selection and setup, not perfect recall of every formula.
- If you become stuck, write down the exact step where the setup stops making sense, move on, and return later.
- After the timed attempt, classify each problem as `clean`, `shaky`, or `blocked` before reviewing notes or asking for hints.

## Problem 1 - Hidden skill level and conditional independence

**Source:** Strategic Practice 2, Thinking Conditionally, Problem 5.

You are going to play 2 games of chess with an opponent whom you have never
played against before. Your opponent is equally likely to be a beginner,
intermediate, or a master. Depending on which, your chances of winning an
individual game are $90\%$, $50\%$, or $30\%$, respectively.

1. What is your probability of winning the first game?
2. You won the first game. Given this information, what is the probability that you will also win the second game? Assume that, given the skill level of your opponent, the outcomes of the games are independent.
3. Explain the distinction between assuming that the outcomes of the games are independent and assuming that they are conditionally independent given the opponent's skill level. Which assumption seems more reasonable, and why?

### My solution

Let $B$, $I$, and $M$ be the events that the opponent is a beginner,
intermediate player, or master, respectively. The three skill levels are equally
likely, so

$$
\mathbb{P}(B)=\mathbb{P}(I)=\mathbb{P}(M)=\frac{1}{3}.
$$

Let $W_1$ and $W_2$ be the events that I win Games 1 and 2, respectively. The
probabilities of winning either game, conditional on the opponent's skill level,
are

$$
\mathbb{P}(W_j\mid B)=\frac{9}{10},
\qquad
\mathbb{P}(W_j\mid I)=\frac{5}{10},
\qquad
\mathbb{P}(W_j\mid M)=\frac{3}{10},
$$

for $j\in\{1,2\}$.

#### Part 1

By the law of total probability,

$$
\begin{aligned}
\mathbb{P}(W_1)
&=
\mathbb{P}(W_1\mid B)\mathbb{P}(B)
+\mathbb{P}(W_1\mid I)\mathbb{P}(I)
+\mathbb{P}(W_1\mid M)\mathbb{P}(M)\\
&=
\frac{9}{10}\frac{1}{3}
+\frac{5}{10}\frac{1}{3}
+\frac{3}{10}\frac{1}{3}\\
&=
\frac{17}{30}.
\end{aligned}
$$

Thus,

$$
\boxed{\mathbb{P}(W_1)=\frac{17}{30}.}
$$

#### Part 2

We want

$$
\mathbb{P}(W_2\mid W_1)
=
\frac{\mathbb{P}(W_1\cap W_2)}{\mathbb{P}(W_1)}.
$$

The two games are independent after conditioning on the opponent's skill
level. Therefore,

$$
\begin{aligned}
\mathbb{P}(W_1\cap W_2)
&=
\mathbb{P}(W_1\mid B)\mathbb{P}(W_2\mid B)\mathbb{P}(B)\\
&\quad+
\mathbb{P}(W_1\mid I)\mathbb{P}(W_2\mid I)\mathbb{P}(I)\\
&\quad+
\mathbb{P}(W_1\mid M)\mathbb{P}(W_2\mid M)\mathbb{P}(M)\\
&=
\frac{1}{3}
\left(
\frac{81}{100}+\frac{25}{100}+\frac{9}{100}
\right)\\
&=
\frac{115}{300}
=
\frac{23}{60}.
\end{aligned}
$$

Hence,

$$
\begin{aligned}
\mathbb{P}(W_2\mid W_1)
&=
\frac{23/60}{17/30}\\
&=
\frac{23}{34}
=
\frac{115}{170}.
\end{aligned}
$$

Thus,

$$
\boxed{\mathbb{P}(W_2\mid W_1)=\frac{23}{34}.}
$$

#### Part 3

If the game outcomes were independent without conditioning, the result of the
first game would not change the probability of winning the second game.

Conditional independence means that once the opponent's skill level is known,
the result of the first game does not affect the second:

$$
\mathbb{P}(W_2\mid W_1,B)=\mathbb{P}(W_2\mid B),
$$

and similarly for intermediate players and masters.

Conditional independence is more reasonable here. Before the skill level is
known, winning the first game gives evidence that the opponent may be a
beginner rather than a master. This updates the probabilities of the skill
levels and therefore changes the probability of winning the second game.

### What I initially missed / corrected

The numerical argument was correct. The notation in the joint-probability
calculation needed one clarification: the probabilities multiplied inside each
mixture term are conditional on the same skill level. For example, the beginner
term is

$$
\mathbb{P}(W_1\mid B)\mathbb{P}(W_2\mid B)\mathbb{P}(B),
$$

not the product of the unconditional probabilities
$\mathbb{P}(W_1)\mathbb{P}(W_2)\mathbb{P}(B)$.

### Intuition

The opponent's skill level is a hidden common cause of both game outcomes.
After observing a win, the beginner case becomes more plausible and the master
case becomes less plausible. This is why

$$
\mathbb{P}(W_2\mid W_1)=\frac{23}{34}
>
\frac{17}{30}
=
\mathbb{P}(W_2).
$$

Once the skill level is fixed, that information channel disappears and the two
games are independent.

### Memory card

- Condition on the hidden variable that controls both outcomes.
- Average over the hidden variable using the law of total probability.
- Conditional independence does not imply unconditional independence.
- Here:

  $$
  \mathbb{P}(W_1)=\frac{17}{30},
  \qquad
  \mathbb{P}(W_2\mid W_1)=\frac{23}{34}.
  $$

## Problem 2 - Distance between two continuous random variables

**Source:** Strategic Practice 7, Joint, Conditional, and Marginal Distributions,
Problem 2.

Let $X$ and $Y$ be i.i.d. $\operatorname{Unif}(0,1)$. Find the expected value and
the standard deviation of the distance between $X$ and $Y$.

### My solution

Let

$$
D=|X-Y|.
$$

Since $X$ and $Y$ are independent,

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

Both variables are uniform on $(0,1)$, so

$$
f_{X,Y}(x,y)=1,
\qquad
0\le x\le 1,\quad 0\le y\le 1.
$$

First compute the expected distance:

$$
\mathbb{E}(D)
=
\int_0^1\int_0^1 |x-y|\,dx\,dy.
$$

By symmetry across the diagonal $x=y$, we can integrate over the triangle
$x\ge y$ and multiply by $2$:

$$
\begin{aligned}
\mathbb{E}(D)
&=
2\int_0^1\int_y^1 (x-y)\,dx\,dy\\
&=
2\int_0^1
\left[
\frac{x^2}{2}-yx
\right]_{x=y}^{x=1}
dy\\
&=
2\int_0^1
\left(
\frac{1}{2}-y+\frac{y^2}{2}
\right)
dy\\
&=
2
\left[
\frac{y}{2}-\frac{y^2}{2}+\frac{y^3}{6}
\right]_0^1\\
&=
\frac{1}{3}.
\end{aligned}
$$

Thus,

$$
\boxed{\mathbb{E}|X-Y|=\frac{1}{3}.}
$$

For the variance, note that

$$
D^2=|X-Y|^2=(X-Y)^2.
$$

Therefore,

$$
\begin{aligned}
\mathbb{E}(D^2)
&=
\int_0^1\int_0^1 (x-y)^2\,dx\,dy\\
&=
\int_0^1
\left[
\frac{x^3}{3}-yx^2+y^2x
\right]_{x=0}^{x=1}
dy\\
&=
\int_0^1
\left(
\frac{1}{3}-y+y^2
\right)
dy\\
&=
\left[
\frac{y}{3}-\frac{y^2}{2}+\frac{y^3}{3}
\right]_0^1\\
&=
\frac{1}{6}.
\end{aligned}
$$

Hence,

$$
\begin{aligned}
\operatorname{Var}(D)
&=
\mathbb{E}(D^2)-\left(\mathbb{E}(D)\right)^2\\
&=
\frac{1}{6}-\frac{1}{9}\\
&=
\frac{1}{18}.
\end{aligned}
$$

The problem asks for the standard deviation, so

$$
\boxed{
\operatorname{SD}(|X-Y|)
=
\sqrt{\frac{1}{18}}
=
\frac{1}{3\sqrt{2}}
=
\frac{\sqrt{2}}{6}.
}
$$

### What I initially missed / corrected

The joint density, symmetry argument, expected value, second moment, and
variance were all correct. I stopped after finding

$$
\operatorname{Var}(|X-Y|)=\frac{1}{18},
$$

but the question asked for the standard deviation. The final step is to take
the square root.

### Intuition

The unit square is divided by the diagonal $x=y$. The distance $|X-Y|$ is $0$
on the diagonal and becomes larger toward the corners $(0,1)$ and $(1,0)$.
Symmetry lets us calculate on one triangular half of the square and double the
result.

### Memory card

- For independent $\operatorname{Unif}(0,1)$ variables, the joint density is $1$
  on the unit square.
- Use symmetry to remove the absolute value:

  $$
  \mathbb{E}|X-Y|
  =
  2\int_0^1\int_y^1(x-y)\,dx\,dy.
  $$

- For the second moment:

  $$
  |X-Y|^2=(X-Y)^2.
  $$

- Final results:

  $$
  \mathbb{E}|X-Y|=\frac{1}{3},
  \qquad
  \operatorname{Var}(|X-Y|)=\frac{1}{18},
  \qquad
  \operatorname{SD}(|X-Y|)=\frac{\sqrt{2}}{6}.
  $$

## Problem 3 - Simple change of variables

**Source:** Strategic Practice 8, Transformations, Problem 1.

Let $X\sim\operatorname{Unif}(0,1)$. Find the PDFs of

$$
U=X^2
\qquad\text{and}\qquad
V=\sqrt{X}.
$$

State the support of each transformed random variable.

### My solution

Since $X\sim\operatorname{Unif}(0,1)$,

$$
f_X(x)=
\begin{cases}
1, & 0\le x\le 1,\\
0, & \text{otherwise}.
\end{cases}
$$

#### Density of $U=X^2$

Solving $u=x^2$ for $x$ initially gives

$$
x=\pm\sqrt{u}.
$$

Because the support of $X$ is $[0,1]$, only the positive branch is possible:

$$
x=\sqrt{u}.
$$

The inverse derivative is

$$
\frac{dx}{du}=\frac{1}{2\sqrt{u}}.
$$

Using the change-of-variables formula,

$$
\begin{aligned}
f_U(u)
&=
f_X(\sqrt{u})
\left|
\frac{dx}{du}
\right|\\
&=
1\cdot\frac{1}{2\sqrt{u}},
\qquad 0<u<1.
\end{aligned}
$$

Therefore,

$$
\boxed{
f_U(u)=
\begin{cases}
\dfrac{1}{2\sqrt{u}}, & 0<u<1,\\
0, & \text{otherwise}.
\end{cases}
}
$$

#### Density of $V=\sqrt{X}$

Solving $v=\sqrt{x}$ for $x$ gives

$$
x=v^2.
$$

The inverse derivative is

$$
\frac{dx}{dv}=2v.
$$

Therefore,

$$
\begin{aligned}
f_V(v)
&=
f_X(v^2)
\left|
\frac{dx}{dv}
\right|\\
&=
1\cdot 2v,
\qquad 0<v<1.
\end{aligned}
$$

Thus,

$$
\boxed{
f_V(v)=
\begin{cases}
2v, & 0<v<1,\\
0, & \text{otherwise}.
\end{cases}
}
$$

### What I initially missed / corrected

The inverse transformations, derivatives, choice of the positive branch for
$U$, and supports were correct. The error was in evaluating the original
Uniform density after substitution.

Inside its support,

$$
f_X(x)=1.
$$

Therefore,

$$
f_X(\sqrt{u})=1
\qquad\text{and}\qquad
f_X(v^2)=1.
$$

I had effectively used $\sqrt{u}$ and $v^2$ as the density values, which led to
the incorrect expressions $1/2$ and $2v^3$.

A normalization check also catches the error: each proposed density integrated
to $1/2$, but a valid PDF must integrate to $1$.

### Intuition

Squaring values in $(0,1)$ moves them toward $0$, so the density of $U=X^2$
is largest near $0$. Taking square roots moves values toward $1$, so the density
of $V=\sqrt{X}$ increases as $v$ approaches $1$.

### Memory card

- For a monotone transformation $Y=g(X)$:

  $$
  f_Y(y)
  =
  f_X(g^{-1}(y))
  \left|
  \frac{d}{dy}g^{-1}(y)
  \right|.
  $$

- Substitute the inverse into the density function. Do not replace the density
  value with the inverse itself.
- Restrict the inverse using the original support.
- Check that the resulting PDF integrates to $1$.
- Here:

  $$
  f_U(u)=\frac{1}{2\sqrt{u}},
  \qquad
  f_V(v)=2v,
  \qquad 0<u,v<1.
  $$

## Problem 4 - Zero covariance does not generally mean independence

**Source:** Strategic Practice 8, Covariance and Correlation, Problem 1.

Two fair six-sided dice are rolled, one green and one orange, with outcomes $X$
and $Y$, respectively.

1. Compute the covariance of $X+Y$ and $X-Y$.
2. Are $X+Y$ and $X-Y$ independent? Show that they are, or that they are not.

### My solution

By bilinearity of covariance,

$$
\begin{aligned}
\operatorname{Cov}(X+Y,X-Y)
&=
\operatorname{Cov}(X,X)
+\operatorname{Cov}(X,-Y)\\
&\quad
+\operatorname{Cov}(Y,X)
+\operatorname{Cov}(Y,-Y)\\
&=
\operatorname{Var}(X)
-\operatorname{Cov}(X,Y)
+\operatorname{Cov}(Y,X)
-\operatorname{Var}(Y)\\
&=
\operatorname{Var}(X)-\operatorname{Var}(Y).
\end{aligned}
$$

Since $X$ and $Y$ are outcomes from two fair six-sided dice, they have the
same variance. Therefore,

$$
\boxed{\operatorname{Cov}(X+Y,X-Y)=0.}
$$

Now let

$$
W=X+Y,
\qquad
Z=X-Y.
$$

For $W$ and $Z$ to be independent, every pair of events determined by them
would need to satisfy the product rule. Consider the events $W=12$ and $Z=3$.
Both have positive probability:

$$
P(W=12)=\frac{1}{36}>0
$$

and

$$
P(Z=3)=\frac{3}{36}>0.
$$

However, $W=12$ forces $X=6$ and $Y=6$, which gives $Z=0$. Thus,

$$
P(W=12,Z=3)=0.
$$

Consequently,

$$
P(W=12,Z=3)
\ne
P(W=12)P(Z=3),
$$

so

$$
\boxed{X+Y\text{ and }X-Y\text{ are not independent}.}
$$

### What I initially missed / corrected

The covariance expansion and the independence counterexample were correct. I
wrote

$$
\operatorname{Var}(X)-\operatorname{Var}(Y)=1
$$

in one line, but because the dice have the same variance, the difference is
$0$. My final conclusion already used the correct value.

I also made the counterexample explicit by writing the joint event as
$P(W=12,Z=3)=0$ and comparing it with the positive product
$P(W=12)P(Z=3)$.

### Intuition

The covariance vanishes because the variation contributed by $X$ and $Y$
cancels in the sum-versus-difference calculation. Independence is stronger:
knowing the sum can restrict which differences are possible. For example, the
maximum sum fixes both dice completely.

### Memory card

- Bilinearity gives

  $$
  \operatorname{Cov}(X+Y,X-Y)
  =
  \operatorname{Var}(X)-\operatorname{Var}(Y).
  $$

- Identically distributed $X$ and $Y$ therefore make the covariance $0$.
- Zero covariance does not generally imply independence.
- To disprove independence, find events $A$ and $B$ such that
  $P(A\cap B)\ne P(A)P(B)$.

## Problem 5 - Conditional residual and conditional variance

**Source:** Strategic Practice 10, Conditional Expectation and Conditional
Variance, Problem 3.

Let $X$ and $Y$ be random variables with finite variances, and let

$$
W=Y-\mathbb{E}(Y\mid X).
$$

This is a residual: the difference between the true value of $Y$ and the
prediction of $Y$ based on $X$.

1. Compute $\mathbb{E}(W)$ and $\mathbb{E}(W\mid X)$.
2. Compute $\operatorname{Var}(W)$ in the case that
   $W\mid X\sim\mathcal{N}(0,X^2)$ and $X\sim\mathcal{N}(0,1)$.

### My solution

By linearity of expectation,

$$
\begin{aligned}
\mathbb{E}(W)
&=
\mathbb{E}\left[Y-\mathbb{E}(Y\mid X)\right]\\
&=
\mathbb{E}(Y)-\mathbb{E}\left[\mathbb{E}(Y\mid X)\right].
\end{aligned}
$$

By the tower property,

$$
\mathbb{E}\left[\mathbb{E}(Y\mid X)\right]=\mathbb{E}(Y).
$$

Therefore,

$$
\boxed{\mathbb{E}(W)=0.}
$$

Conditioning on $X$ gives

$$
\begin{aligned}
\mathbb{E}(W\mid X)
&=
\mathbb{E}\left[Y-\mathbb{E}(Y\mid X)\mid X\right]\\
&=
\mathbb{E}(Y\mid X)
-\mathbb{E}\left[\mathbb{E}(Y\mid X)\mid X\right]\\
&=
\mathbb{E}(Y\mid X)-\mathbb{E}(Y\mid X)\\
&=0.
\end{aligned}
$$

The second conditional expectation equals $\mathbb{E}(Y\mid X)$ because this
quantity is already a function of $X$. Hence,

$$
\boxed{\mathbb{E}(W\mid X)=0.}
$$

For the special case, use the law of total variance:

$$
\operatorname{Var}(W)
=
\mathbb{E}\left[\operatorname{Var}(W\mid X)\right]
+
\operatorname{Var}\left(\mathbb{E}(W\mid X)\right).
$$

Since $\mathbb{E}(W\mid X)=0$, the second term is $0$. Also,
$W\mid X\sim\mathcal{N}(0,X^2)$ implies

$$
\operatorname{Var}(W\mid X)=X^2.
$$

Therefore,

$$
\operatorname{Var}(W)=\mathbb{E}(X^2).
$$

Since $X\sim\mathcal{N}(0,1)$,

$$
\mathbb{E}(X^2)
=
\operatorname{Var}(X)+\left(\mathbb{E}X\right)^2
=1.
$$

Thus,

$$
\boxed{\operatorname{Var}(W)=1.}
$$

### What I initially missed / corrected

The tower-property argument, the conditional expectation, the use of total
variance, and the final answer were correct. In the first expansion of
$\mathbb{E}(W)$, I briefly wrote a plus sign where the definition of $W$
requires a minus sign.

The last step also needs the explicit identity

$$
\mathbb{E}(X^2)
=
\operatorname{Var}(X)+\left(\mathbb{E}X\right)^2
=1,
$$

rather than moving directly from $\operatorname{Var}(X)=1$ to the answer.

### Intuition

The residual subtracts everything predictable from $Y$ using $X$. It is
therefore centered even after $X$ is known. Its unconditional variance is the
average remaining conditional variance, which is $\mathbb{E}(X^2)$ in this
example.

### Memory card

- A conditional residual satisfies

  $$
  W=Y-\mathbb{E}(Y\mid X),
  \qquad
  \mathbb{E}(W\mid X)=0.
  $$

- The tower property then gives $\mathbb{E}(W)=0$.
- The law of total variance is

  $$
  \operatorname{Var}(W)
  =
  \mathbb{E}[\operatorname{Var}(W\mid X)]
  +
  \operatorname{Var}(\mathbb{E}[W\mid X]).
  $$

- If the conditional mean is $0$, only the average conditional variance
  remains.

## Problem 6 - Ratio of sample averages

**Source:** Strategic Practice 11, Law of Large Numbers and Central Limit
Theorem, Problem 4.

Let $X_1,X_2,\ldots$ be i.i.d. positive random variables with mean $2$. Let
$Y_1,Y_2,\ldots$ be i.i.d. positive random variables with mean $3$.

Show that

$$
\frac{X_1+X_2+\cdots+X_n}{Y_1+Y_2+\cdots+Y_n}
\longrightarrow \frac{2}{3}
$$

with probability $1$ as $n\to\infty$. Does it matter whether the $X_i$ are
independent of the $Y_j$? Explain.

### My solution

By the strong law of large numbers,

$$
\overline{X}_n
=
\frac{1}{n}\sum_{j=1}^n X_j
\longrightarrow 2
$$

with probability $1$, and

$$
\overline{Y}_n
=
\frac{1}{n}\sum_{j=1}^n Y_j
\longrightarrow 3
$$

with probability $1$.

Rewrite the ratio of sums as a ratio of sample means:

$$
\frac{X_1+X_2+\cdots+X_n}{Y_1+Y_2+\cdots+Y_n}
=
\frac{\frac{1}{n}\sum_{j=1}^n X_j}
{\frac{1}{n}\sum_{j=1}^n Y_j}
=
\frac{\overline{X}_n}{\overline{Y}_n}.
$$

Since the denominator converges to $3\ne0$, the quotient rule for limits gives

$$
\boxed{
\frac{X_1+X_2+\cdots+X_n}{Y_1+Y_2+\cdots+Y_n}
\longrightarrow
\frac{2}{3}
}
$$

with probability $1$.

Independence between the $X_i$ and the $Y_j$ is not required. Let

$$
A=\lbrace\lim_{n\to\infty}\overline{X}_n=2\rbrace,
\qquad
B=\lbrace\lim_{n\to\infty}\overline{Y}_n=3\rbrace.
$$

The strong law gives $P(A)=P(B)=1$, so $P(A\cap B)=1$ even if $A$ and $B$ are
dependent. On that intersection, both limits hold and therefore so does the
ratio limit.

### What I initially missed / corrected

The use of the law of large numbers, the ratio of sample means, the limit
$2/3$, and the conclusion about independence were correct. To make the proof
complete, I added two details:

- the denominator converges to the nonzero value $3$, which justifies taking
  the ratio of the limits;
- the two probability-one convergence events have a probability-one
  intersection, so cross-independence is unnecessary.

### Intuition

Each long-run average stabilizes separately. Once the numerator average is
close to $2$ and the denominator average is close to $3$, their ratio is close
to $2/3$. Dependence between the two sequences may affect their joint
fluctuations for finite $n$, but it does not remove either almost-sure limit.

### Memory card

- Rewrite ratios of sums using sample means:

  $$
  \frac{\sum_{j=1}^n X_j}{\sum_{j=1}^n Y_j}
  =
  \frac{\overline{X}_n}{\overline{Y}_n}.
  $$

- Apply the strong law to each sequence separately.
- Check that the limiting denominator is nonzero.
- Events with probability $1$ have an intersection with probability $1$;
  independence is not needed for this step.

## Coverage map

- Problem 1: conditioning, Bayes-style updating, latent variables, and conditional independence.
- Problem 2: continuous joint reasoning, distance, expectation, and variance.
- Problem 3: density transformation, support, and Jacobian reasoning.
- Problem 4: covariance identities and the distinction between uncorrelated and independent.
- Problem 5: conditional expectation, residuals, conditional variance, and Gaussian variance structure.
- Problem 6: LLN, almost-sure convergence, and ratios of empirical averages.

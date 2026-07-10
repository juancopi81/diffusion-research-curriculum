# Distributions & Expected Values (Discrete RVs) — Strategic Practice (Lec 9–10)

**Sources:**

- [Stat 110 source catalog](../sources/stat110/strategic-practice/)
- [Strategic Practice and Homework 4 — official PDF](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf)

---

## 1. Distributions and Expected Values for Discrete Random Variables

## Problem 1

**Question.**
Find an example of two discrete random variables $X$ and $Y$ (on the same sample space) such that $X$ and $Y$ have the same distribution (same PMF/CDF), but the event $X=Y$ never occurs.

### My attempt (what I wrote / idea)

- Use **one coin flip** as the sample space.
- Define:
  - $X = 1\{\text{Head}\}$
  - $Y = 1\{\text{Tail}\}$
- Then $(X,Y)$ is always either $(1,0)$ or $(0,1)$, so **$X=Y$ never happens**.

### What I initially missed / corrected

- The key check for "same distribution" is:
  $P(X=1) = P(Y=1)$ and $P(X=0) = P(Y=0)$.
  This holds **only if the coin is fair**.

### Book's solution (for comparison)

- Let $X \sim \text{Bernoulli}(1/2)$, and define $Y = 1 - X$.
- Then $Y$ is also $\text{Bernoulli}(1/2)$ by symmetry, but $X=Y$ is impossible.
- Generalization: $X \sim \text{Binomial}(n,1/2)$, $Y=n-X$ with $n$ odd.

---

## Problem 2

**Question.**
Let $X$ be a random day of the week coded as $1,\dots,7$ with equal probabilities.
Let $Y$ be the _next day after_ $X$ (also coded $1,\dots,7$).
Do $X$ and $Y$ have the same distribution? What is $P(X<Y)$?

### My initial thought (and the correction)

- I initially mixed up unconditional vs conditional:
  - I wrote something like: $P(X=x)=1/7$ while $P(Y \mid X=x)=1$, so "not same distribution."
- Correction:
  - "Same distribution" is about $P(Y=y)$, not $P(Y \mid X=x)$.
  - With wrap-around (after 7 comes 1), the map $x \mapsto y$ is a one-to-one shift mod 7, so $Y$ is also uniform on $\{1,\dots,7\}$.
    ✅ So **they have the same distribution**.

### $P(X<Y)$: where I slipped

- I initially thought "if 7 comes before 1 in the cycle, then 7 < 1," which would make it 1.
- But the inequality $X<Y$ uses **normal integer order** $1<2<\dots<7$. Wrap-around changes the definition of $Y$, not the meaning of "<".
- So $X<Y$ fails only when $X=7$ (since then $Y=1$ and $7<1$ is false).
  - Favorable cases: $X=1,2,3,4,5,6$ (6 cases out of 7)
  - So $P(X<Y)=6/7$.

### Book's solution (for comparison)

- Same distribution since $Y$ is equally likely to be any day.
- $P(X<Y) = P(X\ne 7) = 6/7$.

---

## Problem 3

**Question.**
A coin is tossed repeatedly until it lands Heads for the first time.
Let $X$ be the number of tosses required (including the first Head), and $p=P(\text{Head})$.
Find the CDF of $X$, and for $p=1/2$ sketch its graph.

### My attempt (what I wrote / where it went wrong)

- I tried to shift to a "failures before first success" variable:
  - Let $Y = X-1$, so $Y$ counts the number of Tails before the first Head.
- The idea was correct, but I made two main mistakes at first:
  1. I wrote extra "$+1$" terms in PMF/CDF lines (which can push probabilities above 1).
  2. I mixed up PMF values and CDF values:
     - I listed $1/2, 1/4, 1/8,\dots$ and sketched a **decreasing curve** — that's the PMF (or tail), **not** a CDF.
     - A CDF must be **nondecreasing** and approach 1.

### Corrected direction (still in my "shift + sum" style)

- Since $Y=X-1$ and $Y\in\{0,1,2,\dots\}$:
  - $P(X=k)=P(Y=k-1)$ for $k\in\{1,2,3,\dots\}$
  - For integer $x\ge 1$:

$$
F(x)=P(X\le x)=P(Y\le x-1)=\sum_{k=0}^{x-1}(1-p)^k\,p
$$

- For a fair coin $p=1/2$, the PMF terms are:
  - $P(X=1)=1/2$, $P(X=2)=1/4$, $P(X=3)=1/8$, ...
- The _CDF_ values are cumulative:
  - $F(1)=1/2$
  - $F(2)=1/2+1/4=3/4$
  - $F(3)=1/2+1/4+1/8=7/8$
  - ... so the CDF is a **step function** jumping at integers.

### Sketch

![w02_proof_CDF](/notes/figures/w02_proof_CDF.png)

### Book's solution (for comparison)

- Uses the Geometric story: $X-1 \sim \text{Geometric}(p)$ (in the "# failures before first success" convention).
- PMF: $P(X=k)=p(1-p)^{k-1}$ for $k=1,2,3,\dots$
- CDF for real $x$:

$$
F(x)=P(X\le x)=
\begin{cases}
0, & x<1\\
1-(1-p)^{\lfloor x\rfloor}, & x\ge 1
\end{cases}
$$

- For $p=1/2$: $F(x)=1-2^{-\lfloor x\rfloor}$ for $x\ge 1$.

### How my result matches the book (what was "different" at first)

- My sum form is the same as the book's closed form:
  - $\sum_{k=0}^{x-1}(1-p)^k p = 1-(1-p)^x$ for integer $x\ge 1$.
- The book writes it with $\lfloor x\rfloor$ to define it for **non-integer** $x$ (flat between integers).

## 2. Indicator Random Variables and Linearity of Expectation

## Problem 4

**Question.**
A group of 50 people are comparing their birthdays (assume birthdays are independent, uniformly distributed over 365 days, no Feb 29, etc.). Find (i) the expected number of **pairs** of people with the same birthday, and (ii) the expected number of **days of the year** on which **at least two** of these people were born.

### Part (i) — Expected # of matching pairs (indicator + linearity)

- Let $X$ be the number of pairs $(i,j)$ with the same birthday.
- For each pair $(i,j)$ with $1\le i<j\le 50$, define an indicator:
  - $I_{ij}=1{\text{person }i\text{ and }j\text{ share a birthday}}$.

- Then:

$$
X=\sum_{1\le i<j\le 50} I_{ij}
$$

and by linearity of expectation:

$$
E[X]=\sum_{1\le i<j\le 50} E[I_{ij}]
$$

- For a fixed pair $(i,j)$:

$$
E[I_{ij}] = P(\text{match})=\frac{1}{365}
$$

- Therefore:

$$
E[X] = \binom{50}{2}\cdot \frac{1}{365}.
$$

### What I initially missed / corrected

- I almost wrote $E[X]=I_1+\cdots+I_k$.
  Correction: linearity is about expectations:

$$
E[X]=E[I_1]+\cdots+E[I_k].
$$

- Independence between indicators is **not** required for linearity.

---

### Part (ii) — Expected # of days with at least 2 birthdays

- Let $Y$ be the number of days (out of 365) on which at least two of the 50 people were born.
- For each day $d\in{1,\dots,365}$, define an indicator:
  - $J_d = 1{\text{at least two of the 50 people were born on day }d}$.

- Then:

$$
Y=\sum_{d=1}^{365} J_d
$$

and by linearity + symmetry:

$$
E[Y]=\sum_{d=1}^{365} E[J_d] = 365\cdot E[J_1].
$$

- For a fixed day, let $N$ be the number of people born on that day. Then

$$
N\sim \text{Bin}(50,1/365)
$$

and

$$
E[J_1]=P(N\ge 2)=1-P(N=0)-P(N=1).
$$

- Compute:

$$
P(N=0)=\left(\frac{364}{365}\right)^{50}
$$

and (this is where I initially forgot the “choose which person” factor)

$$
P(N=1)=\binom{50}{1}\cdot \frac{1}{365}\cdot \left(\frac{364}{365}\right)^{49}.
$$

- Therefore:

$$
E[Y]
=365\left[
1-\left(\frac{364}{365}\right)^{50}
-\binom{50}{1}\cdot \frac{1}{365}\cdot \left(\frac{364}{365}\right)^{49}
\right].
$$

### Book's solution (for comparison)

- Same result, using $\binom{50}{1}=50$:

$$
365\left[
1-\left(\frac{364}{365}\right)^{50}
-50\cdot \frac{1}{365}\cdot \left(\frac{364}{365}\right)^{49}
\right].
$$

## Problem 5 — Haribo bags → students (two expectations)

**Question.**
A total of 20 bags of Haribo gummi bears are randomly distributed to the 20 students in a certain Stat 110 section. Each bag is obtained by a random student, and the outcomes of who gets which bag are independent.

Find:

1. the average number of bags that the **first three students** get in total
2. the average number of **students who get at least one bag**

---

## Part (i) — Expected # of bags received by students 1–3

### My approach (bag-indicators)

- For each bag $j \in \{1,2,\dots,20\}$, define an indicator:

$$
X_j =
\begin{cases}
1 & \text{if bag } j \text{ goes to one of students } \{1,2,3\} \\
0 & \text{otherwise}
\end{cases}
$$

- Let $X$ be the total number of bags received by students 1–3:

$$
X=\sum_{j=1}^{20} X_j
$$

- By linearity (and symmetry):

$$
E[X] = \sum_{j=1}^{20}E[X_j] = 20\,E[X_1]
$$

- Since a given bag is equally likely to go to any of the 20 students:

$$
E[X_1]=P(X_1=1)=\frac{3}{20}
$$

- Therefore:

$$
E[X] = 20\cdot \frac{3}{20} = 3
$$

### Book’s approach (student-count RVs)

- Let $X_j^{(\text{book})}$ be the **number of bags** that student $j$ gets.
  Then (for each fixed student $j$):

$$
X_j^{(\text{book})} \sim \text{Bin}\!\left(20,\frac{1}{20}\right)
$$

so

$$
E\!\left[X_j^{(\text{book})}\right] = 20\cdot \frac{1}{20} = 1
$$

- By linearity:

$$
E\!\left[X_1^{(\text{book})} + X_2^{(\text{book})} + X_3^{(\text{book})}\right] = 1+1+1 = 3
$$

### Bridge (why both methods are the same)

Both expressions count the **same total number of bags received by students 1–3**:

- “Count by bags” (my way): sum over bags $j$, whether bag $j$ landed in $\{1,2,3\}$.
- “Count by students” (book): sum over students $1,2,3$, how many bags each got.

So the same random variable $X$ can be written either as

$$
X=\sum_{j=1}^{20} X_j
\qquad \text{or} \qquad
X=X_1^{(\text{book})}+X_2^{(\text{book})}+X_3^{(\text{book})}.
$$

Linearity works in either representation.

### What I initially missed / corrected

- Independence is **not needed** to use linearity:

$$
E\left[\sum_j X_j\right]=\sum_j E[X_j]
$$

always holds.

- But independence _is_ useful (in Part ii) when computing probabilities like $\left(\frac{19}{20}\right)^{20}$.

---

## Part (ii) — Expected # of students who get at least one bag

### My approach (student “at least one” indicators)

- For each student $j \in \{1,2,\dots,20\}$, define an indicator:

$$
Y_j =
\begin{cases}
1 & \text{if student } j \text{ gets }\ge 1 \text{ bag} \\
0 & \text{otherwise}
\end{cases}
$$

- Let $Y$ be the number of students who get at least one bag:

$$
Y=\sum_{j=1}^{20} Y_j
$$

- By linearity + symmetry:

$$
E[Y] = \sum_{j=1}^{20}E[Y_j] = 20\,E[Y_1] = 20\,P(Y_1=1)
$$

- Compute $P(Y_1=1)$ via the complement event “student 1 gets **zero** bags”.

For a single bag, $P(\text{does NOT go to student 1})=\frac{19}{20}$.  
Using independence across the 20 bags:

$$
P(\text{student 1 gets no bags})=\left(\frac{19}{20}\right)^{20}
$$

So:

$$
E[Y_1]=P(Y_1=1)=1-\left(\frac{19}{20}\right)^{20}
$$

- Therefore:

$$
E[Y] = 20\left[1-\left(\frac{19}{20}\right)^{20}\right]
$$

### Book’s answer (same idea, different notation)

The book defines $I_j$ as the indicator that student $j$ gets at least one bag, i.e.

$$
I_j = 1\{X_j^{(\text{book})}\ge 1\}.
$$

Then:

$$
E(I_1+\cdots+I_{20})
=20E(I_1)
=20P(I_1=1)
=20\left[1-\left(\frac{19}{20}\right)^{20}\right].
$$

### Bridge (matching my notation to the book)

- My $Y_j$ **is exactly** the book’s $I_j$.
- The book’s $X_j^{(\text{book})}$ is a _count_ RV (“how many bags student $j$ gets”), which is **different from** my Part (i) $X_j$ (which was a _bag-indexed indicator_).

---

### Quick self-check (1 sentence)

- $\left(\frac{19}{20}\right)^{20}$ is the probability that a specific student gets **zero bags**, because all 20 bags independently avoid that student.

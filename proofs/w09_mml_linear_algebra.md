# Week 9 - S2: MML Linear Algebra Exercises

**Sources:**

- [MML source catalog](../sources/mml/)
- [Mathematics for Machine Learning - official PDF](https://mml-book.github.io/book/mml-book.pdf)

**Source status:** The exercise prompts were verified against the local study
copy of the book. No source solutions were provided, so the solutions below are
independent derivations based on my handwritten work.

For Phase 2, each exercise records the prompt, my polished solution, the main
corrections from review, and any structural insight that makes the result easier
to understand or reuse.

---

## Additional foundation exercise - Exercise 2.1

**Status:** Reviewed and corrected.

**Prompt.**
Consider $\left(\mathbb{R}\setminus\{-1\},\star\right)$, where

$$
a\star b := ab+a+b,
\qquad
a,b\in\mathbb{R}\setminus\{-1\}.
$$

1. Show that the stated set and operation form an Abelian group.
2. Solve

$$
3\star x\star x=15
$$

in this group.

### My solution

Let

$$
G=\mathbb{R}\setminus\{-1\}.
$$

#### Part 1: The group properties

**Closure.**
Take any $a,b\in G$. Suppose, by contradiction, that $a\star b=-1$. Then

$$
ab+a+b=-1,
$$

so

$$
ab+a+b+1=0.
$$

Factoring gives

$$
(a+1)(b+1)=0.
$$

This would imply that $a=-1$ or $b=-1$, contradicting the assumption that
$a,b\in G$. Therefore, $a\star b\in G$, so the operation is closed.

**Associativity.**
For any $a,b,c\in G$,

$$
\begin{aligned}
(a\star b)\star c
&=(ab+a+b)c+(ab+a+b)+c\\
&=abc+ab+ac+bc+a+b+c,
\end{aligned}
$$

while

$$
\begin{aligned}
a\star(b\star c)
&=a(bc+b+c)+a+(bc+b+c)\\
&=abc+ab+ac+bc+a+b+c.
\end{aligned}
$$

Thus,

$$
(a\star b)\star c=a\star(b\star c).
$$

**Neutral element.**
The neutral element is $0$, since

$$
a\star 0=a(0)+a+0=a
$$

and

$$
0\star a=0(a)+0+a=a.
$$

**Inverse element.**
For $a\in G$, let $b$ be its inverse. It must satisfy

$$
a\star b=0.
$$

Therefore,

$$
ab+a+b=0,
$$

which gives

$$
b(a+1)=-a.
$$

Since $a\ne -1$, we may divide by $a+1$:

$$
b=-\frac{a}{a+1}.
$$

We also need to verify that this candidate belongs to $G$. Indeed,

$$
-\frac{a}{a+1}+1
=\frac{1}{a+1}
\ne 0,
$$

so

$$
-\frac{a}{a+1}\ne -1.
$$

Thus every $a\in G$ has an inverse in $G$.

**Commutativity.**
For any $a,b\in G$,

$$
a\star b
=ab+a+b
=ba+b+a
=b\star a.
$$

Therefore, $\left(G,\star\right)$ is an Abelian group.

#### Part 2: Solving the equation

First,

$$
3\star x=3x+3+x=4x+3.
$$

Using associativity,

$$
\begin{aligned}
(3\star x)\star x
&=(4x+3)\star x\\
&=(4x+3)x+(4x+3)+x\\
&=4x^2+8x+3.
\end{aligned}
$$

Hence,

$$
4x^2+8x+3=15.
$$

Rearranging and simplifying,

$$
\begin{aligned}
4x^2+8x-12&=0,\\
x^2+2x-3&=0,\\
(x+3)(x-1)&=0.
\end{aligned}
$$

Therefore,

$$
\boxed{x=-3\quad\text{or}\quad x=1}.
$$

Both values belong to $G$ because neither is $-1$.

### What I corrected after review

**Closure.** I made the closure argument explicit by factoring the relevant
expression:

$$
ab+a+b+1=(a+1)(b+1).
$$

**Inverse membership.** When finding the inverse, I had already checked that
the denominator is nonzero. I also needed to verify that the inverse itself is
not $-1$, so that it belongs to the group.

**Associativity.** I wrote both associative expansions in full to show that
they produce the same expression.

**Final domain check.** I checked that both solutions to the quadratic belong
to the original set.

### Structural insight

The operation becomes ordinary multiplication after shifting every number by
$1$. Define

$$
\phi:G\to\mathbb{R}\setminus\{0\},
\qquad
\phi(a)=a+1.
$$

Then

$$
\begin{aligned}
\phi(a\star b)
&=(a\star b)+1\\
&=ab+a+b+1\\
&=(a+1)(b+1)\\
&=\phi(a)\phi(b).
\end{aligned}
$$

The map $\phi$ is a bijection, with inverse $\phi^{-1}(y)=y-1$. Therefore,
$\left(G,\star\right)$ has the same group structure as
$\left(\mathbb{R}\setminus\{0\},\cdot\right)$.

This explains the results from the direct proof. The neutral element $0$ maps
to the multiplicative identity $1$, while commutativity and associativity come
from ordinary multiplication. The inverse under $\star$ corresponds to taking
a reciprocal:

$$
\phi\left(a^{-1}_{\star}\right)=\frac{1}{a+1}.
$$

Thus,

$$
a^{-1}_{\star}
=\frac{1}{a+1}-1
=-\frac{a}{a+1}.
$$

---

## Additional foundation exercise - Exercise 2.4, selected parts

**Status:** Reviewed; one arithmetic correction in part D.

**Prompt.**
Compute the selected matrix products if they are defined.

### My solution

#### Part A

The first matrix has shape $3\times 2$, while the second has shape
$3\times 3$. The inner dimensions do not match:

$$
(3\times 2)(3\times 3).
$$

Therefore, the product is not defined.

#### Part B

Both matrices have shape $3\times 3$, so the product is defined:

$$
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}
\begin{bmatrix}
1&1&0\\
0&1&1\\
1&0&1
\end{bmatrix}
=
\begin{bmatrix}
4&3&5\\
10&9&11\\
16&15&17
\end{bmatrix}.
$$

#### Part D

The first matrix has shape $2\times 4$, and the second has shape
$4\times 2$. Therefore, the result has shape $2\times 2$:

$$
\begin{bmatrix}
1&2&1&2\\
4&1&-1&-4
\end{bmatrix}
\begin{bmatrix}
0&3\\
1&-1\\
2&1\\
5&2
\end{bmatrix}
=
\begin{bmatrix}
14&6\\
-21&2
\end{bmatrix}.
$$

### What I corrected after review

The upper-right entry in part D was initially written as $5$. Its correct
value is

$$
1(3)+2(-1)+1(1)+2(2)=6.
$$

The other computed entries and the dimension check in part A were correct.
Parts C and E were not attempted.

---

## Additional foundation exercise - Exercise 2.5, part A

**Status:** Reviewed and correct.

**Prompt.**
Find the solution set of the inhomogeneous system

$$
Ax=b,
$$

where

$$
A=
\begin{bmatrix}
1&1&-1&-1\\
2&5&-7&-5\\
2&-1&1&3\\
5&2&-4&2
\end{bmatrix},
\qquad
b=
\begin{bmatrix}
1\\
-2\\
4\\
6
\end{bmatrix}.
$$

### My solution

Start with the augmented matrix:

$$
\left[
\begin{array}{rrrr|r}
1&1&-1&-1&1\\
2&5&-7&-5&-2\\
2&-1&1&3&4\\
5&2&-4&2&6
\end{array}
\right].
$$

Subtracting suitable multiples of the first row from the other rows gives

$$
\left[
\begin{array}{rrrr|r}
1&1&-1&-1&1\\
0&3&-5&-3&-4\\
0&-3&3&5&2\\
0&-3&1&7&1
\end{array}
\right].
$$

Adding the second row to the third and fourth rows gives

$$
\left[
\begin{array}{rrrr|r}
1&1&-1&-1&1\\
0&3&-5&-3&-4\\
0&0&-2&2&-2\\
0&0&-4&4&-3
\end{array}
\right].
$$

Finally, subtracting twice the third row from the fourth produces

$$
\left[
\begin{array}{rrrr|r}
1&1&-1&-1&1\\
0&3&-5&-3&-4\\
0&0&-2&2&-2\\
0&0&0&0&1
\end{array}
\right].
$$

The final row represents the contradiction

$$
0=1.
$$

Therefore, the system is inconsistent and has no solutions:

$$
\boxed{S=\varnothing}.
$$

### Interpretation

The coefficient matrix does not provide the contradiction by itself. The
contradiction appears only in the augmented matrix, because the right-hand side
is incompatible with the linear combinations represented by the columns of
$A$.

---

## Additional foundation exercise - Exercise 2.6

**Status:** Reviewed and correct.

**Prompt.**
Use Gaussian elimination to find all solutions of

$$
Ax=b,
$$

where

$$
A=
\begin{bmatrix}
0&1&0&0&1&0\\
0&0&0&1&1&0\\
0&1&0&0&0&1
\end{bmatrix},
\qquad
b=
\begin{bmatrix}
2\\
-1\\
1
\end{bmatrix}.
$$

### My solution

The augmented matrix is

$$
\left[
\begin{array}{rrrrrr|r}
0&1&0&0&1&0&2\\
0&0&0&1&1&0&-1\\
0&1&0&0&0&1&1
\end{array}
\right].
$$

Subtract the first row from the third, multiply the resulting third row by
$-1$, and then eliminate the fifth-column entries from the first two rows. This
gives

$$
\left[
\begin{array}{rrrrrr|r}
0&1&0&0&0&1&1\\
0&0&0&1&0&1&-2\\
0&0&0&0&1&-1&1
\end{array}
\right].
$$

The pivot variables are $x_2$, $x_4$, and $x_5$. The free variables are
$x_1$, $x_3$, and $x_6$. Let

$$
x_1=c,
\qquad
x_3=d,
\qquad
x_6=e.
$$

The pivot equations give

$$
x_2=1-e,
\qquad
x_4=-2-e,
\qquad
x_5=1+e.
$$

Therefore,

$$
x=
\begin{bmatrix}
c\\
1-e\\
d\\
-2-e\\
1+e\\
e
\end{bmatrix}.
$$

Equivalently,

$$
\boxed{
x=
c\begin{bmatrix}1\\0\\0\\0\\0\\0\end{bmatrix}
+d\begin{bmatrix}0\\0\\1\\0\\0\\0\end{bmatrix}
+e\begin{bmatrix}0\\-1\\0\\-1\\1\\1\end{bmatrix}
+\begin{bmatrix}0\\1\\0\\-2\\1\\0\end{bmatrix}
}.
$$

### Interpretation

The last vector is one particular solution of the inhomogeneous system. The
three vectors multiplied by $c$, $d$, and $e$ describe every solution of the
corresponding homogeneous system. Thus, the complete solution set is a
particular solution plus the null space of $A$.

---

## Curriculum exercise - Exercise 2.10, part A

**Status:** Reviewed and completed.

**Prompt.**
Determine whether the following vectors are linearly independent:

$$
x_1=
\begin{bmatrix}
2\\
-1\\
3
\end{bmatrix},
\qquad
x_2=
\begin{bmatrix}
1\\
1\\
-2
\end{bmatrix},
\qquad
x_3=
\begin{bmatrix}
3\\
-3\\
8
\end{bmatrix}.
$$

### My solution

Place the vectors in the columns of a matrix:

$$
A=
\begin{bmatrix}
2&1&3\\
-1&1&-3\\
3&-2&8
\end{bmatrix}.
$$

The vectors are linearly independent exactly when the homogeneous system

$$
A\lambda=0
$$

has only the trivial solution. Gaussian elimination gives

$$
A
\sim
\begin{bmatrix}
1&0&2\\
0&1&-1\\
0&0&0
\end{bmatrix}.
$$

The third coefficient is free. Setting it equal to $1$ gives

$$
\lambda_1=-2,
\qquad
\lambda_2=1,
\qquad
\lambda_3=1.
$$

Therefore,

$$
-2x_1+x_2+x_3=0.
$$

This is a nontrivial linear combination that produces the zero vector, so the
vectors are not linearly independent. Equivalently,

$$
x_3=2x_1-x_2.
$$

### What I completed after review

My row reduction and conclusion were correct. I made the free variable
explicit and used it to exhibit a nonzero coefficient vector. This turns the
row-reduction evidence into a complete linear-dependence argument.

---

## Curriculum exercise - Exercise 2.17

**Status:** Reviewed and corrected.

**Prompt.**
Consider the linear mapping from three-dimensional real space to
four-dimensional real space defined by

$$
\Phi
\left(
\begin{bmatrix}
x_1\\
x_2\\
x_3
\end{bmatrix}
\right)
=
\begin{bmatrix}
3x_1+2x_2+x_3\\
x_1+x_2+x_3\\
x_1-3x_2\\
2x_1+3x_2+x_3
\end{bmatrix}.
$$

Find its transformation matrix and rank, then compute its kernel and image and
the dimensions of those spaces.

### My solution

Reading the coefficients of $x_1$, $x_2$, and $x_3$ from each output
coordinate gives the transformation matrix

$$
A_\Phi=
\begin{bmatrix}
3&2&1\\
1&1&1\\
1&-3&0\\
2&3&1
\end{bmatrix}.
$$

Gaussian elimination gives

$$
A_\Phi
\sim
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1\\
0&0&0
\end{bmatrix}.
$$

There are three pivot columns. Therefore,

$$
\boxed{\operatorname{rank}(A_\Phi)=3}.
$$

There are no free variables in the homogeneous system

$$
A_\Phi x=0.
$$

Hence the only solution is the zero vector, so

$$
\ker(\Phi)=\{0\},
\qquad
\dim\bigl(\ker(\Phi)\bigr)=0.
$$

All three columns are pivot columns. A basis for the image is therefore given
by the three original columns of the transformation matrix:

$$
\operatorname{Im}(\Phi)
=
\operatorname{span}
\left\{
\begin{bmatrix}
3\\
1\\
1\\
2
\end{bmatrix},
\begin{bmatrix}
2\\
1\\
-3\\
3
\end{bmatrix},
\begin{bmatrix}
1\\
1\\
0\\
1
\end{bmatrix}
\right\}.
$$

Thus,

$$
\dim\bigl(\operatorname{Im}(\Phi)\bigr)=3.
$$

The rank-nullity theorem confirms the result:

$$
\dim(\mathbb{R}^3)
=
\dim\bigl(\ker(\Phi)\bigr)
+
\dim\bigl(\operatorname{Im}(\Phi)\bigr)
=0+3=3.
$$

### What I corrected after review

The calculation and interpretation were correct. The final notation should be

$$
\operatorname{rank}(A_\Phi)=3,
$$

not the dimension of the rank. Rank is already the number of pivot columns,
which is also the dimension of the image.

---

## Additional geometry exercise - Exercise 3.5

**Status:** Reviewed and clarified.

**Prompt.**
In the Euclidean vector space $\mathbb{R}^5$, let

$$
U=
\operatorname{span}
\left\{
\begin{bmatrix}0\\-1\\2\\0\\2\end{bmatrix},
\begin{bmatrix}1\\-3\\1\\-1\\2\end{bmatrix},
\begin{bmatrix}-3\\4\\1\\2\\1\end{bmatrix},
\begin{bmatrix}-1\\-3\\5\\0\\7\end{bmatrix}
\right\}
$$

and

$$
x=
\begin{bmatrix}
-1\\
-9\\
-1\\
4\\
1
\end{bmatrix}.
$$

Determine the orthogonal projection of $x$ onto $U$ and the distance from
$x$ to $U$.

### My solution

The four given generators are not linearly independent. If they are denoted by
$u_1,u_2,u_3,u_4$, respectively, then

$$
u_4=u_1+2u_2+u_3.
$$

Therefore, the first three vectors span the same subspace. Let

$$
B=
\begin{bmatrix}
0&1&-3\\
-1&-3&4\\
2&1&1\\
0&-1&2\\
2&2&1
\end{bmatrix}.
$$

The columns of $B$ are linearly independent, so the orthogonal projection
matrix onto $U$ is

$$
P=B(B^\top B)^{-1}B^\top.
$$

First,

$$
B^\top B=
\begin{bmatrix}
9&9&0\\
9&16&-14\\
0&-14&31
\end{bmatrix},
$$

with inverse

$$
(B^\top B)^{-1}
=
\begin{bmatrix}
\frac{100}{63}&-\frac{31}{21}&-\frac{2}{3}\\
-\frac{31}{21}&\frac{31}{21}&\frac{2}{3}\\
-\frac{2}{3}&\frac{2}{3}&\frac{1}{3}
\end{bmatrix}.
$$

Also,

$$
B^\top x=
\begin{bmatrix}
9\\
23\\
-25
\end{bmatrix}.
$$

The coordinates of the projection in the basis given by the columns of $B$
are therefore

$$
(B^\top B)^{-1}B^\top x
=
\begin{bmatrix}
-3\\
4\\
1
\end{bmatrix}.
$$

Thus,

$$
\boxed{
\pi_U(x)
=
B
\begin{bmatrix}
-3\\
4\\
1
\end{bmatrix}
=
\begin{bmatrix}
1\\
-5\\
-1\\
-2\\
3
\end{bmatrix}
}.
$$

For the distance, compute the orthogonal residual:

$$
r
=
x-\pi_U(x)
=
\begin{bmatrix}
-2\\
-4\\
0\\
6\\
-2
\end{bmatrix}.
$$

Therefore,

$$
\begin{aligned}
d(x,U)
&=\|r\|\\
&=\sqrt{(-2)^2+(-4)^2+0^2+6^2+(-2)^2}\\
&=\sqrt{60}\\
&=\boxed{2\sqrt{15}}.
\end{aligned}
$$

### What I clarified after review

The projection and distance were correct. The projection formula requires a
matrix with linearly independent columns. Using all four original generators
would make the Gram matrix singular. The relation among the generators
justifies replacing them with the first three vectors before applying the
formula.

Computing the projection coordinates first also avoids multiplying out the
entire $5\times5$ projection matrix while producing the same result.

---

## Additional geometry exercise - Exercise 3.8

**Status:** Reviewed and correct.

**Prompt.**
Use the Gram-Schmidt method to turn the basis

$$
b_1=
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix},
\qquad
b_2=
\begin{bmatrix}
-1\\
2\\
0
\end{bmatrix}
$$

into an orthonormal basis for the same two-dimensional subspace of
$\mathbb{R}^3$.

### My solution

Normalize the first basis vector:

$$
c_1
=
\frac{b_1}{\|b_1\|}
=
\frac{1}{\sqrt{3}}
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}.
$$

Since $c_1$ is a unit vector, the projection of $b_2$ onto its direction is

$$
\begin{aligned}
\operatorname{proj}_{c_1}(b_2)
&=(c_1^\top b_2)c_1\\
&=\frac{1}{3}
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}.
\end{aligned}
$$

Remove this component from $b_2$:

$$
\begin{aligned}
v_2
&=b_2-\operatorname{proj}_{c_1}(b_2)\\
&=
\begin{bmatrix}
-1\\
2\\
0
\end{bmatrix}
-
\frac{1}{3}
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}\\
&=\frac{1}{3}
\begin{bmatrix}
-4\\
5\\
-1
\end{bmatrix}.
\end{aligned}
$$

Its norm is

$$
\|v_2\|
=
\frac{\sqrt{42}}{3}.
$$

Normalizing gives

$$
c_2
=
\frac{v_2}{\|v_2\|}
=
\frac{1}{\sqrt{42}}
\begin{bmatrix}
-4\\
5\\
-1
\end{bmatrix}.
$$

Therefore, an orthonormal basis for the subspace is

$$
\boxed{
C=(c_1,c_2)
=
\left(
\frac{1}{\sqrt{3}}
\begin{bmatrix}1\\1\\1\end{bmatrix},
\frac{1}{\sqrt{42}}
\begin{bmatrix}-4\\5\\-1\end{bmatrix}
\right)
}.
$$

As a check,

$$
c_1^\top c_2=0,
\qquad
\|c_1\|=\|c_2\|=1.
$$

### What I corrected after review

No arithmetic correction was needed. I simplified the projection notation by
using the fact that $c_1$ is already a unit vector.

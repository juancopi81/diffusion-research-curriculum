# Week 6 — S2 (Stat110 Practice): Transformations and Convolutions

**Topics:** transformations, Jacobians, convolutions, polar coordinates, Gaussian geometry

**Resources:**

- [Week 6 Lecture 22 notes](../notes/w06_stat110_transformations_convolutions.md)
- `/Users/juanpineros/Downloads/strategic_practice_and_homework_8.pdf`

---

## Warm-up — Lecture-style Transformation

## Warm-up Problem 0

**Prompt.**
In the lecture notes, we found the PDF of $Y=e^Z$ for $Z\sim N(0,1)$. Now let

$$
Z\sim N(0,1),
\qquad
W=e^{Z+1}.
$$

Find the PDF of $W$. State the support of $W$, and identify exactly what changed compared with the lecture example $Y=e^Z$.

**Solution.**
Since

$$
W=e^{Z+1},
$$

we invert the transformation:

$$
z+1=\log w
\qquad\Longrightarrow\qquad
z=\log w-1.
$$

The derivative of the inverse transformation is

$$
\frac{dz}{dw}=\frac{1}{w}.
$$

The support is still positive:

$$
w>0.
$$

Therefore, for $w>0$,

$$
\begin{aligned}
f_W(w)
&=f_Z(\log w-1)\left|\frac{dz}{dw}\right|\\
&=\frac{1}{\sqrt{2\pi}}
\exp\left(-\frac{(\log w-1)^2}{2}\right)\frac{1}{w}.
\end{aligned}
$$

So

$$
\boxed{
f_W(w)=
\frac{1}{w\sqrt{2\pi}}
\exp\left(-\frac{(\log w-1)^2}{2}\right),
\qquad w>0.
}
$$

For $w\le 0$, $f_W(w)=0$.

Compared with the lecture example $Y=e^Z$, the support and Jacobian factor are unchanged. The only change is that the normal variable on the log scale is shifted:

$$
\log W=Z+1\sim N(1,1),
$$

so the exponent changes from $-(\log y)^2/2$ to $-(\log w-1)^2/2$.

---

## Strategic Practice 8 — Transformations

## Practice 8 — Transformations Problem 2

**Prompt.**
Let $U \sim \mathrm{Unif}(0,2\pi)$ and let $T \sim \mathrm{Expo}(1)$ be independent of $U$. Define

$$
X=\sqrt{2T}\cos U
\qquad\text{and}\qquad
Y=\sqrt{2T}\sin U.
$$

Find the joint PDF of $(X,Y)$. Are they independent? What are their marginal distributions?

**Solution.**
Let

$$
A=\sqrt{2T}.
$$

Then

$$
X=A\cos U,
\qquad
Y=A\sin U.
$$

So $(A,U)$ are polar coordinates for $(X,Y)$:

```text
          y
          |
          |        (x,y) = (a cos u, a sin u)
          |          *
          |         /|
          |        / |  y = a sin u
          |       /u |
----------+------*--+------------- x
          |      0  x = a cos u
          |
          radius = a
```

First find the PDF of $A$. Since $A=\sqrt{2T}$,

$$
a^2=2t
\qquad\Longrightarrow\qquad
t=\frac{a^2}{2}.
$$

Also,

$$
\frac{dt}{da}=a.
$$

Since $T\sim \mathrm{Expo}(1)$,

$$
f_T(t)=e^{-t},
\qquad t\ge 0.
$$

Therefore, for $a\ge 0$,

$$
f_A(a)
=f_T\left(\frac{a^2}{2}\right)\left|\frac{dt}{da}\right|
=e^{-a^2/2}a.
$$

Since $A$ and $U$ are independent,

$$
f_{A,U}(a,u)
=f_A(a)f_U(u)
=ae^{-a^2/2}\frac{1}{2\pi},
\qquad a\ge 0,\ 0\le u<2\pi.
$$

Now use the transformation

$$
x=a\cos u,
\qquad
y=a\sin u.
$$

The Jacobian matrix is

$$
\frac{\partial(x,y)}{\partial(a,u)}
=
\begin{pmatrix}
\frac{\partial x}{\partial a} & \frac{\partial x}{\partial u}\\
\frac{\partial y}{\partial a} & \frac{\partial y}{\partial u}
\end{pmatrix}.
$$

Since

$$
x=a\cos u,
\qquad
y=a\sin u,
$$

we get

$$
\frac{\partial(x,y)}{\partial(a,u)}
=
\begin{pmatrix}
\cos u & -a\sin u\\
\sin u & a\cos u
\end{pmatrix}.
$$

Its determinant is

$$
a\cos^2 u+a\sin^2 u
=a(\cos^2 u+\sin^2 u)
=a.
$$

So the inverse Jacobian factor is

$$
\left|\frac{\partial(a,u)}{\partial(x,y)}\right|
=\frac{1}{a}.
$$

Thus, for $(x,y)\ne(0,0)$,

$$
\begin{aligned}
f_{X,Y}(x,y)
&=f_{A,U}(a,u)\left|\frac{\partial(a,u)}{\partial(x,y)}\right|\\
&=\left(ae^{-a^2/2}\frac{1}{2\pi}\right)\frac{1}{a}\\
&=\frac{e^{-a^2/2}}{2\pi}.
\end{aligned}
$$

Finally, rewrite $a$ in terms of $x$ and $y$. Since

$$
x=a\cos u,
\qquad
y=a\sin u,
$$

we square both sides:

$$
x^2=a^2\cos^2 u,
\qquad
y^2=a^2\sin^2 u.
$$

Then add them:

$$
x^2+y^2
=a^2\cos^2 u+a^2\sin^2 u.
$$

Factor out $a^2$:

$$
x^2+y^2
=a^2(\cos^2 u+\sin^2 u).
$$

Since $\cos^2 u+\sin^2 u=1$,

$$
x^2+y^2=a^2.
$$

And since $a\ge 0$,

$$
a=\sqrt{x^2+y^2},
$$

Therefore,

$$
\boxed{
f_{X,Y}(x,y)
=\frac{1}{2\pi}e^{-(x^2+y^2)/2},
\qquad -\infty<x<\infty,\ -\infty<y<\infty.
}
$$

The point $(0,0)$ does not matter for the PDF because it is a single point with probability $0$.

To check independence, factor the joint PDF:

$$
\begin{aligned}
f_{X,Y}(x,y)
&=\frac{1}{2\pi}e^{-(x^2+y^2)/2}\\
&=\frac{1}{2\pi}e^{-x^2/2}e^{-y^2/2}\\
&=\left(\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\right)
\left(\frac{1}{\sqrt{2\pi}}e^{-y^2/2}\right).
\end{aligned}
$$

This separates into one function of $x$ times one function of $y$, so $X$ and $Y$ are independent.

The marginal PDFs are

$$
f_X(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2},
\qquad -\infty<x<\infty,
$$

and

$$
f_Y(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2},
\qquad -\infty<y<\infty.
$$

Therefore,

$$
\boxed{
X\sim N(0,1),
\qquad
Y\sim N(0,1),
\qquad
X\perp Y.
}
$$

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

The book uses the same idea, but takes a slightly faster route. Instead of first defining the radius

$$
A=\sqrt{2T},
$$

it works directly with $(U,T)$. Since

$$
X^2+Y^2
=2T(\cos^2 U+\sin^2 U)
=2T,
$$

we can think of $T$ as half of the squared distance from the origin:

$$
T=\frac{X^2+Y^2}{2}.
$$

The book then uses the Jacobian for the direct transformation from $(U,T)$ to $(X,Y)$. This Jacobian has absolute value $1$, so substituting

$$
t=\frac{x^2+y^2}{2}
$$

into

$$
f_{U,T}(u,t)=\frac{1}{2\pi}e^{-t}
$$

gives the same joint PDF:

$$
f_{X,Y}(x,y)
=\frac{1}{2\pi}e^{-(x^2+y^2)/2}.
$$

So my solution and the book solution are the same conceptually:

- My route makes the radius $A$ explicit first, then uses the usual polar-coordinate Jacobian.
- The book route works directly with $T$, using the fact that $2T$ is the squared radius.

### Intuition

The final joint PDF is

$$
f_{X,Y}(x,y)
=\frac{1}{2\pi}e^{-(x^2+y^2)/2}.
$$

The important part is $x^2+y^2$, which is the squared distance from $(0,0)$. So the density depends only on how far the point is from the origin, not on the direction.

This means:

- points near $(0,0)$ are most likely;
- points farther from $(0,0)$ are less likely;
- points at the same distance from $(0,0)$ have the same density.

Geometrically, the distribution is a circular bell shape centered at the origin.

Independence requires one more fact: the density factors into an $x$-part times a $y$-part. Circular symmetry alone is not enough to prove independence, but here the factorization shows that

$$
X\sim N(0,1),
\qquad
Y\sim N(0,1),
$$

and $X$ and $Y$ are independent.

### Box-Muller method

This result is called the **Box-Muller method**. It gives a way to generate two independent standard Normal random variables from:

- a random angle $U\sim \mathrm{Unif}(0,2\pi)$;
- a random radius controlled by $T\sim \mathrm{Expo}(1)$.

The intuition is:

$$
\text{uniform angle}+\text{right random radius}
\Longrightarrow
\text{2D standard Normal point}.
$$

A concrete real-world application is simulation. Computers are very good at generating Uniform random numbers, but many models need Normal random numbers. Box-Muller converts Uniform randomness into Normal randomness, which is useful in Monte Carlo simulations, uncertainty modeling, synthetic Gaussian noise, and financial simulations where random shocks are often modeled as approximately Normal.

### Memory card (quick review)

- $U$ chooses the direction.
- $A=\sqrt{2T}$ chooses the radius.
- The final point $(X,Y)$ lands in the plane with a circular Normal density.
- The joint PDF factors, so $X$ and $Y$ are independent.
- Each marginal is standard Normal:

  $$
  X\sim N(0,1),
  \qquad
  Y\sim N(0,1).
  $$

---

## Practice 8 — Transformations Problem 3

**Prompt.**
Let $X$ and $Y$ be independent, continuous r.v.s with PDFs $f_X$ and $f_Y$ respectively, and let $T=X+Y$. Find the joint PDF of $T$ and $X$, and use this to give an alternative proof that

$$
f_T(t)=\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx,
$$

a result obtained in class using the law of total probability.

---

## Stat 110 Homework 8

## Homework 8 — Problem 6

**Prompt.**
Let $X,Y$ be continuous r.v.s with a spherically symmetric joint distribution, which means that the joint PDF is of the form

$$
f(x,y)=g(x^2+y^2)
$$

for some function $g$. Let $(R,\theta)$ be the polar coordinates of $(X,Y)$, so

$$
R^2=X^2+Y^2
$$

is the squared distance from the origin and $\theta$ is the angle (in $[0,2\pi)$), with $X=R\cos\theta,\ Y=R\sin\theta$.

(a) Explain intuitively why $R$ and $\theta$ are independent. Then prove this by finding the joint PDF of $(R,\theta)$.

(b) What is the joint PDF of $(R,\theta)$ when $(X,Y)$ is Uniform in the unit disc $\{(x,y): x^2+y^2\le 1\}$?

(c) What is the joint PDF of $(R,\theta)$ when $X$ and $Y$ are i.i.d. $N(0,1)$?

---

## Homework 8 — Problem 5

**Prompt.**
Let $X$ and $Y$ be independent positive r.v.s, with PDFs $f_X$ and $f_Y$ respectively, and consider the product $T=XY$. When asked to find the PDF of $T$, Jacobno argues that "it's like a convolution, with a product instead of a sum. To have $T=t$ we need $X=x$ and $Y=t/x$ for some $x$; that has probability $f_X(x)f_Y(t/x)$, so summing up these possibilities we get that the PDF of $T$ is

$$
\int_0^\infty f_X(x)f_Y(t/x)\,dx.
$$

Evaluate Jacobno's argument, while getting the PDF of $T$ (as an integral) in 2 ways:

(a) using the continuous law of total probability to get the CDF, and then taking the derivative (you can assume that swapping the derivative and integral is valid);

(b) by taking the log of both sides of $T=XY$ and doing a convolution (and then converting back to get the PDF of $T$).

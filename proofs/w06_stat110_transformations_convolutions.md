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

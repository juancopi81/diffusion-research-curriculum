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

### My attempt

I want the PDF of the sum

$$
T=X+Y.
$$

The problem asks for the joint PDF of $T$ and $X$, so I keep $X$ as the second coordinate and transform from the old variables $(X,Y)$ to the new variables $(T,X)$.

For concreteness, I can look at the new-coordinate point

$$
(T,X)=(10,10).
$$

This combines two constraints:

$$
T=10
\qquad\text{and}\qquad
X=10.
$$

The constraint $T=10$ means

$$
x+y=10,
$$

which is a diagonal line in the old $(x,y)$-plane. The constraint $X=10$ is a vertical line:

```text
y
|
10 +\
   | \
   |  \
   |   \    t = x + y = 10
   |    \
   |     \
 0 +------*---------- x
          10
          x = 10
```

The intersection is the old point

$$
(X,Y)=(10,0),
$$

since $10=10+0$.

Let

$$
\vec A=(T,X)
\qquad\text{and}\qquad
\vec B=(X,Y).
$$

In lowercase variables, this transformation is

$$
t=x+y,
\qquad
x=x.
$$

Now invert it. If the new coordinates are $(t,x)$, then the old $X$-coordinate is still $x$, and the old $Y$-coordinate is

$$
y=t-x.
$$

So the inverse map is

$$
(\text{old }x,\text{old }y)=(x,t-x).
$$

The transformation formula says

$$
f_{\vec A}(\vec a)
=
f_{\vec B}(\vec b)
\left|
\det\left(\frac{\partial \vec b}{\partial \vec a}\right)
\right|.
$$

Equivalently, I can compute the forward Jacobian. Since $\vec A=(T,X)$ and $\vec B=(X,Y)$,

$$
\frac{\partial \vec A}{\partial \vec B}
=
\begin{pmatrix}
\frac{\partial t}{\partial x} & \frac{\partial t}{\partial y}\\
\frac{\partial x}{\partial x} & \frac{\partial x}{\partial y}
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix},
\qquad
\det=-1.
$$

Thus the absolute determinant is $1$, so the transformation does not add any area-scaling factor.

Since $X$ and $Y$ are independent,

$$
f_{\vec B}(x,y)=f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

Substitute the inverse point $(x,t-x)$:

$$
f_{\vec B}(x,t-x)
=f_X(x)f_Y(t-x).
$$

Therefore, the joint PDF of $T$ and $X$ is

$$
\boxed{
f_{T,X}(t,x)=f_X(x)f_Y(t-x).
}
$$

Finally, marginalize over $X$ to get the PDF of $T$:

$$
\begin{aligned}
f_T(t)
&=\int_{-\infty}^{\infty} f_{T,X}(t,x)\,dx\\
&=\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx.
\end{aligned}
$$

Thus

$$
\boxed{
f_T(t)=\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx.
}
$$

This is the convolution formula for the PDF of a sum of independent continuous random variables.

### What I initially missed / corrected

- The main idea was right: keep one old variable, solve for the other old variable, use independence, then integrate out the kept variable.
- The sketch uses both constraints from the new-coordinate point $(T,X)=(10,10)$:
  the diagonal line is $T=10$, i.e. $x+y=10$, and the vertical line is $X=10$.
  Their intersection maps back to the old point $(X,Y)=(10,0)$.
- The gotcha is to keep the old point and the new point separate. If the old point were $(X,Y)=(10,10)$, then the new point would be $(T,X)=(20,10)$, not $(10,10)$.
- The move is not "replace $X$ by $Y$." The move is: keep $X=x$ and recover the old $Y$ from $T=t$, giving $Y=t-x$.
- I originally wrote the new vector as $\vec A=(X,T)$. That is valid, but then the joint density is naturally $f_{X,T}(x,t)$. Since the problem asks for the joint PDF of $T$ and $X$, I rewrote the final version as $\vec A=(T,X)$ and $f_{T,X}(t,x)$.
- The book uses $(T,W)$ with $W=X$. That is the same idea, but the extra name $W$ avoids using $X$ as both an old variable and a new coordinate.
- The marginal PDF of $T$ is $f_T(t)$, not a two-variable density. The variable $x$ is integrated out.
- "Summing over all possible $x$" is conceptually right, but since $X$ is continuous, the precise operation is integrating over $x$.
- If $X$ or $Y$ has restricted support, the same integral over $(-\infty,\infty)$ still works because the PDFs are $0$ outside their supports.

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

The book uses the same transformation:

$$
t=x+y,
\qquad
w=x.
$$

For the random variables, this means

$$
T=X+Y,
\qquad
W=X.
$$

The forward Jacobian is

$$
\frac{\partial(t,w)}{\partial(x,y)}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix},
$$

whose absolute determinant is $1$. Therefore no extra scale factor appears when changing variables.

Using the inverse transformation

$$
x=w,
\qquad
y=t-w,
$$

the joint PDF of $(T,W)$ is

$$
f_{T,W}(t,w)
=f_X(w)f_Y(t-w).
$$

Then the marginal PDF of $T$ is found by integrating out $W$:

$$
\begin{aligned}
f_T(t)
&=\int_{-\infty}^{\infty} f_{T,W}(t,w)\,dw\\
&=\int_{-\infty}^{\infty} f_X(w)f_Y(t-w)\,dw.
\end{aligned}
$$

Renaming the dummy integration variable from $w$ to $x$ gives

$$
f_T(t)
=\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx.
$$

So the handwritten solution and the book solution agree. The book's notation is cleaner because it names the carried-along copy of $X$ as $W$, which makes the transformation from old variables $(X,Y)$ to new variables $(T,W)$ explicit.

### Intuition

Take a tiny rectangle around a point $(t,x)$ in the new coordinates $(T,X)$. This means

$$
T\approx t,
\qquad
X\approx x.
$$

Geometrically, we are looking at all outcomes where $T$ is very close to $t$ and $X$ is very close to $x$.

Now translate that tiny rectangle back into the old $(X,Y)$-coordinates. Since

$$
T=X+Y,
$$

knowing $T=t$ and $X=x$ forces

$$
Y=t-x.
$$

So the new point

$$
(T,X)=(t,x)
$$

comes from the old point

$$
(X,Y)=(x,t-x).
$$

That is the conceptual bridge: probability mass near $(T,X)=(t,x)$ comes from probability mass near $(X,Y)=(x,t-x)$.

Because $X$ and $Y$ are independent, the old joint density is

$$
f_{X,Y}(x,y)=f_X(x)f_Y(y).
$$

So at the recovered old point $(x,t-x)$, the density is

$$
f_X(x)f_Y(t-x).
$$

The Jacobian checks whether the transformation stretches or shrinks tiny areas. Here the absolute determinant is $1$, so tiny areas in $(T,X)$-space correspond to same-size tiny areas in $(X,Y)$-space. No extra scaling factor is needed.

Therefore

$$
f_{T,X}(t,x)=f_X(x)f_Y(t-x).
$$

Finally, to get only the density of $T$, forget the value of $X$ by integrating over every possible $x$:

$$
f_T(t)=\int_{-\infty}^{\infty} f_X(x)f_Y(t-x)\,dx.
$$

This is why convolution looks like "sliding" one density against the other.

### Memory card (quick review)

- To find the PDF of $T=X+Y$, keep one old variable as a second coordinate.
- Use $W=X$, so the new variables are $(T,W)$.
- The inverse transformation is $x=w,\ y=t-w$.
- The Jacobian absolute determinant is $1$.
- Therefore $f_{T,W}(t,w)=f_X(w)f_Y(t-w)$.
- Integrating out $w$ gives the convolution formula.

$$
f_T(t)=\int_{-\infty}^{\infty} f_X(w)f_Y(t-w)\,dw.
$$

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

### Part (a)

Intuitively, $R$ and $\theta$ should be independent because the joint PDF only depends on the distance from the origin. If I fix a radius $r$, then every point on the circle with that radius has the same density. So after knowing the distance from the origin, no angle is favored over another angle.

Let

$$
d=\sqrt{x^2+y^2}
$$

be the distance from the origin. Since the joint density is

$$
f_{X,Y}(x,y)=g(x^2+y^2),
$$

the density depends only on $d^2$, not on the angle.

Now use polar coordinates:

$$
X=R\cos\theta,
\qquad
Y=R\sin\theta.
$$

So the transformation is from the new system $(R,\theta)$ to the old system $(X,Y)$:

$$
(r,\theta)\mapsto (x,y)=(r\cos\theta,r\sin\theta).
$$

The change-of-variables formula I am using is:

$$
f_{R,\theta}(r,\theta)
=f_{X,Y}(x(r,\theta),y(r,\theta))
\left|\det\left(\frac{\partial(x,y)}{\partial(r,\theta)}\right)\right|.
$$

In words: evaluate the old joint PDF at the old point that corresponds to the new point, then multiply by the absolute value of the Jacobian determinant.

First evaluate the old joint density at the transformed point:

$$
\begin{aligned}
f_{X,Y}(r\cos\theta,r\sin\theta)
&=g\left((r\cos\theta)^2+(r\sin\theta)^2\right)\\
&=g\left(r^2\cos^2\theta+r^2\sin^2\theta\right)\\
&=g(r^2).
\end{aligned}
$$

Now compute the Jacobian:

$$
\frac{\partial(x,y)}{\partial(r,\theta)}
=
\begin{pmatrix}
\cos\theta & -r\sin\theta\\
\sin\theta & r\cos\theta
\end{pmatrix}.
$$

The determinant is

$$
\begin{aligned}
\det\left(\frac{\partial(x,y)}{\partial(r,\theta)}\right)
&=r\cos^2\theta+r\sin^2\theta\\
&=r.
\end{aligned}
$$

Therefore,

$$
\left|\det\left(\frac{\partial(x,y)}{\partial(r,\theta)}\right)\right|=r.
$$

So the joint PDF of $(R,\theta)$ is

$$
\boxed{
f_{R,\theta}(r,\theta)=r g(r^2),
\qquad r\ge 0,\ 0\le \theta<2\pi.
}
$$

To see the independence from the joint PDF, find the marginal PDFs. For $\theta$,

$$
f_\theta(\theta)
=\int_0^\infty f_{R,\theta}(r,\theta)\,dr
=\int_0^\infty r g(r^2)\,dr.
$$

This does not depend on $\theta$. Since $\theta$ ranges from $0$ to $2\pi$, this constant must be

$$
f_\theta(\theta)=\frac{1}{2\pi}.
$$

For $R$,

$$
\begin{aligned}
f_R(r)
&=\int_0^{2\pi} f_{R,\theta}(r,\theta)\,d\theta\\
&=\int_0^{2\pi} r g(r^2)\,d\theta\\
&=2\pi r g(r^2).
\end{aligned}
$$

Then

$$
f_R(r)f_\theta(\theta)
=\left(2\pi r g(r^2)\right)\left(\frac{1}{2\pi}\right)
=r g(r^2)
=f_{R,\theta}(r,\theta).
$$

Thus $R$ and $\theta$ are independent.

### What I initially missed / corrected

- The intuition should not say that all distances from the origin are equally likely. The corrected idea is: given a fixed distance from the origin, all angles are equally likely.
- The density is $g(x^2+y^2)$, so after setting $d=\sqrt{x^2+y^2}$, it is better to say the density is $g(d^2)$.
- I originally treated the Jacobian as if the final factor were $1/r$. Since the transformation used here is from $(r,\theta)$ to $(x,y)$, the needed area-scaling factor is

$$
\left|\det\left(\frac{\partial(x,y)}{\partial(r,\theta)}\right)\right|=r.
$$

- If I instead use

$$
\left|\det\left(\frac{\partial(r,\theta)}{\partial(x,y)}\right)\right|=\frac{1}{r},
$$

then I must divide by that inverse Jacobian, which again gives the factor $r$.

### Part (b)

Since a point is chosen uniformly in the unit disc, the density must be constant inside the disc and $0$ outside:

$$
f_{X,Y}(x,y)=
\begin{cases}
c, & x^2+y^2\le 1,\\
0, & \text{otherwise.}
\end{cases}
$$

Total probability must be $1$, so

$$
c\cdot \text{Area(unit disc)}=1.
$$

The area of the unit disc is

$$
\pi r^2=\pi,
$$

so

$$
c=\frac{1}{\pi}.
$$

Therefore,

$$
f_{X,Y}(x,y)=
\begin{cases}
\frac{1}{\pi}, & x^2+y^2\le 1,\\
0, & \text{otherwise.}
\end{cases}
$$

From the last part,

$$
f_{R,\theta}(r,\theta)=r g(r^2).
$$

In this case,

$$
g(r^2)=\frac{1}{\pi}
$$

when the point is inside the unit disc. In polar coordinates,

$$
x^2+y^2\le 1
\quad\Longleftrightarrow\quad
r^2\le 1
\quad\Longleftrightarrow\quad
0\le r\le 1.
$$

So the joint PDF is

$$
\boxed{
f_{R,\theta}(r,\theta)=\frac{r}{\pi},
\qquad 0\le r\le 1,\ 0\le \theta<2\pi.
}
$$

It is $0$ outside this range.

### Part (c)

Since $X$ and $Y$ are i.i.d. $N(0,1)$,

$$
f_X(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2},
\qquad
f_Y(y)=\frac{1}{\sqrt{2\pi}}e^{-y^2/2},
$$

for

$$
-\infty<x<\infty,
\qquad
-\infty<y<\infty.
$$

Since $X$ and $Y$ are independent,

$$
\begin{aligned}
f_{X,Y}(x,y)
&=f_X(x)f_Y(y)\\
&=\frac{1}{2\pi}e^{-x^2/2}e^{-y^2/2}\\
&=\frac{1}{2\pi}e^{-(x^2+y^2)/2}.
\end{aligned}
$$

So in the notation from the problem,

$$
g(r^2)=\frac{1}{2\pi}e^{-r^2/2}.
$$

From the last part,

$$
f_{R,\theta}(r,\theta)=r g(r^2).
$$

Therefore,

$$
\boxed{
f_{R,\theta}(r,\theta)=\frac{r}{2\pi}e^{-r^2/2},
\qquad 0\le r<\infty,\ 0\le \theta<2\pi.
}
$$

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

The book uses the same polar-coordinate change of variables. Its intuition for part (a) is that the joint density of $(X,Y)$ depends only on distance from the origin, not on angle. So after knowing $R$, there is no extra information about $\theta$.

The book writes the angle variable as $t$. Since the absolute Jacobian is $r$,

$$
f_{R,\theta}(r,t)
=f_{X,Y}(x,y)r
=r g(r^2),
$$

for

$$
r\ge 0,
\qquad
t\in[0,2\pi).
$$

This factors into a function of $r$ times a constant function of $t$, so $R$ and $\theta$ are independent, with

$$
\theta\sim \text{Unif}(0,2\pi).
$$

For part (b), the book uses

$$
f_{X,Y}(x,y)=\frac{1}{\pi}
$$

inside the unit disc. Therefore,

$$
f_{R,\theta}(r,t)=\frac{r}{\pi},
\qquad 0\le r\le 1,\ t\in[0,2\pi),
$$

and the density is $0$ otherwise. The book also identifies the marginal PDFs:

$$
f_R(r)=2r,
\qquad 0\le r\le 1,
$$

and

$$
f_\theta(t)=\frac{1}{2\pi},
\qquad 0\le t<2\pi.
$$

For part (c), the book uses

$$
f_{X,Y}(x,y)=\frac{1}{2\pi}e^{-(x^2+y^2)/2},
$$

so

$$
g(r^2)=\frac{1}{2\pi}e^{-r^2/2}.
$$

Thus,

$$
f_{R,\theta}(r,t)=\frac{1}{2\pi}r e^{-r^2/2},
\qquad r\ge 0,\ t\in[0,2\pi).
$$

This again shows independence, with marginal PDFs

$$
f_R(r)=r e^{-r^2/2},
\qquad r\ge 0,
$$

and

$$
f_\theta(t)=\frac{1}{2\pi},
\qquad 0\le t<2\pi.
$$

The book notes that this distribution of $R$ is called Weibull; equivalently, $R$ has the same distribution as $W^{1/2}$ for $W\sim \text{Expo}(1/2)$.

### Intuition

The main idea is that polar coordinates separate direction from distance.

The original density has the form

$$
f_{X,Y}(x,y)=g(x^2+y^2),
$$

so it only cares about the squared distance from the origin. All points on the same circle have the same density.

The Jacobian adds the area effect. A thin polar rectangle with radius near $r$ covers area proportional to $r$, so the joint density in polar coordinates becomes

$$
f_{R,\theta}(r,\theta)=r g(r^2).
$$

The important feature is that this expression has no real dependence on $\theta$. The angle is uniform, and the radius carries all the radial information.

This also explains why, for a point uniform in the unit disc, $R$ is not uniform on $[0,1]$. Larger radii have larger circles and therefore more area nearby, giving

$$
f_R(r)=2r,
\qquad 0\le r\le 1.
$$

For the standard Normal case, the radius has density

$$
f_R(r)=r e^{-r^2/2},
\qquad r\ge 0.
$$

So $R^2$ has an exponential distribution with rate $1/2$.

### Memory card (quick review)

- If $f_{X,Y}(x,y)=g(x^2+y^2)$, use polar coordinates.
- The polar-coordinate Jacobian contributes the factor $r$.
- Therefore

  $$
  f_{R,\theta}(r,\theta)=r g(r^2),
  \qquad r\ge 0,\ 0\le \theta<2\pi.
  $$

- Since this does not depend on $\theta$, the angle is uniform:

  $$
  f_\theta(\theta)=\frac{1}{2\pi}.
  $$

- Uniform in the unit disc:

  $$
  f_{R,\theta}(r,\theta)=\frac{r}{\pi},
  \qquad 0\le r\le 1,\ 0\le \theta<2\pi.
  $$

- Independent standard Normals:

  $$
  f_{R,\theta}(r,\theta)=\frac{r}{2\pi}e^{-r^2/2},
  \qquad r\ge 0,\ 0\le \theta<2\pi.
  $$

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

### Part (a) — CDF/LOTP derivation

Independent derivation.

Since $X$ and $Y$ are positive, $T=XY$ is also positive. Therefore, for $t\le 0$,

$$
F_T(t)=0.
$$

For $t>0$, use the continuous law of total probability by conditioning on $X$:

$$
\begin{aligned}
F_T(t)
&=\mathbb{P}(T\le t)\\
&=\mathbb{P}(XY\le t)\\
&=\int_0^\infty \mathbb{P}(XY\le t\mid X=x)f_X(x)\,dx.
\end{aligned}
$$

Given $X=x$, with $x>0$, the inequality $XY\le t$ becomes $xY\le t$, or equivalently $Y\le t/x$. Using independence,

$$
\mathbb{P}(XY\le t\mid X=x)
=\mathbb{P}(Y\le t/x)
=F_Y(t/x).
$$

So

$$
F_T(t)
=\int_0^\infty F_Y(t/x)f_X(x)\,dx.
$$

Differentiate with respect to $t$:

$$
\begin{aligned}
f_T(t)
&=\frac{d}{dt}F_T(t)\\
&=\int_0^\infty \frac{d}{dt}F_Y(t/x)f_X(x)\,dx\\
&=\int_0^\infty f_Y(t/x)\frac{1}{x}f_X(x)\,dx,
\qquad t>0.
\end{aligned}
$$

Thus,

$$
\boxed{
f_T(t)
=
\int_0^\infty f_X(x)f_Y(t/x)\frac{1}{x}\,dx,
\qquad t>0.
}
$$

For $t\le 0$, $f_T(t)=0$. Jacobno's proposed integral is missing the factor $1/x$, so the argument is generally not correct. In change-of-variables language, the missing factor is the Jacobian term from $y=t/x$:

$$
\left|\frac{dy}{dt}\right|=\frac{1}{x}.
$$

### Part (b) — Log transform/convolution derivation

Independent derivation.

Since $X$ and $Y$ are positive, taking logs is valid. Let

$$
A=\log T,
\qquad
B=\log X,
\qquad
C=\log Y.
$$

Since $T=XY$,

$$
A=\log T=\log X+\log Y=B+C.
$$

Also, since $X$ and $Y$ are independent, $B$ and $C$ are independent. Therefore, the PDF of $A$ is the convolution

$$
f_A(a)
=
\int_{-\infty}^{\infty} f_C(a-b)f_B(b)\,db.
$$

Now convert the log-transformed densities back to the original variables. Since $a=\log t$, we have $t=e^a$ and

$$
\frac{dt}{da}=e^a=t.
$$

Thus,

$$
f_A(a)=f_T(e^a)e^a,
$$

so at $a=\log t$,

$$
f_A(\log t)=f_T(t)t.
$$

Similarly, if $b=\log x$, then $x=e^b$ and

$$
f_B(b)=f_X(e^b)e^b=f_X(x)x.
$$

Also,

$$
db=d(\log x)=\frac{1}{x}\,dx.
$$

For the remaining term,

$$
a-b=\log t-\log x=\log(t/x),
$$

so

$$
\begin{aligned}
f_C(a-b)
&=f_C(\log(t/x))\\
&=f_Y(t/x)\frac{t}{x}.
\end{aligned}
$$

Substitute these into the convolution formula:

$$
\begin{aligned}
f_T(t)t
&=
\int_0^\infty
f_Y(t/x)\frac{t}{x}
f_X(x)x
\frac{1}{x}\,dx\\
&=
\int_0^\infty
f_Y(t/x)f_X(x)\frac{t}{x}\,dx.
\end{aligned}
$$

Cancel $t$ from both sides:

$$
\boxed{
f_T(t)
=
\int_0^\infty f_X(x)f_Y(t/x)\frac{1}{x}\,dx,
\qquad t>0.
}
$$

This agrees with part (a). The log-convolution route also shows why Jacobno's argument needs the Jacobian factor $1/x$.

### Book's solution (for comparison)

Source status: verified. The user provided the book excerpt for this problem.

The book's solution agrees with both derivations above. For part (a), it conditions on $X$ and uses the continuous law of total probability:

$$
\mathbb{P}(T\le t)
=
\int_0^\infty
\mathbb{P}(XY\le t\mid X=x)f_X(x)\,dx.
$$

Since $x>0$, the event $XY\le t$ becomes $Y\le t/x$ after conditioning on $X=x$. Using independence, this gives

$$
\mathbb{P}(T\le t)
=
\int_0^\infty F_Y(t/x)f_X(x)\,dx.
$$

Differentiating with respect to $t$ gives

$$
f_T(t)
=
\int_0^\infty f_X(x)f_Y(t/x)\frac{dx}{x},
\qquad t>0.
$$

The book emphasizes that this is not Jacobno's formula: there is an extra $x$ in the denominator. Conceptually, Jacobno is treating point densities as if they were probabilities and is ignoring the Jacobian term.

For part (b), the book uses different letters:

$$
Z=\log T,
\qquad
W=\log X,
\qquad
V=\log Y.
$$

Then

$$
Z=W+V,
$$

so

$$
f_Z(z)
=
\int_{-\infty}^{\infty} f_W(w)f_V(z-w)\,dw.
$$

The log-transform densities are

$$
f_W(w)=f_X(e^w)e^w,
\qquad
f_V(v)=f_Y(e^v)e^v.
$$

Therefore,

$$
\begin{aligned}
f_Z(z)
&=
\int_{-\infty}^{\infty}
f_X(e^w)e^w
f_Y(e^{z-w})e^{z-w}\,dw\\
&=
e^z
\int_{-\infty}^{\infty}
f_X(e^w)f_Y(e^{z-w})\,dw.
\end{aligned}
$$

Transforming back from $Z=\log T$ gives

$$
f_T(t)
=
f_Z(\log t)\frac{1}{t}.
$$

Using $x=e^w$, so $dw=dx/x$, this becomes

$$
f_T(t)
=
\int_0^\infty f_X(x)f_Y(t/x)\frac{dx}{x},
\qquad t>0.
$$

This matches part (a), and again shows that Jacobno is missing the denominator factor $x$.

### Intuition

The product case looks similar to convolution, but the geometry is different.

For a sum,

$$
T=X+Y,
$$

fixing $X=x$ forces

$$
Y=t-x.
$$

As $t$ changes by a small amount, $t-x$ changes by the same small amount, so no extra scale factor appears.

For a product,

$$
T=XY,
$$

fixing $X=x$ forces

$$
Y=t/x.
$$

Now a small change in $t$ produces a smaller or larger change in the required value of $Y$ depending on $x$:

$$
\frac{d}{dt}(t/x)=\frac{1}{x}.
$$

That derivative is the Jacobian factor. It converts density in the $Y$-coordinate into density in the $T$-coordinate after conditioning on $X=x$.

This is the issue in Jacobno's argument. The expression

$$
f_X(x)f_Y(t/x)
$$

identifies the two density factors at the relevant point, but it does not account for how much $Y$ changes when $T$ changes. The missing scale factor is

$$
\frac{1}{x}.
$$

The log method gives the same intuition another way: products become sums after taking logs, but both the log transform and the transform back to $T$ carry Jacobian factors. After simplifying, the same denominator $x$ remains.

### Memory card (quick review)

- For independent positive $X,Y$ and $T=XY$, the support is positive.
- For $t>0$,

  $$
  F_T(t)
  =
  \int_0^\infty F_Y(t/x)f_X(x)\,dx.
  $$

- Differentiating gives

  $$
  f_T(t)
  =
  \int_0^\infty f_X(x)f_Y(t/x)\frac{dx}{x}.
  $$

- Jacobno's formula is missing the Jacobian factor:

  $$
  \left|\frac{d}{dt}(t/x)\right|=\frac{1}{x}.
  $$

- Log method: let $Z=\log T$, $W=\log X$, and $V=\log Y$. Then $Z=W+V$, so use convolution in log-space.
- Transform back with $f_T(t)=f_Z(\log t)/t$ and substitute $x=e^w$ to recover the same formula.

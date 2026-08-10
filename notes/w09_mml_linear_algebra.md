# Week 9 — MML Linear Algebra

## 2.2 Matrices

A matrix $A \in \mathbb{R}^{m \times n}$ has $m$ rows and $n$
columns. Matrices compactly represent systems of equations and, as we
will see later, linear mappings.

### Addition and Multiplication

Matrix addition requires equal shapes:

$$
A,B\in\mathbb{R}^{m\times n}
\quad\Longrightarrow\quad
A+B\in\mathbb{R}^{m\times n}.
$$

For

$$
A\in\mathbb{R}^{m\times n},
\qquad
B\in\mathbb{R}^{n\times q},
$$

the product is defined and $AB\in\mathbb{R}^{m\times q}$. Each entry is
the dot product of a row of $A$ with a column of $B$.

Matrix multiplication is associative and distributive, but generally not
commutative:

$$
(AB)C=A(BC), \qquad (A+B)C=AC+BC,
\qquad AB\neq BA.
$$

### Identity, Inverse, and Transpose

For $A\in\mathbb{R}^{m\times n}$,

$$
I_mA=A,
\qquad
AI_n=A.
$$

A square matrix $A$ is invertible when there is a unique matrix
$A^{-1}$ such that

$$
AA^{-1}=A^{-1}A=I.
$$

Not every square matrix is invertible.

The transpose exchanges rows and columns:

$$
A\in\mathbb{R}^{m\times n}
\quad\Longrightarrow\quad
A^\top\in\mathbb{R}^{n\times m}.
$$

Transposition and inversion reverse product order:

$$
(AB)^\top=B^\top A^\top,
\qquad
(AB)^{-1}=B^{-1}A^{-1}
$$

when the inverses exist.

### Matrix Form of a Linear System

A system of equations can be written compactly as

$$
Ax=b.
$$

The entries of $x$ are the unknown coefficients, and $Ax$ is the
linear combination of the columns of $A$ using those coefficients.
Equivalently, $A$ maps the vector $x$ to $b$.

## 2.3 Solving Systems of Linear Equations

### Particular and General Solutions

A particular solution $x_p$ is one vector satisfying

$$
Ax_p=b.
$$

Every general solution can be written as

$$
x=x_p+x_h,
$$

where $x_h$ is any solution of the homogeneous system $Ax_h=0$.

### Gaussian Elimination

The augmented matrix $[A\mid b]$ records the coefficients and
right-hand side together. The following row operations preserve its
solution set:

- Exchange two rows.
- Multiply a row by a nonzero scalar.
- Add a multiple of one row to another row.

In row-echelon form, zero rows are at the bottom and each pivot lies
strictly to the right of the pivot above it. Pivot columns correspond to
basic variables; non-pivot columns correspond to free variables.

Reduced row-echelon form additionally requires:

1. Every pivot equals one.
2. Each pivot is the only nonzero entry in its column.

A consistent system with free variables can have infinitely many
solutions. A row of the form

$$
[0\ \cdots\ 0\mid c], \qquad c\neq0,
$$

shows that the system is inconsistent and has no exact solution.

### Minus-1 Trick and Matrix Inverses

For a homogeneous system in RREF, the minus-1 trick provides a compact
way to read solution directions associated with free variables. We will
practice the construction later rather than memorize it from reading.

An inverse can be calculated by reducing

$$
[A\mid I]\longrightarrow[I\mid A^{-1}].
$$

This works only when $A$ is square and invertible.

### Large and Approximate Systems

Using $x=A^{-1}b$ is not a general solution strategy because $A$ may
be nonsquare, singular, or too large for explicitly computing an inverse.

An inconsistent system may instead require an approximate least-squares
solution. For very large solvable systems, iterative methods can avoid
the cost of direct Gaussian elimination.

## 2.4 Vector Spaces

### Groups and Vector-Space Axioms

A group is a set together with an operation that satisfies closure,
associativity, the existence of a neutral element, and the existence of an
inverse for every element. An Abelian group additionally requires the
operation to be commutative.

For a real vector space $V$, vector addition must make $V$ an Abelian
group. This provides the zero vector, additive inverses, associativity, and
commutativity.

Scalar multiplication maps a real scalar and a vector back into the vector
space. It must satisfy

$$
\lambda(\psi x)=(\lambda\psi)x,
\qquad
1x=x.
$$

Scalar multiplication and vector addition must also satisfy both
distributive laws:

$$
\lambda(x+y)=\lambda x+\lambda y,
$$

and

$$
(\lambda+\psi)x=\lambda x+\psi x.
$$

Closure guarantees that adding vectors or scaling a vector does not leave
the vector space. Ordinary vector-vector multiplication is not one of the
operations required by the vector-space definition.

### Products Between Column Vectors

If $a,b\in\mathbb{R}^{n\times1}$ are column vectors, the product $ab$ is
not defined under standard matrix multiplication because the neighboring
dimensions do not match.

The inner product is

$$
a^\top b:
\qquad
(1\times n)(n\times1)
\longrightarrow
1\times1.
$$

It produces a scalar. The outer product is

$$
ab^\top:
\qquad
(n\times1)(1\times n)
\longrightarrow
n\times n.
$$

It produces a matrix.

### Vector Subspaces

A subset $U$ of a vector space $V$ is a vector subspace when it contains
the zero vector and is closed under addition and scalar multiplication:

$$
0\in U,
\qquad
x+y\in U,
\qquad
\lambda x\in U
$$

for all $x,y\in U$ and all real scalars $\lambda$. The remaining
vector-space properties are inherited from $V$.

The solution set of a homogeneous system is a subspace. If $Ax=0$ and
$Ay=0$, then

$$
A(x+y)=Ax+Ay=0
$$

and

$$
A(\lambda x)=\lambda Ax=0.
$$

The zero vector is also a solution. Intuitively, this subspace contains all
directions that $A$ sends to zero; it will later be called the kernel or
null space.

By contrast, the solution set of $Ax=b$ with $b\neq0$ is generally not a
subspace because it does not contain the zero vector. When nonempty, it is
a shifted or affine set.

## 2.5 Linear Independence

### Linear Combinations

Given vectors $x_1,\ldots,x_k\in V$, a linear combination is any vector
of the form

$$
\lambda_1x_1+\lambda_2x_2+\cdots+\lambda_kx_k,
$$

where the coefficients are real scalars. The zero vector always has the
trivial representation

$$
0x_1+\cdots+0x_k=0.
$$

### Independence and Redundancy

The vectors are linearly independent when the equation

$$
\lambda_1x_1+\cdots+\lambda_kx_k=0
$$

has only the trivial solution. They are linearly dependent when there is
a solution in which at least one coefficient is nonzero.

Dependence concerns redundancy among whole vectors, not among their
individual components. If one coefficient is nonzero, the equation can
be rearranged to express the corresponding vector as a linear combination
of the others.

### Testing Independence with Row Reduction

Place the vectors into a matrix as columns:

$$
A=[x_1\ \cdots\ x_k].
$$

Then

$$
A\lambda
=
\lambda_1x_1+\cdots+\lambda_kx_k.
$$

Testing linear independence is therefore equivalent to solving the
homogeneous system

$$
A\lambda=0.
$$

If every column is a pivot column, there are no free coefficients and the
only solution is the trivial one. The original vectors are then linearly
independent.

A non-pivot column indicates redundancy. Its position identifies an
original vector that can be expressed as a linear combination of the
original vectors associated with pivot columns.

### Number of Available Directions

If $x_1,\ldots,x_m$ are all linear combinations of only $k$ linearly
independent vectors, they must be linearly dependent whenever $m>k$.
There are more vectors than available independent directions.

For a matrix with $r$ rows and $c$ columns, the columns live in
$\mathbb{R}^r$. Therefore, if $c>r$, the columns must be linearly
dependent because row reduction can produce at most $r$ pivots.

The converse is not true. Having no more vectors than available dimensions
does not guarantee independence. Two identical columns, for example, are
dependent even when the matrix has enough rows.

## 2.6 Basis and Rank

### Span, Basis, and Coordinates

The span of a set of vectors contains every linear combination that can be
constructed from those vectors. A generating set for a vector space spans
the entire space.

A basis is a linearly independent generating set. These two properties play
different roles:

- Spanning guarantees that every vector has a representation.
- Linear independence guarantees that the representation is unique.

If a vector had two representations in the same basis,

$$
x=\alpha_1b_1+\cdots+\alpha_nb_n
$$

and

$$
x=\beta_1b_1+\cdots+\beta_nb_n,
$$

then subtracting the two equations would give

$$
0=(\alpha_1-\beta_1)b_1+\cdots+(\alpha_n-\beta_n)b_n.
$$

Linear independence forces every coefficient difference to be zero.

Every basis of a finite-dimensional vector space contains the same number
of vectors. This number is the dimension of the space. Dimension measures
the number of independent directions, not the number of components written
inside one vector.

### Rank and Pivot Columns

The rank of a matrix is the number of linearly independent columns. It is
also equal to the number of linearly independent rows and to the number of
pivots:

$$
\operatorname{rank}(A)
=
\dim(\operatorname{Col}(A)).
$$

If row reduction identifies pivot columns 1, 2, and 4, then the corresponding
columns of the original matrix form a basis for its column space. The rank
and the dimension of that column space are both three.

The pivot positions come from the row-reduced matrix, but the basis vectors
must be selected from the original matrix. Row operations preserve dependency
relationships and rank, but they transform the actual columns and may change
the column space.

A rank-three matrix has a three-dimensional column space. That space equals
all of $\mathbb{R}^3$ only when its columns live in $\mathbb{R}^3$; in a
larger ambient space it is a three-dimensional subspace.

## 2.7 Linear Mappings

### Preserving Vector-Space Structure

A mapping $\Phi:V\to W$ is linear when it preserves vector addition and
scalar multiplication:

$$
\Phi(\lambda x+\psi y)
=
\lambda\Phi(x)+\psi\Phi(y).
$$

Every linear mapping preserves the origin. For example,

$$
\Phi(0)=\Phi(0+0)=\Phi(0)+\Phi(0)
$$

implies that $\Phi(0)=0$. Consequently, a mapping of the form

$$
T(x)=Ax+c,
\qquad
c\neq0,
$$

is affine rather than linear because $T(0)=c$. A neural-network layer with
a bias is therefore mathematically affine even though software libraries
often call it a linear layer.

### Coordinates Relative to a Basis

Let an ordered basis be collected into a basis matrix:

$$
B=[b_1\ \cdots\ b_n].
$$

If $[x]_B$ is the coordinate vector of $x$ relative to this basis, then

$$
x_{\mathrm{standard}}=B[x]_B.
$$

The matrix $B$ converts basis coordinates into standard coordinates by
forming the corresponding linear combination of the basis vectors. Its
inverse performs the reverse conversion:

$$
[x]_B=B^{-1}x_{\mathrm{standard}}.
$$

The geometric vector does not change during a coordinate conversion; only
its numerical representation changes.

### Matrices of Linear Mappings

Suppose $L$ is the standard-coordinate matrix of a linear mapping $\Phi$.
If the input is described relative to $B$, then

$$
[\Phi(x)]_{\mathrm{standard}}
=
LB[x]_B.
$$

The product

$$
A_\Phi=LB
$$

is the matrix of $\Phi$ for inputs expressed in basis $B$ and outputs
expressed in the standard basis. Its columns are

$$
A_\Phi
=
[\Phi(b_1)\ \cdots\ \Phi(b_n)].
$$

This works because linearity gives

$$
\Phi(\alpha_1b_1+\cdots+\alpha_nb_n)
=
\alpha_1\Phi(b_1)+\cdots+\alpha_n\Phi(b_n).
$$

If the output should instead be expressed relative to another basis $C$,
then

$$
[\Phi(x)]_C
=
C^{-1}LB[x]_B.
$$

Reading from right to left, $B$ converts the input to standard coordinates,
$L$ applies the mapping, and $C^{-1}$ converts the result to output-basis
coordinates. Matrix multiplication therefore represents composition of
compatible linear mappings. A coordinate change describes the same vector,
whereas $\Phi$ generally changes the vector itself.

### Image, Kernel, and Rank-Nullity

For a linear mapping $\Phi:V\to W$, the image is the set of reachable
outputs:

$$
\operatorname{Im}(\Phi)
=
\{\Phi(x):x\in V\}.
$$

For a matrix mapping $x\mapsto Ax$, the image is the column space of $A$,
and its dimension is the rank.

The kernel is the set of inputs that are collapsed to zero:

$$
\ker(\Phi)
=
\{x\in V:\Phi(x)=0\}.
$$

The rank-nullity theorem divides the dimensions of the domain into
directions that remain independent in the output and directions that are
sent to zero:

$$
\dim(\ker(\Phi))
+
\dim(\operatorname{Im}(\Phi))
=
\dim(V).
$$

The domain and codomain must not be confused. For a rank-two mapping from
$\mathbb{R}^4$ to $\mathbb{R}^3$, the image is a two-dimensional plane in
the codomain, while the kernel is a two-dimensional subspace of the domain.
The remaining codomain direction is unreachable; it does not belong to the
kernel.

A linear mapping is injective exactly when its kernel contains only zero.
It is surjective exactly when its image equals the entire codomain. Thus, the
rank-two mapping from $\mathbb{R}^4$ to $\mathbb{R}^3$ is neither injective
nor surjective.

## 3.1 Norms

A norm assigns a nonnegative length to each vector. It is absolutely
homogeneous, satisfies the triangle inequality, and is zero only for the
zero vector:

$$
\|\lambda x\|=|\lambda|\|x\|,
$$

$$
\|x+y\|\leq\|x\|+\|y\|,
$$

and

$$
\|x\|\geq0,
\qquad
\|x\|=0\Longleftrightarrow x=0.
$$

The Euclidean norm and Manhattan norm are

$$
\|x\|_2
=
\sqrt{\sum_i x_i^2}
$$

and

$$
\|x\|_1
=
\sum_i |x_i|,
$$

respectively. The Euclidean norm is induced by the dot product, whereas the
Manhattan norm is not induced by an inner product.

## 3.2 Inner Products

An inner product maps two vectors to a scalar and provides information about
their alignment. For the standard dot product,

$$
\langle x,y\rangle
=
x^\top y
=
\sum_i x_i y_i.
$$

It is related to lengths and angles by

$$
x^\top y
=
\|x\|\|y\|\cos\theta.
$$

The dot product is positive for vectors pointing generally in the same
direction, zero for orthogonal vectors, and negative for vectors pointing
generally in opposite directions.

The scalar projection of $x$ onto the direction of a nonzero vector $y$ is

$$
\frac{x^\top y}{\|y\|},
$$

whereas the complete projected vector is

$$
\frac{x^\top y}{\|y\|^2}y.
$$

## 3.3 Lengths and Distances

An inner product induces a norm:

$$
\|x\|
=
\sqrt{\langle x,x\rangle}.
$$

The corresponding distance between two vectors is the norm of their
difference:

$$
d(x,y)
=
\|x-y\|
=
\sqrt{\langle x-y,x-y\rangle}.
$$

A norm is sufficient to define distance; not every norm must come from an
inner product.

## 3.4 Angles and Orthogonality

Two vectors are orthogonal when their inner product is zero. They are
orthonormal when they are additionally unit vectors.

If the columns of a square matrix $Q$ form an orthonormal basis, then

$$
Q^\top Q
=
QQ^\top
=
I,
$$

so

$$
Q^{-1}=Q^\top.
$$

Multiplication by an orthogonal matrix preserves inner products and
therefore preserves lengths, distances, and angles.

## 3.5 Orthonormal Bases

An orthonormal basis has no redundant directions, its directions are
mutually orthogonal, and every basis vector has unit length. Coordinates in
an orthonormal basis can be obtained directly with inner products rather
than by solving a general linear system.

If the orthonormal basis vectors are the columns of $B$, then

$$
B^\top B=I.
$$

For a square basis matrix, the coordinates of $x$ are therefore

$$
[x]_B=B^\top x.
$$

## 3.6 Orthogonal Complements

For a subspace $U$ of a finite-dimensional inner-product space $V$, the
orthogonal complement contains all vectors orthogonal to every vector in
$U$:

$$
U^\perp
=
\{r\in V:\langle r,u\rangle=0
\text{ for every }u\in U\}.
$$

Every vector has a unique decomposition

$$
x=u+r,
$$

where

$$
u\in U
$$

and

$$
r\in U^\perp.
$$

Most vectors are neither in $U$ nor in $U^\perp$; they are sums of
components from both subspaces.

## 3.8 Orthogonal Projections

### Projection onto a Line

Let a line be spanned by a nonzero vector $b$. A projection onto that line
must have the form

$$
p=\lambda b.
$$

The residual must be orthogonal to the line:

$$
b^\top(x-\lambda b)=0.
$$

Solving for the coordinate and projected vector gives

$$
\lambda
=
\frac{b^\top x}{b^\top b}
=
\frac{b^\top x}{\|b\|^2}
$$

and

$$
p
=
\frac{b^\top x}{\|b\|^2}b.
$$

When $b$ is a unit vector, these simplify to

$$
\lambda=b^\top x
$$

and

$$
p=(b^\top x)b.
$$

The coordinate $\lambda$ is a scalar, while $p$ is the complete projected
vector in the original ambient space.

### The Closest-Point Interpretation

Let $p$ be the orthogonal projection of $x$ onto $U$, and let

$$
r=x-p.
$$

For any other $u\in U$, both $p$ and $u$ belong to $U$, so $p-u\in U$.
Since $r\in U^\perp$, the vectors $r$ and $p-u$ are orthogonal. Therefore,

$$
x-u
=
r+(p-u),
$$

and the Pythagorean theorem gives

$$
\|x-u\|^2
=
\|r\|^2+\|p-u\|^2
\geq
\|r\|^2
=
\|x-p\|^2.
$$

Equality holds only when $u=p$. Thus, the orthogonal projection is the
unique closest point in $U$ to $x$. The residual $r$ is the reconstruction
error.

### Projection onto a General Subspace

Let the linearly independent columns of $B$ form a basis for $U$. Write the
projection as

$$
p=B\lambda.
$$

Requiring the residual to be orthogonal to every column of $B$ produces the
normal equations:

$$
B^\top(x-B\lambda)=0,
$$

so

$$
B^\top B\lambda=B^\top x.
$$

Since $B$ has linearly independent columns,

$$
\lambda
=
(B^\top B)^{-1}B^\top x.
$$

The projected vector and projection matrix are therefore

$$
p
=
B(B^\top B)^{-1}B^\top x
$$

and

$$
P
=
B(B^\top B)^{-1}B^\top.
$$

If the columns of $B$ are orthonormal, then

$$
P=BB^\top.
$$

An orthogonal projection matrix is symmetric and idempotent:

$$
P^\top=P,
\qquad
P^2=P.
$$

Idempotence means that projecting an already projected vector changes
nothing. If $x\in U$, then $Px=x$; the matrix acts as the identity on $U$,
but it is not the identity on the entire ambient space unless $U=V$. If
$x\in U^\perp$, then $Px=0$.

### Connection to PCA

PCA finds orthonormal directions using the variation of an entire centered
dataset. The leading principal components are the directions along which
the projected data have the greatest variance.

Keeping the first $k$ principal components projects every observation onto
the same $k$-dimensional subspace. This is not a per-observation selection
of whichever projections happen to have the greatest length. Equivalently,
the PCA subspace minimizes the total squared reconstruction error over the
dataset.

## Main Takeaways

- Matrix dimensions determine which operations are valid.
- Matrix multiplication combines rows with columns and is order-sensitive.
- Matrix form represents both a system of equations and a column combination.
- The general solution is a particular solution plus homogeneous solutions.
- REF exposes pivots and free variables; RREF makes them easier to read.
- Approximation and computational scale are different reasons for using
  methods beyond direct elimination.
- A vector space combines an Abelian addition operation with compatible
  scalar multiplication.
- A subspace must contain zero and remain closed under addition and scaling.
- Linear independence means that the zero vector has only the trivial
  coefficient representation.
- Pivot positions identify independent original columns; non-pivot positions
  identify redundancy.
- More vectors than available directions guarantees dependence, but having
  fewer vectors does not guarantee independence.
- A basis spans the space without redundant vectors, which makes every
  coordinate representation exist and be unique.
- Rank is the dimension of the column space and can be found from pivot
  positions, but column-space bases use the original matrix columns.
- Basis matrices change coordinate descriptions; transformation matrices
  apply linear mappings.
- Matrix products compose coordinate conversions and linear mappings from
  right to left.
- Rank-nullity uses the dimension of the domain, while the image lives in
  the codomain.
- Inner products induce Euclidean geometry by defining lengths, distances,
  angles, and orthogonality.
- Orthonormal bases simplify coordinates, inverses, and projection formulas.
- Every vector decomposes uniquely into a subspace component and an
  orthogonal residual.
- An orthogonal projection is the unique closest point in a subspace.
- PCA chooses a shared low-dimensional subspace that preserves dataset-wide
  variation and minimizes reconstruction error.

## Questions to Revisit

- Apply the minus-1 trick to a concrete homogeneous system.
- Develop intuition for pseudoinverses and least squares later in the curriculum.
- Compare direct and iterative numerical methods when they become relevant.
- Practice subspace, basis, rank, and linear-mapping concepts with the selected
  Week 9 exercises.
- Revisit the full symbolic basis-change derivation only if later
  eigendecomposition or PCA work requires it.
- Derive the projection formulas again during the selected geometry exercise
  instead of memorizing them without the orthogonality argument.

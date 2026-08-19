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

## 4.2 Eigenvalues and Eigenvectors

### Invariant Directions

For a square matrix $A$, a nonzero vector $v$ is an eigenvector with
eigenvalue $\lambda$ when

$$
Av=\lambda v.
$$

The line spanned by $v$ is an invariant direction: applying $A$ keeps the
result on that same line. The eigenvalue describes the action along the
line. Its absolute value gives the scaling factor, while its sign determines
whether the orientation is preserved or reversed.

- A value greater than one stretches the vector.
- A value between zero and one shrinks the vector.
- A negative value reverses orientation as well as scaling by its absolute
  value.
- A zero value collapses the eigenvector to the origin.

If zero is an eigenvalue, then there is a nonzero vector $v$ such that

$$
Av=0.
$$

The kernel is therefore nontrivial, so a square matrix with eigenvalue zero
is singular.

Eigenvectors are not unique. If $v$ is an eigenvector, then every nonzero
multiple of it is also an eigenvector with the same eigenvalue:

$$
A(cv)=cAv=c\lambda v=\lambda(cv).
$$

### Eigenspaces

The eigenspace associated with $\lambda$ is

$$
E_\lambda
=
\ker(A-\lambda I).
$$

It contains every vector whose direction is scaled by $\lambda$, together
with the zero vector. The zero vector belongs because an eigenspace is a
subspace, although zero itself is not called an eigenvector.

If eigenvectors $p_1$ and $p_2$ satisfy

$$
Ap_1=\lambda_1p_1
$$

and

$$
Ap_2=\lambda_2p_2,
$$

then linearity gives

$$
A(\alpha p_1+\beta p_2)
=
\alpha\lambda_1p_1+\beta\lambda_2p_2.
$$

Thus, when a vector is expressed using eigenvector directions, the
transformation acts independently on each component.

## 4.4 Eigendecomposition and Diagonalization

### Diagonalization in an Eigenvector Basis

Collect eigenvectors into the columns of $P$ and their corresponding
eigenvalues along the diagonal of $D$:

$$
P=[p_1\ \cdots\ p_n].
$$

Then

$$
AP
=
[Ap_1\ \cdots\ Ap_n]
$$

and

$$
PD
=
[\lambda_1p_1\ \cdots\ \lambda_np_n].
$$

The eigenvalue equations therefore imply

$$
AP=PD.
$$

If the eigenvectors are linearly independent, they form a basis and $P$ is
invertible. Multiplying on the appropriate side gives

$$
D=P^{-1}AP
$$

and

$$
A=PDP^{-1}.
$$

Reading the second expression from right to left, $P^{-1}$ converts standard
coordinates into eigenbasis coordinates, $D$ independently scales those
coordinates by the eigenvalues, and $P$ converts the result back to standard
coordinates. Diagonalization therefore describes the same linear mapping in
a basis where its action is only independent scaling along coordinate axes.

### When Diagonalization Exists

A square matrix is diagonalizable exactly when it has enough linearly
independent eigenvectors to form a basis. Distinct eigenvalues guarantee
linearly independent eigenvectors, but distinct eigenvalues are not
necessary. For example, the identity matrix has one repeated eigenvalue and
still has a full basis of eigenvectors.

A matrix that does not have enough independent eigenvectors is defective
and cannot be diagonalized in this form.

Every real symmetric matrix has an orthonormal basis of eigenvectors. In
that case, $P$ is orthogonal, so

$$
P^{-1}=P^\top,
$$

and the decomposition simplifies to

$$
A=PDP^\top.
$$

### Matrix Powers

Diagonalization makes repeated application of a transformation easier. The
neighboring inverse factors cancel:

$$
A^k
=
(PDP^{-1})^k
=
PD^kP^{-1}.
$$

Since $D$ is diagonal, computing $D^k$ only requires raising each eigenvalue
to the power $k$. Geometrically, repeated applications of $A$ repeatedly
scale each eigenvector component by its eigenvalue.

## 4.5 Singular Value Decomposition

### Full SVD and Its Geometry

Every matrix $A\in\mathbb{R}^{m\times n}$ has a singular value
decomposition

$$
A=U\Sigma V^\top,
$$

where

$$
U\in\mathbb{R}^{m\times m},
\qquad
\Sigma\in\mathbb{R}^{m\times n},
\qquad
V\in\mathbb{R}^{n\times n}.
$$

The matrices $U$ and $V$ are orthogonal. Their columns are the left- and
right-singular vectors, respectively. The rectangular matrix $\Sigma$ has
nonnegative singular values on its diagonal and zeros elsewhere.

Applied to a vector $x\in\mathbb{R}^n$, the factors act from right to left:

$$
x
\longmapsto
V^\top x
\longmapsto
\Sigma V^\top x
\longmapsto
U\Sigma V^\top x.
$$

First, $V^\top$ expresses the input in the orthonormal basis of
right-singular vectors. Next, $\Sigma$ scales those coordinates by the
singular values and maps from $\mathbb{R}^n$ to $\mathbb{R}^m$, adding or
removing dimensions when necessary. Finally, $U$ expresses the result in
the standard basis of the codomain.

Unlike eigendecomposition, SVD can describe rectangular transformations
between different vector spaces. It exists for every matrix, including
rank-deficient matrices.

### Singular Vectors and Eigenvectors

For corresponding right- and left-singular vectors,

$$
Av_i=\sigma_i u_i.
$$

Thus, $A$ maps the input direction $v_i$ to the output direction $u_i$ and
scales it by $\sigma_i$. Transposing the SVD also gives

$$
A^\top u_i=\sigma_i v_i.
$$

Combining these equations yields

$$
A^\top A v_i=\sigma_i^2v_i
$$

and

$$
AA^\top u_i=\sigma_i^2u_i.
$$

Therefore, the right-singular vectors are eigenvectors of $A^\top A$, the
left-singular vectors are eigenvectors of $AA^\top$, and their corresponding
nonzero eigenvalues are the squared singular values.

For every $x$,

$$
x^\top A^\top Ax
=
\lVert Ax\rVert^2
\geq 0.
$$

Hence, $A^\top A$ is positive semidefinite. Its eigenvalues are
nonnegative, and the singular values are defined by

$$
\sigma_i=\sqrt{\lambda_i}\geq 0.
$$

### Rank, Kernel, and Stretching

The rank of $A$ equals the number of nonzero singular values. If
$\operatorname{rank}(A)=r$, then

$$
\sigma_1\geq\sigma_2\geq\cdots\geq\sigma_r>0,
$$

with all remaining singular values equal to zero. When $\sigma_i=0$,

$$
Av_i=0,
$$

so $v_i$ belongs to the kernel. The right-singular vectors associated with
zero singular values span the kernel, whose dimension is $n-r$.

The first right-singular vector $v_1$ identifies a direction of maximum
stretching, and the largest singular value is the spectral norm:

$$
\lVert A\rVert_2=\sigma_1.
$$

Larger singular values indicate directions along which the matrix acts more
strongly. This is a statement about the magnitude of the transformation;
semantic importance depends on what the matrix represents.

## 4.6 Matrix Approximation

### Rank-One Components and Truncated SVD

The SVD can be written as a sum of rank-one outer products:

$$
A
=
\sum_{i=1}^{r}\sigma_i u_i v_i^\top.
$$

Each matrix $u_i v_i^\top$ has rank one because every one of its columns is
a scalar multiple of $u_i$. Keeping only the first $k$ terms gives the
rank-$k$ approximation

$$
\widehat A^{(k)}
=
\sum_{i=1}^{k}\sigma_i u_i v_i^\top.
$$

This truncated SVD preserves the direction pairs along which $A$ acts most
strongly and discards components associated with smaller singular values.

### Optimal Approximation

The Eckart-Young theorem states that $\widehat A^{(k)}$ is the best rank-$k$
approximation to $A$ under the spectral norm. No other rank-$k$ matrix has
a smaller spectral-norm error, and

$$
\left\lVert A-\widehat A^{(k)}\right\rVert_2
=
\sigma_{k+1}.
$$

If $\sigma_{k+1}$ is small, the first $k$ components capture most of the
matrix's action under this norm. Truncation trades exact detail for a more
compact representation that can reduce storage and the cost of later matrix
operations.

For a centered data matrix, PCA uses the leading singular directions to
define a lower-dimensional subspace. The leading right-singular vectors
form the projection directions; the truncated matrix is the resulting
low-rank reconstruction, not itself the projection matrix.

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
- Eigenvectors identify invariant lines, and eigenvalues describe the scaling
  and possible orientation reversal along those lines.
- In an eigenvector basis, a diagonalizable transformation acts independently
  on each coordinate.
- Distinct eigenvalues are sufficient but not necessary for diagonalization;
  the actual requirement is a full basis of eigenvectors.
- Real symmetric matrices admit an orthonormal eigenbasis and therefore an
  orthogonal eigendecomposition.
- SVD extends the geometric idea of basis change and scaling to every matrix,
  including rectangular and rank-deficient transformations.
- Singular values quantify the strength of a matrix along paired input and
  output directions; the number of nonzero singular values equals the rank.
- Truncated SVD keeps the strongest rank-one components and gives the optimal
  rank-$k$ approximation under the spectral norm.
- PCA will use leading singular directions as a lower-dimensional projection
  basis and reconstruct data from the retained components.

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

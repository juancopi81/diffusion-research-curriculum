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

## Main Takeaways

- Matrix dimensions determine which operations are valid.
- Matrix multiplication combines rows with columns and is order-sensitive.
- Matrix form represents both a system of equations and a column combination.
- The general solution is a particular solution plus homogeneous solutions.
- REF exposes pivots and free variables; RREF makes them easier to read.
- Approximation and computational scale are different reasons for using
  methods beyond direct elimination.

## Questions to Revisit

- Apply the minus-1 trick to a concrete homogeneous system.
- Develop intuition for pseudoinverses and least squares later in the curriculum.
- Compare direct and iterative numerical methods when they become relevant.

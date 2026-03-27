[Studied from](https://www.3blue1brown.com/)

# Linear Transformations in Machine Learning

## What is a Linear Transformation?

A linear transformation is a function between vector spaces that preserves vector addition and scalar multiplication. In ML, it is typically represented as:

y = Wx + b

- **x**: Input vector (features)
- **W**: Weight matrix (parameters)
- **b**: Bias vector (offset)
- **y**: Output vector

## Mathematical Form

For input vector x ∈ ℝⁿ and weight matrix W ∈ ℝᵐˣⁿ, the transformation is:

y = Wx

If bias is included:

y = Wx + b

## Properties

- **Linearity:**  
  T(a·x₁ + b·x₂) = a·T(x₁) + b·T(x₂)
- **Preserves origin:**  
  If b = 0, the origin maps to the origin.

## Geometric Interpretation

- **Scaling:** Changes the magnitude of vectors.
- **Rotation:** Rotates vectors in space.
- **Shearing:** Shifts one axis in proportion to another.
- **Projection:** Projects vectors onto a subspace.

## Example

Suppose x = [x₁, x₂]ᵗ and W = [[2, 0], [0, 3]]:

y = Wx = [2x₁, 3x₂]ᵗ

This scales x₁ by 2 and x₂ by 3.

# Linear Algebra Fundamentals: Four Fundamental Subspaces

In linear algebra, particularly when working with matrices, understanding the four fundamental subspaces is crucial for grasping concepts like solving systems of linear equations, understanding transformations, and data analysis in machine learning. These subspaces are associated with a given matrix A.

Let A be an m x n matrix.

## 1. Column Space (C(A) or Im(A))
The column space of a matrix A is the span of its column vectors. It consists of all possible linear combinations of the columns of A. If we view A as a linear transformation from R^n to R^m, the column space is the set of all possible output vectors (the image of the transformation).

*   **Key Idea:** It represents all vectors 'b' for which the equation Ax = b has a solution.
*   **Dimension:** The dimension of the column space is the rank of the matrix A.
*   **Analogy:** If the matrix A transforms an input (vector x) into an output (vector b), the column space is the collection of *all possible outputs* this transformation can produce.

## 2. Null Space (N(A) or Ker(A))
The null space of a matrix A consists of all vectors x such that Ax = 0. These are the vectors that are "annihilated" by the transformation A, meaning they are mapped to the zero vector.

*   **Key Idea:** It describes the set of inputs that result in no "change" or "effect" (mapping to zero).
*   **Dimension:** The dimension of the null space is the nullity of the matrix A. According to the Rank-Nullity Theorem, rank(A) + nullity(A) = n (number of columns).
*   **Analogy:** Imagine a filter. The null space contains everything that passes through the filter and comes out as "nothing" (zero).

## 3. Row Space (C(A^T) or Im(A^T))
The row space of a matrix A is the span of its row vectors. Equivalently, it is the column space of its transpose, A^T.

*   **Key Idea:** It's closely related to the column space; its dimension is also equal to the rank of A.
*   **Dimension:** The dimension of the row space is also the rank of the matrix A.
*   **Orthogonality:** The row space is orthogonal to the null space.

## 4. Left Null Space (N(A^T) or Ker(A^T))
The left null space of a matrix A consists of all vectors y such that A^T y = 0. Equivalently, these are the vectors y for which y^T A = 0^T. It is the null space of the transpose of A.

*   **Key Idea:** It plays a crucial role in understanding the solvability of Ax = b and is orthogonal to the column space.
*   **Dimension:** The dimension of the left null space is m - rank(A).
*   **Orthogonality:** The left null space is orthogonal to the column space.

---

### Relationship Between Subspaces (Fundamental Theorem of Linear Algebra)
These four subspaces are intrinsically linked:
*   The column space and the left null space are orthogonal complements in R^m.
*   The row space and the null space are orthogonal complements in R^n.
*   Their dimensions are related by the rank-nullity theorem, providing a complete picture of how a matrix transforms vectors.

---


# 

#!/usr/bin/env python3
"""Exact certificates for the degree-one full Hessian candidate.

2026-11-21 / v0.20. Standard library only, rational/integer arithmetic.

This verifies a smooth degree-one del Pezzo surface with a nonzero direction
on which the Hessian candidate vanishes. It also verifies a second natural
polynomial covariant which all previously computed cyclic tests miss.
Neither computation identifies the actual categorical discrepancy delta_2.
The proof of coordinate covariance and the geometric smoothness argument
are in papers/sections/kuznetsov_hessian_counterexample.tex.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(polynomial, scalar):
    return {exponent: scalar * coefficient
            for exponent, coefficient in polynomial.items()
            if scalar * coefficient}


def multiply(left, right):
    result = {}
    for a, c in left.items():
        for b, d in right.items():
            exponent = tuple(i + j for i, j in zip(a, b))
            result[exponent] = result.get(exponent, Q(0)) + c * d
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def power(polynomial, exponent):
    result = {(0, 0, 0): Q(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def derivative(polynomial, variable):
    result = {}
    for exponent, coefficient in polynomial.items():
        degree = exponent[variable]
        if degree:
            new_exponent = list(exponent)
            new_exponent[variable] -= 1
            result[tuple(new_exponent)] = degree * coefficient
    return result


def binary(coefficients):
    degree = len(coefficients) - 1
    return {(degree - i, i, 0): Q(coefficient)
            for i, coefficient in enumerate(coefficients) if coefficient}


def determinant(matrix):
    matrix = [[Q(value) for value in row] for row in matrix]
    result = Q(1)
    for column in range(len(matrix)):
        pivot = next((i for i in range(column, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            result = -result
        value = matrix[column][column]
        result *= value
        for i in range(column + 1, len(matrix)):
            ratio = matrix[i][column] / value
            for j in range(column, len(matrix)):
                matrix[i][j] -= ratio * matrix[column][j]
    return result


def dense_multiply_mod(left, right, prime):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


x = {(1, 0, 0): Q(1)}
u = {(0, 1, 0): Q(1)}
y = {(0, 0, 1): Q(1)}
A = binary([0, 1, Q(-21, 2), 21, -14])
B = binary([0, Q(-1, 20), Q(7, 2), Q(-49, 2),
            70, Q(-161, 2), Q(343, 10)])
f = add(scale(power(y, 3), Q(1, 3)), multiply(A, y), B)
Ax = derivative(A, 0)
Axx = derivative(A, 0)
Axx = derivative(Axx, 0)
Bx = derivative(B, 0)
Bxx = derivative(Bx, 0)


def vector_field(polynomial):
    return add(multiply(x, derivative(polynomial, 0)),
               scale(multiply(u, derivative(polynomial, 1)), -5))


assert scale(Bxx, 2) == vector_field(A)
assert add(scale(multiply(A, Axx), -2), scale(power(Ax, 2), -1)) == vector_field(B)
H = add(multiply(derivative(derivative(f, 0), 0),
                 derivative(derivative(f, 2), 2)),
        scale(power(derivative(derivative(f, 0), 2), 2), -1))
assert H == add(vector_field(f),
                scale(multiply(Axx, derivative(f, 2)), 2))
print("PASS: H = (x*d_x-5*u*d_u)(f) + 2*A_xx*f_y exactly over Q")

# At u=1, 400*(4*A^3+9*B^2) is this degree-10 polynomial.
# Homogeneously, 400*(4*A^3+9*B^2)=u^2*D_hom(x,u).
D = [-155036, -123480, 1102500, -1228920, 246960, 252252,
     -82320, -12600, 2520, 340, 9]
discriminant = add(scale(power(A, 3), 4), scale(power(B, 2), 9))
homogeneous_D = {(i, 12 - i, 0): Q(coefficient)
                 for i, coefficient in enumerate(D) if coefficient}
assert scale(discriminant, 400) == homogeneous_D
assert D[-1] % 11 != 0
assert 60 % 11 != 0
print("PASS: the displayed homogeneous degree-12 discriminant identity")

# U*D + W*D' = 1 in F_11[x]. Coefficients are ascending in x.
U = [-3, 5, 4, 4, -5, 1, 5, 5, -5]
W = [1, 0, -4, 5, -4, -4, -3, -5, 2, -5]
D_prime = [i * coefficient for i, coefficient in enumerate(D)][1:]
left = dense_multiply_mod(U, D, 11)
right = dense_multiply_mod(W, D_prime, 11)
length = max(len(left), len(right))
bezout = [((left[i] if i < len(left) else 0)
           + (right[i] if i < len(right) else 0)) % 11
          for i in range(length)]
assert bezout == [1] + [0] * (length - 1)
print("PASS: U*D+W*D'=1 mod 11, hence D is squarefree over Q")

# The only possible singular point over u=0 has y=z=0,x!=0.
# Its u-derivative is -x^5/20.
fu_at_boundary = {exponent: coefficient
                  for exponent, coefficient in derivative(f, 1).items()
                  if exponent[1] == exponent[2] == 0}
assert fu_at_boundary == {(5, 0, 0): Q(-1, 20)}
print("PASS: boundary derivative f_u(x,0,0)=-x^5/20 is nonzero for x!=0")

R = add(scale(multiply(A, Axx), 4), scale(power(Ax, 2), -3))
assert R == binary([0, 0, -3, 42, -315, 546, -147])
vector_columns = [multiply(x, derivative(A, 0)),
                  multiply(u, derivative(A, 0)),
                  multiply(x, derivative(A, 1)),
                  multiply(u, derivative(A, 1))]
minor = [[column.get((4 - i, i, 0), Q(0))
          for column in vector_columns] for i in range(4)]
assert determinant(minor) == -378
print("PASS: R is a nonzero sextic and the V->V(A) matrix has a -378 minor")
print("      Thus [R]!=0 on this same smooth surface although [H]=0")

# A second, particularly simple witness for the undetected polynomial term.
A_simple = binary([1, 0, 0, 0, 1])
R_simple = add(scale(multiply(A_simple,
                             derivative(derivative(A_simple, 0), 0)), 4),
               scale(power(derivative(A_simple, 0), 2), -3))
assert R_simple == {(2, 4, 0): Q(48)}
A_cyclic = power(x, 4)
assert not add(scale(multiply(A_cyclic,
                              derivative(derivative(A_cyclic, 0), 0)), 4),
               scale(power(derivative(A_cyclic, 0), 2), -3))
print("PASS: R vanishes for A=x^4, but R=48*x^2*u^4 for A=x^4+u^4")

# The identity is quadratic in the five coefficients of A and in D.
# Polarization on the basis vectors and their pairwise sums is universal.
quartic_basis = [{(4 - i, i, 0): Q(1)} for i in range(5)]
for i, j in combinations_with_replacement(range(5), 2):
    quartic = (quartic_basis[i] if i == j
               else add(quartic_basis[i], quartic_basis[j]))
    axx = derivative(derivative(quartic, 0), 0)
    auu = derivative(derivative(quartic, 1), 1)
    axu = derivative(derivative(quartic, 0), 1)
    binary_hessian = add(multiply(axx, auu), scale(power(axu, 2), -1))
    for dx, du in [(1, 0), (0, 1), (1, 1)]:
        first = add(scale(derivative(quartic, 0), dx),
                    scale(derivative(quartic, 1), du))
        second = add(scale(derivative(first, 0), dx),
                     scale(derivative(first, 1), du))
        left = add(scale(multiply(quartic, second), 4),
                   scale(power(first, 2), -3))
        ell = add(scale(u, dx), scale(x, -du))
        right = scale(multiply(power(ell, 2), binary_hessian), Q(1, 3))
        assert left == right
print("PASS: universal identity R=(ell_D^2/3)*det Hess(A), by polarization")

# Intertwiner multiplicities in the conditional polynomial classification.
# For an SL_2 module, multiplicity of highest weight ell is
# dim(M_ell)-dim(M_{ell+2}); central GL_2 weights also agree.
quartic_weights = range(4, -5, -2)
quadratic_weights = (2, 0, -2)
source_A = Counter(a + b + d
                   for a, b in combinations_with_replacement(quartic_weights, 2)
                   for d in quadratic_weights)
source_B = Counter(b + d for b in range(6, -7, -2)
                   for d in quadratic_weights)
assert (source_A[6], source_A[8]) == (4, 2)
assert (source_B[4], source_B[6]) == (3, 2)
assert source_A[6] - source_A[8] == 2
assert source_B[4] - source_B[6] == 1
assert 12 * Q(-1, 4) + 16 * Q(-1, 8) == -5
assert 12 * 4 + 16 * (-3) == 0
print("PASS: GL2 covariant multiplicities 2+1 and the calibrated ambiguity line")
print("Scope: polynomial candidates only; no general formula for delta_2 is asserted.")

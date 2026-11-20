#!/usr/bin/env python3
"""Exact certificates for the quartic nodal extension criterion (2026-11-21).

Only the Python standard library is used.  The polynomial helpers and their
existing tests are reused from verify_degree_two_hessian_rigidity.  This file
checks the nodal witness, universal cubic tensor contraction along its affine
smoothing, the catalecticant, and finite weight/nilpotent calculations used in
the proof.  It does NOT compute the actual categorical discrepancy, prove its
regularity at the node, or mechanically prove module reflexivity.
"""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, gcd

from verify_degree_two_hessian_rigidity import (
    add, adjugate, catalecticant, columns, degree_four, derivative, fermat,
    hessian, jacobian_columns, monomial, multiply, rank, scale, variables,
)


def gaussian_determinant(matrix):
    matrix = [list(map(Fraction, row)) for row in matrix]
    answer = Fraction(1)
    for j in range(len(matrix)):
        pivot = next((i for i in range(j, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
            answer = -answer
        diagonal = matrix[j][j]
        answer *= diagonal
        for i in range(j + 1, len(matrix)):
            quotient = matrix[i][j] / diagonal
            for k in range(j + 1, len(matrix)):
                matrix[i][k] -= quotient * matrix[j][k]
    return answer


def trim(polynomial):
    polynomial = list(map(Fraction, polynomial))
    while polynomial and not polynomial[-1]:
        polynomial.pop()
    return tuple(polynomial)


def tadd(*polynomials):
    result = [Fraction(0)] * max((len(p) for p in polynomials), default=0)
    for polynomial in polynomials:
        for i, coefficient in enumerate(polynomial):
            result[i] += coefficient
    return trim(result)


def tmul(left, right):
    if not left or not right:
        return ()
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p))
                      for j in range(i + 1, len(p)))


def tdet(matrix):
    answer = ()
    for permutation in permutations(range(len(matrix))):
        term = (Fraction(permutation_sign(permutation)),)
        for i, j in enumerate(permutation):
            term = tmul(term, matrix[i][j])
        answer = tadd(answer, term)
    return answer


def cubic_invariant(family):
    """The four-epsilon contraction, as a polynomial in the parameter t."""
    tensors = {}
    for indices in product(range(3), repeat=4):
        exponent = tuple(indices.count(i) for i in range(3))
        normalization = Fraction(
            factorial(exponent[0]) * factorial(exponent[1]) * factorial(exponent[2]),
            factorial(4),
        )
        tensors[indices] = tmul((normalization,), family.get(exponent, ()))
    answer = ()
    for epsilon_columns in product(tuple(permutations(range(3))), repeat=4):
        sign = 1
        for column in epsilon_columns:
            sign *= permutation_sign(column)
        term = (Fraction(sign),)
        for row in range(3):
            indices = tuple(column[row] for column in epsilon_columns)
            term = tmul(term, tensors[indices])
        answer = tadd(answer, term)
    return answer


node = add(monomial((4, 0, 0)), monomial((0, 4, 0)),
           monomial((2, 2, 0)), monomial((2, 0, 2)), monomial((0, 2, 2)))
x, y, z = variables
assert [derivative(node, i) for i in range(3)] == [
    add(monomial((3, 0, 0), 4), monomial((1, 2, 0), 2), monomial((1, 0, 2), 2)),
    add(monomial((2, 1, 0), 2), monomial((0, 3, 0), 4), monomial((0, 1, 2), 2)),
    add(monomial((2, 0, 1), 2), monomial((0, 2, 1), 2)),
]
node_hessian = hessian(node)
assert [[entry.get((0, 0, 2), 0) for entry in row]
        for row in node_hessian] == [[2, 0, 0], [0, 2, 0], [0, 0, 0]]
node_q = adjugate(node_hessian)[2][2]
assert node_q.get((0, 0, 4), 0) == 4

# Columns are x_j partial_i F, ordered first by i and then by j.
jacobian = columns(jacobian_columns(node))
pivot_monomials = [(0, 1, 3), (0, 2, 2), (0, 3, 1), (0, 4, 0),
                   (1, 0, 3), (1, 1, 2), (1, 2, 1), (1, 3, 0), (2, 0, 2)]
minor = [jacobian[degree_four.index(exponent)] for exponent in pivot_monomials]
assert gaussian_determinant(minor) == 1024
assert rank(jacobian) == 9

# Exact polynomial identities on F_N + t z^4, not numerical sampling.
family = {exponent: (coefficient,) for exponent, coefficient in node.items()}
family[(0, 0, 4)] = (Fraction(0), Fraction(1))
assert cubic_invariant(family) == (Fraction(7, 6), Fraction(13, 2))
assert cubic_invariant({e: (c,) for e, c in fermat.items()}) == (Fraction(6),)

cat_node = catalecticant(node)
cat_direction = catalecticant(monomial((0, 0, 4)))
cat_family = [[trim((cat_node[i][j], cat_direction[i][j]))
               for j in range(6)] for i in range(6)]
assert tdet(cat_family) == (Fraction(-40960), Fraction(860160))
assert gaussian_determinant(cat_node) == -40960

# Enumerate every eigenvalue ratio having at least two zero monomial weights.
zero_weight_counts = {}
for u, v in combinations(degree_four, 2):
    normal = (u[1] * v[2] - u[2] * v[1],
              u[2] * v[0] - u[0] * v[2],
              u[0] * v[1] - u[1] * v[0])
    divisor = gcd(*normal)
    assert divisor
    normal = tuple(entry // divisor for entry in normal)
    if next(entry for entry in normal if entry) < 0:
        normal = tuple(-entry for entry in normal)
    zero_weight_counts[normal] = sum(
        sum(a * b for a, b in zip(weight, normal)) == 0
        for weight in degree_four
    )
assert max(zero_weight_counts.values()) == 5
assert max(count for eigenvalues, count in zero_weight_counts.items()
           if len(set(eigenvalues)) == 3) == 3


def nilpotent_21(polynomial):
    return multiply(x, derivative(polynomial, 1))


def nilpotent_3(polynomial):
    return add(multiply(x, derivative(polynomial, 1)),
               multiply(y, derivative(polynomial, 2)))


monomial_basis = [monomial(exponent) for exponent in degree_four]
assert rank(columns([nilpotent_21(p) for p in monomial_basis])) == 10
assert rank(columns([nilpotent_3(p) for p in monomial_basis])) == 12
invariant_quadratic = add(multiply(y, y), scale(multiply(x, z), -2))
regular_nilpotent_kernel = [monomial((4, 0, 0)),
                            multiply(multiply(x, x), invariant_quadratic),
                            multiply(invariant_quadratic, invariant_quadratic)]
assert all(not nilpotent_3(p) for p in regular_nilpotent_kernel)
assert rank(columns(regular_nilpotent_kernel)) == 3

print('PASS: nodal quartic minor 1024 and Hessian evaluation 4')
print('PASS: exact C(F_N+t z^4)=40960(21t-1), I3=(39t+7)/6')
print('PASS: semisimple zero weights and both nilpotent kernels')
print('Scope: actual categorical pole cancellation is not computed')

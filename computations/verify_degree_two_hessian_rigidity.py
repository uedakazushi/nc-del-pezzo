#!/usr/bin/env python3
"""Exact certificates for the degree-two Hessian candidate (2026-11-21).

Only the Python standard library is required.  All polynomial and matrix
calculations use exact rational arithmetic.  This checks the Klein rank-six
witness, the nontrivial catalecticant ambiguity, and small representation
dimension checks.  It does not prove extension of the actual categorical
quadratic discrepancy across the quartic discriminant.
"""

from fractions import Fraction
from itertools import permutations


def monomial(exponents, coefficient=1):
    return {tuple(exponents): Fraction(coefficient)} if coefficient else {}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(polynomial, coefficient):
    return {exponent: value * coefficient
            for exponent, value in polynomial.items() if value * coefficient}


def multiply(left, right):
    result = {}
    for a, u in left.items():
        for b, v in right.items():
            exponent = tuple(x + y for x, y in zip(a, b))
            result[exponent] = result.get(exponent, Fraction(0)) + u * v
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def derivative(polynomial, variable):
    result = {}
    for exponent, coefficient in polynomial.items():
        if exponent[variable]:
            reduced = list(exponent)
            reduced[variable] -= 1
            result[tuple(reduced)] = coefficient * exponent[variable]
    return result


def hessian(polynomial):
    return [[derivative(derivative(polynomial, i), j)
             for j in range(3)] for i in range(3)]


def adjugate(matrix):
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            rows = [k for k in range(3) if k != j]
            columns = [k for k in range(3) if k != i]
            minor = add(multiply(matrix[rows[0]][columns[0]],
                                 matrix[rows[1]][columns[1]]),
                        scale(multiply(matrix[rows[0]][columns[1]],
                                       matrix[rows[1]][columns[0]]), -1))
            row.append(scale(minor, (-1) ** (i + j)))
        result.append(row)
    return result


def rank(matrix):
    matrix = [list(map(Fraction, row)) for row in matrix]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(pivot_row, len(matrix))
                      if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row:
                value = matrix[i][column]
                matrix[i] = [a - value * b
                             for a, b in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def determinant(matrix):
    result = Fraction(0)
    for permutation in permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix))
                         for j in range(i + 1, len(matrix)))
        term = Fraction((-1) ** inversions)
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        result += term
    return result


degree_four = [(a, b, 4 - a - b) for a in range(5)
               for b in range(5 - a)]
x, y, z = (monomial(e) for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
variables = [x, y, z]


def columns(polynomials):
    return [[polynomial.get(exponent, 0) for polynomial in polynomials]
            for exponent in degree_four]


def jacobian_columns(polynomial):
    partials = [derivative(polynomial, i) for i in range(3)]
    return [multiply(variable, partial)
            for partial in partials for variable in variables]


# Klein quartic: an exact rank-six certificate in the degree-four Jacobian ring.
klein = add(monomial((3, 1, 0)), monomial((0, 3, 1)),
            monomial((1, 0, 3)))
partials = [derivative(klein, i) for i in range(3)]
assert partials == [add(monomial((2, 1, 0), 3), monomial((0, 0, 3))),
                    add(monomial((3, 0, 0)), monomial((0, 2, 1), 3)),
                    add(monomial((0, 3, 0)), monomial((1, 0, 2), 3))]
adj = adjugate(hessian(klein))
reduced = {(0, 0): monomial((0, 4, 0), -21),
           (1, 1): monomial((0, 0, 4), -21),
           (2, 2): monomial((4, 0, 0), -21),
           (0, 1): monomial((0, 2, 2), 63),
           (0, 2): monomial((2, 2, 0), 63),
           (1, 2): monomial((2, 0, 2), 63)}
certificates = {(0, 0): scale(multiply(y, partials[2]), 12),
                (1, 1): scale(multiply(z, partials[0]), 12),
                (2, 2): scale(multiply(x, partials[1]), 12),
                (0, 1): scale(multiply(z, partials[1]), -18),
                (0, 2): scale(multiply(y, partials[0]), -18),
                (1, 2): scale(multiply(x, partials[2]), -18)}
for position in reduced:
    i, j = position
    assert add(adj[i][j], scale(reduced[position], -1)) == certificates[position]
jac = jacobian_columns(klein)
assert rank(columns(jac)) == 9
basis = [monomial(e) for e in [(4, 0, 0), (0, 4, 0), (0, 0, 4),
                               (2, 2, 0), (0, 2, 2), (2, 0, 2)]]
assert rank(columns(jac + basis)) == 15
assert rank(columns(jac + list(reduced.values()))) == 15
q_matrix = [[0, 0, -21, 0, 0, 0],
            [-21, 0, 0, 0, 0, 0],
            [0, -21, 0, 0, 0, 0],
            [0, 0, 0, 0, 126, 0],
            [0, 0, 0, 126, 0, 0],
            [0, 0, 0, 0, 0, 126]]
assert determinant(q_matrix) == 21 ** 3 * 126 ** 3
assert determinant([[3, 0, 1], [1, 3, 0], [0, 1, 3]]) == 28

# Fermat: the Hessian candidate has rank exactly three.
fermat = add(*(monomial(e) for e in [(4, 0, 0), (0, 4, 0), (0, 0, 4)]))
fermat_adj = adjugate(hessian(fermat))
fermat_cofactors = [fermat_adj[i][j] for i in range(3) for j in range(i, 3)]
assert rank(columns(jacobian_columns(fermat) + fermat_cofactors)) == 12

# Catalecticant conventions: fourth derivatives in the six quadratic operators.
quadratic_operators = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def catalecticant(polynomial):
    result = []
    for a in quadratic_operators:
        row = []
        for b in quadratic_operators:
            value = polynomial
            for variable in a + b:
                value = derivative(value, variable)
            assert not set(value).difference({(0, 0, 0)})
            row.append(value.get((0, 0, 0), 0))
        result.append(row)
    return result


# The two mixed rows vanish on every basis vector of the whole cyclic subspace.
cyclic_basis = [monomial((a, 4 - a, 0)) for a in range(5)] + [monomial((0, 0, 4))]
for polynomial in cyclic_basis:
    cat = catalecticant(polynomial)
    assert cat[4] == [0] * 6 and cat[5] == [0] * 6

star = add(fermat, monomial((2, 2, 0)), monomial((0, 2, 2)),
           monomial((2, 0, 2)))
cat_star = catalecticant(star)
assert cat_star == [[24, 4, 4, 0, 0, 0], [4, 24, 4, 0, 0, 0],
                    [4, 4, 24, 0, 0, 0], [0, 0, 0, 4, 0, 0],
                    [0, 0, 0, 0, 4, 0], [0, 0, 0, 0, 0, 4]]
assert determinant(cat_star) == 819200
star_q = adjugate(hessian(star))[2][2]
star_reduced = add(monomial((2, 2, 0), 108), monomial((2, 0, 2), 14),
                   monomial((0, 2, 2), 14))
star_partials = [derivative(star, i) for i in range(3)]
star_certificate = add(scale(multiply(x, star_partials[0]), 6),
                       scale(multiply(y, star_partials[1]), 6),
                       multiply(z, star_partials[2]))
assert add(star_q, scale(star_reduced, -1)) == star_certificate
assert rank(columns(jacobian_columns(star) + [star_reduced])) == 10

# Degree and determinant characters cancel in C^9 / Delta^2.
assert 6 * 9 == 27 * 2
assert 8 * 9 == 36 * 2


def schur_dimension(partition):
    a, b, c = tuple(partition) + (0,) * (3 - len(partition))
    return (a - b + 1) * (a - c + 2) * (b - c + 1) // 2


left_partitions = [(8,), (6, 2), (4, 4)]
right_partitions = [(6, 2), (5, 2, 1), (4, 2, 2)]
assert sum(map(schur_dimension, left_partitions)) == 15 * 16 // 2
assert sum(map(schur_dimension, right_partitions)) == 15 * 6
assert set(left_partitions) & set(right_partitions) == {(6, 2)}

print("PASS: Klein Jacobian relations and candidate rank 6; Fermat rank 3")
print("PASS: cyclic catalecticant vanishing and smooth-witness determinant 819200")
print("PASS: ambiguity witness Jacobian class, character cancellation, Schur dimensions")
print("Scope: the categorical discriminant-extension hypothesis remains unproved")

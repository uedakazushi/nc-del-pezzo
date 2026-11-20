#!/usr/bin/env python3
"""Exact finite certificates for the Ku-constant gluing normal form.

2026-11-21 / v0.21. Standard library only.
This verifies polynomial identities, tangent-space ranks, evaluation ranks,
and the displayed tail jets for rational del Pezzo configurations.
It does not prove Abel reconstruction, formal universality, or compute the
anti-canonical multiplication and the actual quadratic discrepancy.

The polynomial routines are reused from the earlier Hessian certificate;
importing it also rechecks those certificates. Point configurations and
exact row rank are reused from the surface Hochschild calculation.
"""

from fractions import Fraction as Q
from itertools import combinations, permutations, product

from verify_degree_one_hessian_counterexample import (
    add, derivative, determinant, multiply, scale,
)
from verify_surface_kuznetsov import (
    configuration, evaluation, exponents, general_position, rank,
)


def monomial(exponent, coefficient=1):
    return {tuple(exponent): Q(coefficient)} if coefficient else {}


def unit_exponent(size, index):
    return tuple(int(i == index) for i in range(size))


def sign(permutation):
    return (-1) ** sum(permutation[i] > permutation[j]
                       for i in range(len(permutation))
                       for j in range(i + 1, len(permutation)))


def polynomial_det3(matrix):
    return add(*(scale(multiply(multiply(matrix[0][p[0]], matrix[1][p[1]]),
                                matrix[2][p[2]]), sign(p))
                 for p in permutations(range(3))))


def epsilon(i, j, k):
    return sign((i, j, k)) if len({i, j, k}) == 3 else 0


# Independent polynomial variables v0,v1,v2,h00,h01,h02,h11,h12,h22.
variables = [monomial(unit_exponent(9, i)) for i in range(9)]
v = variables[:3]
h00, h01, h02, h11, h12, h22 = variables[3:]
H = [[h00, h01, h02], [h01, h11, h12], [h02, h12, h22]]
C = [[{}, scale(v[2], -1), v[1]],
     [v[2], {}, scale(v[0], -1)],
     [scale(v[1], -1), v[0], {}]]
matrix = [[add(C[i][j], H[i][j]) for j in range(3)] for i in range(3)]
quadratic = add(*(multiply(multiply(v[i], H[i][j]), v[j])
                  for i in range(3) for j in range(3)))
assert polynomial_det3(matrix) == add(quadratic, polynomial_det3(H))
print("PASS: det(C(v)+H)=v^T*H*v+det(H), universally in nine variables")

# Tensor entries use (output index k, v index j, u index i).
indices = list(product(range(3), repeat=3))
gauge_columns = []
for a, b in product(range(3), repeat=2):
    gauge_columns.append([-epsilon(k, j, a) * int(b == i)
                          for k, j, i in indices])
for a, b in product(range(3), repeat=2):
    gauge_columns.append([int(k == a) * epsilon(b, j, i)
                          for k, j, i in indices])
gauge_rows = list(map(list, zip(*gauge_columns)))
assert rank(gauge_rows) == 17
kernel_scalar = [int(a == b) for a, b in product(range(3), repeat=2)] * 2
assert all(sum(row[j] * kernel_scalar[j] for j in range(18)) == 0
           for row in gauge_rows)
print("PASS: the 27-by-18 infinitesimal gauge matrix has rank 17")

cubic_exponents = exponents(3)
x = [monomial(unit_exponent(3, i)) for i in range(3)]
hessian_columns = []
for exponent in cubic_exponents:
    P = monomial(exponent)
    Hess = [[derivative(derivative(P, k), i) for i in range(3)]
            for k in range(3)]
    column = [Hess[k][i].get(unit_exponent(3, j), Q(0))
              for k, j, i in indices]
    hessian_columns.append(column)
    euler = add(*(multiply(multiply(x[k], Hess[k][i]), x[i])
                  for k in range(3) for i in range(3)))
    assert euler == scale(P, 6)
assert rank(list(map(list, zip(*hessian_columns)))) == 10
assert rank(list(map(list, zip(*(gauge_columns + hessian_columns))))) == 27
print("PASS: ten Hessian tensors complement the gauge image; total rank 27")
print("PASS: v^T*Hess(P)(v)*v=6P(v), on a basis and hence for every cubic P")

# Replace GL(U) by SL(U): six off-diagonals and two trace-free diagonals.
slice_gauge = [gauge_columns[3*a+b] for a, b in product(range(3), repeat=2)
               if a != b]
slice_gauge += [[a-b for a, b in zip(gauge_columns[0], gauge_columns[4])],
               [a-b for a, b in zip(gauge_columns[4], gauge_columns[8])]]
slice_gauge += gauge_columns[9:]
square_jacobian = list(map(list, zip(*(slice_gauge + hessian_columns))))
assert len(square_jacobian) == len(square_jacobian[0]) == 27
det = determinant(square_jacobian)
assert det
print(f"PASS: the normalized 27-by-27 slice Jacobian determinant is {det}")


def nullspace(rows):
    """Rational kernel basis, keeping all free columns explicit."""
    matrix = [[Q(a) for a in row] for row in rows]
    pivots = []
    for j in range(len(matrix[0])):
        k = next((i for i in range(len(pivots), len(matrix))
                  if matrix[i][j]), None)
        if k is None:
            continue
        p = len(pivots)
        matrix[p], matrix[k] = matrix[k], matrix[p]
        pivot = matrix[p][j]
        matrix[p] = [a/pivot for a in matrix[p]]
        for i in range(len(matrix)):
            if i != p:
                coefficient = matrix[i][j]
                matrix[i] = [a-coefficient*b for a, b in zip(matrix[i], matrix[p])]
        pivots.append(j)
        if len(pivots) == len(matrix):
            break
    result = []
    for j in range(len(matrix[0])):
        if j not in pivots:
            vector = [Q(0)] * len(matrix[0])
            vector[j] = Q(1)
            for i, p in enumerate(pivots):
                vector[p] = -matrix[i][j]
            result.append(vector)
    return result


def evaluate(polynomial, point):
    return sum(coefficient * point[0]**e[0] * point[1]**e[1] * point[2]**e[2]
               for e, coefficient in polynomial.items())


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def matrix_vector(matrix, vector):
    return [dot(row, vector) for row in matrix]


points = configuration()
assert general_position(points)
jet_checks = 0
for r in (7, 8):
    selected = points[:r]
    assert general_position(selected)
    values = [evaluation(p, cubic_exponents) for p in selected]
    assert rank(values) == r
    basis = nullspace(values)
    assert len(basis) == 10-r
    for vector in basis:
        assert all(dot(row, vector) == 0 for row in values)
    print(f"PASS: {r} rational del Pezzo points: cubic evaluation rank {r}, kernel {10-r}")

    # First and second tail-jet identities are respectively linear and
    # quadratic in the cubic. Basis elements and pairwise sums suffice.
    probes = basis + [[a+b for a, b in zip(left, right)]
                      for left, right in combinations(basis, 2)]
    for vector in probes:
        P = {e: a for e, a in zip(cubic_exponents, vector) if a}
        Hess = [[derivative(derivative(P, i), j) for j in range(3)]
                for i in range(3)]
        for p0 in selected:
            p = list(map(Q, p0))
            assert evaluate(P, p) == 0
            matrix = [[evaluate(Hess[i][j], p) for j in range(3)]
                      for i in range(3)]
            # The chosen rational points have positive norm, so this
            # is a valid explicit choice of the covector n with n.p=1.
            norm = dot(p, p)
            n = [a/norm for a in p]
            Hp = matrix_vector(matrix, p)
            a = cross(n, Hp)
            Ha = matrix_vector(matrix, a)
            b = cross(n, Ha)
            assert dot(n, p) == 1 and dot(p, Hp) == 0
            assert cross(p, a) == [-q for q in Hp]
            assert cross(p, b) == [-q for q in Ha]
            # Since H is symmetric and C is alternating these are
            # both right and left kernel equations modulo h^3:
            # (C+hH)(p+ha+h^2b)=0,
            # (p-ha+h^2b)^T(C+hH)=0.
            assert dot(p, Ha) == 0
            jet_checks += 1
print(f"PASS: {jet_checks} polarized tail-kernel jet checks modulo h^3")
print("Point configuration:", points)
print("Scope: exact finite algebra only; formal universality is proved in the paper,")
print("       and the anti-canonical multiplication/actual discrepancy is not computed.")

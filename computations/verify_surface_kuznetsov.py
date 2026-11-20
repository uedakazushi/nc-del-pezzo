#!/usr/bin/env python3
"""Exact checks for the surface residual point-configuration algebra.

Only the Python standard library is used.  The computations check the
normalized relative Hochschild complex for explicit del Pezzo configurations
and the classical Jacobian Hilbert coefficients.  They do not compute the
noncommutative Hochschild--Serre multiplication or prove rho = shadow.
"""

from fractions import Fraction
from itertools import combinations
from random import Random


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    pivot = 0
    for j in range(len(a[0])):
        k = next((i for i in range(pivot, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        q = a[pivot][j]
        a[pivot] = [v / q for v in a[pivot]]
        for i in range(pivot + 1, len(a)):
            q = a[i][j]
            if q:
                a[i] = [v - q * w for v, w in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def exponents(total):
    return [(i, j, total - i - j)
            for i in range(total + 1) for j in range(total - i + 1)]


def evaluation(p, powers):
    return [p[0] ** i * p[1] ** j * p[2] ** k for i, j, k in powers]


def general_position(points):
    if any(rank(triple) != 3 for triple in combinations(points, 3)):
        return False
    quadrics = exponents(2)
    if any(rank([evaluation(p, quadrics) for p in six]) != 6
           for six in combinations(points, 6)):
        return False
    if len(points) == 8:
        cubics = exponents(3)
        values = [evaluation(p, cubics) for p in points]
        for p in points:
            derivatives = []
            for coordinate in range(3):
                row = []
                for power in cubics:
                    q = list(power)
                    coefficient = q[coordinate]
                    if not coefficient:
                        row.append(0)
                        continue
                    q[coordinate] -= 1
                    row.append(coefficient * p[0] ** q[0]
                               * p[1] ** q[1] * p[2] ** q[2])
                derivatives.append(row)
            if rank(values + derivatives) != 10:
                return False
    return True


def configuration():
    points = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
    rng = Random(1729)
    while len(points) < 8:
        candidate = (1, rng.randint(-20, 20), rng.randint(-20, 20))
        if general_position(points + [candidate]):
            points.append(candidate)
    return points


def hochschild(points):
    r = len(points)
    # C0: vertex scalars; C1: lambda_i, nu_i, and the 3x3 matrix M.
    # d1_i = (lambda_i - nu_i) p_i + p_i M, with p_i a row vector.
    d0 = [[0] * (r + 2) for _ in range(2 * r + 9)]
    for i in range(r):
        d0[i][i], d0[i][r] = 1, -1
        d0[r + i][i], d0[r + i][r + 1] = 1, -1
    for j in range(3):
        d0[2 * r + 3 * j + j][r] = 1
        d0[2 * r + 3 * j + j][r + 1] = -1
    d1 = [[0] * (2 * r + 9) for _ in range(3 * r)]
    for i, p in enumerate(points):
        for j in range(3):
            d1[3 * i + j][i] = p[j]
            d1[3 * i + j][r + i] = -p[j]
            for k in range(3):
                d1[3 * i + j][2 * r + 3 * k + j] = p[k]
    for row in d1:
        for j in range(r + 2):
            assert sum(row[k] * d0[k][j] for k in range(len(row))) == 0
    rank0, rank1 = rank(d0), rank(d1)
    assert (rank0, rank1) == (r + 1, r + 8)
    hh = (r + 2 - rank0, 2 * r + 9 - rank0 - rank1, 3 * r - rank1)
    assert hh == (1, 0, 2 * r - 8)
    return rank0, rank1, hh


def jacobian_hilbert(weights, relations, bound=6):
    coefficients = [1] + [0] * bound
    for w in weights:
        for j in range(w, bound + 1):
            coefficients[j] += coefficients[j - w]
    for degree in relations:
        coefficients = [a - (coefficients[j - degree] if j >= degree else 0)
                        for j, a in enumerate(coefficients)]
    return coefficients


def main():
    points = configuration()
    assert general_position(points)
    for d in (1, 2):
        p = points[:9 - d]
        assert general_position(p)
        rank0, rank1, hh = hochschild(p)
        print(f"d={d}, r={len(p)}, ranks(d0,d1)=({rank0},{rank1}), "
              f"(HH0,HH1,HH2)={hh}")
    d1 = jacobian_hilbert((1, 1, 2), (4, 5, 5))
    d2 = jacobian_hilbert((1, 1, 1), (3, 3, 3))
    assert [d1[j] for j in (1, 2, 4, 5)] == [2, 4, 8, 8]
    assert [d2[j] for j in (1, 3)] == [3, 7]
    print("Classical Jacobian Hilbert coefficients verified.")
    print("Point configurations:", points)
    print("No claim about noncommutative HS products or rho = shadow.")


if __name__ == "__main__":
    main()

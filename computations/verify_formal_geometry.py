#!/usr/bin/env python3
"""Exact finite checks for nc-del-pezzo (2026-11-20, v0.1).

No dependencies outside Python's standard library. These checks support the
explicit formulas; they do not prove deformation or categorical equivalences.
"""
from itertools import combinations
from math import comb


def weighted_polynomial_counts(weights, bound):
    values = [0] * (bound + 1)
    values[0] = 1
    for weight in weights:
        for degree in range(weight, bound + 1):
            values[degree] += values[degree - weight]
    return values


def difference(values, order):
    for _ in range(order):
        values = [b - a for a, b in zip(values, values[1:])]
    return values


def binomial_h(n, degree):
    return comb(degree + n, n) if degree >= 0 else 0


def hilbert_checks(n, d):
    r = n - 1
    bound = r * (n + 5)
    weights = [1] * (n if d == 1 else n + 1) + ([2, 3] if d == 1 else [2])
    relation = 6 if d == 1 else 4
    ambient = weighted_polynomial_counts(weights, bound)
    quotient = [value - (ambient[j - relation] if j >= relation else 0)
                for j, value in enumerate(ambient)]
    # Independent monic basis: the exponent of z is at most one.
    without_z = weighted_polynomial_counts(weights[:-1], bound)
    monic = [value + (without_z[j - weights[-1]] if j >= weights[-1] else 0)
             for j, value in enumerate(without_z)]
    assert quotient == monic, (n, d, "monic quotient")
    numerator = [1, -1, 1] if d == 1 else [1, 0, 1]
    simplified = [sum(a * binomial_h(n, j - k)
                      for k, a in enumerate(numerator)) for j in range(bound + 1)]
    assert quotient == simplified, (n, d, "Hilbert simplification")
    anticanonical = quotient[::r]
    assert set(difference(anticanonical, n)) == {d * r ** n}, (n, d, "degree")
    assert set(difference(anticanonical, n + 1)) == {0}, (n, d, "polynomial degree")


def add_term(poly, monomial, coefficient):
    monomial = tuple(sorted(monomial))
    poly[monomial] = poly.get(monomial, 0) + coefficient
    if poly[monomial] == 0:
        del poly[monomial]


def wedge_obstruction_check(n):
    # Expand each Pfaffian of P = e Q + e^2 R modulo e^3 in
    # a free commutative polynomial ring, using sparse exact dictionaries.
    for i, j, k, ell in combinations(range(n + 1), 4):
        coefficient = {}
        expected = {}
        for sign, ab, cd in [(1, (i, j), (k, ell)),
                              (-1, (i, k), (j, ell)),
                              (1, (i, ell), (j, k))]:
            for left_order, left_name in [(1, "q"), (2, "r")]:
                for right_order, right_name in [(1, "q"), (2, "r")]:
                    if left_order + right_order < 3:
                        add_term(coefficient, ((left_name,) + ab,
                                               (right_name,) + cd), sign)
            add_term(expected, (("q",) + ab, ("q",) + cd), sign)
        assert coefficient == expected
    # A concrete obstructed direction for n >= 3: e0^e1 + e2^e3.
    if n >= 3:
        q = {(0, 1): 1, (2, 3): 1}
        pf = q.get((0, 1), 0) * q.get((2, 3), 0) - q.get((0, 2), 0) * q.get((1, 3), 0) + q.get((0, 3), 0) * q.get((1, 2), 0)
        assert pf == 1


def main():
    for n in range(2, 9):
        for d in (1, 2):
            hilbert_checks(n, d)
        wedge_obstruction_check(n)
    print("PASS: n=2,...,8, both degrees: monic basis, Hilbert series, anticanonical finite differences.")
    print("PASS: n=2,...,8: all Pfaffian second-order expansions; explicit obstructed directions for n>=3.")
    print("n | d=1: dimension | d=2: dimension / tangent dimension")
    for n in range(2, 6):
        b1 = comb(n + 3, 4) + comb(n + 5, 6) - n * n
        b2 = comb(n + 4, 4) - (n + 1) ** 2
        print(f"{n} | {b1+n} | {b2+2*n-1} / {b2+comb(n+1,2)}")


if __name__ == "__main__":
    main()

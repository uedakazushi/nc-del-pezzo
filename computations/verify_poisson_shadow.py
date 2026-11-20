#!/usr/bin/env python3
"""Exact universal-jet identities for the Poisson shadow (2026-11-20).

All coefficients are integers in a free polynomial ring in the direction
coordinates and the first/second jets of an arbitrary polynomial F.  The
degree-two Jacobiators are compared with explicit Pluecker multiples before
imposing the Pluecker equations.  This finite index check supports the
all-dimensional proof in poisson_shadow_comparison.tex; it does not prove
the moduli, etale, or flatness statements.
"""
from itertools import combinations

from verify_formal_geometry import add_term


def variable(name):
    return {(name,): 1}


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            add_term(result, monomial, coefficient)
    return result


def scale(poly, coefficient):
    return {m: coefficient * c for m, c in poly.items() if coefficient * c}


def multiply(*polys):
    result = {(): 1}
    for poly in polys:
        product = {}
        for m, c in result.items():
            for n, d in poly.items():
                add_term(product, m + n, c * d)
        result = product
    return result


def jet(*indices):
    return variable(("F",) + tuple(sorted(indices)))


def derivative(poly, index):
    result = {}
    for monomial, coefficient in poly.items():
        for position, symbol in enumerate(monomial):
            if symbol[0] == "F":
                differentiated = ("F",) + tuple(sorted(symbol[1:] + (index,)))
                add_term(result, monomial[:position] + (differentiated,)
                         + monomial[position + 1:], coefficient)
    return result


def alternating_matrix(size):
    return [[{} for _ in range(size)] for _ in range(size)]


def put(matrix, i, j, poly):
    matrix[i][j] = poly
    matrix[j][i] = scale(poly, -1)


def jacobi(matrix, i, j, k):
    return add(*(multiply(matrix[a][ell], derivative(matrix[b][c], ell))
                 for a, b, c in [(i, j, k), (j, k, i), (k, i, j)]
                 for ell in range(len(matrix))))


def casimir_checks(matrix):
    for i in range(len(matrix)):
        assert not add(*(multiply(matrix[i][j], jet(j))
                         for j in range(len(matrix)))), ("Casimir", i)


def degree_one(n):
    y, z = n, n + 1
    directions = [variable(("D", i)) for i in range(n)]
    matrix = alternating_matrix(n + 2)
    for i in range(n):
        put(matrix, i, y, multiply(directions[i], jet(z)))
        put(matrix, z, i, multiply(directions[i], jet(y)))
    put(matrix, y, z, add(*(multiply(directions[i], jet(i))
                           for i in range(n))))
    casimir_checks(matrix)
    for triple in combinations(range(n + 2), 3):
        assert not jacobi(matrix, *triple), ("degree one", n, triple)


def p(i, j):
    if i == j:
        return {}
    return scale(variable(("P", min(i, j), max(i, j))), 1 if i < j else -1)


def pluecker(i, j, k, ell):
    return add(multiply(p(i, j), p(k, ell)),
               scale(multiply(p(i, k), p(j, ell)), -1),
               multiply(p(i, ell), p(j, k)))


def degree_two(size):
    z = size
    matrix = alternating_matrix(size + 1)
    for i, j in combinations(range(size), 2):
        put(matrix, i, j, multiply(p(i, j), jet(z)))
    for i in range(size):
        put(matrix, i, z,
            scale(add(*(multiply(p(i, j), jet(j)) for j in range(size))), -1))
    casimir_checks(matrix)
    for i, j, k in combinations(range(size), 3):
        expected = add(*(multiply(pluecker(i, j, k, ell),
                                  add(multiply(jet(z), jet(z, ell)),
                                      scale(multiply(jet(ell), jet(z, z)), -1)))
                         for ell in range(size)))
        assert jacobi(matrix, i, j, k) == expected, ("xxx", size, i, j, k)
    for i, j in combinations(range(size), 2):
        expected = scale(add(*(multiply(pluecker(i, j, ell, m),
                                        jet(ell), jet(z, m))
                               for ell in range(size) for m in range(size))), -1)
        assert jacobi(matrix, i, j, z) == expected, ("xxz", size, i, j)


def main():
    for n in range(2, 7):
        degree_one(n)
        degree_two(n + 1)
    print("PASS: n=2,...,6, degree one: all universal-jet Jacobi and Casimir identities.")
    print("PASS: n=2,...,6, degree two: all Jacobiators equal their stated Pluecker multiples.")
    print("PASS: degree two Casimir identities hold even before imposing Pluecker relations.")


if __name__ == "__main__":
    main()

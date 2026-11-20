#!/usr/bin/env python3
"""Exact symmetry constraints on the quadratic categorical-shadow discrepancy.

Standard-library certificate; no roots of unity or floating-point arithmetic.
Diagonal characters are integer vectors modulo the orders of cyclic factors.
The residual permutation constraints are solved over Q.

Actual coefficients use the separately proved cyclic-period comparison.
This script verifies its normalized Hessian specializations algebraically;
it does not prove that categorical comparison theorem.
"""

from fractions import Fraction
from itertools import combinations_with_replacement, product


def nullspace(rows, columns):
    matrix = [[Fraction(x) for x in row] for row in rows]
    pivots = []
    row = 0
    for col in range(columns):
        pivot = next((i for i in range(row, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][col]
        matrix[row] = [x / scale for x in matrix[row]]
        for i in range(len(matrix)):
            if i != row and matrix[i][col]:
                scale = matrix[i][col]
                matrix[i] = [a - scale * b for a, b in zip(matrix[i], matrix[row])]
        pivots.append(col)
        row += 1
    free = [j for j in range(columns) if j not in pivots]
    result = []
    for col in free:
        vector = [Fraction(0) for _ in range(columns)]
        vector[col] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -matrix[i][col]
        result.append(vector)
    return result


def add_character(a, b):
    return tuple(x + y for x, y in zip(a, b))


def symmetric_characters(characters):
    pairs = list(combinations_with_replacement(range(len(characters)), 2))
    return pairs, [add_character(characters[i], characters[j]) for i, j in pairs]


def invariant_homs(output_chars, input_chars, orders, permutation_actions):
    allowed = [(i, j) for i, a in enumerate(output_chars)
               for j, b in enumerate(input_chars)
               if all((x - y) % n == 0 for x, y, n in zip(a, b, orders))]
    index = {pair: k for k, pair in enumerate(allowed)}
    equations = []
    for output_action, input_action in permutation_actions:
        for old, (i, j) in enumerate(allowed):
            new_i, sign_i = output_action[i]
            new_j, sign_j = input_action[j]
            new = index[new_i, new_j]
            equation = [0] * len(allowed)
            equation[new] += 1
            equation[old] -= sign_i * sign_j
            equations.append(equation)
    return allowed, nullspace(equations, len(allowed))


def permute_exponent(exponent, permutation):
    result = [0] * len(exponent)
    for old, new in enumerate(permutation):
        result[new] = exponent[old]
    return tuple(result)


def symmetric_action(pairs, action):
    index = {pair: i for i, pair in enumerate(pairs)}
    result = []
    for i, j in pairs:
        new_i, sign_i = action[i]
        new_j, sign_j = action[j]
        result.append((index[tuple(sorted((new_i, new_j)))], sign_i * sign_j))
    return result


def verify_degree_two():
    # X: z^2/2+x0^4+x1^4+x2^4=0. Diagonal cover mu4^3 x mu2.
    # Tangent action: f -> b^2 f(A^-1 x). Poisson: P -> b^-1 wedge^2(A)P.
    tangent = sorted(a for a in product(range(3), repeat=3) if sum(a) == 4)
    tangent_chars = [tuple(-x for x in a) + (2,) for a in tangent]
    poisson = [(0, 1), (0, 2), (1, 2)]
    poisson_chars = [tuple(int(k in ij) for k in range(3)) + (-1,)
                      for ij in poisson]
    pairs, input_chars = symmetric_characters(poisson_chars)
    assert len(tangent) == 6 and len(pairs) == 6
    for character in tangent_chars + poisson_chars + input_chars:
        # The central weighted mu4 acts trivially.
        assert (sum(character[:3]) + 2 * character[3]) % 4 == 0
    actions = []
    for permutation in [(1, 0, 2), (0, 2, 1)]:
        out = [(tangent.index(permute_exponent(a, permutation)), 1) for a in tangent]
        exterior = []
        for i, j in poisson:
            new_i, new_j = permutation[i], permutation[j]
            exterior.append((poisson.index(tuple(sorted((new_i, new_j)))),
                             1 if new_i < new_j else -1))
        actions.append((out, symmetric_action(pairs, exterior)))
    allowed, basis = invariant_homs(tangent_chars, input_chars, (4, 4, 4, 2), actions)
    assert len(allowed) == 3 and len(basis) == 1
    terms = [(tangent[i], pairs[j], coefficient)
             for (i, j), coefficient in zip(allowed, basis[0]) if coefficient]
    assert len(terms) == 3 and len({term[2] for term in terms}) == 1
    for exponent, (i, j), coefficient in terms:
        assert i == j and coefficient == 1
        assert exponent == tuple(2 * int(k in poisson[i]) for k in range(3))
    print("d2: dim H1(T)=6, dim Sym2(P)=6, diagonal invariants=3, full invariants=1")
    print("    generator: p01^2*[x0^2*x1^2] + p02^2*[x0^2*x2^2] + p12^2*[x1^2*x2^2]")
    return terms


def verify_degree_one():
    # X: z^2/2+y^3/3+x0^6+x1^6=0. Diagonal cover mu6^2 x mu3 x mu2.
    # Tangent: F -> b^2 F(A^-1 x,c^-1 y); Poisson: D -> (c/b)AD.
    tangent = sorted((a, b, e) for a, b in product(range(5), repeat=2)
                     for e in range(2) if a + b + 2 * e == 6)
    tangent_chars = [(-a, -b, -e, 2) for a, b, e in tangent]
    poisson_chars = [(1, 0, 1, -1), (0, 1, 1, -1)]
    pairs, input_chars = symmetric_characters(poisson_chars)
    assert len(tangent) == 8 and len(pairs) == 3
    for character in tangent_chars + poisson_chars + input_chars:
        # The central weighted mu6 acts trivially.
        assert (character[0] + character[1] + 2 * character[2]
                + 3 * character[3]) % 6 == 0
    out = [(tangent.index((b, a, e)), 1) for a, b, e in tangent]
    swap = [(1, 1), (0, 1)]
    actions = [(out, symmetric_action(pairs, swap))]
    allowed, basis = invariant_homs(tangent_chars, input_chars, (6, 6, 3, 2), actions)
    assert len(allowed) == 2 and len(basis) == 1
    terms = [(tangent[i], pairs[j], coefficient)
             for (i, j), coefficient in zip(allowed, basis[0]) if coefficient]
    assert set(terms) == {((4, 0, 1), (0, 0), Fraction(1)),
                          ((0, 4, 1), (1, 1), Fraction(1))}
    print("d1: dim H1(T)=8, dim Sym2(P)=3, diagonal invariants=2, full invariants=1")
    print("    generator: D0^2*[x0^4*y] + D1^2*[x1^4*y]")
    return terms


def poly_add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def poly_mul(a, b):
    result = {}
    for u, x in a.items():
        for v, y in b.items():
            exponent = tuple(i + j for i, j in zip(u, v))
            result[exponent] = result.get(exponent, 0) + x * y
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def poly_scale(a, c):
    return {u: c * x for u, x in a.items() if c * x}


def derivative(a, variable):
    result = {}
    for u, x in a.items():
        if u[variable]:
            exponent = list(u)
            exponent[variable] -= 1
            result[tuple(exponent)] = x * u[variable]
    return result


def monomial(exponent, coefficient=1):
    return {tuple(exponent): coefficient}


def verify_covariant_specializations():
    # d2 polynomial variables x0,x1,x2,p01,p02,p12.
    f = poly_add(*(monomial([4 * int(i == j) for i in range(6)]) for j in range(3)))
    hessian = [[derivative(derivative(f, i), j) for j in range(3)] for i in range(3)]
    adjugate = [[{} for _ in range(3)] for _ in range(3)]
    for i, j in product(range(3), repeat=2):
        rows = [k for k in range(3) if k != j]
        cols = [k for k in range(3) if k != i]
        minor = poly_add(poly_mul(hessian[rows[0]][cols[0]], hessian[rows[1]][cols[1]]),
                         poly_scale(poly_mul(hessian[rows[0]][cols[1]],
                                             hessian[rows[1]][cols[0]]), -1))
        adjugate[i][j] = poly_scale(minor, (-1) ** (i + j))
    q = [monomial((0, 0, 0, 0, 0, 1)),
         monomial((0, 0, 0, 0, 1, 0), -1),
         monomial((0, 0, 0, 1, 0, 0))]
    quadratic = poly_add(*(poly_mul(poly_mul(q[i], adjugate[i][j]), q[j])
                           for i, j in product(range(3), repeat=2)))
    expected = poly_add(monomial((2, 2, 0, 2, 0, 0), 144),
                        monomial((2, 0, 2, 0, 2, 0), 144),
                        monomial((0, 2, 2, 0, 0, 2), 144))
    assert quadratic == expected
    # d1 variables x0,x1,y,D0,D1.
    b = poly_add(monomial((6, 0, 0, 0, 0)), monomial((0, 6, 0, 0, 0)))
    directions = [monomial((0, 0, 0, 1, 0)), monomial((0, 0, 0, 0, 1))]

    def directional(a):
        return poly_add(*(poly_mul(directions[i], derivative(a, i)) for i in range(2)))

    quadratic = poly_mul(monomial((0, 0, 1, 0, 0)), directional(directional(b)))
    expected = poly_add(monomial((4, 0, 1, 2, 0), 30),
                        monomial((0, 4, 1, 0, 2), 30))
    assert quadratic == expected
    print("covariants: d2 q^T adj(Hess f)q = 144*generator; d1 y*D^2(A6) = 30*generator")
    # On the cyclic Fermat directions the period theorem gives 1/8 of the
    # active two-variable Hessian determinant. The d1 y-y Hessian is 2*y.
    assert Fraction(144, 8) == 18
    assert Fraction(2 * 30, 8) == Fraction(15, 2)
    print("period-input Fermat tensors: c2=18; c1=15/2; all mixed terms vanish")


if __name__ == "__main__":
    verify_degree_two()
    verify_degree_one()
    verify_covariant_specializations()
    print("All exact character, permutation, and polynomial checks passed.")
    print("Normalization: z^2/2, and in degree one y^3/3; the period theorem is an external proof input.")

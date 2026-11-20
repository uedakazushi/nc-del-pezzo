#!/usr/bin/env python3
"""Exact certificate for the degree-two highest-active Poisson shadow.

2026-11-20 / v0.16. Standard library only; run from any working directory.
Reuses the coefficient/free-word arithmetic and De Laet central-element
certificate in verify_cubic_top.py (that module also runs its own checks).

Scope and normalization:
  h=1, [x,y]=z, U=alpha*(x^4+y^4)/4+beta*x^2*y^2;
  a=b+3, b=-2+2*beta/3, c=alpha;
  F_shadow=z^2/2+A*(x^4+y^4)/4+B*x^2*y^2.
A and B are represented by the existing engine's variables d and e.
Everything is an exact polynomial identity over Q, before specialization.
The rational formulas hold where their displayed denominators are nonzero.

This verifies coordinate identities, coprimality, the normalizer action,
the transverse Lie calculation, and the exact discriminant certificates
used in the degree-four and S4 monodromy proofs.
The passage to all lower coefficients, normalized-center torsors, and
the quotient by all equivalences is proved in the paper, not by this
finite computation. No assertion of novelty is made.
"""
from fractions import Fraction
from itertools import permutations

from verify_cubic_top import (
    NAMES, C, r1, r2, a, b, c, d, e,
    const, variable, add, mul, neg, nadd, scale, around, words,
)


def substitute(poly, replacements):
    """Simultaneous polynomial substitution in the shared exact ring."""
    result = {}
    for exponent, coefficient in poly.items():
        term = const(coefficient)
        for name, power in zip(NAMES, exponent):
            for _ in range(power):
                term = mul(term, replacements.get(name, variable(name)))
        result = add(result, term)
    return result


def degree(poly, name):
    index = NAMES.index(name)
    return max((exponent[index] for exponent in poly), default=-1)


D = words('xxxx', 'yyyy')
W1 = words('xyxy', 'yxyx')
W2 = words('yxxy', 'xyyx')
W3 = words('xxyy', 'yyxx')
S = scale(nadd(W1, W2, W3), const(Fraction(1, 6)))
z_squared = nadd(W1, scale(W2, const(-1)))
relation = scale(nadd(around(r1, '', 'x'), around(r1, 'x', ''),
                      around(r2, '', 'y'), around(r2, 'y', '')),
                 const(Fraction(1, 2)))
assert relation == nadd(scale(W1, b), scale(W2, a), scale(W3, a),
                       scale(D, c))

rho = add(a, neg(b))
kz = neg(mul(a, add(mul(b, b), neg(mul(c, c)))))
kd_numerator = mul(c, add(mul(const(2), a, a, a),
                          mul(const(-2), a, c, c), mul(b, b, b),
                          neg(mul(b, c, c))))
ks_numerator = mul(const(6), a,
                   add(mul(const(2), a, a, b), mul(a, b, b),
                       neg(mul(a, c, c)), mul(const(-2), b, c, c)))
kr_numerator = neg(add(mul(a, a, a), mul(a, a, b), mul(a, b, b),
                       neg(mul(add(mul(const(2), a), b), c, c))))
# FREE-word identity: rho*C = rho*kz*z^2 + kd_num*D + ks_num*S + kr_num*relation.
assert not nadd(scale(C, rho), scale(z_squared, neg(mul(rho, kz))),
               scale(D, neg(kd_numerator)), scale(S, neg(ks_numerator)),
               scale(relation, neg(kr_numerator)))

A, B = d, e
specialization = {'a': add(b, const(3))}
A_num = substitute(mul(const(2), kd_numerator), specialization)
A_den = substitute(mul(rho, kz), specialization)
B_num0 = substitute(ks_numerator, specialization)
B_den0 = substitute(mul(const(2), rho, kz), specialization)
B_num = mul(const(3), add(mul(add(b, const(1)), c, c),
                         neg(mul(b, add(b, const(2)), add(b, const(3))))))
B_den = add(mul(b, b), neg(mul(c, c)))
assert mul(B_num0, B_den) == mul(B_num, B_den0)
# c^2*(3b+B+3) = b*(3b^2+bB+15b+18), after substituting B=B_num/B_den.
assert mul(c, c, add(mul(add(mul(const(3), b), const(3)), B_den), B_num)) == (
    mul(b, add(mul(add(mul(const(3), b, b), mul(const(15), b), const(18)), B_den),
               mul(b, B_num))))
# A/c = 2*(bB+6b+3B+9)/(3b(b+3)), with both A,B denominators cleared.
assert mul(const(3), b, add(b, const(3)), A_num, B_den) == (
    mul(const(2), c, A_den,
        add(mul(add(b, const(3)), B_num),
            mul(add(mul(const(6), b), const(9)), B_den))))

quadratic = add(mul(const(3), b, b), mul(b, B), mul(const(15), b), const(18))
linear = add(mul(b, B), mul(const(6), b), mul(const(3), B), const(9))
N = mul(const(4), quadratic, linear, linear)
Q = mul(const(9), b, add(b, const(3)), add(b, const(3)),
        add(mul(const(3), b), B, const(3)))
R_num = mul(b, quadratic)
R_den = add(mul(const(3), b), B, const(3))
L_num = mul(const(2), linear)
L_den = mul(const(3), b, add(b, const(3)))
assert mul(N, R_den, L_den, L_den) == mul(Q, R_num, L_num, L_num)
assert degree(N, 'b') == degree(Q, 'b') == 4
# Q has the three distinct roots below over Q(B). None is a root of N.
for pole in ({}, const(-3), mul(const(Fraction(-1, 3)), add(B, const(3)))):
    assert substitute(N, {'b': pole})
assert substitute(N, {'b': {}}) == mul(const(648), add(B, const(3)), add(B, const(3)))
assert substitute(N, {'b': const(-3)}) == mul(const(-972), B)
# R(b)=b*quadratic/(3b+B+3) has a simple zero at b=0, hence is not a square.
assert substitute(quadratic, {'b': {}}) == const(18)
assert substitute(add(mul(const(3), b), B, const(3)), {'b': {}}) == add(B, const(3))


def matrix_product(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j]
                           for k in range(len(right)))
                       for j in range(len(right[0])))
                 for i in range(len(left)))


# Effective normalizer N(V_4)/V_4 on the symmetric quartic coefficient plane.
identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
reflection_t = ((Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1)))
reflection_r = ((Fraction(1, 2), Fraction(1)),
                (Fraction(3, 4), Fraction(-1, 2)))
assert matrix_product(reflection_t, reflection_t) == identity
assert matrix_product(reflection_r, reflection_r) == identity
rotation = matrix_product(reflection_t, reflection_r)
assert matrix_product(matrix_product(rotation, rotation), rotation) == identity
normalizer = {identity}
pending = [identity]
while pending:
    element = pending.pop()
    for generator in (reflection_t, reflection_r):
        new_element = matrix_product(element, generator)
        if new_element not in normalizer:
            normalizer.add(new_element)
            pending.append(new_element)
    assert len(normalizer) <= 6
assert len(normalizer) == 6

# Check f((x+y)/sqrt(2),(-x+y)/sqrt(2)) directly. All monomials have
# degree four, so the common square-root factor contributes exactly 1/4.
def binary_product(left, right):
    result = {}
    for (i, j), value in left.items():
        for (k, ell), other in right.items():
            exponent = (i + k, j + ell)
            result[exponent] = result.get(exponent, Fraction(0)) + value * other
    return {exponent: value for exponent, value in result.items() if value}


def binary_power(value, exponent):
    result = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        result = binary_product(result, value)
    return result


linear_x = {(1, 0): Fraction(1), (0, 1): Fraction(1)}
linear_y = {(1, 0): Fraction(-1), (0, 1): Fraction(1)}
x_four = binary_power(linear_x, 4)
y_four = binary_power(linear_y, 4)
mixed = binary_product(binary_power(linear_x, 2), binary_power(linear_y, 2))
alpha, beta = variable('alpha'), variable('beta')
alpha_r = add(mul(const(Fraction(1, 2)), alpha), beta)
beta_r = add(mul(const(Fraction(3, 4)), alpha), mul(const(Fraction(-1, 2)), beta))
for i in range(5):
    exponent = (i, 4 - i)
    transformed = add(
        mul(const((x_four.get(exponent, Fraction(0))
                   + y_four.get(exponent, Fraction(0))) / 16), alpha),
        mul(const(mixed.get(exponent, Fraction(0)) / 4), beta))
    expected = (mul(const(Fraction(1, 4)), alpha_r) if i in (0, 4)
                else beta_r if i == 2 else {})
    assert transformed == expected

# T acts by c -> -c, while R acts by the affine substitutions below
# because c=alpha and b=-2+2*beta/3. Verify equivariance with denominators
# cleared, so the assertion is a polynomial identity rather than sampling.
assert substitute(A_num, {'c': neg(c)}) == neg(A_num)
assert substitute(A_den, {'c': neg(c)}) == A_den
assert substitute(B_num, {'c': neg(c)}) == B_num
assert substitute(B_den, {'c': neg(c)}) == B_den
reflection_substitution = {
    'b': mul(const(Fraction(1, 2)), add(c, neg(b), const(-6))),
    'c': mul(const(Fraction(1, 2)), add(c, mul(const(3), b), const(6))),
}
an, ad, bn, bd = [substitute(poly, reflection_substitution)
                  for poly in (A_num, A_den, B_num, B_den)]
assert mul(an, const(2), A_den, B_den) == (
    mul(ad, add(mul(A_num, B_den), mul(const(2), B_num, A_den))))
assert mul(bn, const(4), A_den, B_den) == (
    mul(bd, add(mul(const(3), A_num, B_den), mul(const(-2), B_num, A_den))))

# Columns: the two slice directions, followed by H,E,F in sl_2.
# Rows: x^4,x^3*y,x^2*y^2,x*y^3,y^4.
zero, one = {}, const(1)
quarter = const(Fraction(1, 4))
lie_matrix = [
    [quarter, zero, alpha, zero, zero],
    [zero, zero, zero, mul(const(2), beta), alpha],
    [zero, one, zero, zero, zero],
    [zero, zero, zero, alpha, mul(const(2), beta)],
    [quarter, zero, neg(alpha), zero, zero],
]
determinant = {}
for permutation in permutations(range(5)):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(5) for j in range(i + 1, 5))
    term = const((-1) ** inversions)
    for row, column in enumerate(permutation):
        term = mul(term, lie_matrix[row][column])
    determinant = add(determinant, term)
assert determinant == mul(const(Fraction(1, 2)), alpha,
                          add(mul(const(4), beta, beta), neg(mul(alpha, alpha))))

print('PASS: De Laet quartic -> fully symmetrized coordinates, exact free-word identity.')
print('PASS: normalized shadow coefficients and both inverse identities, all denominators cleared.')
print('PASS: A^2=N(b,B)/Q(b,B), deg_b N=deg_b Q=4, gcd over Q(B) equals 1.')
print('PASS: c^2=R(b,B) has odd valuation at b=0; supports the degree-four field-tower proof.')
print('PASS: binary quartic normalizer reflections, faithful S3 action, and exact shadow equivariance.')
print('PASS: slice plus Lie orbit determinant = alpha*(4*beta^2-alpha^2)/2.')
print('Scope: exact coefficient certificates; torsor, lower-term, and full moduli arguments are in the paper.')


def power(poly, exponent):
    result = const(1)
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def coefficients(poly, name):
    """Highest coefficient first, with the chosen variable removed."""
    index = NAMES.index(name)
    highest = max((e[index] for e in poly), default=-1)
    result = [{} for _ in range(highest + 1)]
    for exponent, coefficient in poly.items():
        exp = list(exponent)
        value = exp[index]
        exp[index] = 0
        result[highest-value][tuple(exp)] = coefficient
    return result


def derivative(poly, name):
    index = NAMES.index(name)
    result = {}
    for exponent, coefficient in poly.items():
        if exponent[index]:
            exp = list(exponent)
            degree = exp[index]
            exp[index] -= 1
            result[tuple(exp)] = coefficient * degree
    return result


def determinant_dp(matrix):
    """Division-free determinant by subsets; exact coefficient arithmetic."""
    size = len(matrix)
    values = {0: const(1)}
    for row in range(size):
        new_values = {}
        for mask, value in values.items():
            for column in range(size):
                if mask & (1 << column) or not matrix[row][column]:
                    continue
                inversions = (mask >> (column + 1)).bit_count()
                term = mul(value, matrix[row][column], const((-1)**inversions))
                new_mask = mask | (1 << column)
                new_values[new_mask] = add(new_values.get(new_mask, {}), term)
        values = new_values
    return values.get((1 << size) - 1, {})


def resultant(left, right, name):
    f, g = coefficients(left, name), coefficients(right, name)
    m, n = len(f)-1, len(g)-1
    matrix = [[{} for _ in range(m+n)] for _ in range(m+n)]
    for shift in range(n):
        matrix[shift][shift:shift+m+1] = f
    for shift in range(m):
        matrix[n+shift][shift:shift+n+1] = g
    return determinant_dp(matrix)


F = add(mul(A, A, Q), neg(N))
u = mul(const(Fraction(1, 12)),
        add(mul(const(3), A, A), mul(const(4), B, B)))
v = mul(const(Fraction(1, 108)), B,
        add(mul(const(9), A, A), mul(const(-4), B, B)))
disc_invariant = add(
    mul(add(const(1), mul(const(-8), v)), power(u, 3)),
    mul(const(3), power(add(mul(const(2), v), const(-1)), 2), u, u),
    mul(add(mul(const(-6), power(v, 3)), mul(const(153), v, v),
            mul(const(216), v), const(-24)), u),
    power(v, 4), mul(const(-104), power(v, 3)),
    mul(const(-615), v, v), mul(const(-266), v), const(1))
disc = mul(const(944784*136048896), A, A,
           add(B, const(3)), add(B, const(3)), disc_invariant)
leading = coefficients(F, 'b')[0]
# For a quartic, Res(F,F') = leading(F) * Disc(F).
assert resultant(F, derivative(F, 'b'), 'b') == mul(leading, disc)

reflection = {
    'd': add(mul(const(Fraction(1, 2)), A), B),
    'e': add(mul(const(Fraction(3, 4)), A),
             mul(const(Fraction(-1, 2)), B)),
}
assert substitute(u, reflection) == u
assert substitute(v, reflection) == v
assert substitute(disc_invariant, reflection) == disc_invariant

H = add(mul(const(820125), power(A, 8)),
        mul(const(-17781768), power(A, 6)),
        mul(const(-68102208), power(A, 4)),
        mul(const(2738419200), A, A), const(20480000))
assert substitute(disc, {'e': const(1)}) == mul(const(-15116544), A, A, H)
bezout_u = add(mul(const(-2), power(A, 6)),
               mul(const(-4), power(A, 4)), const(-5))
bezout_v = add(mul(const(3), power(A, 7)),
               mul(const(2), power(A, 5)), mul(const(2), power(A, 3)),
               mul(const(5), A))
bezout = add(mul(bezout_u, H), mul(bezout_v, derivative(H, 'd')), const(-1))
assert all(value.denominator == 1 and value.numerator % 11 == 0
           for value in bezout.values())
assert 820125 % 11 != 0
index_A = NAMES.index('d')
assert all(e[index_A] % 2 == 0 for e in H)
at_leading_zero = sum(value * Fraction(196, 9)**(e[index_A]//2)
                      for e, value in H.items())
assert at_leading_zero == 28171411200
assert substitute(H, {'d': {}}) == const(20480000)

quadratic = add(mul(const(3), b, b), mul(const(16), b), const(18))
assert 16**2 - 4*3*18 == 40
assert substitute(quadratic, {'b': {}}) == const(18)
assert substitute(quadratic, {'b': const(Fraction(-4, 3))}) == const(2)
assert substitute(quadratic, {'b': const(-3)}) == const(-3)
branch_quartic = mul(b, add(mul(const(3), b), const(4)), quadratic)
assert substitute(branch_quartic, {'b': const(-3)}) == const(-45)
# A=2(7b+12)w/[3b(b+3)(3b+4)], w^2=branch_quartic.
num_squared = mul(const(4), power(add(mul(const(7), b), const(12)), 2),
                  branch_quartic)
den_squared = mul(const(9), b, b, power(add(b, const(3)), 2),
                  power(add(mul(const(3), b), const(4)), 2))
assert mul(num_squared, substitute(Q, {'e': const(1)})) == (
    mul(den_squared, substitute(N, {'e': const(1)})))

print('PASS: full quartic discriminant, computed by a division-free Sylvester determinant.')
print('PASS: compact invariant discriminant and exact normalizer invariance.')
print('PASS: B=1 degree-eight branch polynomial, mod 11 Bezout certificate, leading coprimality.')
print('PASS: connected genus-one witness curve identities and distinct branch factors.')
print('Scope: exact identities; genus, ramification, S4 monodromy and descent are proved in the paper.')

# The anti-invariant needed for descent of the orientation double cover.
p_orientation = mul(A, add(mul(A, A), mul(const(-4), B, B)))
delta_quartic = add(power(u, 3), mul(const(-27), v, v))
assert mul(p_orientation, p_orientation) == mul(const(64), delta_quartic)
assert substitute(p_orientation, reflection) == neg(p_orientation)
assert substitute(p_orientation, {'d': neg(A)}) == neg(p_orientation)
assert 11337408**2 == 944784*136048896
for value, expected in [(Fraction(0), Fraction(-10368)),
                        (Fraction(-3), Fraction(972)),
                        (Fraction(-4, 3), Fraction(-512, 9))]:
    assert substitute(F, {'e': const(1), 'b': const(value)}) == const(expected)
print('PASS: normalizer anti-invariant, orientation square class, and smooth branch-plane witnesses.')

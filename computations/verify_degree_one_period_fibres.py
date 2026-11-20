#!/usr/bin/env python3
"""Exact nonconstancy certificate for point-curve j on a degree-five shadow fibre.

Standard-library polynomial arithmetic over Q only. The categorical use of
this certificate requires an intrinsic elliptic invariant of the residual
category, separately established in the geometric argument.
"""

import contextlib
import io
from fractions import Fraction
from math import gcd, lcm

with contextlib.redirect_stdout(io.StringIO()):
    import verify_degree_one_period_quadratic as quadratic

p, curve = quadratic.p, quadratic.curve
add, neg, mul, power = p.add, p.minus, p.multiply, p.power
constant, variable, sub = p.constant, p.variable, p.substitute
coefficient = quadratic.coefficient


def trim(a):
    a = [Fraction(x) for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def uadd(*polynomials):
    out = [Fraction(0)] * max((len(a) for a in polynomials), default=0)
    for a in polynomials:
        for i, x in enumerate(a):
            out[i] += x
    return trim(out)


def uscale(a, c):
    return trim([c * x for x in a])


def umul(a, b):
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def upower(a, exponent):
    out = [Fraction(1)]
    for _ in range(exponent):
        out = umul(out, a)
    return out


def udivmod(a, b):
    a, b = trim(a), trim(b)
    assert b
    q = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        offset, c = len(a) - len(b), a[-1] / b[-1]
        q[offset] += c
        for i, x in enumerate(b):
            a[offset + i] -= c * x
        a = trim(a)
    return trim(q), a


def ugcd(a, b):
    while b:
        a, b = b, udivmod(a, b)[1]
    return uscale(a, 1 / a[-1]) if a else []


def primitive(a):
    a = trim(a)
    denominator = lcm(*(x.denominator for x in a))
    integers = [int(x * denominator) for x in a]
    content = gcd(*integers)
    if integers[-1] < 0:
        content = -content
    return [x // content for x in integers]


# Compute the complete quartic at h=1 and descend k^2=-alpha.
k, beta = variable('k'), variable('c')
H = sub(sub(curve.H, curve.params), {
    'h': constant(1),
    'b': add(mul(constant(6), beta), mul(constant(-4), power(k, 3))),
})
aq, bq, cq = (coefficient(H, 'q', i) for i in (2, 1, 0))
R = mul(constant(Fraction(-1, 12)), add(power(bq, 2), mul(constant(-4), aq, cq)))
a, b, c, d, e = (coefficient(R, 't', i) for i in (4, 3, 2, 1, 0))
I = add(mul(constant(12), a, e), mul(constant(-3), b, d), power(c, 2))
J = add(mul(constant(72), a, c, e), mul(constant(9), b, c, d),
        mul(constant(-27), a, power(d, 2)), mul(constant(-27), power(b, 2), e),
        mul(constant(-2), power(c, 3)))


def descend(polynomial, scale):
    out = {}
    ki, bi = p.NAMES.index('k'), p.NAMES.index('c')
    for exponent, value in polynomial.items():
        assert all(not x for i, x in enumerate(exponent) if i not in (ki, bi))
        assert exponent[ki] % 2 == 0
        alpha_degree, beta_degree = exponent[ki] // 2, exponent[bi]
        value *= scale * (-1) ** alpha_degree
        assert value.denominator == 1
        out[alpha_degree, beta_degree] = int(value)
    return out


bar_I, bar_J = descend(I, 9), descend(J, 27)
assert len(bar_I) == 18 and len(bar_J) == 35

# I_shadow=J_shadow=-5 has source alpha=0,beta=1.
# beta(T)=(-12 T^3-35 T^2+30 T+75)/(30 T+75).
beta_num, beta_den = trim([75, 30, -35, -12]), trim([75, 30])
T = trim([0, 1])
F = trim([0, -1125, -1025, 120, 340, 112])
assert ugcd(F, beta_den) == [Fraction(1)]
assert ugcd(F, trim([F[i] * i for i in range(1, len(F))])) == [Fraction(1)]


def substitute_beta(polynomial, max_beta_degree):
    terms = []
    for (i, j), value in polynomial.items():
        terms.append(uscale(umul(upower(T, i), umul(upower(beta_num, j),
                          upower(beta_den, max_beta_degree - j))), value))
    return uadd(*terms)


def centre_bivariate(polynomial):
    ai, bi = p.NAMES.index('a'), p.NAMES.index('b')
    out = {}
    for exponent, value in polynomial.items():
        assert all(not x for i, x in enumerate(exponent) if i not in (ai, bi))
        out[exponent[ai], exponent[bi]] = value
    return out


# Independently check that the stated beta(T) and quintic give the claimed
# shadow fibre using the original central coefficients and depression.
cN = substitute_beta(centre_bivariate(quadratic.c_num), 1)
cD = umul(substitute_beta(centre_bivariate(quadratic.c_den), 0), beta_den)
dN = substitute_beta(centre_bivariate(quadratic.d_num), 2)
dD = umul(substitute_beta(centre_bivariate(quadratic.d_den), 0), upower(beta_den, 2))
assert uadd(cN, umul(uadd([5], uscale(upower(T, 2), -4)), cD)) == []
shadow_J_plus_five = uadd(umul(dN, cD), uscale(umul(T, umul(cN, dD)), 2),
    umul(uadd([5], uscale(upower(T, 3), Fraction(-16, 3))), umul(cD, dD)))
assert udivmod(shadow_J_plus_five, F)[1] == []

I_num = substitute_beta(bar_I, 4)
J_num = substitute_beta(bar_J, 6)
I_mod, J_mod = (udivmod(g, F)[1] for g in (I_num, J_num))
I_cube, J_square = (udivmod(g, F)[1] for g in (upower(I_mod, 3), upower(J_mod, 2)))
j_num = uscale(I_cube, 6912)
j_den = uadd(uscale(I_cube, 4), uscale(J_square, -1))
assert ugcd(F, j_den) == [Fraction(1)]
j_at_zero = Fraction(j_num[0], j_den[0])
assert j_at_zero == Fraction(1022208, 3125)
same_j_numerator = uadd(uscale(j_num, j_at_zero.denominator),
                       uscale(j_den, -j_at_zero.numerator))
assert ugcd(F, same_j_numerator) == T

# Small exact reduction certificate.  Q-gcd above is independently checked;
# this mod-101 Euclidean chain is included as a readable witness.
same_primitive = primitive(same_j_numerator)
prime = 101
same_mod = [(x * pow(same_primitive[-1], -1, prime)) % prime for x in same_primitive]
assert same_mod == [0, 18, 46, 31, 1]
F_mod = [int(x) % prime for x in F]
assert F_mod == [0, 87, 86, 19, 37, 11]
quartic_mod, cubic_mod = F_mod[1:], same_mod[1:]
quadratic_mod, linear_mod = [4, 35, 49], [17, 82]


def equal_mod(a, b):
    return all(int(x) % prime == 0 for x in uadd(a, uscale(b, -1)))


assert equal_mod(quartic_mod, uadd(umul([100, 11], cubic_mod), quadratic_mod))
assert equal_mod(cubic_mod, uadd(umul([76, 33], quadratic_mod), linear_mod))
assert (82 * 70 + 17) % prime == 0
assert (49 * 70 ** 2 + 35 * 70 + 4) % prime == 53

# All ordinary denominator factors used in the centre and depression are units.
for denominator in ([1, 1], [5, 1], [5, 2], [9, 1]):
    assert ugcd(F, trim(denominator)) == [Fraction(1)]

print('PASS: complete point-curve invariants descend from k to alpha=-k^2')
print('PASS: j_E=6912*bar_I^3/(4*bar_I^3-bar_J^2), bar_I=9I, bar_J=27J')
print('Witness: I_shadow=J_shadow=-5, alpha0=0, beta0=1')
print('PASS: original centre formula and depression give this fibre after substitution')
print('F(T)=T*(112*T^4+340*T^3+120*T^2-1025*T-1125), squarefree')
print('j_E(alpha0)=1022208/3125')
print('PASS: every required denominator and elliptic discriminant is coprime to F')
print('mod 101: F/T=11*T^4+37*T^3+19*T^2+86*T+87')
print('mod 101: normalized equal-j remainder/T=T^3+31*T^2+46*T+18')
print('mod 101 Euclidean remainders: 49*T^2+35*T+4, 82*T+17, 53')
print('PASS: gcd(F,numerator(j_E(T)-1022208/3125))=T')
print('The point-curve j-invariant is not constant on the generic degree-five shadow fibre.')
print('Since the extension has prime degree 5, j_E generates it and generically separates all five branches.')
print('This calculation alone does not prove that unmarked Kuznetsov components differ.')

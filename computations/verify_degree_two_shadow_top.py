#!/usr/bin/env python3
"""Exact certificate for the degree-two highest-active Poisson shadow.

2026-11-20 / v0.14. Standard library only; run from any working directory.
Reuses the coefficient/free-word arithmetic and De Laet central-element
certificate in verify_cubic_top.py (that module also runs its own checks).

Scope and normalization:
  h=1, [x,y]=z, U=alpha*(x^4+y^4)/4+beta*x^2*y^2;
  a=b+3, b=-2+2*beta/3, c=alpha;
  F_shadow=z^2/2+A*(x^4+y^4)/4+B*x^2*y^2.
A and B are represented by the existing engine's variables d and e.
Everything is an exact polynomial identity over Q, before specialization.
The rational formulas hold where their displayed denominators are nonzero.

This proves the coordinate identities and the coprimality used in the
function-field degree-four argument for this TWO-COEFFICIENT TOP FAMILY.
It does not compute the degree of the full moduli morphism: lower active
coefficients, membership in the common nc open, and all equivalences must
still be considered. No assertion of novelty is made.
"""
from fractions import Fraction

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

print('PASS: De Laet quartic -> fully symmetrized coordinates, exact free-word identity.')
print('PASS: normalized shadow coefficients and both inverse identities, all denominators cleared.')
print('PASS: A^2=N(b,B)/Q(b,B), deg_b N=deg_b Q=4, gcd over Q(B) equals 1.')
print('PASS: c^2=R(b,B) has odd valuation at b=0; supports the degree-four field-tower proof.')
print('Scope: fixed h=1, symmetric two-coefficient highest-active quartic; full moduli degree unresolved.')

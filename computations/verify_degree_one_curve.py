#!/usr/bin/env python3
"""Exact certificates for the relative degree-one elliptic point curve.

Only the Python standard library is required. All identities are checked in
polynomial rings over Q, without numerical sampling. The explicitly marked
last calculation is a first-order h-jet used to detect sigma^6 != identity.
Smoothness, Cartier divisors, THCR comparison and Noetherianity use the
geometric proofs in elliptic_degree_one_relative.tex, not finite testing.
"""
from fractions import Fraction


NAMES = ('a', 'b', 'c', 'k', 'rho', 'h', 'w0', 'z0', 'w1', 'z1',
         't', 'q', 'w', 'u', 'v', 'eta')
ZERO = (0,) * len(NAMES)


def constant(value):
    return {ZERO: Fraction(value)} if value else {}


def variable(name):
    exponent = [0] * len(NAMES)
    exponent[NAMES.index(name)] = 1
    return {tuple(exponent): Fraction(1)}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for exponent, value in polynomial.items():
            out[exponent] = out.get(exponent, Fraction(0)) + value
    return {exponent: value for exponent, value in out.items() if value}


def minus(polynomial):
    return {exponent: -value for exponent, value in polynomial.items()}


def multiply(*polynomials):
    out = constant(1)
    for polynomial in polynomials:
        nxt = {}
        for exponent, value in out.items():
            for other, coefficient in polynomial.items():
                total = tuple(x + y for x, y in zip(exponent, other))
                nxt[total] = nxt.get(total, Fraction(0)) + value * coefficient
        out = {exponent: value for exponent, value in nxt.items() if value}
    return out


def power(polynomial, exponent):
    return multiply(*([polynomial] * exponent))


def substitute(polynomial, substitutions):
    """Simultaneous polynomial substitution, without recursive substitution."""
    out = {}
    for exponent, value in polynomial.items():
        term = constant(value)
        for name, degree in zip(NAMES, exponent):
            term = multiply(term, power(substitutions.get(name, variable(name)),
                                        degree))
        out = add(out, term)
    return out


def divide_h(polynomial, exponent):
    """Exact polynomial division, asserting h-divisibility term by term."""
    index = NAMES.index('h')
    out = {}
    for monomial, value in polynomial.items():
        assert monomial[index] >= exponent
        quotient = list(monomial)
        quotient[index] -= exponent
        out[tuple(quotient)] = value
    return out


def mod_h(polynomial, order):
    index = NAMES.index('h')
    return {exponent: value for exponent, value in polynomial.items()
            if exponent[index] < order}


a, b, c, k, rho, h, w0, z0, w1, z1, t, q, w, u, v, eta = (
    variable(name) for name in NAMES)
one = constant(1)
C = add(power(a, 2), minus(power(c, 2)))
ac = add(a, c)
parameters = {'a': add(one, multiply(k, power(h, 2))),
              'b': multiply(rho, power(h, 2)), 'c': constant(-2)}

# H = det(M)/c is the negative of Stephenson's equation (2.1.9).
H = add(
    multiply(a, C, add(power(t, 2), power(q, 2))),
    multiply(a, b, ac, add(multiply(power(t, 2), q),
                           multiply(t, power(q, 2)))),
    multiply(add(multiply(power(a, 2), c), minus(power(b, 3)),
                 minus(power(c, 3))), t, q),
    minus(multiply(a, power(b, 2), add(t, q))),
    minus(multiply(power(a, 2), b)))
assert substitute(H, {'t': q, 'q': t}) == H

# Bihomogenize H to degree (2,2) in (w0:z0),(w1:z1).
H_hom = {}
ti, qi = NAMES.index('t'), NAMES.index('q')
for exponent, coefficient in H.items():
    i, j = exponent[ti], exponent[qi]
    assert i <= 2 and j <= 2
    residual = list(exponent)
    residual[ti] = residual[qi] = 0
    H_hom = add(H_hom, multiply({tuple(residual): coefficient},
                               power(w0, 2-i), power(z0, i),
                               power(w1, 2-j), power(z1, j)))
M11 = add(multiply(c, w0, z1), multiply(a, z0, w1))
M12 = multiply(add(multiply(a, w0), multiply(b, z0)), w1)
M21 = add(multiply(a, b, c, w0, w1),
          multiply(power(b, 2), c, w0, z1), multiply(a, C, z0, z1))
M22 = add(multiply(c, C, z0, w1), multiply(a, b, ac, z0, z1),
          multiply(a, C, w0, z1))
assert add(multiply(M11, M22), minus(multiply(M12, M21))) == multiply(c, H_hom)
delta = add(multiply(w0, z1), minus(multiply(z0, w1)))
H_special_parameters = substitute(H_hom, parameters)
assert mod_h(H_special_parameters, 1) == multiply(constant(-3), power(delta, 2))
divide_h(add(H_special_parameters, multiply(constant(3), power(delta, 2))), 2)

# The finite h-chart and the chart at infinity both divide by h^2 exactly.
G = divide_h(substitute(substitute(H, parameters),
                         {'q': add(t, multiply(h, w))}), 2)
G0 = add(multiply(constant(-3), power(w, 2)),
         multiply(constant(-6), k, power(t, 2)),
         multiply(constant(-2), rho, power(t, 3)), minus(rho))
assert mod_h(G, 1) == G0
H_infinity = substitute(H_hom, {'w0': u, 'z0': one, 'w1': v, 'z1': one})
G_infinity = divide_h(substitute(substitute(H_infinity, parameters),
                                  {'v': add(u, multiply(h, eta))}), 2)
G_infinity0 = add(multiply(constant(-3), power(eta, 2)),
                  multiply(constant(-6), k, power(u, 2)),
                  multiply(constant(-2), rho, u),
                  minus(multiply(rho, power(u, 4))))
assert mod_h(G_infinity, 1) == G_infinity0
infinity_divisor = substitute(multiply(a, ac, eta,
    add(multiply(add(a, minus(c)), eta), multiply(rho, h))), parameters)
assert substitute(G_infinity, {'u': {}}) == infinity_divisor

# Exact agreement with the original classical Weierstrass equation.
y_classical, z_classical = add(multiply(rho, t), k), multiply(rho, w)
beta_classical = multiply(constant(Fraction(1, 6)),
                         add(power(rho, 3), multiply(constant(4), power(k, 3))))
F_classical = add(multiply(constant(Fraction(1, 2)), power(z_classical, 2)),
                  multiply(constant(Fraction(1, 3)), power(y_classical, 3)),
                  minus(multiply(power(k, 2), y_classical)), beta_classical)
assert multiply(constant(6), F_classical) == minus(multiply(power(rho, 2), G0))
discriminant = add(multiply(constant(-4), power(k, 6)),
                   multiply(constant(9), power(beta_classical, 2)))
assert discriminant == multiply(constant(Fraction(1, 4)), power(rho, 3),
                                add(power(rho, 3), multiply(constant(8), power(k, 3))))

# sigma(t,q)=(q,r), r=R/D. The first identity certifies preservation of H.
D = add(a, multiply(b, t))
R = minus(add(multiply(c, q), multiply(a, t)))
shift_H_cleared = add(
    multiply(a, C, add(multiply(power(q, 2), power(D, 2)), power(R, 2))),
    multiply(a, b, ac, add(multiply(power(q, 2), R, D),
                           multiply(q, power(R, 2)))),
    multiply(add(multiply(power(a, 2), c), minus(power(b, 3)),
                 minus(power(c, 3))), q, R, D),
    minus(multiply(a, power(b, 2), add(multiply(q, power(D, 2)), multiply(R, D)))),
    minus(multiply(power(a, 2), b, power(D, 2))))
assert shift_H_cleared == multiply(add(power(a, 2), minus(multiply(b, c, q))), H)

# The outer symmetry gives the inverse shift. Write s=Snum/[D*(a+bq)].
assert add(multiply(add(multiply(a, D), multiply(b, R)), t),
           multiply(c, q, D), multiply(a, R)) == {}
D_next = add(a, multiply(b, q))
Snum = minus(add(multiply(c, R), multiply(a, q, D)))
relation5_cleared = add(multiply(a, t, R, D_next), multiply(a, q, Snum),
                        multiply(c, t, Snum), multiply(b, D, D_next))
assert relation5_cleared == minus(H)

# Q=(infinity,infinity), P=(infinity,(b:c-a)); sigma(Q)=P.
assert substitute(H_hom, {'w0': {}, 'z0': one, 'w1': {}, 'z1': one}) == {}
assert substitute(H_hom, {'w0': {}, 'z0': one,
                          'w1': b, 'z1': add(c, minus(a))}) == {}
assert add(multiply(a, C, b), multiply(a, b, ac, add(c, minus(a)))) == {}

# The lifted w-component is regular and its numerator is exact.
W = add(w, minus(multiply(h, add(multiply(k, add(t, q)), multiply(rho, t, q)))))
chart = {'q': add(t, multiply(h, w))}
assert substitute(substitute(add(R, minus(multiply(q, D))), parameters), chart) == (
    multiply(h, substitute(W, chart)))
assert mod_h(substitute(substitute(D, parameters), chart), 2) == one

# First-order certificate only: six shifts cannot be the generic identity.
drift = add(multiply(constant(2), k, t), multiply(rho, power(t, 2)))
jet = {'t': add(t, multiply(h, w)), 'w': add(w, minus(multiply(h, drift)))}
assert mod_h(substitute(W, chart), 2) == jet['w']
sixfold_t, sixfold_w = t, w
for _ in range(6):
    sixfold_t = mod_h(substitute(sixfold_t, jet), 2)
    sixfold_w = mod_h(substitute(sixfold_w, jet), 2)
assert sixfold_t == add(t, multiply(constant(6), h, w))
assert sixfold_w == add(w, minus(multiply(constant(6), h, drift)))
dG_dt = add(multiply(constant(-12), k, t), multiply(constant(-6), rho, power(t, 2)))
dG_dw = multiply(constant(-6), w)
assert add(multiply(dG_dt, w), minus(multiply(dG_dw, drift))) == {}

print('PASS: point-curve determinant and double-diagonal specialization')
print('PASS: both exact blowup charts, Weierstrass equation and infinity divisor')
print('PASS: cleared shift, inverse and degree-five relation identities')
print('PASS: distinguished sections P,Q and the kernel identity sigma(Q)=P')
print('PASS: exact lifted shift and first-order sixfold nontriviality')
print('Polynomial arithmetic over Q; only the final shift jet is modulo h^2')

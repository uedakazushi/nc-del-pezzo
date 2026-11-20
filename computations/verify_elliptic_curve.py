#!/usr/bin/env python3
"""Exact identities for the relative elliptic point curve and its shift.

Standard library only. Polynomial identities hold over Q with independent
parameters; no numerical sampling is used. The final, explicitly first-order
check detects that sigma^4 is not generically the identity. Smoothness,
relative THCR identification and Noetherianity are proved in the manuscript,
not inferred from these finite calculations.
"""
from fractions import Fraction


NAMES = ('a', 'b', 'c', 'alpha', 'beta', 'h',
         'u', 'v', 'U', 'V', 't', 's', 'w')
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


def minus(polynomial):
    return {exponent: -value for exponent, value in polynomial.items()}


def square(polynomial):
    return multiply(polynomial, polynomial)


def substitute(polynomial, substitutions):
    """Simultaneous substitution into the fixed ambient polynomial ring."""
    out = {}
    for exponent, value in polynomial.items():
        term = constant(value)
        for name, power in zip(NAMES, exponent):
            factor = substitutions.get(name, variable(name))
            for _ in range(power):
                term = multiply(term, factor)
        out = add(out, term)
    return out


def mod_h(polynomial, order):
    index = NAMES.index('h')
    return {exponent: value for exponent, value in polynomial.items()
            if exponent[index] < order}


a, b, c, alpha, beta, h, u, v, U, V, t, s, w = (
    variable(name) for name in NAMES)
one, two = constant(1), constant(2)
parameters = {
    'a': add(one, multiply(constant(Fraction(2, 3)), beta, square(h))),
    'b': add(constant(-2),
             multiply(constant(Fraction(2, 3)), beta, square(h))),
    'c': multiply(alpha, square(h)),
}

# The two multilinearized cubic relations form a 2-by-2 matrix in the
# coordinates of the third point. Its determinant is the (2,2) point curve.
matrix = (
    (add(multiply(a, v, V), multiply(c, u, U)),
     add(multiply(a, u, V), multiply(b, v, U))),
    (add(multiply(a, v, U), multiply(b, u, V)),
     add(multiply(a, u, U), multiply(c, v, V))),
)
determinant = add(multiply(matrix[0][0], matrix[1][1]),
                  minus(multiply(matrix[0][1], matrix[1][0])))
H = add(multiply(a, c, add(multiply(square(u), square(U)),
                           multiply(square(v), square(V)))),
        minus(multiply(a, b, add(multiply(square(u), square(V)),
                                 multiply(square(v), square(U))))),
        multiply(add(square(c), minus(square(b))), u, v, U, V))
assert determinant == H

delta = add(multiply(u, V), minus(multiply(v, U)))
Q = add(multiply(alpha, a, add(multiply(square(u), square(U)),
                               multiply(square(v), square(V)))),
        multiply(add(multiply(square(alpha), square(h)),
                     minus(multiply(two, beta, b))), u, v, U, V))
assert substitute(H, parameters) == substitute(
    add(minus(multiply(a, b, square(delta))), multiply(square(h), Q)),
    parameters)

# In the h-chart of Bl_(h,delta), u=U=1 and s=t+h*w.
affine = {'u': one, 'v': t, 'U': one, 'V': s}
H_affine = substitute(H, affine)
G = add(minus(multiply(a, b, square(w))), substitute(Q, affine))
chart = {'s': add(t, multiply(h, w))}
assert substitute(substitute(H_affine, parameters), chart) == multiply(
    square(h), substitute(substitute(G, parameters), chart))
G0 = add(multiply(two, square(w)),
         multiply(alpha, add(one, square(square(t)))),
         multiply(constant(4), beta, square(t)))
assert mod_h(substitute(substitute(G, parameters), chart), 1) == G0

# sigma(t,s)=(s,r), r=R/D. Check the point-curve identity with denominators
# cleared before specialization, over Q[a,b,c,t,s].
D = add(a, multiply(c, t, s))
R = minus(add(multiply(a, t), multiply(b, s)))
H_shift_cleared = add(
    multiply(a, c, add(square(D), multiply(square(s), square(R)))),
    minus(multiply(a, b, add(multiply(square(s), square(D)), square(R)))),
    multiply(add(square(c), minus(square(b))), s, R, D))
assert H_shift_cleared == multiply(
    add(square(a), minus(multiply(b, c, square(s)))), H_affine)

# On the blowup, w'=(r-s)/h has this regular numerator; no h inverse is
# introduced. D is 1 on h=0 in this chart.
W = add(multiply(a, w),
        minus(multiply(h, add(multiply(two, beta, s),
                              multiply(alpha, t, square(s))))))
assert substitute(substitute(add(R, minus(multiply(s, D))), parameters), chart) == (
    multiply(h, substitute(substitute(W, parameters), chart)))
assert mod_h(substitute(substitute(D, parameters), chart), 2) == one

# The exact identities yield the following first-order jet. Fourfold
# composition gives t -> t+4*h*w modulo h^2. w is not zero on G0=0.
drift = add(multiply(two, beta, t), multiply(alpha, t, square(t)))
jet = {'t': add(t, multiply(h, w)),
       'w': add(w, minus(multiply(h, drift)))}
assert mod_h(substitute(substitute(W, parameters), chart), 2) == jet['w']
fourfold_t, fourfold_w = t, w
for _ in range(4):
    fourfold_t = mod_h(substitute(fourfold_t, jet), 2)
    fourfold_w = mod_h(substitute(fourfold_w, jet), 2)
assert fourfold_t == add(t, multiply(constant(4), h, w))
assert fourfold_w == add(w, minus(multiply(constant(4), h, drift)))

# The infinitesimal shift is tangent to the classical elliptic curve.
dG_dt = add(multiply(constant(4), alpha, t, square(t)),
             multiply(constant(8), beta, t))
dG_dw = multiply(constant(4), w)
assert add(multiply(dG_dt, w), minus(multiply(dG_dw, drift))) == {}

print('PASS: multilinear cubic determinant and exact blowup equation')
print('PASS: classical elliptic equation and regular lifted shift')
print('PASS: exact point-curve shift identity with denominators cleared')
print('PASS: first-order fourfold shift and tangent vector field')
print('Exact polynomial arithmetic over Q; final shift check is modulo h^2')

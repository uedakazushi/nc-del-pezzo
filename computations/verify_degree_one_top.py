#!/usr/bin/env python3
"""Exact identities for the degree-one Weierstrass / Stephenson top.

Standard library only. All identities are checked in a free algebra over
Q[h,k,rho], with alpha=-k^2 and beta=(rho^3+4k^3)/6. This parametrizes the
finite cover used in the manuscript. The checks verify signs, scales and
denominators; AS regularity and universal flatness use the cited theorems.
"""
from fractions import Fraction as F


NAMES = ('h', 'k', 'rho')
ZERO = (0,) * len(NAMES)


def constant(value):
    return {ZERO: F(value)} if value else {}


def variable(name):
    exponent = [0] * len(NAMES)
    exponent[NAMES.index(name)] = 1
    return {tuple(exponent): F(1)}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for exponent, value in polynomial.items():
            out[exponent] = out.get(exponent, F(0)) + value
    return {exponent: value for exponent, value in out.items() if value}


def multiply(*polynomials):
    out = constant(1)
    for polynomial in polynomials:
        nxt = {}
        for exponent, value in out.items():
            for other, coefficient in polynomial.items():
                total = tuple(x + y for x, y in zip(exponent, other))
                nxt[total] = nxt.get(total, F(0)) + value * coefficient
        out = {exponent: value for exponent, value in nxt.items() if value}
    return out


def power(polynomial, exponent):
    return multiply(*(polynomial for _ in range(exponent)))


def minus(polynomial):
    return {exponent: -value for exponent, value in polynomial.items()}


def nadd(*polynomials):
    out = {}
    for polynomial in polynomials:
        for word, coefficient in polynomial.items():
            out[word] = add(out.get(word, {}), coefficient)
    return {word: coefficient for word, coefficient in out.items()
            if coefficient}


def scale(polynomial, coefficient):
    return {word: value for word, old in polynomial.items()
            if (value := multiply(old, coefficient))}


def nmultiply(*polynomials):
    out = {'': constant(1)}
    for polynomial in polynomials:
        out = nadd(*({u + v: multiply(a, b)}
                     for u, a in out.items()
                     for v, b in polynomial.items()))
    return out


def words(*monomials):
    return nadd(*({word: constant(1)} for word in monomials))


def commutator(left, right):
    return nadd(nmultiply(left, right),
                scale(nmultiply(right, left), constant(-1)))


def cyclic(polynomial):
    return nadd(*({min(word[i:] + word[:i] for i in range(len(word))): c}
                  if word else {'': c}
                  for word, c in polynomial.items()))


def derivative(polynomial, letter):
    return nadd(*({word[i + 1:] + word[:i]: c}
                  for word, c in polynomial.items()
                  for i, char in enumerate(word) if char == letter))


def change_y(polynomial, replacement):
    return nadd(*(scale(nmultiply(*(replacement if char == 'y' else words(char)
                                   for char in word)), coefficient)
                  for word, coefficient in polynomial.items()))


h, k, rho = (variable(name) for name in NAMES)
h2, k3, rho2 = power(h, 2), power(k, 3), power(rho, 2)
alpha = minus(power(k, 2))
beta = multiply(constant(F(1, 6)),
                add(power(rho, 3), multiply(constant(4), k3)))
delta = add(multiply(constant(4), power(alpha, 3)),
            multiply(constant(9), power(beta, 2)))
vminus = add(multiply(constant(6), beta), minus(multiply(constant(4), k3)))
vplus = add(multiply(constant(6), beta), multiply(constant(4), k3))
assert vminus == power(rho, 3)
assert multiply(vminus, vplus) == multiply(constant(4), delta)

a = add(constant(1), multiply(k, h2))
b = multiply(rho, h2)
c = constant(-2)
as_product = multiply(a, add(a, c),
                      add(power(c, 2), minus(multiply(a, c)), minus(power(a, 2))))
D1 = multiply(add(constant(1), multiply(alpha, power(h, 4))),
              add(constant(5), multiply(alpha, power(h, 4))))
assert as_product == minus(D1)

x, y, Y = words('x'), words('y'), words('Y')
U = nadd(scale(words('yyy'), constant(F(1, 3))),
         scale(words('xxxxy'), alpha), scale(words('xxxxxx'), beta))
bracket = commutator(x, y)
W = nadd(scale(nmultiply(bracket, bracket), constant(F(-1, 2))), scale(U, h2))
assert cyclic(W) == cyclic(nadd(words('xxyy'),
                               scale(words('xyxy'), constant(-1)), scale(U, h2)))
R4, R5 = derivative(W, 'y'), derivative(W, 'x')
# Eliminating z=[x,y]/h gives minus these two cyclic derivatives.
assert nadd(R4, commutator(bracket, x), scale(derivative(U, 'y'), minus(h2))) == {}
assert nadd(R5, commutator(y, bracket), scale(derivative(U, 'x'), minus(h2))) == {}

f4 = nadd(scale(words('xxY', 'Yxx'), a), scale(words('xYx'), c),
          scale(words('YY'), b))
f5 = nadd(scale(words('YYx', 'xYY'), a), scale(words('YxY'), c),
          scale(words('xxxxx'), b))
W_standard = nadd(scale(words('xxYY'), a),
                  scale(words('xYxY'), multiply(constant(F(1, 2)), c)),
                  scale(words('YYY'), multiply(constant(F(1, 3)), b)),
                  scale(words('xxxxxx'), multiply(constant(F(1, 6)), b)))
assert derivative(W_standard, 'Y') == f4
assert derivative(W_standard, 'x') == f5
replacement = nadd(scale(Y, rho), scale(words('xx'), k))
assert cyclic(change_y(W, replacement)) == cyclic(scale(W_standard, rho2))
assert change_y(R4, replacement) == scale(f4, rho)
assert nadd(change_y(R5, replacement),
            scale(nadd(nmultiply(x, f4), nmultiply(f4, x)), multiply(k, rho))) == (
                scale(f5, rho2))
assert nadd(commutator(x, f5), commutator(Y, f4)) == {}

print('PASS: finite-cover unit identity and explicit AS-open polynomial')
print('PASS: eliminated relations with exact signs and scales')
print('PASS: Weierstrass-to-Stephenson cyclic potential and relation ideals')
print('PASS: weighted cyclic syzygy in the free algebra')
print('Exact coefficient ring: Q[h,k,rho]; no numerical sampling or finite jets')

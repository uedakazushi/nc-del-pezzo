#!/usr/bin/env python3
"""Universal point-curve identities for every binary quartic, including f=0.

Standard-library exact arithmetic over Q[a,b,c,d,e,h,t,q,w].  No parameter
sampling is used.  The final fourfold-shift check alone is modulo h^2.
Flatness, ribbon cohomology, THCR comparison and Noetherianity are proved in
degree_two_gorenstein_curve.tex; they are not conclusions of this script.
"""
from fractions import Fraction


NAMES = ('a', 'b', 'c', 'd', 'e', 'h', 't', 'q', 'w')
ZERO = (0,) * len(NAMES)


class P(dict):
    """A sparse polynomial in the fixed certificate ring."""
    @staticmethod
    def coerce(x):
        return x if isinstance(x, P) else P({ZERO: Fraction(x)}) if x else P()

    def __add__(self, other):
        out = P(self)
        for monomial, coefficient in self.coerce(other).items():
            out[monomial] = out.get(monomial, 0) + coefficient
            if not out[monomial]:
                del out[monomial]
        return out

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        out = P()
        for m, c in self.items():
            for n, d in self.coerce(other).items():
                exponent = tuple(x + y for x, y in zip(m, n))
                out[exponent] = out.get(exponent, 0) + c*d
        return P({m: c for m, c in out.items() if c})

    __rmul__ = __mul__

    def __pow__(self, power):
        out = self.coerce(1)
        for _ in range(power):
            out = out*self
        return out

    def sub(self, **substitutions):
        out = P()
        for monomial, coefficient in self.items():
            term = self.coerce(coefficient)
            for name, exponent in zip(NAMES, monomial):
                term *= substitutions.get(name, variables[name])**exponent
            out += term
        return out

    def divide_h(self, power):
        index = NAMES.index('h')
        out = P()
        for monomial, coefficient in self.items():
            assert monomial[index] >= power
            exponent = list(monomial)
            exponent[index] -= power
            out[tuple(exponent)] = coefficient
        return out

    def mod_h(self, power):
        index = NAMES.index('h')
        return P({m: c for m, c in self.items() if m[index] < power})


variables = {}
for i, name in enumerate(NAMES):
    exponent = list(ZERO)
    exponent[i] = 1
    variables[name] = P({tuple(exponent): Fraction(1)})
a, b, c, d, e, h, t, q, w = (variables[name] for name in NAMES)
one = P.coerce(1)

A = a + b*(t+q) + c*t*q
B = b + c*(t+q) + d*t*q
C = c + d*(t+q) + e*t*q
M00, M01 = t*q + 4*h**2*A, q-2*t + 4*h**2*B
M10, M11 = t-2*q + 4*h**2*B, one + 4*h**2*C
H = M00*M11 - M01*M10
Q = (H-2*(q-t)**2).divide_h(2)
f = a + 4*b*t + 6*c*t**2 + 4*d*t**3 + e*t**4
assert Q.sub(q=t).mod_h(1) == 4*f
assert H.sub(t=q, q=t) == H

G = H.sub(q=t+h*w).divide_h(2)
assert G.mod_h(1) == 2*w**2 + 4*f
# In particular the zero quartic is retained as a ribbon, not discarded.
assert G.sub(a=P(), b=P(), c=P(), d=P(), e=P()) == 2*w**2

D = M11
N = -M10
K = (one + 8*h**2*(c+2*d*q+e*q**2)
     + 16*h**4*(c**2-b*d+(c*d-b*e)*q+(d**2-c*e)*q**2))
# Homogeneous substitution (t,q) -> (q,N/D) with denominator D^2 cleared.
shifted = P()
ti, qi = NAMES.index('t'), NAMES.index('q')
for monomial, coefficient in H.items():
    t_degree, q_degree = monomial[ti], monomial[qi]
    assert q_degree <= 2
    residual = list(monomial)
    residual[ti] = residual[qi] = 0
    shifted += P({tuple(residual): coefficient})*q**t_degree*N**q_degree*D**(2-q_degree)
assert shifted == K*H

W = w-4*h*(B+q*C)
assert (N-q*D).sub(q=t+h*w) == h*W.sub(q=t+h*w)
assert D.sub(q=t+h*w).mod_h(2) == one
f_t = 4*b + 12*c*t + 12*d*t**2 + 4*e*t**3
assert W.sub(q=t+h*w).mod_h(2) == w-h*f_t
assert 4*f_t*w + 4*w*(-f_t) == P()

t4, w4 = t, w
for _ in range(4):
    t4 = t4.sub(t=t+h*w, w=w-h*f_t).mod_h(2)
    w4 = w4.sub(t=t+h*w, w=w-h*f_t).mod_h(2)
assert t4 == t+4*h*w
assert w4 == w-4*h*f_t

print('PASS: all-coefficient cubic point matrix and exact blowup equation')
print('PASS: classical double cover, including the nonreduced zero-quartic ribbon')
print('PASS: universal shift identity with all denominators cleared')
print('PASS: regular lifted shift and first-order fourfold displacement')
print('Exact arithmetic over Q with independent quartic coefficients; final shift is mod h^2')

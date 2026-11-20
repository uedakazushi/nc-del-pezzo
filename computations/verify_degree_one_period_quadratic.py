#!/usr/bin/env python3
"""Exact quadratic comparison of the degree-one point curve and shadow.

Uses only the standard library and the existing exact polynomial arithmetic.
This verifies equations and j-invariants, not the categorical period theorem
needed to identify the point-curve deformation with rho_Ku.

Normalization:
  F = z^2/2 + y^3/3 + alpha*x^4*y + beta*x^6 + u^6;
  [x,y] = h*z.
"""

import contextlib
import io
from fractions import Fraction

with contextlib.redirect_stdout(io.StringIO()):
    import verify_degree_one_integral_curve as curve

p = curve.p
add, neg, mul, power = p.add, p.minus, p.multiply, p.power
sub, div_h, mod_h = p.substitute, p.divide_h, p.mod_h
constant, variable = p.constant, p.variable
h, k, gamma, t = curve.h, curve.k, curve.gamma, curve.t
one = constant(1)


def scale(polynomial, scalar):
    return mul(constant(scalar), polynomial)


def coefficient(polynomial, name, degree):
    index = p.NAMES.index(name)
    result = {}
    for exponent, value in polynomial.items():
        if exponent[index] == degree:
            residual = list(exponent)
            residual[index] = 0
            result[tuple(residual)] = value
    return result


def unit_quotient(numerator, denominator, order):
    """Truncate a quotient whose denominator has constant nonzero h^0 term."""
    special = mod_h(denominator, 1)
    assert len(special) == 1 and p.ZERO in special
    scalar = special[p.ZERO]
    perturbation = scale(add(denominator, neg(special)), 1 / scalar)
    assert mod_h(perturbation, 1) == {}
    term, inverse = one, {}
    for _ in range(order):
        inverse = add(inverse, term)
        term = mod_h(neg(mul(term, perturbation)), order)
    return mod_h(scale(mul(numerator, inverse), 1 / scalar), order)


# Discriminant in q of the exact integral point curve from the existing proof.
H = sub(curve.H, curve.params)
aq, bq, cq = (coefficient(H, 'q', i) for i in (2, 1, 0))
discriminant = add(power(bq, 2), scale(mul(aq, cq), -4))
quartic = scale(div_h(discriminant, 2), Fraction(-1, 12))
quartic_jet = mod_h(quartic, 4)
special = add(scale(power(t, 3), 2), scale(mul(k, power(t, 2)), 6), gamma)
correction = add(power(t, 4), scale(mul(k, power(t, 3)), 4),
                 scale(mul(power(k, 2), power(t, 2)), 60),
                 scale(mul(gamma, t), -28), scale(mul(k, gamma), -28))
assert quartic_jet == add(special, scale(mul(power(h, 2), correction), Fraction(-1, 12)))

# Classical binary-quartic invariants; the cubic is homogenized to degree four.
a, b, c, d, e = (coefficient(quartic_jet, 't', i) for i in (4, 3, 2, 1, 0))
I = mod_h(add(scale(mul(a, e), 12), scale(mul(b, d), -3), power(c, 2)), 4)
J = mod_h(add(scale(mul(a, c, e), 72), scale(mul(b, c, d), 9),
              scale(mul(a, power(d, 2)), -27),
              scale(mul(power(b, 2), e), -27), scale(power(c, 3), -2)), 4)
alpha_cover = neg(power(k, 2))
beta_cover = scale(add(gamma, scale(power(k, 3), 4)), Fraction(1, 6))
assert I == add(scale(alpha_cover, -36), scale(mul(beta_cover, power(h, 2)), -90))
assert J == add(scale(beta_cover, -648), scale(mul(power(alpha_cover, 2), power(h, 2)), 1080))

# Direct marked coordinate calculation, without using the invariant formula.
# t=v/(1+h^2*v/24); the fourth power clears the binary quartic denominator.
mobius = add(t, scale(mul(power(h, 2), power(t, 2)), Fraction(-1, 24)))
mobius_factor = add(one, scale(mul(power(h, 2), t), Fraction(1, 6)))
cubic = mod_h(mul(sub(quartic_jet, {'t': mobius}), mobius_factor), 4)
expected_cubic = add(
    mul(add(constant(2), scale(mul(k, power(h, 2)), Fraction(1, 6))), power(t, 3)),
    mul(add(scale(k, 6), scale(mul(power(k, 2), power(h, 2)), -5)), power(t, 2)),
    scale(mul(gamma, power(h, 2), t), Fraction(5, 2)), gamma,
    scale(mul(k, gamma, power(h, 2)), Fraction(7, 3)))
assert cubic == expected_cubic
normalized = mod_h(mul(cubic, add(one, scale(mul(k, power(h, 2)), Fraction(-1, 12)))), 4)
translation = add(t, neg(k), scale(mul(power(k, 2), power(h, 2)), Fraction(11, 12)))
depressed = mod_h(sub(normalized, {'t': translation}), 4)
alpha_tilde = add(alpha_cover, mul(power(h, 2), add(
    scale(beta_cover, Fraction(5, 2)), scale(mul(alpha_cover, k), Fraction(-1, 6)))))
beta_tilde = add(beta_cover, mul(power(h, 2), add(
    scale(power(alpha_cover, 2), Fraction(-5, 3)), scale(mul(beta_cover, k), Fraction(-1, 4)))))
assert depressed == add(scale(power(t, 3), 2), scale(mul(alpha_tilde, t), 6), scale(beta_tilde, 6))
eta = add(one, scale(mul(k, power(h, 2)), Fraction(1, 24)))
assert mod_h(mul(power(eta, 4), alpha_tilde), 4) == add(alpha_cover,
    scale(mul(beta_cover, power(h, 2)), Fraction(5, 2)))
assert mod_h(mul(power(eta, 6), beta_tilde), 4) == add(beta_cover,
    scale(mul(power(alpha_cover, 2), power(h, 2)), Fraction(-5, 3)))

# Independent coefficient variables for the shadow calculation.
alpha, beta = variable('a'), variable('b')
scaled_parameters = {'a': mul(alpha, power(h, 4)), 'b': mul(beta, power(h, 6))}
c_num = scale(add(scale(power(alpha, 2), 5), scale(mul(alpha, beta), -6),
                  scale(alpha, 3), scale(beta, -15)), 5)
c_den = scale(add(alpha, constant(5)), 3)
d_num = neg(add(scale(power(alpha, 4), 2), scale(power(alpha, 3), 6),
                scale(mul(power(alpha, 2), beta), -36), scale(power(alpha, 2), -20),
                scale(mul(alpha, power(beta, 2)), 36), scale(mul(alpha, beta), -51),
                scale(power(beta, 2), 90), scale(beta, -15)))
d_den = scale(mul(add(alpha, one), add(alpha, constant(5))), 3)
c_h = unit_quotient(div_h(sub(c_num, scaled_parameters), 4),
                    sub(c_den, scaled_parameters), 4)
d_h = unit_quotient(div_h(sub(d_num, scaled_parameters), 6),
                    sub(d_den, scaled_parameters), 4)
assert c_h == add(alpha, scale(mul(beta, power(h, 2)), -5))
assert d_h == add(beta, scale(mul(power(alpha, 2), power(h, 2)), Fraction(4, 3)))

# Depression y = Y + 2*alpha*h^2*x^2; its quadratic correction to J matters.
alpha_sh = mod_h(add(c_h, scale(mul(power(alpha, 2), power(h, 4)), -4)), 4)
beta_sh = mod_h(add(d_h, scale(mul(alpha, power(h, 2), c_h), 2),
                    scale(mul(power(alpha, 3), power(h, 6)), Fraction(-16, 3))), 4)
alpha_E = add(alpha, scale(mul(beta, power(h, 2)), Fraction(5, 2)))
beta_E = add(beta, scale(mul(power(alpha, 2), power(h, 2)), Fraction(-5, 3)))
assert alpha_sh == add(alpha, scale(mul(beta, power(h, 2)), -5))
assert beta_sh == add(beta, scale(mul(power(alpha, 2), power(h, 2)), Fraction(10, 3)))
assert add(alpha_E, neg(alpha_sh)) == scale(mul(beta, power(h, 2)), Fraction(15, 2))
assert add(beta_E, neg(beta_sh)) == scale(mul(power(alpha, 2), power(h, 2)), -5)

# j = 1728*4*alpha^3/(4*alpha^3+9*beta^2), with all denominators cleared.
N0 = scale(power(alpha, 3), 6912)
D0 = add(scale(power(alpha, 3), 4), scale(power(beta, 2), 9))
for a_jet, b_jet, numerator_coefficient in (
        (alpha_E, beta_E, 51840), (alpha_sh, beta_sh, -103680)):
    N = mod_h(scale(power(a_jet, 3), 6912), 4)
    D = mod_h(add(scale(power(a_jet, 3), 4), scale(power(b_jet, 2), 9)), 4)
    K = scale(mul(power(alpha, 2), beta), numerator_coefficient)
    assert mod_h(add(mul(N, D0), neg(mul(N0, D)),
                     neg(mul(power(h, 2), K, D))), 4) == {}

# At alpha=0, j is cubically ramified. The first nonzero term is h^6;
# unknown O(h^4) coefficient corrections can only affect j from h^8 onward.
for slope, expected in ((Fraction(5, 2), 12000), (Fraction(-5), -96000)):
    assert Fraction(6912, 9) * slope ** 3 == expected

print('PASS: exact q-discriminant, h^2-divisibility and quartic expansion')
print('PASS: I=-36*alpha-90*beta*h^2; J=-648*beta+1080*alpha^2*h^2 modulo h^4')
print('PASS: marked Mobius, cubic depression and Weierstrass-unit transformations')
print('PASS: point alpha_E=alpha+(5/2)*beta*h^2; beta_E=beta-(5/3)*alpha^2*h^2')
print('PASS: shadow alpha_sh=alpha-5*beta*h^2; beta_sh=beta+(10/3)*alpha^2*h^2')
print('PASS: difference ((15/2)*beta,-5*alpha^2)*h^2 modulo h^4')
print('PASS: generic j difference =155520*alpha^2*beta/(4*alpha^3+9*beta^2)*h^2')
print('PASS: Fermat j_E=12000*beta*h^6; j_sh=-96000*beta*h^6 modulo h^8')
print('Normalization: z^2/2+y^3/3+alpha*x^4*y+beta*x^6+u^6=0, [x,y]=h*z.')
print('The categorical interpretation requires the equivariant period comparison theorem.')

#!/usr/bin/env python3
"""Exact all-coefficient certificates for the degree-one integral point curve.

The polynomial arithmetic is reused from verify_degree_one_curve.py.  Its
checks run on import but their output is suppressed here.  The independent
coefficient gamma uses that module's otherwise unused variable slot 'b'.
No division by gamma, alpha, beta or the elliptic discriminant is made.
Only the explicitly marked final sigma calculation is modulo h**2.
"""
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import verify_degree_one_curve as p

add, minus, mul, power = p.add, p.minus, p.multiply, p.power
sub, divide_h, mod_h = p.substitute, p.divide_h, p.mod_h
constant, variable = p.constant, p.variable
a, c, k, h, t, q, w, u, v, eta, w0, z0, w1, z1 = (
    variable(name) for name in
    ('a', 'c', 'k', 'h', 't', 'q', 'w', 'u', 'v', 'eta',
     'w0', 'z0', 'w1', 'z1'))
gamma = variable('b')
one = constant(1)
C = add(power(a, 2), minus(power(c, 2)))
ac = add(a, c)
params = {'a': add(one, mul(k, power(h, 2))), 'c': constant(-2)}

H = add(
    mul(a, C, add(power(t, 2), power(q, 2))),
    mul(a, power(h, 2), ac,
        add(mul(power(t, 2), q), mul(t, power(q, 2)))),
    mul(add(mul(power(a, 2), c), minus(mul(gamma, power(h, 6))),
            minus(power(c, 3))), t, q),
    minus(mul(a, gamma, power(h, 4), add(t, q))),
    minus(mul(power(a, 2), gamma, power(h, 2))))
assert sub(H, {'t': q, 'q': t}) == H

H_hom = {}
ti, qi = p.NAMES.index('t'), p.NAMES.index('q')
for exponent, value in H.items():
    i, j = exponent[ti], exponent[qi]
    assert i <= 2 and j <= 2
    residual = list(exponent)
    residual[ti] = residual[qi] = 0
    H_hom = add(H_hom, mul({tuple(residual): value},
                           power(w0, 2-i), power(z0, i),
                           power(w1, 2-j), power(z1, j)))

M11 = add(mul(c, w0, z1), mul(a, z0, w1))
M12 = mul(add(mul(a, w0), mul(power(h, 2), z0)), w1)
M21 = add(mul(a, gamma, power(h, 2), c, w0, w1),
          mul(gamma, power(h, 4), c, w0, z1), mul(a, C, z0, z1))
M22 = add(mul(c, C, z0, w1), mul(a, power(h, 2), ac, z0, z1),
          mul(a, C, w0, z1))
assert add(mul(M11, M22), minus(mul(M12, M21))) == mul(c, H_hom)
delta = add(mul(w0, z1), minus(mul(z0, w1)))
H_parameter = sub(H_hom, params)
assert mod_h(H_parameter, 1) == mul(constant(-3), power(delta, 2))
divide_h(add(H_parameter, mul(constant(3), power(delta, 2))), 2)

G = divide_h(sub(sub(H, params), {'q': add(t, mul(h, w))}), 2)
G0 = add(mul(constant(-3), power(w, 2)),
         mul(constant(-6), k, power(t, 2)),
         mul(constant(-2), power(t, 3)), minus(gamma))
assert mod_h(G, 1) == G0
H_inf = sub(H_hom, {'w0': u, 'z0': one, 'w1': v, 'z1': one})
G_inf = divide_h(sub(sub(H_inf, params),
                    {'v': add(u, mul(h, eta))}), 2)
assert mod_h(G_inf, 1) == add(mul(constant(-3), power(eta, 2)),
    mul(constant(-6), k, power(u, 2)), mul(constant(-2), u),
    minus(mul(gamma, power(u, 4))))
assert sub(G_inf, {'u': {}}) == sub(mul(a, ac, eta,
    add(mul(add(a, minus(c)), eta), h)), params)

y0 = add(t, k)
beta = mul(constant(p.Fraction(1, 6)),
           add(gamma, mul(constant(4), power(k, 3))))
F0 = add(mul(constant(p.Fraction(1, 2)), power(w, 2)),
         mul(constant(p.Fraction(1, 3)), power(y0, 3)),
         minus(mul(power(k, 2), y0)), beta)
assert mul(constant(6), F0) == minus(G0)

# r=R/D and s=Snum/[D*(a+h^2 q)]; both relations are exact.
D = add(a, mul(power(h, 2), t))
R = minus(add(mul(c, q), mul(a, t)))
D_next = add(a, mul(power(h, 2), q))
Snum = minus(add(mul(c, R), mul(a, q, D)))
shift_H = add(
    mul(a, C, add(mul(power(q, 2), power(D, 2)), power(R, 2))),
    mul(a, power(h, 2), ac,
        add(mul(power(q, 2), R, D), mul(q, power(R, 2)))),
    mul(add(mul(power(a, 2), c), minus(mul(gamma, power(h, 6))),
            minus(power(c, 3))), q, R, D),
    minus(mul(a, gamma, power(h, 4),
              add(mul(q, power(D, 2)), mul(R, D)))),
    minus(mul(power(a, 2), gamma, power(h, 2), power(D, 2))))
assert shift_H == mul(add(power(a, 2), minus(mul(power(h, 2), c, q))), H)
assert add(mul(add(mul(a, D), mul(power(h, 2), R)), t),
           mul(c, q, D), mul(a, R)) == {}
rel5 = add(mul(a, t, R, D_next), mul(a, q, Snum),
           mul(c, t, Snum), mul(gamma, power(h, 2), D, D_next))
assert rel5 == minus(H)

# The two sections persist at gamma=k=0, including the cuspidal fibre.
Q_section = {'w0': {}, 'z0': one, 'w1': {}, 'z1': one}
P_section = {'w0': {}, 'z0': one, 'w1': power(h, 2),
             'z1': add(c, minus(a))}
assert sub(H_hom, Q_section) == {}
assert sub(H_hom, P_section) == {}
assert add(mul(a, C, power(h, 2)),
           mul(a, power(h, 2), ac, add(c, minus(a)))) == {}

W = add(w, minus(mul(h, add(mul(k, add(t, q)), mul(t, q)))))
chart = {'q': add(t, mul(h, w))}
assert sub(sub(add(R, minus(mul(q, D))), params), chart) == (
    mul(h, sub(W, chart)))
assert mod_h(sub(sub(D, params), chart), 2) == one

# This final assertion alone is a first-order certificate.
drift = add(mul(constant(2), k, t), power(t, 2))
jet = {'t': add(t, mul(h, w)), 'w': add(w, minus(mul(h, drift)))}
six_t, six_w = t, w
for _ in range(6):
    six_t = mod_h(sub(six_t, jet), 2)
    six_w = mod_h(sub(six_w, jet), 2)
assert six_t == add(t, mul(constant(6), h, w))
assert six_w == add(w, minus(mul(constant(6), h, drift)))
assert sub(G0, {'k': {}, 'b': {}}) == add(
    mul(constant(-3), power(w, 2)), mul(constant(-2), power(t, 3)))

print('PASS: all-coefficient point-curve determinant and double diagonal')
print('PASS: exact finite/infinity blowups, Weierstrass and cusp specialization')
print('PASS: cleared shift/inverse, degree-four and degree-five relations')
print('PASS: sections, Cartier-divisor factorization and lifted shift')
print('PASS: sixfold shift is nonidentity modulo h^2')
print('Exact Q-polynomial certificates; no elliptic discriminant inverted')

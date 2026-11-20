#!/usr/bin/env python3
"""Exact degree-two period jets and nonconstancy on a shadow fibre.

Only standard-library rational polynomial arithmetic is used. The existing
degree-one modules supply shared arithmetic, not geometric assumptions.
The categorical interpretation of the point curve is proved in the paper.
"""

import contextlib
import io
from fractions import Fraction as Q

with contextlib.redirect_stdout(io.StringIO()):
    import verify_degree_one_period_quadratic as jets
    import verify_degree_one_period_fibres as univariate

p = jets.p
add, neg, mul, power = p.add, p.minus, p.multiply, p.power
constant, variable, sub = p.constant, p.variable, p.substitute
scale, quotient = jets.scale, jets.unit_quotient
trim, ua, um, up, us = (univariate.trim, univariate.uadd,
                       univariate.umul, univariate.upower, univariate.uscale)
udiv, ugcd = univariate.udivmod, univariate.ugcd

alpha, beta, h = (variable(name) for name in ('a', 'b', 'h'))
one = constant(1)
a = add(one, scale(mul(beta, power(h, 2)), Q(2, 3)))
b = add(constant(-2), scale(mul(beta, power(h, 2)), Q(2, 3)))
c = mul(alpha, power(h, 2))
K = scale(mul(power(a, 2), b, c), 4)
M = add(power(add(power(c, 2), neg(power(b, 2))), 2),
        scale(mul(power(a, 2), add(power(c, 2), power(b, 2))), -4))
alpha_E = p.mod_h(scale(p.divide_h(K, 2), Q(-1, 8)), 4)
beta_E = p.mod_h(scale(p.divide_h(M, 2), Q(-1, 32)), 4)
assert alpha_E == add(alpha, mul(alpha, beta, power(h, 2)))
assert beta_E == add(beta, scale(mul(add(scale(power(alpha, 2), 3),
    scale(power(beta, 2), -4)), power(h, 2)), Q(1, 8)))

# Independently expand the fully symmetrized central element, before taking
# its quotient by the Jacobian relations.
kz = neg(mul(a, add(power(b, 2), neg(power(c, 2)))))
kD = scale(mul(c, add(scale(power(a, 3), 2),
    scale(mul(a, power(c, 2)), -2), power(b, 3),
    neg(mul(b, power(c, 2))))), Q(1, 3))
kS = scale(mul(a, add(scale(mul(power(a, 2), b), 2),
    mul(a, power(b, 2)), neg(mul(a, power(c, 2))),
    scale(mul(b, power(c, 2)), -2))), 2)
alpha_sh = quotient(p.divide_h(scale(kD, 2), 2), kz, 4)
beta_sh = quotient(p.divide_h(kS, 2), scale(kz, 2), 4)
assert alpha_sh == add(alpha, scale(mul(alpha, beta, power(h, 2)), -2))
assert beta_sh == add(beta, scale(mul(add(scale(power(alpha, 2), 3),
    scale(power(beta, 2), -4)), power(h, 2)), Q(-1, 4)))

# Hessian/8, with x,y represented by spare variable slots u,v.
x, y = variable('u'), variable('v')
Hxx = add(scale(mul(alpha, power(x, 2)), 3), scale(mul(beta, power(y, 2)), 2))
Hyy = add(scale(mul(alpha, power(y, 2)), 3), scale(mul(beta, power(x, 2)), 2))
Hxy = scale(mul(beta, x, y), 4)
hessian = add(mul(Hxx, Hyy), neg(power(Hxy, 2)))
delta_a = p.divide_h(add(alpha_E, neg(alpha_sh)), 2)
delta_b = p.divide_h(add(beta_E, neg(beta_sh)), 2)
delta_f = add(scale(mul(delta_a, add(power(x, 4), power(y, 4))), Q(1, 4)),
              mul(delta_b, power(x, 2), power(y, 2)))
assert scale(delta_f, 8) == hessian
# Multiplication by alpha avoids division in the Jacobian reduction.
reduced = add(scale(mul(alpha, power(alpha, 2)), Q(9, 8)),
              scale(mul(alpha, power(beta, 2)), Q(-9, 2)))
expected = scale(mul(alpha, add(power(alpha, 2), scale(power(beta, 2), -4))), Q(9, 8))
assert reduced == expected

# At alpha=4,beta=1, hold the shadow fixed to second order.
fixed_shadow = {'a': add(constant(4), scale(power(h, 2), 8)),
                'b': add(one, scale(power(h, 2), 11))}
Ae, Be = (p.mod_h(sub(g, fixed_shadow), 4) for g in (alpha_E, beta_E))
lam = quotient(scale(Be, 4), Ae, 4)
assert lam == add(one, scale(power(h, 2), Q(27, 2)))
j_num = scale(power(add(power(lam, 2), constant(12)), 3), 16)
j_den = power(add(power(lam, 2), constant(-4)), 2)
j_jet = quotient(j_num, j_den, 4)
assert j_jet == add(constant(Q(35152, 9)), scale(power(h, 2), 94640))

# A complete h=1 shadow fibre: B=1, A^2=-125/9.
T = trim([0, 1])
aT, rden = trim([3, 1]), trim([4, 3])
q0, ell = trim([18, 16, 3]), trim([12, 7])
rnum = um(T, q0)  # c^2 = rnum/rden
N = us(um(q0, up(ell, 2)), 4)
D = us(um(T, um(up(aT, 2), rden)), 9)
F = ua(N, us(D, Q(125, 9)))
assert F == us(um([1, 1], [1152, 1716, 771, 107]), 9)
assert ugcd(F, [i * F[i] for i in range(1, len(F))]) == [Q(1)]

# D(t)=k(1+t^4)+m t^2.  Clear rden^2 from m and rden^4
# from k^2 so that the j formula is evaluated entirely in Q[T].
Mnum = ua(up(ua(rnum, us(um(up(T, 2), rden), -1)), 2),
    us(um(up(aT, 2), um(ua(rnum, um(up(T, 2), rden)), rden)), -4))
K2num = us(um(up(aT, 4), um(up(T, 2), um(rnum, up(rden, 3)))), 16)
Jnum = us(up(ua(up(Mnum, 2), us(K2num, 12)), 3), 16)
Jden = um(K2num, up(ua(up(Mnum, 2), us(K2num, -4)), 2))
Jnum, Jden = (udiv(g, F)[1] for g in (Jnum, Jden))
assert ugcd(F, Jden) == [Q(1)]
value = lambda f, t: sum(x * t ** i for i, x in enumerate(f))
j0 = value(Jnum, -1) / value(Jden, -1)
assert j0 == Q(300763, 35721)
same = ua(us(Jnum, j0.denominator), us(Jden, -j0.numerator))
assert ugcd(F, same) == [Q(1), Q(1)]
same_primitive = univariate.primitive(same)
assert [(x * pow(same_primitive[-1], -1, 101)) % 101
        for x in same_primitive] == [6, 37, 32, 1]
assert [int(x) % 101 for x in F] == [66, 57, 62, 24, 54]
equal_mod = lambda a, b: all(int(x) % 101 == 0 for x in ua(a, us(b, -1)))
assert equal_mod([66, 57, 62, 24, 54], ua(um([13, 54], [6, 37, 32, 1]), [89, 60, 72]))
assert equal_mod([6, 37, 32, 1], ua(um([68, 94], [89, 60, 72]), [14, 14]))
assert equal_mod([89, 60, 72], um([28, 34], [14, 14]))
for denominator in (T, aT, rden, ell,
                    ua(um(up(T, 2), rden), us(rnum, -1))):
    assert ugcd(F, denominator) == [Q(1)]

print('PASS: degree-two point and shadow jets, all alpha,beta coefficients')
print('PASS: quadratic discrepancy = Hessian(f)/8')
print('PASS: shadow-fixed example j_E = 35152/9 + 94640*h^2 + O(h^4)')
print('Witness: B=1, A^2=-125/9; F=9*(T+1)*(107*T^3+771*T^2+1716*T+1152)')
print('PASS: squarefree fibre; every displayed denominator is a unit modulo F')
print('PASS: j_E(-1)=300763/35721; gcd(F,numerator(j_E-j_E(-1)))=T+1')
print('mod 101 Euclidean remainders: 72*T^2+60*T+89, 14*T+14, 0')
print('The point-curve j-invariant does not descend through the degree-four shadow map.')
print('Unmarked Ku separation also requires the intrinsic-invariant and monodromy proofs.')

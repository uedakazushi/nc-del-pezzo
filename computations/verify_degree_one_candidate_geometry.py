#!/usr/bin/env python3
"""Exact geometry certificates for the calibrated degree-one candidates.

2026-11-21 / v0.21. Standard library only.
This concerns T_s=H_1+s R_1, not the unidentified categorical discrepancy.
The small polynomial routines are reused from the existing Hessian certificate;
importing that file also rechecks its certificates.
"""

import verify_degree_one_hessian_counterexample as previous

Q = previous.Q
add = previous.add
scale = previous.scale
multiply = previous.multiply
power = previous.power
derivative = previous.derivative
determinant = previous.determinant
dense_multiply_mod = previous.dense_multiply_mod


def monomial(a, b, c=0, coefficient=1):
    return {(a, b, c): Q(coefficient)}


one = monomial(0, 0)
x = monomial(1, 0)
u = monomial(0, 1)
t = monomial(0, 0, 1)


def substitute(polynomial, values):
    result = {}
    for exponent, coefficient in polynomial.items():
        term = scale(one, coefficient)
        for value, degree in zip(values, exponent):
            term = multiply(term, power(value, degree))
        result = add(result, term)
    return result


def specialize_t(polynomial, value):
    return substitute(polynomial, [x, u, scale(one, value)])


def second_x(polynomial):
    return derivative(derivative(polynomial, 0), 0)


# t=8s+7. The reduced representative of 8*T_s(d_x) is
# 2*y*B_xx+c*A*A_xx+d*A_x^2.
c = add(scale(t, 4), scale(one, -30))
d = add(scale(one, 20), scale(t, -3))


def check_null_identities(A, B, vector_field):
    assert scale(second_x(B), 2) == vector_field(A)
    assert add(multiply(c, multiply(A, second_x(A))),
               multiply(d, power(derivative(A, 0), 2))) == vector_field(B)


# A short family with the nilpotent field x*d_u.
A = add(monomial(3, 1), monomial(0, 4, 1, -3))
B = add(monomial(6, 0, 0, Q(1, 60)), monomial(3, 3, 1, -1),
        monomial(0, 6, 1, 90), monomial(0, 6, 2, -12))
check_null_identities(A, B,
                      lambda p: multiply(x, derivative(p, 1)))
R = add(scale(multiply(A, second_x(A)), 4),
        scale(power(derivative(A, 0), 2), -3))
assert R == add(monomial(4, 2, 0, -3), monomial(1, 5, 1, -72))
print("PASS: the short family has T_s(d_x)=0 and R=-3*x^4*u^2-72*t*x*u^5")

# In these generic polynomial routines the first variable is now y,
# the second v=x^3, and the third remains t.
y, v = x, u
f = add(scale(power(y, 3), Q(1, 3)), multiply(v, y),
        scale(multiply(t, y), -3), scale(power(v, 2), Q(1, 60)),
        scale(multiply(t, v), -1), scale(t, 90), scale(power(t, 2), -12))
g = substitute(f, [y, add(scale(t, 3), scale(power(y, 2), -1)), t])
h = add(power(y, 2), scale(y, -30), scale(t, 27))
quotient = add(scale(t, Q(9, 20)), scale(power(y, 2), Q(1, 60)),
               scale(y, Q(-1, 6)), scale(one, -5))
remainder = scale(multiply(add(scale(t, -3), scale(y, 2)),
                           add(scale(t, 3), scale(one, -25))), 3)
assert g == add(multiply(h, quotient), remainder)
linear_a = add(scale(t, 18), scale(one, -150))
linear_b = add(scale(power(t, 2), -27), scale(t, 225))
resultant = add(power(linear_b, 2),
                scale(multiply(linear_a, linear_b), 30),
                scale(multiply(t, power(linear_a, 2)), 27))
expected = scale(multiply(multiply(t, add(t, scale(one, -8))),
                          power(add(scale(t, 3), scale(one, -25)), 2)), 81)
assert resultant == expected
assert add(power(add(scale(one, 45), scale(t, -6)), 2), scale(t, -3)) == \
    scale(multiply(add(scale(t, 3), scale(one, -25)),
                   add(scale(t, 4), scale(one, -27))), 3)
print("PASS: exact critical-point elimination; exceptional t=0,8,25/3,27/4")

# A second family with x*d_x-5*u*d_u fills the three nonzero exceptions.
AA = add(monomial(3, 1), monomial(2, 2, 1, Q(-3, 2)),
         monomial(1, 3, 2, Q(3, 7)), monomial(0, 4, 3, Q(-1, 14)),
         monomial(0, 4, 2, Q(3, 14)))
BB = add(monomial(5, 1, 0, Q(-1, 20)), monomial(4, 2, 1, Q(1, 2)),
         monomial(3, 3, 2, Q(-1, 2)), monomial(2, 4, 3, Q(5, 14)),
         monomial(2, 4, 2, Q(-15, 14)), monomial(1, 5, 4, Q(-1, 28)),
         monomial(1, 5, 3, Q(-3, 14)), monomial(1, 5, 2, Q(45, 28)),
         monomial(0, 6, 5, Q(-1, 98)), monomial(0, 6, 4, Q(87, 490)),
         monomial(0, 6, 3, Q(-9, 14)))
check_null_identities(AA, BB,
                      lambda p: add(multiply(x, derivative(p, 0)),
                                    scale(multiply(u, derivative(p, 1)), -5)))
assert specialize_t(AA, Q(7)) == previous.A
assert specialize_t(BB, Q(7)) == previous.B
print("PASS: the long family is universally null; t=7 is the earlier example")


def affine_dense(polynomial, value):
    """Specialize u=1,t=value; return coefficients in ascending x degree."""
    polynomial = substitute(polynomial, [x, one, scale(one, value)])
    degree = max(exponent[0] for exponent in polynomial)
    return [polynomial.get((i, 0, 0), Q(0)) for i in range(degree + 1)]


certificates = {
    Q(8): (
        [-3, -2, -3, 0, -3, -5, 0, -5, 3, -5, -2],
        [-4, 0, 1, 4, -3, -4, 5, 0, -3],
        [0, 4, -2, -1, -5, 1, 0, -3, 2, -3]),
    Q(25, 3): (
        [1, -3, 3, 4, -5, -1, 5, 0, -4, 1, -2],
        [5, 5, -3, -5, 5, -2, -5, 1, -5],
        [5, 3, 3, 5, 3, -3, -3, 2, 4, -5]),
    Q(27, 4): (
        [-1, -2, 4, -4, -3, 0, 1, 3, -3, 0, -2],
        [2, 0, 3, -1, -2, 1, 1],
        [4, 3, -4, -4, -5, -5, 1, 1]),
}
Delta = scale(add(scale(power(AA, 3), 4), scale(power(BB, 2), 9)), 400)
for value, (P, U, W) in certificates.items():
    rational_coefficients = affine_dense(Delta, value)
    coefficients = [q.numerator * pow(q.denominator, -1, 11) % 11
                    for q in rational_coefficients]
    assert coefficients == [a % 11 for a in P]
    assert rational_coefficients[-1] == 9
    P_prime = [i * a for i, a in enumerate(P)][1:]
    left = dense_multiply_mod(U, P, 11)
    right = dense_multiply_mod(W, P_prime, 11)
    length = max(len(left), len(right))
    check = [((left[i] if i < len(left) else 0)
              + (right[i] if i < len(right) else 0)) % 11
             for i in range(length)]
    assert check == [1] + [0] * (length - 1)
    print(f"PASS: t={value}: U*P+W*P'=1 mod 11; the long-family surface is smooth")

# The old boundary argument is uniform in t for the long family.
assert {e: a for e, a in derivative(BB, 1).items() if e[1] == 0} == \
    monomial(5, 0, 0, Q(-1, 20))
print("PASS: the long-family boundary derivative is -x^5/20 for every t")

# A=0 makes R vanish identically.  The y components of the quotient have
# no Jacobian relations, so this minor proves rank three for every s.
B_rank = add(monomial(6, 0), monomial(3, 3), monomial(0, 6))
columns = [second_x(B_rank), derivative(derivative(B_rank, 0), 1),
           derivative(derivative(B_rank, 1), 1)]
matrix = [[column.get(e, Q(0)) for column in columns]
          for e in [(4, 0, 0), (2, 2, 0), (0, 4, 0)]]
assert determinant(matrix) == 8100
print("PASS: A=0, B=x^6+x^3*u^3+u^6 has candidate rank 3 for every s")
print("Scope: all s != -7/8 have a smooth candidate null direction;")
print("       s=-7/8 and the actual categorical discrepancy remain undecided.")

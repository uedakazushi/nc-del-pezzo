#!/usr/bin/env python3
"""Exact degree-one centre, degree-five Poisson map, and S5 certificates.

2026-11-20 / v0.17.

Standard library only.  Over Q[alpha,beta], with h=1, eliminate
z=[x,y] and use the two weighted relations r4,r5.  Explicit free-algebra
certificates verify the centre after clearing 6(alpha+1)(alpha+5).
An exact rational rank check at alpha=beta=0 proves generic uniqueness
in the full seven-dimensional symmetric weight-six space.  The subsequent
commutative identities verify the depressed cubic and the coprimality
needed for the function-field degree five. Exact discriminants, a finite-field
Bezout certificate, depression, and scaling identities support the S5 proof.
The zero-fibre factorization and its nonzero discriminant support the finite
normalization at the classical locus; a quadratic Hensel jet is checked exactly.
The full lower-term, center-torsor, and moduli-quotient arguments are supplied
in the manuscript; these finite identities are not a formal proof of them.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations


NAMES = ("alpha", "beta", "I")
ZERO = (0, 0, 0)


class P(dict):
    @staticmethod
    def coerce(value):
        return value if isinstance(value, P) else P({ZERO: F(value)}) if value else P()

    def __add__(self, other):
        result = P(self)
        for m, c in self.coerce(other).items():
            result[m] = result.get(m, 0) + c
            if not result[m]:
                del result[m]
        return result

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        result = P()
        for m, c in self.items():
            for n, d in self.coerce(other).items():
                exponent = tuple(a+b for a, b in zip(m, n))
                result[exponent] = result.get(exponent, 0) + c*d
        return P({m: c for m, c in result.items() if c})

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = self.coerce(1)
        for _ in range(exponent):
            result *= self
        return result

    def sub(self, **values):
        result = P()
        for monomial, coefficient in self.items():
            term = self.coerce(coefficient)
            for name, exponent in zip(NAMES, monomial):
                term *= self.coerce(values.get(name, variables[name]))**exponent
            result += term
        return result

    def rational_beta(self, numerator, denominator):
        """Return denominator**degree_beta * self(beta=numerator/denominator)."""
        degree = max((m[1] for m in self), default=0)
        result = P()
        for (a, b, i), coefficient in self.items():
            result += coefficient*alpha**a*I**i*numerator**b*denominator**(degree-b)
        return result


variables = {}
for index, name in enumerate(NAMES):
    exponent = list(ZERO)
    exponent[index] = 1
    variables[name] = P({tuple(exponent): F(1)})
alpha, beta, I = (variables[name] for name in NAMES)


def nadd(*polynomials):
    result = {}
    for p in polynomials:
        for word, coefficient in p.items():
            result[word] = result.get(word, P()) + coefficient
            if not result[word]:
                del result[word]
    return result


def nscale(p, coefficient):
    return {w: c*coefficient for w, c in p.items() if c*coefficient}


def nmul(p, q):
    return nadd(*({w+v: a*b} for w, a in p.items() for v, b in q.items()))


def comm(p, q):
    return nadd(nmul(p, q), nscale(nmul(q, p), -1))


def sym(word):
    orbit = set("".join(w) for w in permutations(word))
    return {w: P.coerce(F(1, len(orbit))) for w in orbit}


x, y = sym("x"), sym("y")
z = comm(x, y)
r4 = nadd(comm(z, x), nscale(sym("yy"), -1), nscale(sym("xxxx"), -alpha))
r5 = nadd(comm(y, z), nscale(sym("xxxy"), -4*alpha), nscale(sym("xxxxx"), -6*beta))
relations = {"r4": r4, "r5": r5}

den_c = 3*(alpha+5)
num_c = 5*(5*alpha**2-6*alpha*beta+3*alpha-15*beta)
den_d = 3*(alpha+1)*(alpha+5)
num_d = -(2*alpha**4+6*alpha**3-36*alpha**2*beta-20*alpha**2
          +36*alpha*beta**2-51*alpha*beta+90*beta**2-15*beta)
Q = 6*(alpha+1)*(alpha+5)
omega_scaled = nadd(
    nscale(nmul(z, z), 3*(alpha+1)*(alpha+5)),
    nscale(sym("yyy"), 2*(alpha+1)*(alpha+5)),
    nscale(sym("xxyy"), -2*alpha*Q),
    nscale(sym("xxxxy"), 2*(alpha+1)*num_c),
    nscale(sym("xxxxxx"), 2*num_d),
)


def certificate(pairs):
    result = {}
    for relation, left, right, other_left, other_right, coefficient in pairs:
        r = relations[relation]
        positive = {left+w+right: c*coefficient for w, c in r.items()}
        negative = {other_left+w+other_right: -c*coefficient for w, c in r.items()}
        result = nadd(result, positive, negative)
    return result


certificate_x = [
    ("r4", "", "xxx", "xxx", "", 9*alpha*(alpha+1)),
    ("r4", "", "xy", "yx", "", 3*(alpha+1)*(2*alpha+5)),
    ("r4", "", "yx", "xy", "", -15*(alpha+1)),
    ("r4", "x", "xx", "xx", "x", 3*alpha*(alpha+1)),
    ("r4", "x", "y", "y", "x", 4*alpha*(alpha+1)),
    ("r5", "", "y", "y", "", -(alpha+1)*(2*alpha+5)),
]
p = 4*alpha**3+13*alpha**2-24*alpha*beta-15*alpha-60*beta
q = -2*alpha**3+alpha**2-24*alpha*beta+9*alpha-60*beta+30
r = -8*alpha**2+12*alpha*beta-11*alpha+30*beta-15
s = 8*alpha**3+20*alpha**2-12*alpha*beta-30*beta
t = 2*alpha**3+11*alpha**2-12*alpha*beta-3*alpha-30*beta
u = 2*alpha**3-alpha**2-12*alpha*beta-15*alpha-30*beta
v = 2*alpha**3+8*alpha**2-12*alpha*beta-6*alpha-30*beta
certificate_y = [
    ("r4", "", "xxxx", "xxxx", "", p),
    ("r4", "", "xxy", "yxx", "", -3*(alpha+1)*(alpha+5)),
    ("r4", "", "xyx", "xyx", "", q),
    ("r4", "", "yxx", "xxy", "", -3*(alpha+1)*(4*alpha+5)),
    ("r4", "", "yy", "y", "y", r),
    ("r4", "x", "xxx", "xxx", "x", s),
    ("r4", "x", "xy", "yx", "x", t),
    ("r4", "x", "yx", "xy", "x", u),
    ("r4", "xx", "y", "y", "xx", v),
    ("r5", "", "xy", "y", "x", r),
    ("r5", "", "yx", "xy", "", 3*(alpha+1)*(2*alpha+5)),
]
assert comm(omega_scaled, x) == certificate(certificate_x)
assert comm(omega_scaled, y) == certificate(certificate_y)
print("PASS: full-coefficient free-algebra centre certificates (12 and 22 terms)")


@lru_cache(None)
def words(weight):
    if weight == 0:
        return ("",)
    if weight < 0:
        return ()
    return tuple("x"+w for w in words(weight-1))+tuple("y"+w for w in words(weight-2))


def rref(rows):
    rows = [[F(x) for x in row] for row in rows]
    pivots = []
    k = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(k, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        scalar = rows[k][column]
        rows[k] = [x/scalar for x in rows[k]]
        for i in range(len(rows)):
            if i != k and rows[i][column]:
                scalar = rows[i][column]
                rows[i] = [a-scalar*b for a, b in zip(rows[i], rows[k])]
        pivots.append(column)
        k += 1
        if k == len(rows):
            break
    return rows[:k], pivots


def reduction_at_origin(weight, polynomials):
    basis = words(weight)
    rows = []
    for degree, rel in ((4, r4), (5, r5)):
        for left_weight in range(weight-degree+1):
            for left in words(left_weight):
                for right in words(weight-degree-left_weight):
                    row = {left+w+right: c.get(ZERO, F(0)) for w, c in rel.items()}
                    rows.append([row.get(w, F(0)) for w in basis])
    reduced, pivots = rref(rows)
    output = []
    for p in polynomials:
        row = [p.get(w, P()).get(ZERO, F(0)) for w in basis]
        for relation, pivot in zip(reduced, pivots):
            scalar = row[pivot]
            row = [a-scalar*b for a, b in zip(row, relation)]
        output.append(row)
    return output


ansatz = [nmul(z, z), sym("yyy"), sym("xxyy"), sym("xxxxy"), sym("xxxxxx")]
assert len(rref(reduction_at_origin(6, ansatz))[1]) == 5
images_x = reduction_at_origin(7, [comm(p, x) for p in ansatz])
images_y = reduction_at_origin(8, [comm(p, y) for p in ansatz])
assert len(rref([a+b for a, b in zip(images_x, images_y)])[1]) == 4


def eliminate_z(p):
    result = {}
    for word, coefficient in p.items():
        term = {"": P.coerce(1)}
        for letter in word:
            term = nmul(term, z if letter == "z" else sym(letter))
        result = nadd(result, nscale(term, coefficient))
    return result


full_ansatz = ansatz+[eliminate_z(sym("xxxz")), eliminate_z(sym("xyz"))]
assert len(rref(reduction_at_origin(6, full_ansatz))[1]) == 7
images_x = reduction_at_origin(7, [comm(p, x) for p in full_ansatz])
images_y = reduction_at_origin(8, [comm(p, y) for p in full_ansatz])
assert len(rref([a+b for a, b in zip(images_x, images_y)])[1]) == 6
print("PASS: independent seven-term symmetric basis and generic centre dimension one")

# y=Y+2*alpha*x**2 removes the quadratic term, preserving D=1.
num_I = num_c-4*alpha**2*den_c
num_J = num_d+2*alpha*(alpha+1)*num_c-16*alpha**3*(alpha+1)*(alpha+5)
num_beta = -(12*alpha**3+35*alpha**2+3*alpha*I-15*alpha+15*I)
den_beta = 15*(2*alpha+5)
assert not (num_I-I*den_c).rational_beta(num_beta, den_beta)
N = (112*alpha**5+340*alpha**4+156*alpha**3*I+900*alpha**3
     +450*alpha**2*I+475*alpha**2-18*alpha*I**2+675*alpha*I
     +75*alpha-90*I**2-75*I)
den_J_after = 75*(alpha+1)*(2*alpha+5)
assert not (num_J*den_J_after-N*den_d).rational_beta(num_beta, den_beta)
assert N.sub(alpha=-1) == -8*(3*I+2)*(3*I+17)
assert N.sub(alpha=F(-5, 2)) == -F(5, 2)*(3*I+65)*(6*I+55)
assert max(m[0] for m in N) == 5
assert {m: c for m, c in N.items() if m[0] == 5} == {(5, 0, 0): F(112)}
print("PASS: depressed-cubic map, elimination, exact coprimality, and degree five")


# The existing three-variable polynomial ring is reused below with beta as J.
# This is an exact coefficient certificate; moduli descent is proved in the paper.
J_branch = beta
quintic = N-J_branch*den_J_after


def coefficients_in_alpha(polynomial, degree):
    coefficients = [P() for _ in range(degree+1)]
    for (a, b, i), coefficient in polynomial.items():
        coefficients[a] += P({(0, b, i): coefficient})
    return coefficients


def determinant_polynomial(matrix):
    """Subset expansion: exact determinant over the existing Q-polynomial ring."""
    dimension = len(matrix)
    partial = {0: P.coerce(1)}
    for row in matrix:
        following = {}
        for mask, value in partial.items():
            for column, entry in enumerate(row):
                if mask & (1 << column) or not entry:
                    continue
                sign = -1 if (mask >> (column+1)).bit_count() % 2 else 1
                next_mask = mask | (1 << column)
                following[next_mask] = following.get(next_mask, P())+sign*value*entry
        partial = following
    return partial.get((1 << dimension)-1, P())


coefficients = coefficients_in_alpha(quintic, 5)
derivative = [i*coefficients[i] for i in range(1, 6)]
# Four shifts of F (degree 5), five shifts of F' (degree 4).
sylvester = []
for shift in range(4):
    sylvester.append([P()]*shift+list(reversed(coefficients))+[P()]*(3-shift))
for shift in range(5):
    sylvester.append([P()]*shift+list(reversed(derivative))+[P()]*(4-shift))
# (-1)^(5*4/2)=1 and the leading coefficient of F is 112.
discriminant = F(1, 112)*determinant_polynomial(sylvester)
assert all(a == 0 for a, b, i in discriminant)
assert max(b for a, b, i in discriminant) == 6
assert {(a, b, i): c for (a, b, i), c in discriminant.items() if b == 6} == {
    (0, 6, 0): F(-8680203000000000000)
}
D0 = (1157360400*J_branch**6+114742255536*J_branch**5
      -1260129809475*J_branch**4-5034506238090*J_branch**3
      -13419254573985*J_branch**2-245130767140*J_branch-1041634158)
assert discriminant.sub(I=0) == -7500000000*D0
print("PASS: exact quintic discriminant, J-degree six, constant leading coefficient")


def derivative_in_beta(polynomial):
    return P({(a, b-1, i): b*c for (a, b, i), c in polynomial.items() if b})


# Bezout identity in F_19[J]; the leading degree-six coefficient is nonzero.
modulus = 19
d0_mod = 5*J_branch**6-3*J_branch**5-6*J_branch**4-J_branch**3+9*J_branch**2-3*J_branch-8
bezout_u = -7*J_branch**4+J_branch**3+4*J_branch**2+2*J_branch+5
bezout_v = -2*J_branch**5+7*J_branch**4+5*J_branch**3-6*J_branch**2+9*J_branch-1
assert all(c.denominator == 1 and c.numerator % modulus == 0 for c in (D0-d0_mod).values())
assert 1157360400 % modulus != 0
bezout_error = bezout_u*d0_mod+bezout_v*derivative_in_beta(d0_mod)-1
assert all(c.denominator == 1 and c.numerator % modulus == 0 for c in bezout_error.values())
# The two finite poles never cancel over C(I); at I=0 both evaluations are nonzero.
assert N.sub(alpha=-1, I=0) == P.coerce(-272)
assert N.sub(alpha=F(-5, 2), I=0) == P.coerce(-F(17875, 2))
assert max(m[0] for m in den_J_after) == 2
print("PASS: modulo-19 squarefreeness certificate and simple finite poles")

# General depressed cubic, using the three polynomial variables as B,C,D and
# a separate univariate coefficient list for Y.
def commutative_univariate_product(left, right):
    result = [P() for _ in range(len(left)+len(right)-1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return result


B_depress, C_depress, D_depress = alpha, beta, I
linear = [-B_depress, P.coerce(1)]
square = commutative_univariate_product(linear, linear)
cube = commutative_univariate_product(square, linear)
depressed = [F(1, 3)*a for a in cube]
for i, coefficient in enumerate(square):
    depressed[i] += B_depress*coefficient
for i, coefficient in enumerate(linear):
    depressed[i] += C_depress*coefficient
depressed[0] += D_depress
assert depressed == [D_depress-B_depress*C_depress+F(2, 3)*B_depress**3,
                      C_depress-B_depress**2, P(), P.coerce(F(1, 3))]

# Exact x=h*x' scaling of every independent potential monomial.
# For a monomial c*x^i*y^j, h*d_x changes its coefficient by h^i;
# h^(-1)[z,h*x'] and h^(-1)[h*x',y] give the target relations.
h_scale = I
for x_degree in range(7):
    for y_degree in range(4):
        if x_degree+2*y_degree > 6:
            continue
        if x_degree:
            assert h_scale*x_degree*h_scale**(x_degree-1) == x_degree*h_scale**x_degree
        if y_degree:
            assert y_degree*h_scale**x_degree == h_scale**x_degree*y_degree
scaled_c_numerator = num_c.sub(alpha=alpha*h_scale**4, beta=beta*h_scale**6)
scaled_d_numerator = num_d.sub(alpha=alpha*h_scale**4, beta=beta*h_scale**6)
assert all(i >= 4 for a, b, i in scaled_c_numerator)
assert all(i >= 6 for a, b, i in scaled_d_numerator)
assert P({(a, b, 0): c for (a, b, i), c in scaled_c_numerator.items() if i == 4}) == 15*alpha
assert P({(a, b, 0): c for (a, b, i), c in scaled_d_numerator.items() if i == 6}) == 15*beta
print("PASS: full depressed-cubic identities and h-scaling of the coefficient relations")
print("Scope: exact coefficient identities; degree five and S5 descent to moduli use the paper's proofs")

# The five distinct roots over the classical zero section and the formal branch
# through alpha=0. beta is still J_branch in this exact coefficient calculation.
zero_quartic = 112*alpha**4+340*alpha**3+900*alpha**2+475*alpha+75
assert quintic.sub(I=0, beta=0) == alpha*zero_quartic
assert discriminant.sub(I=0, beta=0) == P.coerce(7812256185000000000)
assert zero_quartic.sub(alpha=0) == P.coerce(75)
formal_root_two_jet = (I+5*J_branch-F(212, 15)*I**2
                       -F(304, 3)*I*J_branch-F(370, 3)*J_branch**2)
formal_error = quintic.sub(alpha=formal_root_two_jet)
assert all(a == 0 and b+i >= 3 for a, b, i in formal_error)
print("PASS: classical five-root factorization, nonzero discriminant, and quadratic Hensel inverse")

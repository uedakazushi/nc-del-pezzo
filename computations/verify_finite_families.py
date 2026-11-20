#!/usr/bin/env python3
"""Exact universal PBW/Casimir identity, standard library only.

Q[h,p1,p2,p3,p4,p5,q1,q2,q3]<x,y,z>,
[x,y]=h*z, [y,z]=h*P'(x), [z,x]=h*Q'(y),
deg P<=5, deg Q<=3. All coefficients commute.
This verifies polynomial identities, not a truncated parameter expansion.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

VARS = ('h', 'p1', 'p2', 'p3', 'p4', 'p5', 'q1', 'q2', 'q3')
ZERO = (0,) * len(VARS)

def c(v):
    return {ZERO: Fraction(v)} if v else {}

def var(name):
    exp = [0] * len(VARS)
    exp[VARS.index(name)] = 1
    return {tuple(exp): Fraction(1)}

def padd(*polys):
    out = {}
    for poly in polys:
        for exp, value in poly.items():
            out[exp] = out.get(exp, Fraction(0)) + value
    return {exp: value for exp, value in out.items() if value}

def pmul(*polys):
    out = c(1)
    for poly in polys:
        nxt = {}
        for a, av in out.items():
            for b, bv in poly.items():
                exp = tuple(x + y for x, y in zip(a, b))
                nxt[exp] = nxt.get(exp, Fraction(0)) + av * bv
        out = {exp: value for exp, value in nxt.items() if value}
    return out

def nadd(*polys):
    out = {}
    for poly in polys:
        for word, value in poly.items():
            out[word] = padd(out.get(word, {}), value)
    return {word: value for word, value in out.items() if value}

def nscale(poly, scalar):
    return {word: pmul(scalar, value) for word, value in poly.items() if pmul(scalar, value)}

h = var('h')
p = [c(0)] + [var('p' + str(i)) for i in range(1, 6)]
q = [c(0)] + [var('q' + str(i)) for i in range(1, 4)]
P = {'x' * i: p[i] for i in range(1, 6)}
Q = {'y' * j: q[j] for j in range(1, 4)}
Pd = {'x' * (i-1): pmul(c(i), p[i]) for i in range(1, 6)}
Qd = {'y' * (j-1): pmul(c(j), q[j]) for j in range(1, 4)}
rules = {
    'yx': {'xy': c(1), 'z': pmul(c(-1), h)},
    'zx': nadd({'xz': c(1)}, nscale(Qd, h)),
    'zy': nadd({'yz': c(1)}, nscale(Pd, pmul(c(-1), h))),
}

@lru_cache(None)
def nfword(word):
    for i in range(len(word)-1):
        pair = word[i:i+2]
        if pair in rules:
            return nadd(*(nscale(nfword(word[:i] + w + word[i+2:]), coeff)
                          for w, coeff in rules[pair].items()))
    return {word: c(1)}

def nf(poly):
    return nadd(*(nscale(nfword(word), coeff) for word, coeff in poly.items()))

def comm(poly, generator):
    return nf(nadd({generator + w: v for w, v in poly.items()},
                   {w + generator: pmul(c(-1), v) for w, v in poly.items()}))

def sym(a, b):
    words = {''.join(w) for w in permutations('x' * a + 'y' * b)}
    return {w: c(Fraction(1, len(words))) for w in words}

def at_overlap(word, position):
    pair = word[position:position+2]
    return nadd(*({word[:position] + w + word[position+2:]: coeff}
                  for w, coeff in rules[pair].items()))

# The sole overlap for the three rules. Auxiliary weight (6,10,15)
# decreases strictly in correction terms; lex z>y>x orders swaps.
assert nf(at_overlap('zyx', 0)) == nf(at_overlap('zyx', 1))

corr = nadd(*(nscale(sym(i-2, j-2),
            pmul(c(Fraction(i*(i-1)*j*(j-1), 12)), h, h, p[i], q[j]))
            for i in range(2, 6) for j in range(2, 4)))
extra = nadd(
    {'x': pmul(c(Fraction(2,3)),h,h,h,h,p[5],
                padd(pmul(c(3),q[1],q[3]),pmul(c(-1),q[2],q[2])))},
    nscale(Pd, pmul(c(Fraction(-3,2)),h,h,h,h,h,h,p[5],q[3],q[3])))
omega = nadd({'zz': c(Fraction(1, 2))}, P, Q, nscale(corr, c(-1)), extra)
for generator in ('x', 'y', 'z'):
    assert comm(omega, generator) == {}, generator

# Every correction has auxiliary weight <30, and no z² term.
correction = nf(nadd(nscale(corr, c(-1)), extra))
assert all(sum({'x':6,'y':10,'z':15}[letter] for letter in word)<30
           for word in correction)
assert all(word.count('z')<=1 for word in correction)
def specialize_p5(poly, degree):
    if degree == 1:
        return poly
    index = VARS.index('p5')
    return {exp: val for exp, val in poly.items() if exp[index] == 0}

for degree, word_weights, equation_weight, aux_weights, aux_degree in (
        (1, {'x':1,'y':2,'z':3}, 6, {'x':6,'y':10,'z':15}, 30),
        (2, {'x':1,'y':1,'z':2}, 4, {'x':3,'y':4,'z':6}, 12)):
    coefficient_weights = {'h':0}
    coefficient_weights.update({'p'+str(i):equation_weight-i*word_weights['x']
                               for i in range(1,6)})
    coefficient_weights.update({'q'+str(j):equation_weight-j*word_weights['y']
                               for j in range(1,4)})
    def is_homogeneous(poly, target):
        for word, coeff in poly.items():
            for exp in specialize_p5(coeff, degree):
                weight = sum(word_weights[ch] for ch in word)
                weight += sum(e*coefficient_weights[v] for e,v in zip(exp,VARS))
                assert weight == target, (degree,word,exp,weight,target)
    is_homogeneous(omega, equation_weight)
    for lhs, rhs in rules.items():
        is_homogeneous(rhs, sum(word_weights[ch] for ch in lhs))
        for word, coeff in rhs.items():
            if not specialize_p5(coeff, degree):
                continue
            left = sum(aux_weights[ch] for ch in lhs)
            right = sum(aux_weights[ch] for ch in word)
            assert right < left or (right == left and word < lhs)
    for word, coeff in correction.items():
        if specialize_p5(coeff, degree):
            assert sum(aux_weights[ch] for ch in word) < aux_degree
            assert word.count('z') <= 1
print('PASS: both del Pezzo internal gradings and terminating auxiliary orders')
print('PASS: sole overlap and all three universal Casimir commutators')
print('PASS: correction is lower auxiliary degree, monic quadratic z term preserved')
print('Exact coefficient ring: Q[' + ','.join(VARS) + ']')
print('Distinct cached word reductions:', nfword.cache_info().currsize)

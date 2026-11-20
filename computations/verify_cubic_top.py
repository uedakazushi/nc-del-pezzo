#!/usr/bin/env python3
"""Exact free-algebra certificates for the cubic Sklyanin top.

Standard library only. Verifies a relation-ideal certificate, not a finite
jet or sample of parameter values. The quartic is De Laet, arXiv:1612.06158,
Section 5.2. The normalized h=0 limit is checked with t=h^2.
"""
from fractions import Fraction as F

# All coefficient rings are polynomial subrings of Q[a,b,c,alpha,beta,t].
NAMES = ('a', 'b', 'c', 'alpha', 'beta', 't')
ZERO = (0,) * len(NAMES)
def const(value):
    return {ZERO: F(value)} if value else {}
def variable(name):
    ex = [0] * len(NAMES)
    ex[NAMES.index(name)] = 1
    return {tuple(ex): F(1)}
def add(*polys):
    out = {}
    for poly in polys:
        for ex, value in poly.items():
            out[ex] = out.get(ex, F(0)) + value
    return {ex: value for ex, value in out.items() if value}
def mul(*polys):
    out = const(1)
    for poly in polys:
        nxt = {}
        for ex, value in out.items():
            for ey, val in poly.items():
                ez = tuple(x+y for x,y in zip(ex,ey))
                nxt[ez] = nxt.get(ez,F(0)) + value*val
        out = {ex: value for ex, value in nxt.items() if value}
    return out
def neg(poly):
    return {ex: -v for ex,v in poly.items()}
def nadd(*polys):
    out = {}
    for poly in polys:
        for word, coeff in poly.items():
            out[word] = add(out.get(word,{}),coeff)
    return {word: coeff for word,coeff in out.items() if coeff}
def scale(poly, coeff):
    return {word: v for word,c in poly.items() if (v:=mul(c,coeff))}
def nmul(p,q):
    return nadd(*({u+v:mul(a,b)} for u,a in p.items() for v,b in q.items()))
def around(p,u,v):
    return {u+w+v:c for w,c in p.items()}
def comm(p,q):
    return nadd(nmul(p,q),scale(nmul(q,p),const(-1)))
def words(*ws):
    return {w:const(1) for w in ws}

a,b,c,alpha,beta,t = (variable(n) for n in NAMES)
a2,b2,c2 = mul(a,a),mul(b,b),mul(c,c)
r1 = {'yyx':a, 'xyy':a, 'yxy':b, 'xxx':c}
r2 = {'xxy':a, 'yxx':a, 'xyx':b, 'yyy':c}
C = nadd(scale(words('xyxy','yxyx'),mul(b,add(a2,neg(c2)))),
         scale(words('yxxy','xyyx'),mul(a,add(b2,neg(a2)))),
         scale(words('xxyy','yyxx'),mul(a,add(c2,neg(a2)))),
         scale(words('xxxx','yyyy'),mul(c,add(a2,neg(b2)))))
# A nine-term identity in the FREE algebra, before quotienting.
terms = [(neg(add(a2,c2)),r1,'','xx'),
         (mul(const(-2),a,c),r1,'','yy'),
         (add(a2,b2),r1,'x','x'),
         (neg(add(b2,neg(c2))),r1,'xx',''),
         (mul(const(2),a,c),r1,'yy',''),
         (mul(const(-2),a,b),r2,'','xy'),
         (neg(add(a2,b2)),r2,'','yx'),
         (add(a2,b2),r2,'x','y'),
         (mul(const(2),a,b),r2,'yx','')]
certificate = nadd(*(scale(around(r,u,v),coef) for coef,r,u,v in terms))
assert comm(C,words('x')) == certificate
swap = str.maketrans({'x':'y','y':'x'})
assert {w.translate(swap):v for w,v in C.items()} == C
assert comm(C,words('y')) == {w.translate(swap):v for w,v in certificate.items()}

subs = {'a':add(const(1),mul(const(F(2,3)),beta,t)),
        'b':add(const(-2),mul(const(F(2,3)),beta,t)),
        'c':mul(alpha,t)}
def substitute(poly):
    out={}
    for ex,value in poly.items():
        term=const(value)
        for name,power in zip(NAMES,ex):
            for _ in range(power):
                term=mul(term,subs.get(name,variable(name)))
        out=add(out,term)
    return out
def mod_t(poly):
    return {ex:v for ex,v in poly.items() if ex[-1]==0}
def divide_t(poly):
    assert all(ex[-1]>0 for ex in poly)
    return {ex[:-1]+(ex[-1]-1,):v for ex,v in poly.items()}
Ct={w:substitute(v) for w,v in C.items()}
C0={w:mod_t(v) for w,v in Ct.items() if mod_t(v)}
dC={w:divide_t(add(v,neg(C0.get(w,{})))) for w,v in Ct.items()}
Ux=nadd(scale(words('xxx'),alpha),
        scale(words('xyy','yxy','yyx'),mul(const(F(2,3)),beta)))
Uy=nadd(scale(words('yyy'),alpha),
        scale(words('yxx','xyx','xxy'),mul(const(F(2,3)),beta)))
x,y=words('x'),words('y')
delta=comm(x,y)
E=nadd(nmul(x,Ux),nmul(y,Uy))
assert nadd({w:substitute(v) for w,v in r1.items()},
            comm(y,delta),scale(Ux,neg(t))) == {}
assert nadd({w:substitute(v) for w,v in r2.items()},
            comm(delta,x),scale(Uy,neg(t))) == {}
# C0 = -4[x,y]^2 + x[y,[x,y]] + y[[x,y],x].
assert C0 == nadd(scale(nmul(delta,delta),const(-4)),
                  nmul(x,comm(y,delta)),nmul(y,comm(delta,x)))
# Omega = z²/2 - ((C-C0)/t + E)/8, a polynomial in t=h².
omega_xy=scale(nadd(dC,E),const(F(-1,8)))
expected=nadd(scale(words('xxxx','yyyy'),mul(const(F(1,4)),alpha)),
              scale(words('xxyy','xyxy','xyyx','yxxy','yxyx','yyxx'),
                    mul(const(F(1,6)),beta)))
assert {w:mod_t(v) for w,v in omega_xy.items() if mod_t(v)} == expected
print('PASS: nine-term free-algebra certificate for both quartic commutators')
print('PASS: Sklyanin parameter substitution and eliminated relations')
print('PASS: C0 identity and polynomial normalized classical limit')
print('Exact coefficient ring: Q[a,b,c,alpha,beta,t], t=h^2')

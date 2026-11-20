#!/usr/bin/env python3
"""Exact finite-jet certificate for the simultaneous degree-one center.

Work in Q[h,a0,...,a4,b0,...,b6]<x,y,z> modulo h^6, with
[x,y]=h*z, [z,x]=h*(y^2+A(x)),
[y,z]=h*(Sym(A'(x)*y)+B'(x)), deg A<=4, deg B<=6.
All polynomial coefficients are independent variables. No numerical sampling
or third-party package is used. This is explicitly a finite jet, not an exact
central-element formula at finite h. Its role is Lemma
degree-one-fourth-center-jet in the main paper.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import prod

VARS=('h',)+tuple('a'+str(i) for i in range(5))+tuple('b'+str(i) for i in range(7))
ZERO=(0,)*len(VARS)
LIMIT=5
def c(v): return {ZERO:Q(v)} if v else {}
def var(name):
 e=list(ZERO);e[VARS.index(name)]=1;return {tuple(e):Q(1)}
def pa(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,Q(0))+v
 return {k:v for k,v in d.items() if v}
def pm(*ps):
 d=c(1)
 for p in ps:
  t={}
  for k,v in d.items():
   for l,w in p.items():
    m=tuple(a+b for a,b in zip(k,l))
    if m[0]<=LIMIT:t[m]=t.get(m,Q(0))+v*w
  d={k:v for k,v in t.items() if v}
 return d
def na(*ps):
 d={}
 for p in ps:
  for w,v in p.items():d[w]=pa(d.get(w,{}),v)
 return {w:v for w,v in d.items() if v}
def ns(p,q):return {w:pm(q,v) for w,v in p.items() if pm(q,v)}
def symword(word):
 ws=set(map(''.join,permutations(word)))
 return {w:c(Q(1,len(ws))) for w in ws}
h=var('h'); aa=[var('a'+str(i)) for i in range(5)];bb=[var('b'+str(i)) for i in range(7)]
def derivative(co,j):
 return {'x'*(i-j):pm(c(prod(range(i-j+1,i+1))),co[i]) for i in range(j,len(co))}
A=lambda j:derivative(aa,j)
B=lambda j:derivative(bb,j)
def np(*ps):
 d={'':c(1)}
 for p in ps:d=na(*({w+v:pm(a,b)} for w,a in d.items() for v,b in p.items()))
 return d
def sy(p):return na(*(ns(symword(w),v) for w,v in p.items()))
rules={
 'yx':('xy',{'z':c(-1)}),
 'zx':('xz',na({'yy':c(1)},A(0))),
 'zy':('yz',ns(na(sy(np(A(1),{'y':c(1)})),B(1)),c(-1)))
}
@lru_cache(None)
def nfword(w,N):
 for i in range(len(w)-1):
  pair=w[i:i+2]
  if pair in rules:
   ordered,rem=rules[pair]
   out=nfword(w[:i]+ordered+w[i+2:],N)
   if N>0:out=na(out,*(ns(nfword(w[:i]+v+w[i+2:],N-1),pm(h,k)) for v,k in rem.items()))
   return out
 return {w:c(1)}
def nf(p,N):
 out={}
 for w,k in p.items():
  for e,v in k.items():
   if e[0]<=N:out=na(out,ns(nfword(w,N-e[0]),{e:v}))
 return out
def comm(p,g,N):return nf(na({w+g:v for w,v in p.items()},{g+w:pm(c(-1),v) for w,v in p.items()}),N)
def flatcom(p,N):
 d={}
 for g in 'xyz':
  for w,q in comm(p,g,N).items():
   for e,v in q.items():d[(g,w,e)]=v
 return d
F=na({'zz':c(Q(1,2)),'yyy':c(Q(1,3))},sy(np(A(0),{'y':c(1)})),B(0))
C2=[sy(np(A(2),{'yy':c(1)})),sy(np(B(2),{'y':c(1)})),np(A(0),A(2)),np(A(1),A(1))]
sol2=(Q(-1,6),Q(-1,6),Q(0),Q(1,12))
Omega2=na(F,*(ns(b,pm(c(v),h,h)) for b,v in zip(C2,sol2)))
assert not flatcom(Omega2,3)
C4=[sy(np(A(4),{'yyy':c(1)})),sy(np(B(4),{'yy':c(1)})),
    sy(np(A(0),A(4),{'y':c(1)})),sy(np(A(1),A(3),{'y':c(1)})),sy(np(A(2),A(2),{'y':c(1)}))]
C4 += [np(A(i),B(4-i)) for i in range(5)]
sol4=(Q(0),Q(0),Q(1,180),Q(1,72),Q(0),Q(1,180),Q(1,120),Q(-1,120),Q(-1,180),Q(0))
Omega4=na(Omega2,*(ns(b,pm(c(v),h,h,h,h)) for b,v in zip(C4,sol4)))
for generator in 'xyz':
 assert not comm(Omega4,generator,5), generator

# Internal grading: coefficient a_i has weight 4-i, b_i has weight 6-i.
weights={'h':0,**{'a'+str(i):4-i for i in range(5)},
         **{'b'+str(i):6-i for i in range(7)}}
for word,coeff in Omega4.items():
 for exponent in coeff:
  assert sum({'x':1,'y':2,'z':3}[u] for u in word)+sum(e*weights[name] for e,name in zip(exponent,VARS))==6
# The fully symmetric (not ordered) expression has exactly z^2/2.
assert Omega4['zz']==c(Q(1,2))
assert all('z' not in word or word=='zz' for word in Omega4)
print('PASS: universal order-two correction is central modulo h^4')
print('PASS: all three order-four corrected commutators vanish modulo h^6')
print('PASS: internal degree six and fully symmetric z^2 normalization')
print('Exact coefficient ring: Q[h,a0,...,a4,b0,...,b6]/(h^6)')
print('This certificate proves the finite jet only; the full center uses the geometric lifting proof.')

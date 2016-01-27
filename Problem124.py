from UsefulFunctions import *
from functools import reduce
from operator import mul
def rad(n):
    primes = primeDecomposition(n).keys()
    return reduce(mul,primes)
print rad(2)
def comp(m,n):
    rm = rad(m)

    rn = rad(n)

    if rm>rn:
        return 1
    elif rm<rn:
        return -1
    else:
        if m>n:
            return 1
        else:
            return -1

n = range(2,21)
print n, map(rad,n)
n.sort(cmp = comp)
print n
nums = range(2,100001)

a = sorted(nums,cmp=comp)
print a[9998],a[9999],a[10000],a[10001]

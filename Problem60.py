__author__ = 'Opemipo'
import itertools
import math
import random

def primeslessthan(n):
    if n==1:
        return []

    nums =[1]*n
    listofprimes = []
    nums[0] =nums[1]=0
    i=2
    while i*i<n:
        if nums[i] is 1:
            listofprimes.append(i)
            ti = i*i
            a = n - ti
            b = i
            nm = a/b +int(a%b>0)
            nums[ti::i] = [0]*nm
        i = i+1
    for b in xrange(i,n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes

def concatenate(n,m):
    res =0
    d = 1
    while m>0:
        res += (m%10)*d
        m/=10
        d*=10
    #d = 1
    while n>0:
        res += (n%10)*d
        n/=10
        d *= 10
    return res
def miller_rabin(m, k):
    s=1
    t = (m-1)/2
    while t%2 == 0:
        t /= 2
        s += 1

    for r in range(0,k):
        rand_num = random.randint(1,m-1)
        y = pow(rand_num, t, m)
        prime = False

        if (y == 1):
            prime = True


        for i in range(0,s):
            if (y == m-1):
                prime = True
                break
            else:
                y = (y*y)%m

        if not prime:
            return False

    return True

def isprime(n):
    if n<2:
        return False
    if n%2==0:
        return False
    if n%3==0:
        return False
    if n%5==0:
        return False
    else:
        return miller_rabin(n,10)

def satisfyProperty(i):
    for j in itertools.permutations(i,2):
        if isprime(concatenate(j[0],j[1]))== False:
            return False
    return True

N,K = 20000,5#map(int,raw_input().split())

listprimes = primeslessthan(N)
flag = False
for i in itertools.combinations(listprimes,K):
    if satisfyProperty(i):
        print sum(i),i


__author__ = 'Opemipo'
from UsefulFuntions import *
def eulertotient(n):

    res = n
    i = 2
    while i*i<=n:
        if n%i==0:
            res -= res/i
            while n%i == 0:
                n/=i
        i+=1
    if n>1:
        res -= res/n
    return res
def sameDigits(n,m):
    sn = list(str(n))
    sm = list(str(m))
    sn.sort()
    sm.sort()
    if sn == sm:
        return True
    else:
        return False


maxi = 0
maxval = 0
for i in xrange(2,30029):
    euler = eulertotient(i)
    #print maxval,i
    if maxi<float(i)/euler:

        maxi = float(i)/euler
        maxval = i
print maxval,maxi

print 'other solution'
listprimes = primeslessthan(10000000)
#print listprimes
n = 2
i =1
while n<1000000000000000000:
    print listprimes[i]
    n *= listprimes[i]
    print n,'val = ', float(n)/eulertotient(n)
    i += 1
print 'max = ', n/listprimes[i-1]
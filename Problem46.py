__author__ = 'Opemipo'

import math
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

def isprime(n):
    if n<2:
        return False
    if n%2==0:
        return False
    if n%3==0:
        return False
    if pow(210,n-1,n)!=1:
        return False
    else:
        i = 1
        sign = -1
        test =5
        limit = int(math.sqrt(n))
        while test< limit+1:
            limit =n/test
            test= 6*i+sign
            if n%test==0:
                return False
            sign =-sign
            test= 6*i+sign
            if n%test==0:
                return False
            #print test
            i+=1
            #test+=1

        return True

def isGoldbach(N):
    listprimes = primeslessthan(N)
    for j in listprimes:
        if (N-j)%2 == 1:
            #print N
            pass
        elif int(math.sqrt((N-j)/2))**2 == ((N-j)/2):
            return True
    return False

for i in xrange(1,20000,2):
    if not isGoldbach(i) and not isprime(i):
        print i
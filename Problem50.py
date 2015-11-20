__author__ = 'Opemipo'
import random
import math

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
def numdigits(n):
    return int(math.log10(n))+1

#N = input()
max =0
maxPrime = 0
flag = False
listprimes = primeslessthan(1700000)
l = len(listprimes)
partialSum = [0]*(l+1)
for i in xrange(1,l+1):
    partialSum[i] = partialSum[i-1]+listprimes[i-1]

for k in reversed(xrange(l)):
    for i in xrange(l-k+2):
        print partialSum[k-1+i]-partialSum[i], numdigits(partialSum[k-1+i]-partialSum[i])
        if (partialSum[k-1+i]-partialSum[i])>1000000:
            break
        if isprime(partialSum[k-1+i]-partialSum[i]) and (partialSum[k-1+i]-partialSum[i])<1000000:
            max = k
            maxprime = partialSum[k-1+i]-partialSum[i]
            flag = True
            break
    if flag:
        break
print maxprime,max


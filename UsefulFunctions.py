__author__ = 'Opemipo'
import math
def millerrabin(n):
    num = n-1
    s = 0
    d = 1
    while num%2 == 0:
        s += 1
        num/=2
    d = num

    for a in [2,3,5,7,11,13,17,19,23]:
        x = pow(a,d,n)
        if x == 1 or x == n-1:
            continue
        for j in xrange(1,s):
            x = pow(x,2,n)
            if x == 1:
                return False
            if x == n-1:
                break
    return True
import random
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


#print millerrabin(200)

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

#print 'lenght',len(primeslessthan(10000))-len(primeslessthan(1000))

def primeDecomposition(n):
    listprimes = primeslessthan(int(math.sqrt(n))+1)
    #print listprimes
    primefactorization = {}
    for a in listprimes:
        if a >n:
            break
        while n%a == 0:
            primefactorization[a] = primefactorization.get(a,0)+1
            n/=a
        if n==1:
            break
    if n>1:
        primefactorization[n] = 1
    return primefactorization


'''
i = 20
len1 = len(primeDecomposition(i-4))
len2 = len(primeDecomposition(i-3))
len3 = len(primeDecomposition(i-2))
len4 = len(primeDecomposition(i-1))

for i in xrange(2000,200000):
    len1 = len2
    len2 = len3
    len3 = len4
    len4 = len(primeDecomposition(i))
    if len1==len2==len3==len4==4:
        print i-3,

'''


def factorial(n):
    if n<0:
        return 'error'
    if n==0:
        return 1
    prod =1
    for i in xrange(1,n+1):
        prod *= i
    return prod
def list2num(listnum):
    num = 0
    d = 1
    for i in reversed(listnum):
        num +=(i*d)
        d *= 10
    return num
#print list2num([1,3,4,5])
def theNthPerm(na,numdigit):
    n = na#-1
    num = numdigit
    perm =[]
    while num>0:
        perm.append(n/factorial(num-1))
        n%=factorial(num-1)
        num -= 1

    return perm

def perm(n,numdigit):
    word =[]
    alphabets = range(1,numdigit+1)
    order = theNthPerm(n,numdigit)

    for i in order:
        #pick the ith item left
        word.append(alphabets[i])
        #i += 1
        del alphabets[i]
    return word

def pandigital(n):
    permations =[]
    for i in xrange(factorial(n)):
        permations.append(list2num(perm(i,n)))
    return permations

def numdigits(n):
    return int(math.log10(n))+1

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

def primesbetween(m,n):
    if n==1:
        return []

    nums =[1]*n
    listofprimes = []
    nums[0] =nums[1]=0
    i=2
    while i*i<n:
        if nums[i] is 1 :
            #print i,m
            if i>=m:
                #print i, 'here'
                listofprimes.append(i)
            ti = i*i
            a = n - ti
            b = i
            nm = a/b +int(a%b>0)
            nums[ti::i] = [0]*nm
            #print 'here'
        i = i+1
    for b in xrange(i,n):
        if nums[b] is 1:
            if b>=m:
                listofprimes.append(b)

def isPower(n, b):
    return b**int(math.log(n, b)+.5)==n

def isPandigital(n,k):
    num = n
    numdigit = numdigits(n)
    if numdigit > k:
        return False
    #print 'here', numdigit
    a = set([])
    i = 0
    while n>0: #for i in xrange(numdigit):
        if n%10==0:
            return False
        if k==8:
            if n%10==9:
                return False

        a.add(n%10)
        n /= 10
        i+=1
    if len(a)== k and i==k:
        return True
    else:
        return False


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

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        if (sieve[i]):
            k = i * i
        while (k <= n):
            sieve[k] = False
            k += i
        i += 1
    return sieve

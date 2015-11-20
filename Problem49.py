__author__ = 'Opemipo'
import math
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

    return listofprimes
FourDigitPrimes = primesbetween(1000,1000000)
def sameDigits(n,m):
    sn = list(str(n))
    sm = list(str(m))
    sn.sort()
    sm.sort()
    if sn == sm:
        return True
    else:
        return False
#print sameDigits(1487,4817)

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
def numdigits(n):
    return int(math.log10(n))+1
print 'here'
for i in xrange(len(FourDigitPrimes)):
    for j in xrange(i,len(FourDigitPrimes)):
        if sameDigits(FourDigitPrimes[i],FourDigitPrimes[j]):
            d = FourDigitPrimes[j]-FourDigitPrimes[i]
            newNum = FourDigitPrimes[j]+d
            if numdigits(FourDigitPrimes[i]) is not numdigits(FourDigitPrimes[j]):
                print ' broken'
                break
            if sameDigits(newNum,FourDigitPrimes[j]) and isprime(newNum) and d>0:
                print FourDigitPrimes[i],FourDigitPrimes[j],newNum,#FourDigitPrimes[i]+FourDigitPrimes[j]+newNum

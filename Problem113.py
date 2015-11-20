"""Solution based on a recursive formula. I will be using dynamic programming or is it
memoization?"""
from math import factorial

InAr = [[-1 for i in xrange(101)] for i in xrange(101)]
DeAr = [[-1 for i in xrange(11)] for i in xrange(11)]


def incrNum(n,r):
    if n==0:
        return 1
    if r == 0:
        InAr[n][r]=1
        return 1
    if InAr[n][r]==-1:
        s = 0
        for i in xrange(0,r+1):
            s+=incrNum(n-1,i)
        InAr[n][r] = s
        return InAr[n][r]
    else:
        return InAr[n][r]

def decNum(n,r):
    """Decreasing numbers with n digits and r being the last digit"""
    
    if n==1:
        return 1
    if r == 10:
        DeAr[n][r]=1
        return 1
    if DeAr[n][r]==-1:
        s = 0
        for i in xrange(r,11):
            s+=decNum(n-1,i)
        DeAr[n][r] = s
        return DeAr[n][r]
    else:
        return DeAr[n][r]
def NumInc(n):
    return factorial(n+9)/(factorial(9)*factorial(n))


def NumDec(n):
    return factorial(n+10)/(factorial(10)*factorial(n))


def numNonBouncy(n):
    return factorial(n+9)/(factorial(9)*factorial(n))+factorial(n+10)/(factorial(10)*factorial(n))-2-10*n

print incrNum(8,9)
print NumInc(8)
print decNum(9  ,0)
print NumDec(8)
#print numNonBouncy(6)
#print numNonBouncy(10)
#print numNonBouncy(100)

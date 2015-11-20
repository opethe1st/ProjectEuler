__author__ = 'Opemipo'
import math

def combination(n,r):
    #print n,r,' n and r'
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
def numovermillion(n,k):
    if n<23:
        return 0
    r = 1
    a = combination(n,r)
    while a< k:
        r += 1
        a = combination(n,r)
    return n-2*r+1

N,K = map(int,raw_input().split())
count = 0
for i in xrange(23,N+1):
    #print i, numovermillion(i)
    count += numovermillion(i,K)
print count


#print math.factorial(1000)
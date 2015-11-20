""""""
#from __future__ import division
import time as t
from UsefulFunctions import primeDecomposition
def numFactors(n):
    prod = 1
    primes = primeDecomposition(n)
    for k in primes.keys():
        prod*=(2*primes[k]+1)
    return (prod+1)/2

def numSoln(n):
    return numFactors(n)

#print numSoln(4)


#'''
start = t.time()
i = 1000
nSoln = numSoln(i)
while nSoln<=1000:
    i+=1
    nSoln = numSoln(i)
    #print nSoln
print i
print 'it took ',t.time()-start
#'''

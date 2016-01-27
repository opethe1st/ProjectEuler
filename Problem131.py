from UsefulFunctions import primeslessthan
import math

primes = primeslessthan(1000000)

def solve(p):
    #3x2-3x+1-p
    #solution is -b+-sqrt(b2-4ac)/2a
    if ((3+math.sqrt(9-4*(1-p)*3))/(2*3))%1==0:
        return True
    else:
        return False
    return (3+math.sqrt(9-4*(1-p)*3))/(2*3)

count = 0
for p in primes:
    if solve(p):
        print p
        count+=1
print count

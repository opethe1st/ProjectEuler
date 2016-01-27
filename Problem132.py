
from UsefulFunctions import primeslessthan

listprimes = primeslessthan(1000000)

print pow(10,1000000000,7)
count = 0
s = 0
for p in listprimes:
    
    if pow(10,1000000000,9*p)==1:
        print p
        s+=p
        count+=1
    if count==40:
        break
print count, s

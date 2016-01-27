from UsefulFunctions import *

#print primeslessthan(10000)
for i,p in enumerate(primeslessthan(10000000)):
    if ((2*(i+1)*p)%p**2>10e11):
        print i+1,p
        break

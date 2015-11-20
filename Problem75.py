__author__ = 'Opemipo'
import math
import fractions

L =1500000
triangle = [0]*(L+1)

res = 0
nMax = int(math.sqrt(L/2))

for m in xrange(2,nMax):
    for n in xrange(1,m):
        #print m,n
        if (n+m)%2==1 and fractions.gcd(n,m)==1:
            p = 2*m*(n+m)
            #print p
            while p<=L:
                triangle[p]+=1
                if triangle[p]==1:
                    res+=1
                if triangle[p]==2:
                    res-=1
                p+=2*m*(n+m)

print res

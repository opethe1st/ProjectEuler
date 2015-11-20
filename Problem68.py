__author__ = 'Opemipo'

import numpy

A = numpy.array([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1],[1,0,0,0,1]])

#from numpy  import *
import itertools

def isValid(a):
    N = len(a)
    seta = set(a)
    #x = s-a[-1]-a[0]
    for i in xrange(0,N):
        x = s-a[i]-a[i-1]

        if x<=0 or x>2*N:
            return False
        seta.add(x)
    #print seta,len(seta)
    if len(seta) == 2*N:
        #print 'true'
        return True
    else:
        return False




N = 10
s = 27
res = []
#print isValid([5,3,1,4,2])

def formdigits(outer,inner):
    res = []
    #print outer,inner
    for i in xrange(N-1):
        #print i,[outer[i],inner[i],inner[i+1]]
        res.extend([outer[i],inner[i],inner[i+1]])
    res.extend([outer[-1],inner[-1],inner[0]])
    #print res ,type(res)
    return "".join(map(str,res))
#print formdigits([1,2,3,4,6],[5,6,7,7,8])


for a in itertools.combinations(range(1,2*N+1),N):
    #print 'here'
    if sum(a)!=(N*s-N*(2*N+1)):
        #print 'here2'
        continue
    else:
        #print 'here'
        for b in itertools.permutations(a,N):
            #print b
            if isValid(b):
                outer =[0]*N
                for i in xrange(1,N):
                    outer[i-1] = s-b[i]-b[i-1]
                outer[-1] = s- b[-1]-b[0]
                if outer[0]==min(outer):
                    #print outer,b
                    res.append(formdigits(outer,b))
                    #res.append(a)
res.sort()
for n in res:
    print n
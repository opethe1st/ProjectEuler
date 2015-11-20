__author__ = 'Opemipo'

import math
def penta(n):
    return n*(3*n-1)/2
def ispenta(P):
    num = int(math.sqrt(2*P/3))+1
    #print num
    if P == num*(3*num-1)/2:
        return True
    else:
        return False
'''
N,m = 10000,1000#map(int,raw_input().split())
for k in xrange(1,m):
    for i in xrange(k+1,N):
        if ispenta(penta(i)+penta(i-k)) and ispenta(penta(i)-penta(i-k)):
            print penta(i)-penta(i-k)
'''
i = 1
res = -1
while res == -1:
    for j in xrange(1,i):
        if ispenta(penta(i)+2*penta(j)) and ispenta(penta(i)+penta(j)):
            res = penta(i),penta(j),penta(i)-penta(j)
            #print ispenta(penta(i)-penta(j)),ispenta(penta(i)+penta(j))
    i+=1
print res
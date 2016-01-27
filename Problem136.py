"""
"""
import math
count = 0
Num = 50000000
#Num = 100
for n in xrange(Num):
    k = 0
    for d in xrange(int(math.ceil(math.sqrt(n)/4.0)),int(math.ceil((math.sqrt(n/2.0))))+2):
        try:
            #print d,
            if (math.sqrt(4*d**2-n)%1==0 and d+math.sqrt(4*d**2-n)>0):
                k+=1
        except ValueError:
            pass
    if k==1:
        count+=1
        print n
print count

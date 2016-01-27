"""go through the numbers. from 10 is sum of digit raised to a particular power equal to the number?
if yes, add to the sequence.
How about go through only the numbers that are powers.How can that be done in order? a**b.
This reminds of an earlier problem.I will have to check """
import math
import time as t
i = 10
def sumofdigits(n,b):
    s = 0
    while n>0:
        d = n%b
        s+=d
        n/=b
    return s

#print sumofdigits(12345)

def generatePowers(n):
    l = set()
    for i in xrange(2,int(math.sqrt(n))+2):
        p = i
        while p<n:
            p*=i
            l.add(p)
    return sorted(list(l))

#print generatePowers(1000000)

def isPower(a, b):
    l = int(math.log(a))
    p = a**(l)
    while p<b and a>1:
        p*=a
    if b==p:
        return True
    else:
        return False
start = t.time()
seq = []
count = 0
for p in generatePowers(10e10):
    if isPower(sumofdigits(p,10),p):
        print p,
        seq.append(p)
        count+=1
        print count


print seq, len(seq)
print 'It took',t.time()-start

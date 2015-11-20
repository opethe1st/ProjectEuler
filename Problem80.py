__author__ = 'Opemipo'

from decimal import *
getcontext().prec = 102

def intr(n):
    if n=='.':
        return 0
    else:
        return int(n)

print str(Decimal(2).sqrt())
print len(str(Decimal(2).sqrt()))
print sum(map(intr,list(str(Decimal(2).sqrt()))[:-2]))

def intr(n):
    if n=='.':
        return 0
    else:
        return int(n)

summ = 0
for i in xrange(1,101):

    print i,sum(map(intr,list(str(Decimal(i).sqrt())[:-2])))
    summ+=sum(map(intr,list(str(Decimal(i).sqrt())[:-2])))
print summ


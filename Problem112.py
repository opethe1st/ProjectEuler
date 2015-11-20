""""
Some thoughts on the problem. This doesnt deal with just powers of 10. The final task is to find the
least number for which the proportion of bouncy number is exactly 99%.
prelimary task would be to find for a given number, the proportion of bouncy numbers below it.
need a way of identifying if a given number is a bouncy number.
My initial strategy is to start from 100. and count bouncy number and calculate the proportion till we
get 99%.
"""
import time as t
def isBouncyNumber(n):
    "takes a number. returns true or false"
    l = list(str(n))
    lsorted = sorted(l)
    lrsorted = list(reversed(lsorted))  #sorted(l,reverse=True)
    if l==lsorted or l== lrsorted:
        return False
    else:
        return True

#print isBouncyNumber(1234567)
#print isBouncyNumber(2434556)
start = t.time()
prop = 0 # for 1-100 all non-bouncy numbers. they are increasing or decreasing

i = 100
BouncyCount = 0.0
while prop!=0.99:
    i+=1
    if isBouncyNumber(i):
        BouncyCount+=1
    prop = BouncyCount/i
    #print i ,prop

print i,t.time()-start
BouncyCount=0
for i in xrange(1,1000000):
    if isBouncyNumber(i):
        BouncyCount+=1
print 1000000-BouncyCount-1

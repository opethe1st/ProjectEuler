__author__ = 'Opemipo'

def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)


count = 0
A =2
for d in xrange(5,12001):
    for n in xrange(d/(A+1)+1,d-1/A+1):
        if gcd(n,d)==1:
            count+=1

print count


import math
def isPandigital(n):
    num = n
    a = set([])
    for i in xrange(9):
        if n%10==0:
            return False
        a.add(n%10)
        n /= 10
    if len(a)== 9:
        return True
    else:
        return False

def numdigits(n):
    return int(math.log10(n))+1

sum = 0
prod = set([])
for i in xrange(1,10):
    for j in xrange(1234,9876):
        if numdigits(i*j)==4:
            n = i*pow(10,8)+j*pow(10,4)+i*j
            #print n
            if isPandigital(n):
                prod.add(i*j)

for i in xrange(12,98):
    for j in xrange(123,987):
        if numdigits(i*j)==4:
            n = i*pow(10,7)+j*pow(10,4)+i*j
            #print n
            if isPandigital(n):
                prod.add(i*j)

print prod
for i in list(prod):
    sum += i

print sum
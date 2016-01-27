from UsefulFunctions import eulertotient
import fractions
#'''
def A(n):
    print
    print n,
    for i in xrange(2,n+1):
        if pow(10,i,9*n)==1:
            print 'p',pow(10,i,9*n),'i',i
            return i
    return -1
'''
def A(n):
    x = 1
    k = 1
    while x!=0 and fractions.gcd(10,n)==1:
        x = (10*x+1)%n
        k+=1
    return k
'''
#print An(7)
#print An(41)

for i in xrange(1000000,1000100):
    print i
    if A(i)>1000000:
        print i, A(i)
        break

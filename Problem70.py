__author__ = 'Opemipo'
def eulertotient(n):

    res = n
    i = 2
    while i*i<=n:
        if n%i==0:
            res -= res/i
            while n%i == 0:
                n/=i
        i+=1
    if n>1:
        res -= res/n
    return res
def sameDigits(n,m):
    sn = list(str(n))
    sm = list(str(m))
    sn.sort()
    sm.sort()
    if sn == sm:
        return True
    else:
        return False


mini = 100000
minival = 10000
for i in xrange(2,1000001):
    #print i
    euler = eulertotient(i)
    if mini>float(i)/euler and sameDigits(euler,i):
        #if mini>float(i)/euler:
        mini = float(i)/euler
        minival = i
print minival,mini

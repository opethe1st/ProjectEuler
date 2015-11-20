__author__ = 'Opemipo'

def P(L):
    phi = range(L+1)
    for n in range(2, L+1):
        if phi[n] == n:
            for k in range(n, L+1, n):
                phi[k] -= phi[k] // n
    return sum(phi) - 1

print "Project Euler 72 Solution =", P(1000000)




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

D = 1000000
s = 0
for a in xrange(2,D+1):
    #print eulertotient(a)
    s+=eulertotient(a)
print s


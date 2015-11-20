def sumdigits(n):
    s = 0
    while n>0:
        s += n%10
        n /= 10
    return s
def a(n):
    if n==0:
        return 2
    if n%3!=2:
        return 1
    else:
        return 2*(n+1)/3

hn1 = 1
kn1 = 0
hn2 = 0
kn2 = 1

def numberIterations(n):
    hn1 = 1
    kn1 = 0
    hn2 = 0
    kn2 = 1

    for i in xrange(n):
        hn = a(i)*hn1 + hn2
        kn = a(i)*kn1 + kn2
        #print hn,kn,a(i)
        hn2 = hn1
        kn2 = kn1
        hn1 = hn
        kn1 = kn
    return hn,kn

print sumdigits(numberIterations(100)[0])
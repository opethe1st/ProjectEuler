
def maxr(a):
    l = []
    for i in xrange(1,a+2):
        l.append((2*(i)*a)%(a**2))
    return max(l)

#print maxr(7)
s = 0
for i in xrange(3,1001):
    #print maxr(i)
    s+=maxr(i)
print s

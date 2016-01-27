import time
start = time.time()
n = 7100
#A = [i*i for i in xrange(n)]

#partialSumSq = [(i*(i+1)*(2*i+1)/6) for i in xrange(n-1)]

def sumsq(i):
    return (i*(i+1)*(2*i+1)/6)
def isPalindrome(n):
    return str(n) == str(n)[::-1]

count = 0
s = 0
listn = set()
for i in xrange(2,n-1):
    for j in reversed(xrange(i-1)):
        #print i,j,partialSumSq[i]-partialSumSq[j]
        p = sumsq(i)-sumsq(j)
        if p>10e7:
            break
        if isPalindrome(p) and (p<10e7) :
            #print j,i,  p
            count+=1
            #s+=p
            listn.add(p)
print count
print sum(listn)
print 'it took ',time.time()-start

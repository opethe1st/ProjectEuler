__author__ = 'Opemipo'


import math
def isPower(n, b):
    #changing the definition to mean, b is the exponent
    a = int(pow(n,1.0/b))
    if pow(a,b)==n:
        return True
    elif pow(a+1,b)==n:
        return True
    else:
        return False
    #return b**int(math.log(n, b)+.5)==n


def highestPower(n):
    highestpowerpossible = int(math.log(n,2))
    for i in reversed(xrange(2,highestpowerpossible+1)):
        if isPower(n,i):
            return i
    return 1
print isPower(1024,2)
print highestPower(1024)
N = input()

countdup = 0
for a in xrange(2,N+1):
    k = highestPower(a)
    count = 0
    s1 = set([])
    for i in xrange(2,k):
        if k%i==0:
            for l in xrange(1,i):
                #print 'i',l,
                #print 'here',l,i
                for j in xrange(2,N*l/i+1):
                    if j%l==0 :
                        #print 'j',j
                        s1.add(j)


    for i in xrange(1,k):
        #print 'i',i,
        for j in xrange(2,N*i/k+1):

            if j%i==0 :
                #print 'j',j,
                s1.add(j)
    #print s1,
    count = len(s1)
    countdup += len(s1)
    #print a,'dup',count, countdup#,pow(N-1,2)
#print countdup
print pow(N-1,2)-countdup

N = input()

#print 'repeats?',repeat(4,3)
s1 = set([])
distinctpowersn = {}

def finddistinctpowers(N):
    #if distinctpowersn.has_key(N):
        #return distinctpowersn[N]
    count = 0
    for a in xrange(2,N+1):
        for b in xrange(2,N+1):
            if distinctpowersn.has_key(math.log(a**b)):
                continue
            else:
                distinctpowersn[math.log(a**b)] = 1
                count+=1
    #distinctpowersn[N] = len(s1)
    return count, pow(N-1,2)-count
print finddistinctpowers(N)
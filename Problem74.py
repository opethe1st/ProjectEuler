__author__ = 'Opemipo'

def nextNum(a):
    import math
    summ=0
    while a>0:
        d=a%10
        summ+=math.factorial(d)
        a=a/10
    return summ

print nextNum(0)

def generateChain(i,maxl):
    ls = []
    count = 0
    while i not in ls and count<=maxl:
        ls.append(i)
        count+=1
        i = nextNum(i)
    if maxl==i:
        ls=[]
    return ls

print generateChain(0,6)
nterms = [0]*1000001

print generateChain(145,6)
for i in xrange(1000001):
    #print
    if nterms[i]==0:
        #print i
        chain = generateChain(i,61)
        update = len(chain)
        for a in chain:
            if a<=1000000:
                nterms[a]=update
            update-=1
    #print 'i',i

count = 0
for i in xrange(1000000):
    print 'i',i
    if nterms[i]==60:
        count +=1
print count
"""
minimal product sum numbers.
"""
""" Thinking...procedure...need a way of finding the a product sum number of a given length. Then the minimal one
what is the upperlimit on the product sum number?

"""
import time as t
limit = 10
val = [[] for i in xrange(limit)]
val[1] = [0]
val[2] = [2]
val[3] = [3]


start = t.time()
for n in xrange(4,limit):
    for i in xrange(2,n+1):
        if n%i==0:
            val[n].extend([a+i for a in val[n/i]])
            val[n] = list(set(val[n]))

#'''
for i in xrange(len(val)):
    print i, val[i]

print "It took",t.time()-start ,"seconds"
#'''
#'''
mink = [[] for a in xrange(limit)]
br = False
for k in xrange(2,limit):
    for p in xrange(2,limit):
        for s in val[p]:
            if p-s<=k:
                print 'k,s,p',k,s,p
                mink[k]=p
                br = True
                break
            if br:
                break
print mink
#'''

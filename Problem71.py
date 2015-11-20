__author__ = 'Opemipo'

maxi = 0.4
maxval = 2,5
for d in xrange(2,1000001):
    n = 3*d/7 # this is less than
    if d%7!=0 and float(n)/d>maxi:
        #print 'here'
        maxi = float(n)/d
        maxval = n,d
    #pass
    #for n in xrange(2*d/5,3*d/7):
        #print n,d
        #if mini>float(n/d):
            #mini = float(n/d)
            #minival = n,d

print maxval,maxi

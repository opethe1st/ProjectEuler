__author__ = 'Opemipo'
#target number is given. Consider all rectangular grids that the number of triangles is nearest to target.
#say target is 10 whats the closest triangle number to it. then examine the numbers from
# Given target find the squareroot. find the nearest triangle number to the squareroot. divide to get the another number find the nearest triangle number
#to that number. Multiply the two numbers

import math

target = 100
a = int(math.sqrt(2*target))
#nearestTriNumb = a*(a+1)/2
#print nearestTriNumb

def nearestTribNumb(target):
    a = int(math.sqrt(2*target))
    return a*(a+1)/2

#for a in xrange(2,200):
    #print a,nearestTribNumb(a),math.fabs(a-nearestTribNumb(a))<= math.fabs(a-nearestTribNumb(a-1))

def nearest(target):
    setNum = []
    n = nearestTribNumb(target)
    a = int(math.sqrt(2*n))
    print 'a',a,'nearest',n
    for i in xrange(1,a+1):
        otherpart = n/(i*(i+1)/2)
        print 'other',otherpart
        b = int(math.sqrt(2*(otherpart-1)))
        print i,b
        setNum.append(b*i)

    return max(setNum)

print nearest(18)
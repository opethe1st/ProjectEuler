
"""
Solution.
Need to generate OP(k,n) for k<=n.
Given n terms, have a function to generate the polynominal that is a best fit.
Evaluate the terms of the given polynomial for 1 -> n+1.
How to get a solver that solves in integral or in fractions at worse
"""
#from numpy import *
from numpy import polynomial as p
import numpy
import math
def P(n):
    return (1-n + pow(n,2)-pow(n,3)+pow(n,4)-pow(n,5)+pow(n,6)-pow(n,7)+pow(n,8)-pow(n,9)+pow(n,10))

def generateFunction(points):
    n = len(points)
    A = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            A[i][j] = pow(points[i][0],j)
    A = numpy.array(A)
    x = [points[i][0] for i in xrange(n)]
    y = [points[i][1] for i in xrange(n)]
    poly = numpy.linalg.solve(A,y) #There is a problem with this... at particular point it gives errors
    #poly = p.polynomial.polyfit(x,y,n)
    #print 'poly',poly
    return poly #poly.coef()


def function(poly,x):
    n = len(poly)
    poly = [(poly[i]) for i in xrange(n)]
    powers = [0 for i in xrange(n)]
    for i in xrange(n):
        powers[i] = pow(x,i)
    return numpy.dot(powers,poly)


points = [(i,P(i)) for i in xrange(1,12)]
#points = [(i,i**3) for i in xrange(1,12)]
print points
FITs = []
n = len(points)
for i in xrange(n-1):
    subpoints = points[:i+1]
    print 'subpoints',subpoints
    f = generateFunction(subpoints)
    print f
    m = len(subpoints)
    print 'y',
    for j in xrange(1,m+2):
        y = int(function(f,j))

        print y,points[j-1][1]
        if abs(points[j-1][1]-int(function(f,j)))>2:
            FITs.append(function(f,j))
            break

print 'Fits',FITs, sum(FITs)

#The python numpy.linalg.solve isn't exact. How can one make it more exact? answer is 37076114526.0

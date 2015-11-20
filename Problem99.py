__author__ = 'Opemipo'

import math
f = open('input','r')
maxmag = 0
maxInd = -1
for i in xrange(1,1001):
    base,exponent = map(int,f.readline().split(','))
    magnitude = math.log10(base)*exponent
    if magnitude>maxmag:
        maxmag = magnitude
        maxInd = i

print maxInd
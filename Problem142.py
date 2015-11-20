__author__ = 'Opemipo'

def isSquare(a):
    import math
    return pow(math.floor(math.sqrt(a)),2)==a

print isSquare(81)
'''
for mn in xrange(20000):
    for m in xrange(3,mn/2):
        if isSquare(2*m*(mn-m)) and isSquare(m**2+2*m*(mn-m)) and isSquare((mn-m)**2+2*m*(mn-m)):
            print 2*m*(mn-m),m**2+2*m*(mn-m),(mn-m)**2+2*m*(mn-m)
'''
#'''
for a in xrange(3,200):
    for b in xrange(3,a):
        for c in xrange(3,b):
            if isSquare(a**2+b**2+c**2) and ((isSquare(a**2+b**2) or isSquare(b**2+c**2)) or (isSquare(b**2+c**2) and isSquare(a**2+c**2))):
                print a,b,c
'''
for a in xrange(200):
    for b in xrange(200):
        for c in xrange(200):
            if

'''
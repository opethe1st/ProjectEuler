__author__ = 'Opemipo'

from math import factorial
import math

def list2num(listnum):
    num = 0
    d = 1
    for i in reversed(listnum):
        num +=(i*d)
        d *= 10
    return num
#print list2num([1,3,4,5])
def theNthPerm(na,numdigit):
    n = na
    num = numdigit
    perm =[]
    while num>0:
        perm.append(n/factorial(num-1))
        n%=factorial(num-1)
        num -= 1

    return perm
def numdigits(n):
    return int(math.log10(n))+1
def perm(n,number):
    word =[]

    alphabets =[]#range(1,numdigit+1)
    while number>0:
        alphabets.append(number%10)
        number/=10
    alphabets.reverse()
    order = theNthPerm(n,len(alphabets))

    for i in order:
        #pick the ith item left
        word.append(alphabets[i])
        #i += 1
        del alphabets[i]
    return word
#print perm(4,53232)
def genPermutations(n):
    numdigit = numdigits(n)
    permations = set([])
    for i in xrange(factorial(numdigit)):
        permations.add(list2num(perm(i,n)))
    return permations
def isCube2(n):
    #print cuberoot(n),n
    return n==pow( cuberoot(n) ,3)

def cuberoot(n):
    k = 3
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s
#print 'here', cuberoot(56623104)


#print 'here',isCube2(56623104)
def countCubes(l):
    count = 0
    for a in l:
        if isCube2(a):
            count += 1
    return count
#print genPermutations(41063625)
#print 'the count', countCubes(genPermutations(41063625))
def baseP(n):
    s = str(n)
    l = list(s)
    l.sort()
    return tuple(l)
#print baseP(56623104) == baseP(41063625)

#I need something to save all the cube numbers associated with a certain baseP

i = 10
numdigit = 2
cube = pow(i,3)
numCubesPerm = {}
leastCubePerm = {} # a dictionary that keep track of the least cube
if numCubesPerm.get(baseP(cube),0):
    leastCubePerm[baseP(cube)] = cube
numCubesPerm[baseP(cube)] = numCubesPerm.get(baseP(cube),0)+1


while numCubesPerm.get(baseP(cube),0) != 5 :
    i+=1
    cube = pow(i,3)
    if numdigits(cube)>numdigit:
        numdigit+=1
        #print 'here'
        numCubesPerm = {}
        leastCubePerm = {}
    if numCubesPerm.get(baseP(cube),0)==0:
        leastCubePerm[baseP(cube)] = cube
    numCubesPerm[baseP(cube)] = numCubesPerm.get(baseP(cube),0)+1
    #print i,cube
print leastCubePerm[baseP(cube)]


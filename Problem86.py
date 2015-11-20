__author__ = 'Opemipo'
import math
import itertools
def shortestpath(a,b,c):
    path1 = math.sqrt((a+b)**2+c**2)
    path2 = math.sqrt((b+c)**2+a**2)
    path3 = math.sqrt((a+c)**2+b**2)
    #print 'path',path1,path2,path3,a+c,b
    return min(path1,path2,path3)

#print shortestpath(6,5,3)

def isInt(a):
    return a%1==0
'''
#print isInt(10.0)
count = 0
i = 1

while count<=1:

    for a in range(1,i):
        #print 'i',i
        for b in range(1,a+1):

            #print i,a,b
            if isInt(shortestpath(i,a,b)):
                #print 'correct',i,a,b
                count+=1
    for b in xrange(1,i):
        #print i
        #print i,i,b
        if isInt(shortestpath(i,i,b)):
            #print 'correct',i,i,b
            count+=1
    #print i,i,i
    if isInt(shortestpath(i,i,i)):
        count+=1
    print i
    i+=1

print i-1, count
'''

def f(m):
    l = 3
    count = 0
    while l<=m:
        wh =3
        while wh<(2*l+1):
            if (math.sqrt(l**2+wh**2))%1==0:
                if wh<=l:
                    count +=wh/2
                else:
                    count += 1 + (l - (wh+1)/2)
            wh+=1
        l+=1
    return count

print f(1000)

def f2(m):
    count = 0
    k = 1
    while k<=m:
        #print k
        if m%k!=0:
            k+=1
            continue
        else:
            #print k
            for a in xrange(2,int(math.sqrt(m/(1*k)))+1):
                for b in xrange(1,a):
                    if k*(a**2+b**2)<=m:
                        #print k*()
                        count+=1
            k+=1
    return count

import fractions

def f3(m):
    count = 0
    maxhyp = int(m*math.sqrt(5))
    for k in xrange(1,maxhyp/5+1):
        if maxhyp%k==0:
            a2b2 = maxhyp/k
            for a in xrange(2,int(math.sqrt(a2b2/2))+1):
                for b in xrange(1,a):
                    if fractions.gcd(a,b)==1:
                        k,n = a**2-b**2,2*a*b
                        #print k,n
                        count+=1

        else:
            continue
    return count

#print f2(100)
#print f3(100000)
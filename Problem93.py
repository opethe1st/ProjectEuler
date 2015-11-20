"""Description of the program"""
from __future__ import division #used to make sure that by default division 2/3 = 0.66 not 0
import itertools    #library that includes code for dealing with tools
import string
import time as t

start = t.time()

def longest1n(s):
    """Take a set, returns the length of the longest 1-n subsequence"""
    l = list(sorted(s))
    count = 0
    i=0
    j=-1
    if l[1]==1:
        i=1
        j = 1
    elif l[0]==1:
        i=0
        j=1
    while i<len(l) and l[i]==j:
        count+=1
        i+=1
        j+=1
    return count

count = 0
max1n =0
maxabcd = None
operators  = ['+','-','*','/']
distinctN = set()
s = range(0,10)
#test = [1,2,5,8]
for a1,b1,c1,d1 in itertools.combinations(s,4):
    #picks combinations of digits
    distinctN = set()
    listn= [a1,b1,c1,d1]
    for a,b,c,d in itertools.permutations([a1,b1,c1,d1]):
        #picks permutations of a1,b1,c1,d1
        for x,y,z in itertools.product(operators,operators,operators):
            #Here every possible combination of brackets is checked.
            #There is a lot of code here that is repeated. It could be refactored.
            try:
                newexpr = '('+str(a)+x+str(b)+')'+y+str(c)+z+str(d)
                res = abs(eval(newexpr))
                if res ==int(res): #checks that the result is an integer.
                    distinctN.add(abs(eval(newexpr)))
                    count+=1
            except ZeroDivisionError :
                pass
            try:
                newexpr = '('+str(a)+x+str(b)+y+str(c)+')'+z+str(d)
                res = abs(eval(newexpr))
                if res ==int(res):
                    distinctN.add(abs(eval(newexpr)))
                    count+=1
            except ZeroDivisionError :
                pass
            try:
                newexpr = '('+str(a)+x+str(b)+')'+y+'('+str(c)+z+str(d)+')'
                res = abs(eval(newexpr))
                if res ==int(res):
                    distinctN.add(abs(eval(newexpr)))
                    count+=1
            except ZeroDivisionError :
                pass
            try:
                newexpr = '('+'('+str(a)+x+str(b)+')'+y+str(c)+')'+z+str(d)
                res = abs(eval(newexpr))
                if res ==int(res):
                    distinctN.add(abs(eval(newexpr)))
                    count+=1
            except ZeroDivisionError :
                pass
            try:
                newexpr = str(a)+x+'('+str(b)+y+str(c)+')'+z+str(d)
                res = abs(eval(newexpr))
                if res ==int(res):
                    distinctN.add(abs(eval(newexpr)))
                    count+=1

            except ZeroDivisionError :
                pass

    l = longest1n(distinctN)
    if l >max1n:
        max1n=l
        maxDistinctN = distinctN
        maxabcd = "".join(map(str,sorted([a,b,c,d])))

print count
print maxabcd,max1n,'distinctN \n',maxDistinctN
end = t.time()
print 'elapsed time ',(end-start)

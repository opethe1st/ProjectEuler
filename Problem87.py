import UsefulFuntions
import math

num = 10000000

sqrtnum = int(math.sqrt(num))+1
#print sqrtnum*sqrtnum
cubertnum = int(pow(num,float(1)/3))+1
#print cubertnum*cubertnum*cubertnum
fourthrtnum = int(pow(num,float(1)/4))+1
#print fourthrtnum*fourthrtnum*fourthrtnum*fourthrtnum

p2 = UsefulFuntions.primeslessthan(sqrtnum)
#print len(p2)
p3 = UsefulFuntions.primeslessthan(cubertnum)
#print len(p3)
p4 = UsefulFuntions.primeslessthan(fourthrtnum)
#print len(p4)

setnum = set([])
for a in p2:
    for b in p3:
        for c in p4:
            if (a**2+b**3+c**4)<=num:
                #print a,b,c,a+b+c
                setnum.add(a**2+b**3+c**4)
print len(setnum)
A = sorted(setnum)
#print A


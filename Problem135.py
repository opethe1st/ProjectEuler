
import math

#n = 2*d*z+3*d**2-z**2
dic = {}
'''
for i in xrange(1,25000):
    for j in xrange(int(math.ceil(i/2)),i):
        n = i**2-j**2-(2*j-i)**2
        if n>0 and n<1000000:
            dic[n]= dic.get(n,0)+1
'''
for d in xrange(1,10000):
    z = 0
    n = 2*d*z+3*d**2-z**2
    while (z<10000):
        dic[n]= dic.get(n,0)+1
        z+=1
        n = 2*d*z+3*d**2-z**2
count = 0
for val in dic.keys():
    if dic[val]==10:
         count+=1
print count, dic[1155]

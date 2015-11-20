import math

#Find a way to generate all the octagonal numbers between 1000 and 9999
'''
n = int(math.sqrt(1000/3))+1
res = n*(3*n-2)
print 'res',res
count = 0
while res<9999:
    print res,
    n +=1
    res = n*(3*n-2)
    count += 1
    print count
'''


def generate3gonal(start,end):

    i=int(math.sqrt(start*2)+1)
    n = int(math.sqrt(end*2))
    while i<n:
        yield i*(i+1)/2
        i+=1

def generate4gonal(start,end):
    i = int(math.sqrt(start)+1)
    n = int(math.sqrt(end)+1)
    while i<n:
        yield i*i
        i+=1

def generate5gonal(start,end):
    i = int(math.sqrt(2*start/3))+1
    #print 'i',i,
    n = int(math.sqrt(2*end/3)+1)

    while i<n:
        yield i*(3*i-1)/2
        i+=1

def generate6gonal(start,end):
    i = int(math.sqrt(start/2)+1)
    n = int(math.sqrt(end/2)+1)
    while i<n:
        yield i*(2*i-1)
        i+=1

def generate7gonal(start,end):
    i = int(math.sqrt(start*2/5)+1)
    n = int(math.sqrt(end*2/5)+1)
    while i<n:
        yield i*(5*i-3)/2
        i+=1

def generate8gonal(start,end):
    i = int(math.sqrt(start/3)+1)
    n = int(math.sqrt(end/3)+2)
    while i<n:
        yield i*(3*i-2)
        i+=1



def findNgonal(prefix,n):
    #given a prefix and n find an ngonal satifying the property
    start = prefix*100
    res = []
    if n==3:
        start-=50
        for a in generate3gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res

    elif n==4:
        start-=50
        for a in generate4gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res
        pass
    elif n==5:
        start-=50
        for a in generate5gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res
    elif n==6:
        start-=50
        for a in generate6gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res
    elif n==7:
        start-=50
        for a in generate7gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res
    elif n==8:
        start-=50
        for a in generate8gonal(start,start+500):
            #print 'a',a
            if a/100==prefix:
                res.append(a)
        if res==[]:
            return False
        else:
            return res

#for a in generate6gonal(1000,9999):
    #print a

#print findNgonal(96,8)
#s = 0

def satisfyProperty(origin,start,A,sumn):
    if len(A)==1:
        #s +=start
        for a in findNgonal(start%100,A[0]):
            if a ==origin:
                return sumn


    prefix = start%100
    #print prefix
    for a in A:
        b = findNgonal(prefix,a)
        if b == False:
            return 0
        for c in b:
            sumn+=c
            return satisfyProperty(origin,c,A[1:],sumn)

print satisfyProperty(8128,8128,(5,4,3),0)

for a in generate3gonal(1000,9999):
    print 'n',a
    if satisfyProperty(a,a,[5,4,3],0)>0:
        print 'a'.a

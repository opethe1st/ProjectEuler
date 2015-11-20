__author__ = 'Opemipo'

A =[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
currentBest = [0]



# Enter your code here. Read input from STDIN. Print output to STDOUT
currentlist = [0]
currentMaxList = [0]
modMaxList = [0]*3
n=0

def modlist(s):
    a=[float('inf')]
    a.extend(s)
    a=a+[float('inf')]
    return a

def interMax(la):
    a = modlist(la)
    #print a
    intermax = [float('inf')]*len(la)+[float('inf')]
    for i in xrange(len(la)+1):
        #print a[i],a[i+1]
        intermax[i] = min(a[i],a[i+1])
    #print intermax, "this is intermax"
    return intermax

#
# print interMax([75])

#f = open("test.txt", "r")
#s = f.readline()
def case():
    s = raw_input()
    while s!='':

        slist = s.split()
        snumlist = map(int, slist)
        #print snumlist, 'this is the current input'
        inMaxList =interMax(currentMaxList)
        currentMaxList = [snumlist[i]+inMaxList[i] for i in xrange(len(snumlist)) ]
        #print currentMaxList,"current max list"
        s = raw_input()

    print max(currentMaxList),  'this is the max'
'''
#n = input()
for i in xrange(n):
    currentlist = [0]
    currentMaxList = [0]
    modMaxList = [0]*3
    n=0

    num = input()
    #s = raw_input()
    for i in xrange(num):
        s = raw_input()
        slist = s.split()
        snumlist = map(int, slist)
        #print snumlist, 'this is the current input'
        inMaxList =interMax(currentMaxList)
        currentMaxList = [snumlist[i]+inMaxList[i] for i in xrange(len(snumlist)) ]
        #print currentMaxList,"current max list"
        #s = raw_input()

    print max(currentMaxList)

'''
def diagonal(ar,i,n):
    diag = []
    if i<=n:
        for j in xrange(i):
            diag.append(ar[i-j-1][j])
    else:
        for j in xrange(0,2*n-i):
            diag.append(ar[n-j-1][j+i-n])
    return diag

def newMin(ar):
    l = len(ar)
    newar = []
    for i in xrange(l-1):
        newar.append(min(ar[i],ar[i+1]))
    return newar

ar = [[1,2,3],[4,5,6],[7,8,9]]




currentlist = [0]
currentMaxList = [0]
modMaxList = [0]*3
n=5

#num = 5
#s = raw_input()
f = open("input","r")
s = f.read()
slist = s.split()
n = len(slist)
snumlist=[[]for i in xrange(n) ]
#print snumlist
print n

for i in xrange(n):
    snumlist[i] =map(int, slist[i].split(","))

    #print snumlist[i]
#print snumlist, 'this is the current input'
A = snumlist
print 'Start here is\n\n'
for i in xrange(1,n+1):

    print i,n
    snumlist = diagonal(A,i,n)
    print 'diag',snumlist
    inMaxList =interMax(currentMaxList)
    print 'max',inMaxList
    currentMaxList = [snumlist[i]+inMaxList[i] for i in xrange(len(snumlist)) ]
    print currentMaxList,"current max list"
        #s = raw_input()

print min(currentMaxList)
ar = currentMaxList[:]
for i in xrange(n-1):
    nmax = newMin(ar)
    diag = diagonal(A,i+n+1,n)
    ar = [nmax[i]+diag[i] for i in xrange(len(nmax))]
    print 'ar',ar

print ar


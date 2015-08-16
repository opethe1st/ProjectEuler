
import time
t = time.time()
def column(A,j):
    n = len(A[0])
    a = []
    for i in xrange(n):
        a.append(A[i][j])
    return a
# I suspect this might be part of what is slowing it down. How about transposing the matrix instead and using the defined
#row operations? or from the onset, picking the items such that the rows are the columns
def partialSumA(B):
    ps = [0]*(len(B)+1)
    for i in xrange(1,(len(B)+1)):
        ps[i]=ps[i-1]+B[i-1]
    return ps

def partialSum(B,i,j):
    if i>j:
        raise "Error i>j"
    return ps[j]-ps[i]

#test the partial Sum functions
A = [1,2,3,4,5,6,7,8,9,10]


def MinPathSum3ways(A):
    n = len(A)
    minPathSF = column(A,0)
    for i in xrange(1,n):
        minPathSF = nextStep(minPathSF,column(A,i))
    return min(minPathSF)

def nextStep(A,B):
    n = len(A)
    newMinPath = [float('inf')]*n
    global ps
    ps = partialSumA(B)
    for i in xrange(n):
        for j in xrange(i+1):
            newMinPath[i] = min(newMinPath[i],A[j]+partialSum(B,j,i+1))
            #newMinPath[i] = min(newMinPath[i],A[j]+sum(B[j:i+1]))
        for j in xrange(i+1,n):
            newMinPath[i] = min(newMinPath[i], A[j]+partialSum(B,i,j+1))
            #newMinPath[i] = min(newMinPath[i], A[j]+sum(B[i:j+1]))
    return newMinPath

#A = [[131,673,234,103,18],[201,96,342,965,150],[630,808,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
A = [[] for i in xrange(80)]

f = open("p082_matrix.txt","r")
for i in xrange(80):
    A[i] = map(int,f.readline().split(","))
    #print A
#print A
#t = time.time()
print MinPathSum3ways(A)
print "Elapsed time",time.time()-t

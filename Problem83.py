from Queue import PriorityQueue
import time
#Copied Code

#Copied Code

def convert2Graph(A):
    #length of a side square matrix A
    n = len(A[0])
    #values of corresponsing to each vertices
    vertices = [0]*(n**2)
    #Graph containing info how the vertices are connected
    G = [0]*(n**2)
    #used to calculate what vertice corespnds to a particular entry in an array
    def c(i,j):
        return i*n+j
    #these loops are to convert the array into vertices
    for i in xrange(n):
        for j in xrange(n):
            vertices[c(i,j)] = A[i][j]

    #This section deals with building the vertices
    #Inner array, each vertex connected to four vertices
    for i in xrange(1,n-1):
        for j in xrange(1,n-1):
            G[c(i,j)] = [c(i-1,j),c(i,j-1),c(i+1,j),c(i,j+1)]
    #the edges, except the corner vertices - all connected to 3 vertices
    for j in xrange(1,n-1):
        G[c(0,j)] = [c(0,j-1),c(0,j+1),c(1,j)]
    for j in xrange(1,n-1):
        G[c(n-1,j)] = [c(n-1,j-1),c(n-1,j+1),c(n-2,j)]
    for i in xrange(1,n-1):
        G[c(i,0)] = [c(i-1,0),c(i+1,0),c(i,1)]
    for i in xrange(1,n-1):
        G[c(i,n-1)] = [c(i-1,n-1),c(i+1,n-1),c(i,n-2)]
    G[c(0,0)] = [c(0,1),c(1,0)]
    G[c(n-1,0)] = [c(n-1,1),c(n-2,0)]
    G[c(0,n-1)] = [c(1,n-1),c(0,n-2)]
    G[c(n-1,n-1)] = [c(n-1,n-2),c(n-2,n-1)]
    return G,vertices

def relax(u,v):
        if sp[u]+vertices[v]<sp[v]:
            sp[v] = sp[u]+vertices[v]
            pred[v] = u

def dijkstra(G,s):
    n = len(G)
    global pred
    pred = [None]*n
    global sp
    sp = [float("inf")]*n
    sp[0] = vertices[0]
    q = range(n)
    while not q == []:

        u = min(q,key=lambda v:sp[v])
        #print u,G[u]
        q.remove(u)
        for v in G[u]:
            relax(u,v)

    return sp

#test
#A = [[10,2,3],[4,5,6],[7,8,9]]
A = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
'''
#I think there is something wrong with this Priority Queue implementation
A = [[] for i in xrange(80)]
f = open("p083_matrix.txt","r")
for i in xrange(80):
    A[i] = map(int,f.readline().split(","))
#'''
#print A
G,vertices = convert2Graph(A)
#G graph of vertices not values
t = time.time()
print dijkstra(G,0)[-1]
print "Elapsed time",time.time()-t
#test

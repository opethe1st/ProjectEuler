#Dynamic programming solution

p = [[0 for j in xrange(10)] for i in xrange(20)]
print p[1]
for i in xrange(20):
    if i<=3:
        p[i][1]=1
    else:
        p[i][1]=0

p[2][2]=4
p[2][3]=9
p[3][2]=8
p[3][3]=27
for k in xrange(10):
    p[1][k]=(k+1)

print p
for k in xrange(3,10):
    for n in xrange(1,20):
        p[n][k]=p[n][k-1]+p[n-1][k-1]+p[n-1][k-2]+p[n-1][k-3]

print p
print p[4][3]
print p[1][1]

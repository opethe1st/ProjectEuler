
def isreversible(n):
    r = str(n)[::-1]

    revn = int(r)
    #print n, revn
    c = 0
    while n !=0:
        #print revn%10,n%10,c
        if (revn%10 + n%10+ c)%2==0:
            return False
        c = (revn%10 + n%10)/10
        #print c , 'c'
        revn/=10
        n/=10

    return True

print isreversible(2325)
count = 0
for i in xrange(1,1000000000):
    if isreversible(i):
        count +=1
print count
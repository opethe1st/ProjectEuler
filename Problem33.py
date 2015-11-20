
def list2num(a):
    d = 1
    num = 0
    for i in reversed(a):
        num += (i*d)
        d *= 10
    return num

def removeDigits(a):
    lda = [list(str(a[0])),list(str(a[1]))]
    for i in lda[0]:
        for j in lda[1]:
            if i == j:
                lda[0].remove(i)
                lda[1].remove(j)
    return [list2num(map(int,lda[0])),list2num(map(int,lda[1]))]

print removeDigits([11,20])
def isCurious(n):
    m = removeDigits(n)
    if m==n:
        return False
    if n[0]*m[1]==n[1]*m[0]:
        return True
    else:
        return False

print isCurious([11,20])

l = []
for i in xrange(11,100):
    for j in xrange(i+1,100):
        if isCurious([i,j]):
            l.append([i,j])

print l
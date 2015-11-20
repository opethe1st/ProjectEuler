
def isPandigital(n,k):
    num = n

    a = set([])
    for i in xrange(9):
        if n%10==0:
            return False
        a.add(n%10)
        n /= 10
    if len(a)== 9:
        return True
    else:
        return False

max = 918273645
for i in xrange(9123,9877):
    num = i*100000+2*i
    #print num
    if isPandigital(num):
        if num > max:
            max = num
print max
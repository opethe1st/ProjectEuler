
def palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

mx = 0
for i in xrange(100,1000):
    for j in xrange(i,1000):
        p = i*j
        if (palindrome(p) and mx<p):
            mx = p

print mx

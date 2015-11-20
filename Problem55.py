__author__ = 'Opemipo'

def reverseNum(n):
    m = 0
    while n>0:

        m *= 10
        m += n%10
        n /= 10
    return m

def isPalindrome(n):
    s = str(n)
    r = s[::-1]
    if r == s:
        return True
    else:
        return False

def oneiteration(n):
    return n + reverseNum(n)

def countiterationtoPal(n):
    count = 1
    n = oneiteration(n)
    while isPalindrome(n) is False:
        n = oneiteration(n)
        count += 1
        if count >50:
            return -1

    return n


print countiterationtoPal(4994)
def isLychrel(n):
    m = countiterationtoPal(n)
    if m ==-1:
        return -1
    else:
        return m

count = 0
palins = {}
N = input()
for i in xrange(1,N+1):
    a = countiterationtoPal(i)
    if a > 0:
        #print i
        palins[a]=palins.get(a,0)+1
        count += 1


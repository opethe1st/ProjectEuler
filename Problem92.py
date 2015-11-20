__author__ = 'Opemipo'

def squaredigit(n):
    res = 0
    while(n != 0):
        res += (n%10)**2
        n/=10
    return res
#print squaredigit(85)
count =0
n = 10000000
Nums = [0]*n
Nums[89]=1
i=1
while i<n:
    if Nums[i]==1:
        i+=1
        continue
    next = i
    chain = []
    while (next!=89 and next !=1 and Nums[next]!=1):
        chain.append(next)
        #print next,
        next = squaredigit(next)
    #print next
    if next!=1:
        for a in chain:
            if a<n:
                Nums[a]=1
    i+=1

count = 0
for a in Nums:
    if a==1:
        count+=1
print count
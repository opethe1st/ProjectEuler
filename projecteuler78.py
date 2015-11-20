
def generalDp(v,numtobemade):
    #Initializer code
    #v is an array which includes zero of the "denominations" ( like in a coin changing problem
    lenvalue = len(v)
    n = [[0]*(numtobemade+1) for i in xrange(lenvalue)]

    for i in xrange(1,lenvalue):
        n[i][0] = 1                 #if the value to be made is zero there is only one way of making the change
    for j in xrange(1,numtobemade+1):
        n[i][j] = 1                 #if the value


    #end initializer code

    for i in xrange(1,lenvalue):
        for j in xrange(1,numtobemade+1):
            if v[i]>j:
                n[i][j] = n[i-1][j]
            else:
                n[i][j] = n[i][j-v[i]]+n[i-1][j]

    return n[lenvalue-1][numtobemade]

num = -1

i = 1

while num !=0:
    i = i+1
    num = generalDp(range(i+1),i)%1000000
print i
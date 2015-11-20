
def f(n):
    count = 0
    for x2 in xrange(0,n+1):
        for x1 in xrange(0,n+1):
            for y2 in xrange(0,n+1):
                for y1 in xrange(0,n+1):
                    #print (x1,y1),(x2,y2)
                    if(((x1,y1)!=(0,0)) and ((x2,y2)!=(0,0)) and (x1,y1)!=(x2,y2)) and ((x1,y1)!=(0,0) or  (x2,y1))!=(0,0) and ((x1**2+y1**2-x1*x2-y1*y2)==0 or (x1,y2)==(0,0))  :
                        #print (x1,y1),(x2,y2)
                        count+=1
    return count
for a in xrange(1,11):
    print a, f(a)
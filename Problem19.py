__author__ = 'Opemipo'


def getParameters(date):
    y,m,d =date[0],date[1],date[2]
    q = d
    if m<3:
        m+=12
        y-=1
    k = y%100
    j = y/100
    return (q,m,y)

def getDate(t):
    q,m,y = t[0],t[1],t[2]
    return (q+((26*(m+1))/10)+y+(y/4)+6*(y/100)+(y/400)+6)%7

def lessthan(Date1,Date2):
    Y1,M1,D1 = Date1[0],Date1[1],Date1[2]
    Y2,M2,D2 = Date2[0],Date2[1],Date2[2]
    if Y1<Y2:
        return True
    elif Y1>Y2:
        return False
    else:
        if M1<M2:
            return True
        elif M1>M2:
            return False
        else:
            if D1<D2:
                return True
            elif D1>D2:
                return False
            else:
                return True

#print 'less than', lessthan([2015,2,2],[2015,1,1])
def dateGen(Date1,Date2):
    date = Date1
    if date[1]<12:
        date = [date[0],date[1]+1,1]
    else:
        date = [date[0]+1,1,1]
    while lessthan(date,Date2):
        if date[1]<12:
            yield date
            #date = [date[0],date[1]+1,1]

        else:
            yield date
            #date = [date[0]+1,1,1]
        if date[1]<12:
            date = [date[0],date[1]+1,1]
        else:
            date = [date[0]+1,1,1]

#'''
count = 0
Date1,Date2 = [1901,1,1],[2001,12,31]
for date in dateGen(Date1,Date2):
        if getDate(getParameters(date))==0:
            count+=1
            print 'Sunday',date
        #print date
print count
#'''
def countDate(Date1,Date2):
    count = 0
    for date in dateGen(Date1,Date2):
        if getDate(getParameters(date))==0:
            count+=1
    if Date1[2]==0:
        if getDate(getParameters(Date1))==0:
            #print 'here'
            count+=1
    return count


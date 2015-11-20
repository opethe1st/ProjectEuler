def roman(digit):
    if digit == 'M':
        return 1000
    elif digit == 'D':
        return 500
    elif digit == 'C':
        return 100
    elif digit == 'L':
        return 50
    elif digit == 'X':
        return 10
    elif digit == 'V':
        return 5
    elif digit == 'I':
        return 1
    else:
        return "error"

def evalRoman(romNum):

    current = roman(romNum[0])
    Ssum = 0
    Ssum += current
    n = len(romNum)
    for i in xrange(1,n):
        current = roman(romNum[i])
        previous = roman(romNum[i-1])
        Ssum+=current
        if previous<current:
            Ssum -= (2*previous)

    return Ssum

def num2Rom(num):
    res = ""
    thousand = num/1000
    num %= 1000
    if thousand>0:
        res += thousand*"M"

    hundred = num/100
    num %=100

    if hundred ==9:
        res += "CM"
    elif hundred>=5:
        res +="D"
        hundred-=5
        if hundred >0:
            res += hundred*"C"
    elif hundred == 4:
        res += "CD"
    elif hundred >0:
        res += hundred*"C"

    tenth = num/10
    num %= 10
    if tenth == 9:
        res+="XC"
    elif tenth>=5:
        res +="L"
        tenth-=5
        if tenth>0:
            res += tenth*"X"
    elif tenth == 4:
        res += "XL"
    elif tenth > 0:
        res+= tenth *"X"

    unit = num

    if unit ==9:
        res+="IX"
    elif unit>=5:
        res+="V"
        unit -= 5
        if unit>0:
            res += unit*"I"
    elif unit == 4:
        res += "IV"
    elif unit > 0:
        res += unit*"I"

    return res
for i in xrange(1,1000):
    b1 = i
    a1 = num2Rom(b1)
    if b1!=evalRoman(a1):
        print 'error'
    print b1,a1, "\t\t\t",evalRoman(a1)

'''
saved = 0
f = open("p089_roman.txt")
romNum = f.readline().strip()
numval = evalRoman(romNum)
eromNum = num2Rom(numval)
saved += (len(eromNum)-len(romNum))
romNum = f.readline().strip()
while romNum!="":
    #print romNum
    numval = evalRoman(romNum)
    eromNum = num2Rom(numval)
    saved += (len(romNum)-len(eromNum))
    romNum = f.readline().strip()
print saved
'''

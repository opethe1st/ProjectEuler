__author__ = 'Opemipo'

def convert2ASCII(message):
    Ascii = []
    for ch in message:
        Ascii.append(str(ord(ch)))
    return Ascii
    pass

#print convert2ASCII('abcdes')
def decrypt(message,key):
    #Message is a list with ASCII values as string
    l = len(message)
    newMessage =[]
    for i in xrange(l):
        newMessage.append(str(int(message[i])^ord(key[i%3])))
    return newMessage

def sumAscii(message):
    summ = 0
    for ch in message:
        summ+=ord(ch)
    return summ

def convert2Str(message):
    msg = map(chr,map(int,message))
    return "".join(msg)

def isEngChar(i):
    if (64<ord(i)<91 or 96<ord(i)<123 or 59<ord(i)<70 or 38<ord(i)<42 or 57<ord(i)<60 or 44<ord(i)<47 or 31<ord(i)<34 or i == 39 or i ==63 ):
    #if (31<ord(i)<127):
        #print 'i',i
        return True
    return False


def isEnglish(plainMsg):
    import string
    print plainMsg.lower()
    for ch in plainMsg[:10]:
        #print 'ch', ch
        if not isEngChar(ch):
            #print 'here'
            return False
    if plainMsg.find(' ')<0 or plainMsg.find('the')<0 or plainMsg.find('a')<0 or plainMsg.find('of')<0 or plainMsg.find('in')<0 or plainMsg.find('and')<0:
        return False
    return True

import string
import re
f = open("input","r")
code = f.read()
code = re.split(',',code)
#print 'code',code
codedmsg = decrypt(code,'abc')
#print 'codedmsg',codedmsg
import itertools
i = 1
key = 'god'
#code2 = convert2ASCII(code)
#print 'code3',code,len(code)
code5 = convert2Str(decrypt(code,key))
print 'code5',code5
print 'isEng',isEnglish(code5)

count = 0
for key in itertools.permutations('abcdefghijklmnopqrstuvwyz',3):
    message = convert2Str(decrypt(code,key))

    if isEnglish(message):
        #print 'here'
        count +=1
        #print convert2Str(decrypt(code,key)),key,sumAscii(message)
        print "".join(key)
#print count
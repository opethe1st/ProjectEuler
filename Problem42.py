__author__ = 'Opemipo'
import math
def convertWord(word):
    Sum = 0
    lword = list(word)
    print lword
    for letter in lword:
        #print letter, type(letter)
        val = ord(letter)-ord('A')+1
        #print val
        Sum+=val
    return Sum

#print convertWord("SKY")

def isTriangle(n):
    a = int(math.sqrt(2*n))
    if n == a*(a+1)/2:
        return True
    else:
        return False

f = open('input','r')
Words = f.readline().split(',')
total = 0
for word in Words:
    value = convertWord(word[1:-1])
    if isTriangle(value):
        total+=1
print total
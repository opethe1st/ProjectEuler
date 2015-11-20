""" a Program to solve Sudoku puzzles

Pseudocode
first, record the position of all the spaces in the array.
for each space, create a list with the item being the row, and the other the column

while there is still empty space in the array.
    iterate through the spaces.
        try to figure out the digits that can fill up that space.
        if there is only one possible digit, then fill the space in the original with that digit and remove from spaces
        (If I am to make progress then, after iterating through the spaces, there must be one with just one possible digit)

spaces represented by zeroes.
the figuring out digits part, need to be able to select the row and column and the blocks
"""


#definitions
def column(A,j):
    n = len(A[0])
    a = []
    for i in xrange(n):
        a.append(A[i][j])
    return a

def Block(A,sector):
    rown,coln = sector
    block = [[0]*3 for i in xrange(3)] #3 is hard. I should make it programmable
    setblock = set([])
    for i in xrange(3):
        for j in xrange(3):
            block[i][j] = A[rown*3+i][coln*3+j]
            setblock.add(A[rown*3+i][coln*3+j])
    #return block
    return setblock

def Blocks(A,sector):
    rown,coln = sector
    block = [[0]*3 for i in xrange(3)] #3 is hard. I should make it programmable
    setblock = set([])
    for i in xrange(3):
        for j in xrange(3):
            block[i][j] = A[rown*3+i][coln*3+j]
            #setblock.add(A[rown*3+i][coln*3+j])
    #return block
    return block


def block(a): #used by Block
    """finds the block that an element belongs to"""
    i,j =a
    if i<3:
        rown = 0
    elif 2<i<6:
        rown = 1
    elif i<9:
        rown = 2
    if j<3:
        coln = 0
    elif 2<j<6:
        coln = 1
    elif j<9:
        coln = 2
    block = rown,coln
    return block


def fix(a,d):
    """finds out if a particular space can be fixed with a value"""
    i,j=a
    b = block(a)
    if i%3==0:
        adjrow1 = i+1
        adjrow2 = i+2
    elif i%3==1:
        adjrow1 = i-1
        adjrow2 = i+1
    elif i%3==2:
        adjrow1 = i-2
        adjrow2 = i-1

    if j%3==0:
        adjcol1 = j+1
        adjcol2 = j+2
    elif j%3==1:
        adjcol1 = j-1
        adjcol2 = j+1
    elif j%3==2:
        adjcol1 = j-2
        adjcol2 = j-1

    def singleSq(a):
        row = A[a[0]]
        col = column(A,a[1])
        blockD = Block(A,block(a))
        #possD = set(range(1,10))-(set(row).union(set(col)).union(blockD))
        dic = {}
        for n,a in enumerate(A[i]):
            if a ==0:
                possD = set(range(1,10))-(set(row).union(set(col)).union(blockD))
                for p in possD:
                    dic[p]= dic.get(p,0)+1

        if dic.get(d,0)==1:
            print a,d
            return True

        dic = {}
        for n,a in enumerate(column(A,j)):
            if a ==0:
                possD = set(range(1,10))-(set(row).union(set(col)).union(blockD))
                for p in possD:
                    dic[p]= dic.get(p,0)+1
        if dic[d]==1:
            return True

        dic = {}
        Blk = Blocks(A,b)
        for m in xrange(3):
            for n in xrange(3):
                if Blk[m][n]==0:
                    possD = set(range(1,10))-(set(row).union(set(col)).union(blockD))
                    for p in possD:
                        dic[p]= dic.get(p,0)+1
        if dic[d]==1:
                return True
        return False
        pass
    #print i,j,A[i][j],i,adjcol1,A[i][adjcol1],i,adjcol2, A[i][adjcol2],adjrow1,j, A[adjrow1][j],adjrow2,j, A[adjrow2][j]
    if (((d in set(A[adjrow1]))and(d in set(A[adjrow2]))) and ((d in set(column(A,adjcol1)))and(d in set(column(A,adjcol2)))))\
    or (((d in set(A[adjrow1]))and(d in set(A[adjrow2]))) and A[i][adjcol1]!=0 and A[i][adjcol2]!=0) \
    or (((d in set(column(A,adjcol1)))and(d in set(column(A,adjcol2)))) and A[adjrow1][j]!=0 and A[adjrow2][j]!=0)\
    or ((d in set(A[adjrow1])) and (d in set(A[adjrow2]) and (A[i][adjcol1]!=0) and (d in set(column(A,adjcol2)))))\
    or ((d in set(A[adjrow1])) and (d in set(A[adjrow2]) and (A[i][adjcol2]!=0) and (d in set(column(A,adjcol1)))))\
    or ((d in set(column(A,adjcol1))) and (d in set(column(A,adjcol2)) and (A[adjrow1][j]!=0) and (d in set(A[adjrow2]))))\
    or ((d in set(column(A,adjcol1))) and (d in set(column(A,adjcol2)) and (A[adjrow2][j]!=0) and (d in set(A[adjrow1]))))\
    or singleSq(a):
        #print A[i][j],A[i][adjcol1],A[i][adjcol2],A[adjrow1][j],A[adjrow2][j]
        return True
    else:
        return False

#print 'does it fix',fix((4,1),3)
def possibledigits(a):
    """this is critical. it takes as input the coordinates of the space and then analyzes it to find the
    possible digits that can fill the space. There is global A"""
    row = A[a[0]]
    col = column(A,a[1])
    blockD = Block(A,block(a))
    possD = set(range(1,10))-(set(row).union(set(col)).union(blockD))
    for d in possD:
        if fix(a,d):
            possD = [d]

    return list(possD)



def singleSquare(pos):
    '''Checks if a space can be fixed, this is true if a number appears as a candidate in
    a single area (row,column and box) '''
    i,j=pos
    b = block(pos)
    dic = {}
    for n,a in enumerate(A[i]):
        if a ==0:
            possD = possibledigits((i,n))
            for p in possD:
                dic[p]= dic.get(p,0)+1
    for k in dic.keys():
        if dic[k]==1:

            return [k]
    return False
'''
    dic = {}
    for n,a in enumerate(column(A,j)):
        if a ==0:
            possD = possibledigits((n,j))
            for p in possD:
                dic[p]= dic.get(p,0)+1
    for k in dic.keys():
        if dic[k]==1:
            return [k]
'''
#    return False
#    return False
'''
    dic = {}
    Blk = Blocks(A,b)
    for m in xrange(3):
        for n in xrange(3):
            if Blk[m][n]==0:
                possD = possibledigits((3*b[0]+m,3*b[1]+n))
                for p in possD:
                    dic[p]= dic.get(p,0)+1
    for k in dic.keys():
        if dic[k]==1:
            return [k]
#            '''
#    return False


#Keep track of the spaces

def solveMatrix(A):
    l = len(A[0])
    spaces = []
    for i in xrange(l):
        for j in xrange(l):
            if A[i][j]==0:
                spaces.append((i,j))
                #print i,j,possibledigits((i,j))

    print 'num of spaces',len(spaces),'num of filled in squares',81-len(spaces)
    count = 0
    #while spaces != []:
    for _ in xrange(60):
        for space in spaces:
            poss = possibledigits(space)
            if singleSquare(space)!=False:
                #poss=singleSquare(space)
                pass
            #print space,poss
            if len(poss)==1:
                A[space[0]][space[1]] = poss[0]
                spaces.remove(space)
        #for a in A:
            #print a
        #print
        count+=1
#'''
    print 'Solution Matrix'
    for a in A:
        print a
    print 'Count',count


    #Test for correctness
    test = True
    for i in xrange(9):
        #print (set(range(1,10))-set(A[i]))==set(),
        test=(test and (set(range(1,10))-set(A[i]))==set())
        #print (set(range(1,10))-set(column(A,i)))==set(),
        test=(test and (set(range(1,10))-set(column(A,i)))==set())
    for i in xrange(3):
        for j in xrange(3):
            #print (set(range(1,10))-set(Block(A,(i,j))))==set(),
            test = (test and (set(range(1,10))-set(Block(A,(i,j))))==set())
    print 'Solved? ', test
    return test
#'''

#Assume that A is the 2-d array with the numbers
f = open('p096_sudoku.txt','r')
countSolved = 0
for n in xrange(50):

    name = f.readline().strip()
    print name
    A = [[] for _ in xrange(9)]
    for i in xrange(9):
        A[i] = map(int,list(f.readline().strip()))
        print A[i]

    if solveMatrix(A):
        countSolved+=1
    print
print 'Number solved',countSolved

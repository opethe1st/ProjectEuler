
def order(card):
    #print type(card)
    if card.isdigit():
        return int(card)
    else:
        if card =="T":
            return 10
        elif card == "J":
            return 11
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        elif card == "A":
            return 14

def compare(str1,str2):
    ord1 = order(str1)
    ord2 = order(str2)

    if ord1>ord2:
        return True
    elif ord1<ord2:
        return False
    else:
        return "equal"

#print compare("A","J")

def isHighestCard(hand):
    highestCard = hand[0][:-1]
    for a in hand[1:]:
        if compare(a[:-1],highestCard):
            highestCard = a[:-1]
    return highestCard

print isHighestCard(["5D","6D","9D","10D","AD"])

def isRoyalFlush(Hand):
    DiamondsRoyal = ["AD","KD","QD","JD","10D"]
    ClubsRoyal = ["AC","KC","QC","JC","10C"]
    HeartsRoyal = ["AH","KH","QH","JH","10H"]
    SpadesRoyal = ["AS","KS","QS","JS","10S"]
    print sorted(ClubsRoyal)
    hand = sorted(Hand)
    if hand==sorted(DiamondsRoyal) or hand ==sorted(ClubsRoyal) or hand==sorted(HeartsRoyal) or hand==sorted(SpadesRoyal):
        return True
    else:
        return False

#print isRoyalFlush(["AC","KC","QC","JC","10C"])

def isSameDeck(Hand):
    Deck = Hand[0][-1]
    for a in Hand[1:]:
        if Deck is not a[-1]:
            return False
    return True

def orderHand(Hand):
    orderH = []
    for a in Hand:
        orderH.append(order(a[:-1]))
    return sorted(orderH)

#print 'orderhand',orderHand(["AC","KC","QC","JC","10D"])
def isStraight(Hand):
    nhand = orderHand(Hand)
    first = nhand[0]
    consecutive = range(first,first+5)
    if nhand == consecutive:
        return True
    else:
        return False

#print 'isStraight', isStraight(["10C","KC","QC","JC","9D"])
#print isSameDeck(["AC","KC","QC","JC","10D"])
def isStraightFlush(hand):
    #make sure that the cards in the desk are all of the same suit and that they follow sequentially.
    if isSameDeck(hand):
        if isStraight(hand):
            return True
        else:
            return False
    else:
        return False
#print "isStraightFlush", isStraightFlush(["10C","KC","QC","JC","9C"])

def isTofKind(Hand,t):
    nhands = orderHand(Hand)
    count = {}
    for a in nhands:
        count[a] = count.get(a,0)+1
    if t in count.values():
        return True
    else:
        return False

#print 'is4ofKind', isTofKind(["10C","10C","10C","9C","9C"],4)

def isFlush(Hand):
    return isSameDeck(Hand)

def twoPairs(Hand):
    nhands = orderHand(Hand)
    count = {}
    number = 0
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.values():
        if a==2:
            number+=1
    if number==2:
        return True
    else:
        return False

def onePair(Hand):
    nhands = orderHand(Hand)
    count = {}
    number = 0
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.values():
        if a==2:
            number+=1
    if number==1:
        return True
    else:
        return False

def isFullHouse(Hand):
    nhands = orderHand(Hand)
    count = {}
    number = 0
    for a in nhands:
        count[a] = count.get(a,0)+1
    if 3 in count.values() and 2 in count.values():
        return True
    else:
        return False

#print 'isFullHouse', isFullHouse(["10C","10C","8C","8C","8C"])

#print 'onePair ',onePair(["10C","10C","8C","JC","KC"])

def ValueOf4kind(Hand):
    nhands = orderHand(Hand)
    count = {}
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.keys():
        if count[a]==4:
            return a
    pass

def ValueOf3kind(Hand):
    nhands = orderHand(Hand)
    count = {}
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.keys():
        if count[a]==3:
            return a
    pass

def ValueOf2Kind(Hand):
    nhands = orderHand(Hand)
    count = {}
    twopair = []
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.keys():
        if count[a]==2:
            twopair.append(a)
    return max(twopair)


def ValueOf1Kind(Hand):
    nhands = orderHand(Hand)
    count = {}
    for a in nhands:
        count[a] = count.get(a,0)+1
    for a in count.keys():
        if count[a]==2:
            return a
    pass

def rankType(Hand):
    #Want to modify this such that it returns a list or a tuple with the rank first, then the highest value in the rank
    #the highestvalue in the hand, the next highest , the next highest . So this is 7 items.
    h = orderHand(Hand)
    h.reverse()
    print h
    if isRoyalFlush(Hand):
        a = [10,14]
        a.extend(h)
        return a
    elif isStraightFlush(Hand):
        a = [9,isHighestCard(Hand)]
        a.extend(h)
        return a
    elif isTofKind(Hand,4):
        a = [8,ValueOf4kind(Hand)]
        a.extend(h)
        return a
    elif isFullHouse(Hand):
        a = [7,ValueOf3kind(Hand)]
        a.extend(h)
        return a
    elif isFlush(Hand):
        a = [6,isHighestCard(Hand)]
        a.extend(h)
        return a
    elif isStraight(Hand):
        a = [5,isHighestCard(Hand)]
        a.extend(h)
        return a
    elif isTofKind(Hand,3):
        a = [4,ValueOf3kind(Hand)]
        a.extend(h)
        return a
    elif twoPairs(Hand):
        a = [3,ValueOf2Kind(Hand)]
        a.extend(h)
        return a
    elif onePair(Hand):
        a = [2,ValueOf2Kind(Hand)]
        a.extend(h)
        return a
    elif isHighestCard(Hand):
        a = [1]
        a.extend(h)
        return a
    else:
        return -1

#print rankType(["10C","9D","8S","7H","AC"])
def compareRank(H1,H2):
    if rankType(H1)[0]>rankType(H2)[0]:
        return True
    elif rankType(H1)[0]<rankType(H2)[0]:
        return False
    else:
        return 'equal'


def compareHands(H1,H2):
    rankType1 = rankType(H1)
    #print 'rank1',rankType1
    rankType2 = rankType(H2)
    #print 'rank2',rankType2
    for i in xrange(len(rankType1)):
        if rankType1[i]>rankType2[i]:
            return True
        elif rankType1[i]<rankType2[i]:
            return False

#Done I think

def splitHands(H):
    Hands = H.split()
    print Hands
    return Hands[:5],Hands[5:]

print 'compare Hands', compareHands(["10C","10C","8C","JC","KC"],["10C","10C","8C","8C","8C"])

count = 0
f = open("Problem54.txt","r")
game = f.readlines()
for a in game:
    hands = splitHands(a)
    if compareHands(hands[0],hands[1]):
        print 'Player 1'
    else:
        print 'Player 2'

print count

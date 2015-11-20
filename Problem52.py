
def samedigits(n,m):
    ln = list(str(n))
    lm = list(str(m))
    for i in lm:
        if i not in ln:
            return False
    return True

i = 1

while not(samedigits(i,2*i) and samedigits(i,3*i) and samedigits(i,4*i) and samedigits(i,5*i) and samedigits(i,6*i)):
    i += 1
print i,2*i,3*i,4*i,5*i,6*i

from UsefulFunctions import primeslessthan

primes = primeslessthan(100000)

s = 0
for p in primes:
    remainder = set()
    r = pow(10,10,9*p)
    remainder.add(r)
    if r==1:
        print p
        s+=p
        continue
    r = pow(r,10,9*p)
    while r not in remainder:
        #print remainder

        remainder.add(r)
        if r == 1:
            remainder.add(r)
            print p
            s+=p
            break
        r = pow(r,10,9*p)

    if r==1:
        continue
print 'sum',sum(primes)-s

import math
sum = 0
p = 4
while p<1000000000:
	if (p%3==0):
		continue
	elif (p%3==1):
		s = (p-1)/3
		area =  (s-1)*math.sqrt((3*s**2-s)/2)/2
		if (area%1==0):
			sum+=p
	else:
		s = (p+1)/3
		area = (s+1)*math.sqrt((3*s**2+s)/2)/2
		if area%1==0:
			sum+=p
	p+=1

print sum

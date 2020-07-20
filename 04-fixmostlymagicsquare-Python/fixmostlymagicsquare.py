# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.


def fixmostlymagicsquare(L):
	pass
	r1=r2=r3=c1=c2=c3=0

	for i in range (len(L)):
		if i==0:
			r1=sum(l[i])
		if i==1:
			r2=sum(l[i])
		if i==2:
			r3=sum(l[i])
	for i in range(len(L[0])):
		if i==0:
			c1=L[0][0]+L[0][1]+L[0][2]
		if i==1:
			c2=L[1][0]+L[1][1]+L[1][2]
		if i==2:
			c3=L[2][0]+L[2][1]+L[2][2]
	if r1==r2 and r1!=r3:
		if c1==c2 and c1!=c3:
			a=r1-r3
			L[2][2]
	# Your code goes here
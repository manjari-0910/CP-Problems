# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.
import numpy as np

def fixmostlymagicsquare(L):
	pass
	l1=[]
	l2=[]
	s1=0
	s2=0
	row=0
	col=0
	for i in L:
		l1.append(i)
	for i in range(len(l1)):
		if np.any(l1.count(l1[i])==1):
			row=i
			s2=l1[i]
		else:
			s1=l1[i]
	trans=np.array(L).T
	for i in trans:
		l2.append(i)
	for i in range(len(l2)):
		if np.any(l2.count(l2[i])==1):
			col=i
	if s2>s1:
		diff=s2-s1
	else:
		diff=s1-s2
	L[row][col]=l[row][col]-diff
	return L

	# Your code goes here
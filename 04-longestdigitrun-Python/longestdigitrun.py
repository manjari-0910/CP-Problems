# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n=abs(n)
	c=m=p=0
	l1=l2=[]
	while (n>0):
		rem=n%10
		if rem==p:
			c+=1
			if c>=m:
				m=c
				l1.append(rem)
		else:
			c=1
			p=rem
			l2.append(rem)
		n=n//10
	if m==0:
		return min(l2)
	else:
		return min(l1)

	pass
# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.

def isautomorphic(n):
	s=str(n**2)
	n=str(n)
	if s[len(s)-len(n):] == n:
		return True
	return False

def nthautomorphicnumbers(n):
	# Your code goes here
	i=1
	c=0
	while c<n:
		if isautomorphic(i):
			c+=1
		i+=1

	return i-1
	pass
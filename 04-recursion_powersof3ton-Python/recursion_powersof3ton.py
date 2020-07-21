# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.

def recursion_powersof3ton(n):
	# Your code goes here
	return power3(n,[],1)
	pass

def power3(n,l,i):
	if i>n:
		return l
	else:
		if i**3<n:
			l.append(i**3)
		i+=1
		return power3(n,l,i)
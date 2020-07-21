# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.

def recursion_powersof3ton(n):
	# Your code goes here
	return power3(n,[],0)
	pass

def power3(n,l,i):
	if i>n:
		if len(l)==0:
			return None
		return l
	else:
		if 3**i<=n:
			l.append(3**i)
		i+=1
		return power3(n,l,i)
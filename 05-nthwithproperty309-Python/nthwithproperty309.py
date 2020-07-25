# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def is309(n):
	i=n**5
	li={'0','1','2','3','4','5','6','7','8','9'}
	return (set(str(i))==li)
def nthwithproperty309(n):
	# Your code goes here
	c=1
	i=309
	while (c!=n):
		if is309(i):
			c+=1
		i+=1
	return i-1
	pass
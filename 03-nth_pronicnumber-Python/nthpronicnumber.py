# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

def ispronic(n):
    i=1
    while (i<(n//2)+1):
        if n%i==0 and (n//i)==i+1:
            return True
        i+=1
    return False

def nthpronicnumber(n):
	# Your code goes here
	i=1
	c=0
	while c<n:
		if ispronic(i):
			c+=1
		i+=1

	return i-1

	pass
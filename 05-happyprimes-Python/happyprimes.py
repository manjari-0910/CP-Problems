# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!
import math

def sqr(n):
	return n**2

def ishappynumber(n):
	# your code goes here

	if n<1:
		return False
	if n==1:
		return True
	while n!=1:
		if len(str(n))==1:
			break
		l=list(str(n))
		l=list(map(int,l))
		l=list(map(sqr,l))
		n=sum(l)
	if n==1:
		return True
	else:
		return False
	pass

def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
        return True

def ishappyprimenumber(n):
    # Your code goes here
    if isprime(n) and ishappynumber(n):
        return True
    return False
    pass
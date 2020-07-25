# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).
import math
def isprime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

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

def fun_nth_happy_prime(n):
	c=0
	i=1
	while c<=n:
		i+=1
		if ishappynumber(i) and isprime(i):
			c+=1
	return i
	# return 0
# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def isprime(n):
	if n<2:
		return False
	else:
		for i in range(2,(n//2)+1):
			if n%i==0:
				return False
		return True

def rotate(n):
	n=str(n)
	n=n[-1]+n[:len(n)-1]
	return int(n)

def nthcircularprime(n):
	# Your code goes here
	i=2
	while (n>=0):
		if isprime(i):
			c=1
			for j in range(len(str(i))):
				i=rotate(i)
				if isprime(i):
					c+=1
		if c==len(str(i)):
			n-=1
		i+=1
	return i

	pass
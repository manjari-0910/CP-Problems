# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
# import sympy

def isprime(n):
	for i in range(2,n//2):
		if n%i==0:
			return False
	return True

def isaddprime(n):
	li=list(str(n))
	li=list(map(int,li))
	return isprime(sum(li))

def fun_nth_additive_prime(n):
	if n==0:
		return 2
	else:
		c=0
		num=1
		while(c<n):
			if isprime(num) :
				if isaddprime(num):
					c+=1
			num+=1
		if c==n:
			return num
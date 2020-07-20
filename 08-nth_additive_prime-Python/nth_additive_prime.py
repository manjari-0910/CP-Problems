# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
# import sympy

def isprime(n):
	for i in range(2,(n//2)+1):
		if n%i==0:
			return False
	return True

def addprime(n):
	n=list(str(n))
	n=list(map(int,n))
	return isprime(sum(n))

def fun_nth_additive_prime(n):
	#code goes here
	num=1
	while n>0:
		if isprime(num) and addprime(num):
			n-=1
		num+=1
	return num

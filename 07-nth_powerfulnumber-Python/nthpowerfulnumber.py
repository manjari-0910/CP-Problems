# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math as mt

MAXN = 100001

# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]

# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):

        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i

    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):

        # checking if i is prime
        if (spf[i] == i):

            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):

                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i

# A O(log n) function returning prime
# factorization by dividing by smallest
# prime factor at every step
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]

    return ret

# Driver code

# precalculating Smallest Prime Factor
sieve()

def ispowerful(n):
	factors=getFactorization(n)
	for i in factors:
		if n%(i**2)!=0:
			return False
	return True

def nthpowerfulnumber(n):
	# Your code goes here
	count=0
	i=1
	while (count<=n):
		if ispowerful(i):
			count+=1
		i+=1
	return i-1
	pass

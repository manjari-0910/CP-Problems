# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math

def isprime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def istrunkprime(i):
    if '0' in str(i):
        return False
    while len(str(i))>1:
        i=int(str(i)[1:])
        if isprime(i)==False:
            return False
    return True


def fun_nth_lefttruncatableprime(n):
    i=2
    while (n>=0):
        if len(str(i))>=1 and istrunkprime(i) and isprime(i):
            n-=1
        i+=1

    return i-1

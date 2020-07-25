# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
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

def factors(a):
    li=[]
    while a%2==0:
        li.append(2)
        a=a//2

    for i in range(3, int(math.sqrt(a)) + 1, 2):
        while a % i == 0:
            li.append(i)
            a = a // i
    if a>2:
        li.append(int(a))
    return li

def sumof(n):
    li=[int(i) for i in str(n)]
    return sum(li)


def fun_nth_smithnumber(n):
    count=0
    i=4
    while (count<n):
        i+=1
        digitsum=sumof(i)
        numfactors=factors(i)
        primesum=sum([sumof(j) for j in numfactors])
        if digitsum==primesum and isprime(i)==False:
            count+=1
    return (i)





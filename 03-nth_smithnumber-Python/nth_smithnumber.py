# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(a):
    if a<=1:
        return False
    else:
        for i in range(2,(a//2)+1):
            if a%i==0:
                return False
        return True

def factors(a):
    li=[]
    for i in range(2,(a//2)+1):
        if a%i==0 and isprime(i)==True:
            li.append(i)
    return li


def fun_nth_smithnumber(n):
    count=0
    li=[]
    i=4
    while (count<n):
        if isprime(i)==False:
            digits=list(str(i))
            digits=list(map(int,digits))
            s=sum(digits)
            primes=factors(i)
            for j in primes:
                if isprime(i/j) and j+(i/j)==s:
                    count+=1
    return (i)





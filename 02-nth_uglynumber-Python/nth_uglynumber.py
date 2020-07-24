# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

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

def isugly(n):
    # li=[]
    for i in range(1,(n//2)+1):
        if n%i==0 and isprime(i):
            if i!=2 and i!=3 and i!=5:
                return False
    return True

def fun_nth_uglynumber(n):
    if n==0:
        return 1
    else:
        i=1
        c=1
        while c<n:
            i+=1
            if isugly(i):
                c+=1
    return i

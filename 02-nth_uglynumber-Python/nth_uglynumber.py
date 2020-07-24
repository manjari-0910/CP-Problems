# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def maxDivide( a, b ):
    while a % b == 0:
        a = a / b
    return a

def isugly(n):
    n=maxDivide(n,2)
    n=maxDivide(n,3)
    n=maxDivide(n,5)
    return n==1

def fun_nth_uglynumber(n):
    i=1
    c=1
    while c<=n:
        i+=1
        if isugly(i):
            c+=1
    return i

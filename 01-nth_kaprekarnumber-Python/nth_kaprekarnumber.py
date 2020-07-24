# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def remzeros(n):
    n=str(n)
    count=0
    for i in n[::-1]:
        if i=='0':
            count+=1
        else:
            break

    return int(n[:len(n)-count])

def iskaprekar(i):
    n=str(i**2)
    if len(n)>1:
        if i==(int(n[:len(n)//2])+int(n[len(n)//2:])):
            return True
        else:
            m=remzeros(n[:len(n)//2])
            if int(m)+int(n[len(n)//2:])==i:
                return True
    return False

def fun_nth_kaprekarnumber(n):
    if n==0:
        return 1
    i=9
    count=0
    while(count<n):
        if iskaprekar(i):
            count+=1
        i+=1
    return i-1
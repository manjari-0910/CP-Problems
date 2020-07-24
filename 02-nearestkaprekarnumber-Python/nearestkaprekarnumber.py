# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
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

def fun_nearestkaprekarnumber(n):
    li=[]
    for i in range(11):
        li.append(fun_nth_kaprekarnumber(i))
    for i in range(len(li)-1):
        if n>li[i] and n<li[i+1]:
            if n-li[i]<=n+li[i+1]:
                return li[i]
            else:
                return li[i+1]


    # return 1
# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def issmall(num):
    prev = 10
    while (num):
        rem = num % 10
        num /= 10
        if rem > prev:
            return False
        prev = rem
    return True


def fun_nth_tidynumber(n):
    c=0
    i=0
    while c<=n:
        if issmall(i):
            c+=1
        i+=1
    return i-1
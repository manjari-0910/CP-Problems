# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def issmall(n):
    if n<10:
        return True
    else:
        while(n!=0):
            rem=n%10
            n=n//10
            rem2=n%10
            if rem2>rem:
                return False
        return True


def fun_nth_tidynumber(n):
    c=0
    i=1
    while True:
        if issmall(i):
            if c==n:
                break
            c+=1
        i+=1
    return i


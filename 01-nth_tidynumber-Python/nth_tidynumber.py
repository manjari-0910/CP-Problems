# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def issmall(n):
    n=list(str(n))
    n=list(map(int,n))
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            return False
    return True


def fun_nth_tidynumber(n):
    if len(str(n))==1:
        return n+1
    else:
        c=6
        i=10
        while c<=n:
            if issmall(i):
                c+=1
            i+=1
        return i
    return 0
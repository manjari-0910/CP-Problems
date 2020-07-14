"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    f=0
    s=1
    if position==0:
        return f
    elif position==1:
        return s
    else:
        for i in range(2,position+1):
            temp=f+s
            f=s
            s=temp
        return s
    return -1

# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def isLychrel(num):
    for i in range(25):
        num = num + reverse(num)
        if num == reverse(num):
            return False
    return True

def reverse(num):
    reverse = 0
    while (num > 0):
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = int(num / 10)
    return reverse

def nthlychrelnumbers(n):
	# your code goes here
	i=196
	c=0
	while c<n:
		if isLychrel(i):
			c+=1
		i+=1
	return i-1
	pass
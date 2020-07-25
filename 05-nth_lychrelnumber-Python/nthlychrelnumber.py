# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

MAX_ITERATIONS = 20;

# Function to check whether number is
# Lychrel Number
def isLychrel(number):

    for i in range(MAX_ITERATIONS):
        number = number + reverse(number)
        if number == reverse(number):
            return False
    return True

def reverse(number):
    reverse = 0
    while (number > 0):
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = int(number / 10)
    return reverse

def nthlychrelnumbers(n):
	# your code goes here
	i=1
	c=0
	while c<n:
		if isLychrel(i):
			c+=1
		i+=1
	return i-1
	pass
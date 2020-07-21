# Write the function alternatingSum(a) that takes a list of numbers and returns the
# alternating sum (where the sign alternates from positive to negative or vice versa).
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(l):
	if (len(l)==0):
		return 0
	else:
		pos=0
		neg=0
		for i in range(len(l)):
			if i%2==0:
				pos+=l[i]
			else:
				neg+=l[i]
		return (pos-neg)
	# return 0



# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l):
	sum=0
	return rec(l,0,sum)
	# return 0

def rec(l,i,sum):
	if i==len(l):
		return sum
	else:
		if i%2==0:
			sum+=l[i]
		else:
			sum-=l[i]
		i+=1
		return rec(l,i,sum)

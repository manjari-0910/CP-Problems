# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l):
	p,n =rec(l,0,[],[])
	return sum(p)-sum(n)
	# return 0

def rec(l,i,p,n):
	if i > len(l):
		return p,n
	if i%2==0:
		p.append(i)
	else:
		n.append(i)
	i+=1
	rec(l,i,p,n)

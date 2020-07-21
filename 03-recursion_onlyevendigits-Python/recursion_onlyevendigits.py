# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
		return evenonly(l,[],0)

def evenonly(l,a,i):
	if i==len(l):
		return a
	else:
		li=list(str(l[i]))
		li=list(map(int,li))
		li2=[]
		for j in li:
			if j%2==0:
				li2.append(j)
		li2=list(map(str,li2))
		li2=''.join(li2)
		if len(li2)==0:
			a.append(0)
		elif int(li2)%2==0:
			a.append(int(li2))
		i+=1
		return evenonly(l,a,i)
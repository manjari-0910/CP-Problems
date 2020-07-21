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
		n=l[i]
		li=[]
		for i in range (len(l[i])):
			rem=n%10
			n=n//10
			if rem%2==0:
				li.append(rem)
		li=list(map(str,li[::-1]))
		li2=''.join(li)
		if int(li2)%2==0:
			a.append(int(li2))
		i+=1
		return evenonly(l,a,i)
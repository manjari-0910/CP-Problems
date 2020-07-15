# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative
# single digit (between 0 and 9 inclusive). This function returns the number n with
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left,
# so the 0th digit is the rightmost digit.



def fun_set_kth_digit(n, k, d):
	num=list(str(n)[::-1])
	try:
		if num[k] in "0123456789":
			num[k]=str(d)
		elif(num[k] in "-"):
			num[k]=str(d)
			num.append("-")
		return int(''.join(num[::-1]))
	except:
		num.append(str(d))
		return int(''.join(num[::-1]))



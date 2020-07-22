# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	if x==0:
		return y
	elif y==0:
		return x
	elif len(str(x))==1 and len(str(y))==1:
		return x+y
	else:
		a=x+y
		if len(str(x))==len(str(y)):
			l=len(str(x))-1
			a=str(a)[-l:]
			return (int(a)-10)



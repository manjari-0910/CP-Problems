# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
import math
def islegaltriangle(s1, s2, s3):
	# your code goes here
	if s1<=0 or s2<=0 or s3<=0:
		return False
	maxi=max(max(s1,s2),s3)
	if maxi==s1 and s2+s3>s1:
		return True
	elif maxi==s2 and s1+s3>s2:
		return True
	elif maxi==s3 and s2+s1>s3:
		return True
	else:
		return False
	pass

def trianglearea(s1, s2, s3):
	# your code goes here
	if islegaltriangle(s1,s2,s3):
		s=(s1+s2+s3)/2
		area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
		return area
	else:
		return 0
	pass

def fun_distance(x1, y1, x2, y2):
	# your code goes here
	if x1==x2 and y1==y2:
		return 0
	else:
		# dist=0
		return (math.sqrt(math.pow((y2-y1),2) + math.pow((x2-x1),2)))

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	ab=fun_distance(x1, y1, x2, y2)
	bc=fun_distance(x3, y3, x2, y2)
	ca=fun_distance(x1, y1, x3, y3)
	return trianglearea(ab,bc,ca)
	pass
# Write the function fun_distance(x1, y1, x2, y2)
# that takes four int values x1, y1, x2, y2
# that represent the two points (x1, y1) and (x2, y2),
# and returns the distance between those points as a int.
import math

def fun_distance(x1, y1, x2, y2):
	# your code goes here
	if x1==x2 and y1==y2:
		return 0
	else:
		# dist=0
		return math.sqrt((math.pow(y2-y1),2) + (math.pow(x2-x1),2))
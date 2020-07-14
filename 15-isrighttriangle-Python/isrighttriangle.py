# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def slope(x1,y1,x2,y2):
	return (y2-y1)/(x2-x1)

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	ab = slope(x1,y1,x2,y2)
	bc = slope(x2,y2,x3,y3)
	ca = slope(x3,y3,x1,y1)
	if ab * bc == -1:
		return True
	elif bc*ca == -1:
		return True
	elif ab*ca == -1:
		return True
	else:
		return False
	pass

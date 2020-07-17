# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.

def isrotated(w1, w2):
	for i in range(len(w1)):
		if (w1[i:]+w1[:i] == w2) or (w2[i:]+w2[:i] == w1):
			return True
	if w1[::-1]==w2:
		return True
	return False
	pass
# Write the function getAverage(values) that takes a string of
# comma-separated non-negative integer values, and returns their
# average as a float (even though the values themselves are integers).
# Note that some values may not be non-negative integers, and these
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.


# import math

def fun_getaverage(s):
	s=s.split(',')
	li=[]
	for i in s:
		try:
			if float(i)>=0:
				li.append(float(i))
		except:
			m=0
	if len(li)==0:
		return 0.0
	else:
		return (sum(li)/len(li))


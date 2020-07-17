# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().

def fun_replace(s1, s2, s3):
	try:
		i1=s1.index(s2)
		s=s1[:i1]
		s+=s3
		s+=s1[i1+len(s2):]

		return s
	except:
		return s1
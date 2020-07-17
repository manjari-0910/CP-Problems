# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().

def multipletimes(s1,s2):
	c=0
	for i in range (len(s1)-len(s2)):
		if s2 in s1[i:]:
			c+=1
	return c

def fun_replace(s1, s2, s3):
	try:
		if multipletimes(s1,s2)==1:
			i1=s1.index(s2)
			s=s1[:i1]
			s+=s3
			s+=s1[i1+len(s2):]
		else:
			c=multipletimes(s1,s2)
			i1=0
			while c!=0:
				i1=s1[i1+len(s2):].index(s2)
				s=s1[:i1]
				s+=s3
				s+=s1[i1+len(s2):]
				c-=1
		return s
	except:
		return s1
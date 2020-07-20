# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	s=s.strip()
	if len(s)==1:
		return s
	else:
		li=[]
		for i in s:
			if (s.count(i),i) not in li and i!=' ':
				li.append((s.count(i),i))
		li.sort(key=lambda x:x[0],reverse=True)
		try:
			return li[n-1][1]
		except:
			return li[0][1]



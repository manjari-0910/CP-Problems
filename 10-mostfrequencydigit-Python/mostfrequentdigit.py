# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n=str(n)
	d={}
	for i in n:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	s=""
	max=0
	same=[]
	for i in d:
		if d[i]>max:
			max=d[i]
			s=i
	for i in d:
		if d[i]==max:
			same.append(d)
	same = list(map(int,same))
	if len(same)>1:
		return min(same)
	if max==1:
		return int(n[0])
	else:
		return int(s)
	pass
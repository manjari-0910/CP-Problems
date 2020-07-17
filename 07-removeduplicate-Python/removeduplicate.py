# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	if len(text)<=1:
		return text
	else:
		d={}
		for i in text:
			if i in d:
				d[i]+=1
			else:
				d[i]=1
		return ''.join(list(d.keys()))
	pass
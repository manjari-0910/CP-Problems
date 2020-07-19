"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(a,lo,hi):
	i=lo
	j=hi+1
	while True:
		i+=1
		while (a[i]<a[lo]):
			i+=1
			if i==hi:
				break
		j-=1
		while a[lo]<a[j]:
			j-=1
			if j==lo:
				break
		if (i>=j):
			break
		a=each(a,i,j)
	a=each(a,lo,j)
	return j

def each(a,x,j):
	int a[x],a[y]=a[y],a[x]
	return a

def quicksort(array,low,high):
	if low<high:
		j=partition(array,low,high)
		quicksort(arr,low,j-1)
		quicksort(arr,j+1,high)
	return

def quicksort(array):
	# Your code goes here
	quicksort(array,0,len(array)-1)
	return array
	pass
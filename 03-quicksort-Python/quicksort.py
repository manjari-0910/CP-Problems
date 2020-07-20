"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array,lo,hi):
	pivot=array[lo]
	i=lo+1
	j=hi
	while True:
		while (i<=j and array[j]>=pivot):
			j-=1
		while (i<=j and array[i]<=pivot):
			i+=1
		if i<=j:
			array[i],array[j]=array[j],array[i]
		else:
			break
	array[lo],array[hi]=array[hi],array[lo]
	return hi

def qsort(array,low,high):
	if low<high:
		j=partition(array,low,high)
		qsort(array,low,j-1)
		qsort(array,j+1,high)
	return

def quicksort(array):
	# Your code goes here
	qsort(array,0,len(array)-1)
	return array
	pass
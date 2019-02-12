def quickSort(lst):
	quickSortHelper(lst, 0, len(lst)-1)

def quickSortHelper(lst, first, last):
	if first < last:
		splitpoint = partition(lst, first, last)
		quickSortHelper(lst, first, splitpoint-1)
		quickSortHelper(lst, splitpoint+1, last)

def partition(lst, first, last):
	pivotvalue = lst[first]
	left = first+1
	right = last

	done = False
	while not done:
		while left <= right and lst[left] <= pivotvalue:
			left += 1
		while right >= left and lst[right] >= pivotvalue:
			right -= 1
		if right < left:
			done = True
		else:
			lst[left], lst[right] = lst[right], lst[left]
	lst[first], lst[right] = lst[right], lst[first]
	return right

lst =  [54,26,93,17,77,31,44,55,20]
quickSort(lst)
print(lst==[17, 20, 26, 31, 44, 54, 55, 77, 93])

def pivoting(array):
	'''
	pivit around the first element
	using O(n) extra memory
	Note: we can always swap the pivot element
	with the first element
	'''
	pivot = array[0] 

	result_array = [0]*len(array) # pre-allocated array

	left_pointer = 0
	right_pointer = len(result_array)-1

	for i in range(1,len(array)):
		if array[i] < pivot:
			result_array[left_pointer] = array[i]
			left_pointer += 1
		elif array[i] > pivot:
			result_array[right_pointer] = array[i]
			right_pointer -= 1

	result_array[left_pointer] = pivot

	return result_array

def partition(array, leftBoundary, rightBoundary):
	'''
	partition a subarray in O(n) time
	essentially the same as pivoting
	but does not need extra space
	'''
	pivot = array[leftBoundary]
	i = leftBoundary + 1

	for j in range(i, rightBoundary+1):
		if array[j] < pivot:
			array[j], array[i] = array[i], array[j]
			i += 1

	array[leftBoundary], array[i-1] = array[i-1], array[leftBoundary]
	return i - 1 # position of pivot in new array

def quickSort(array,start,end):
	if len(array) == 1:
	 	return array
	if start < end:
		pivot_index = partition(array,start,end)
		quickSort(array,start,pivot_index-1)
		quickSort(array,pivot_index+1,end)
		return array


# print(partition([1],0,0))

# print(partition([1,1,1,1],0,3))
# print(partition([2,2,1,1],0,3))

# print(partition([1,2],0,1))
# print(partition([2,1],0,1))

# print(partition([9,8,5],1,2))
# print(partition([9,8,5],0,2))

# print(partition([3,2,7,4,5],0,4))
# print(partition([3,2,7,4,5],1,3))
# print(partition([1,1,1,1,1],0,4))
# print(partition([3,2,7,4,5],3,4))
# print(partition([1,1,1,1,2],0,4))

# print(quickSort([1,1,1,1,2],0,4))
# print(quickSort([1,1,1,1,2],1,4))

# print(quickSort([1,1],0,1))
# print(quickSort([1,1,1],0,2))
# print(quickSort([1,1,1,1],0,3))

# print(quickSort([1,2],0,1))
# print(quickSort([1,1,2],0,2))
# print(quickSort([1,1,1,2],0,3))

# print(quickSort([1,1,1,1,2],0,4))
# print(quickSort([1,1,1,1,2],0,-1))
# print(quickSort([1,1,1,1,2],1,4))
# print(quickSort([1,1,1,1,1,2],0,5))

# print(quickSort([5,3,4,6,2,1,7],0,6))
# print(quickSort([13,45,23,75,36,87],0,5))

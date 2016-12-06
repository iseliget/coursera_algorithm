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

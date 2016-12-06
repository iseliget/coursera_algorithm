def merge(left_array,right_array):
	'''
	will be used in merge sort
	assuming len(left_array) = len(right_array)
	'''
	result_array = [0]*(len(left_array)+len(right_array))
	left_index, right_index = 0, 0

	for result_index in range(0,len(result_array)):
		if (left_index < len(left_array)-1) and (right_index < len(right_array)-1):
			if left_array[left_index] <= right_array[right_index]:
				result_array[result_index] = left_array[left_index]
				left_index += 1
			else:
				result_array[result_index] = right_array[right_index]
				right_index += 1
		# when left_index makes to the end
		elif left_index == len(left_array)-1:
			if right_index > len(right_array)-1:
				result_array[-1] = left_array[-1]
				return result_array
			elif left_array[left_index] < right_array[right_index]:
				result_array[result_index] = left_array[left_index]
				result_array[result_index+1:] = right_array[right_index:]
				return result_array
			else:
				result_array[result_index] = right_array[right_index]
				right_index += 1
		# when right_index makes to the end
		elif right_index == len(right_array)-1:
			if left_index > len(left_array)-1:
				result_array[-1] = right_array[-1]
			elif right_array[right_index] < left_array[left_index]:
				result_array[result_index] = right_array[right_index]
				result_array[result_index+1:] = left_array[left_index:]
				return result_array
			else:
				result_array[result_index] = left_array[left_index]
				left_index += 1
				
	return result_array

def mergeSort(array):
	if len(array) < 2:
		return array
	else:
		left_array = mergeSort(array[0:len(array)//2])
		right_array = mergeSort(array[len(array)//2:])

		return merge(left_array,right_array)

def crossInv(left_array,right_array):
	result_array = [0]*(len(left_array)+len(right_array))
	left_index, right_index = 0, 0
	inversions = 0

	for result_index in range(0,len(result_array)):
		if (left_index < len(left_array)-1) and (right_index < len(right_array)-1):
			if left_array[left_index] <= right_array[right_index]:
				result_array[result_index] = left_array[left_index]
				left_index += 1
			else:
				result_array[result_index] = right_array[right_index]
				right_index += 1
				inversions += len(left_array[left_index:])
		# when left_index makes to the end
		elif left_index == len(left_array)-1:
			if right_index > len(right_array)-1:
				result_array[-1] = left_array[-1]
				return [result_array, inversions]
			elif left_array[left_index] <= right_array[right_index]:
				result_array[result_index] = left_array[left_index]
				result_array[result_index+1:] = right_array[right_index:]
				#inversions += len(left_array[left_index:])
				return [result_array, inversions]
			else:
				result_array[result_index] = right_array[right_index]
				inversions += len(left_array[left_index:])
				right_index += 1
		# when right_index makes to the end
		elif right_index == len(right_array)-1:
			if left_index > len(left_array)-1:
				result_array[-1] = right_array[-1]
				return [result_array, inversions]
			elif right_array[right_index] <= left_array[left_index]:
				result_array[result_index] = right_array[right_index]
				result_array[result_index+1:] = left_array[left_index:]
				inversions += len(left_array[left_index:])
				return [result_array, inversions]
			else:
				result_array[result_index] = left_array[left_index]
				# inversions += len(left_array[left_index:])
				left_index += 1
		# print(result_array)
		# print(inversions)


def mergeSort(array):
	if len(array) < 2:
		return [array,0]
	else:
		l = mergeSort(array[0:len(array)//2])[0]
		linv = mergeSort(array[0:len(array)//2])[1]

		r = mergeSort(array[len(array)//2:])[0]
		rinv = mergeSort(array[len(array)//2:])[1]

		c = crossInv(l, r)[0]
		cinv = crossInv(l, r)[1]

		tinv = linv + rinv + cinv

		return [c,tinv]

print(crossInv([1,2],[4,8]))
print(crossInv([4,8],[1,2]))
print(crossInv([1,4],[2,3]))
print(crossInv([2,3],[1,4]))
print(crossInv([1,4],[2,5]))
print(crossInv([2,5],[1,4]))

print(mergeSort([3]))
print(mergeSort([2,4]))
print(mergeSort([3,4,2]))
print(mergeSort([1]))
print(mergeSort([5,6]))
print(mergeSort([1,5,6]))
print(mergeSort([3,2,4,1,5,6]))
print(mergeSort([8,4]))
print(mergeSort([2,1]))
print(mergeSort([8,4,2,1]))

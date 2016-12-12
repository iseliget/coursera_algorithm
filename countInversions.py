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


def countInv(array):
	if len(array) < 2:
		return [array,0]
	else:
		result1 = countInv(array[0:len(array)//2])
		l = result1[0]
		linv = result1[1]

		result2 = countInv(array[len(array)//2:])
		r = result2[0]
		rinv = result2[1]

		result3 = crossInv(l,r)
		c = result3[0]
		cinv = result3[1]

		tinv = linv + rinv + cinv

		return [c,tinv]

def slowInv(array):
	inversions = 0
	for i in range(0,len(array)):
		for j in range(i,len(array)):
			if array[i] > array[j]:
				inversions += 1
	return inversions

print(countInv([1, 6, 3, 2, 4, 5]))
print(countInv([9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]))
print(countInv([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]))
print(countInv([4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]))

def bubble_sort(l):
	'''
	complexity O(n^2)
	'''
	for num_of_pass in range(0,len(l)-1):
		for i in range(0,len(l)-1):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
		print("Pass " + str(num_of_pass) + ". Result: " + str(l))
	return l

def selection_sort(l):
	for i in range(0,len(l)):
		unsorted_list = l[i:]
		minimum = min(unsorted_list) # this step is O(n)
		l[l.index(min(unsorted_list))] = l[i]
		l[i] = minimum
		print(l)
	return l


def merge(array1,array2):
	'''
	will be used in merge sort
	'''
	result = [0]*len(array1)*2

	i = 0
	j = 0

	for k in range(0,len(result)):
		if i != len(array1)-1 and j != len(array2)-1:
			if array1[i] < array2[j]:
				result[k] = array1[i]
				i = i + 1
			elif array1[i] > array2[j]:
				result[k] = array2[j]
				j = j + 1
		elif i == len(array1)-1:
			if j > len(array2)-1:
				result[-1] = array1[-1]
				return result
			elif array1[i] < array2[j]:
				result[k] = array1[i]
				result[k+1:] = array2[j:]
				return result
			else:
				result[k] = array2[j]
				j = j + 1
		elif j == len(array2)-1:
			if i > len(array1)-1:
				result[-1] = array2[-1]
			elif array2[j] < array1[i]:
				result[k] = array2[j]
				result[(k+1):] = array1[i:]
				return result
			else:
				result[k] = array1[i]
				i = i + 1
				
	return result

def mergeSort(array):
	if len(array) == 1:
		return array
	else:
		left_array = mergeSort(array[0:len(array)//2])
		right_array = mergeSort(array[len(array)//2:])
		return merge(left_array,right_array)


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


#bubble_sort([-1,-3,-1,0,25,9,7,5,17])
selection_sort([5,4,3,2,1])

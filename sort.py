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

bubble_sort([-1,-3,-1,0,25,9,7,5,17])

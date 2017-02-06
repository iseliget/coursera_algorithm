# This script compares the differences between
# using adjacency list and adjacency matrix

def breath_first_search(adjacency_list,node):
	explored = list()

	myQueue = queue()
	myQueue.enqueue(node)

	while myQueue.isEmpty == False:
		# contributes to O(|V|)
		current_node = myQueue.dequeue()

		# contributes to O(|E|)
		for adjacent_node in current_node:
			if adjacent_node not in explored:
				myQueue.enqueue(adjacent_node)
				explored.append(adjacent_node)
			else:
				pass

	# overall time complexity is O(|V| + |E|)


def breath_first_search(adjacency_matrix,node):
	explored = list()

	myQueue = queue()
	myQueue.enqueue(node)

	while myQueue.isEmpty == False:
		# contributes to O(|V|)
		current_node = myQueue.dequeue()

		# contributes to O(|V|)
		for nodes in adjacency_matrix(current_node,:):
			if nodes == 1:
				if nodes not in explored:
					myQueue.enqueue(nodes)
					explored.append(nodes)
				else:
					pass
			else:
				pass

	# overall time complexity is O(|V|^2)

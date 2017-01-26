class queue(object):
	list_of_items = []

	def __init__(self):
		pass

	def enqueue(self,item):
		self.list_of_items.append(item)

	def dequeue(self):
		return self.list_of_items.pop(0)

	def isEmpty(self):
		if len(self.list_of_items)==0:
			return True
		else:
			return False

	def peek(self):
		try:
			return self.list_of_items[0]
		except IndexError:
			print("empty queue")

# Implement the graph using adjacency list
# The graph is a tree
myGraph = [[1,2],[0,3,4],[0,4,5],[1,6,7],[1,2],[2,8,9,10],[3],[3],[5],[5],[5]]

myQueue = queue()
myQueue.enqueue(0) # start with node 0

explored_node = []
distance = [0] + [100000000]*10 # any large number will do

while myQueue.isEmpty()==False:
	current_node = myQueue.dequeue()
	for adj_nodes in myGraph[current_node]:
		if adj_nodes in explored_node:
			pass
		else:
			distance[adj_nodes] = distance[current_node] + 1
			explored_node.append(adj_nodes)
			myQueue.enqueue(adj_nodes)
	explored_node.append(current_node)

print(distance) # distance[i] tells you the number of edges from node 0 to node i

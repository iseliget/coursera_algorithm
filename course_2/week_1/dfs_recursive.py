class stack(object):
	list_of_items = []

	def __init__(self):
		pass

	def push(self,item):
		self.list_of_items.append(item)

	def top(self):
		return self.list_of_items[-1]

	def pop(self):
		self.list_of_items.pop()

	def isEmpty(self):
		return self.list_of_items==[]

	def getSize(self):
		return len(self.list_of_items)

# Implement the graph using adjacency list
# The graph is a tree
myGraph = [[1,2],[0,3,4],[0,4,5],[1,6,7],[1,2],[2,8,9,10],[3],[3],[5],[5],[5]]
exploredNodes = []

def dfs(node):
	if node in exploredNodes:
		pass
	else:
		exploredNodes.append(node)
		for adj_nodes in myGraph[node]:
			dfs(adj_nodes)

dfs(0)
print(exploredNodes)

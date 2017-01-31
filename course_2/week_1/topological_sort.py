# Implement the graph using adjacency list
# The graph is a tree

# myGraph = [[1,2],[3,4],[4,5],[],[],[]]
# myGraph = [[1,2],[3],[3],[]]
# myGraph = [[3],[4],[0,1,5],[],[3],[4]]
# myGraph = [[],[0,2],[]]
# myGraph = [[1],[],[0,3],[]]

labels = [0]*len(myGraph)
exploredNodes = []
current_label = len(myGraph)

def dfs(graph,node):
	global current_label
	global exploredNodes

	exploredNodes.append(node)

	for adj_nodes in graph[node]:
		if adj_nodes not in exploredNodes:
			dfs(graph,adj_nodes)

	labels[node] = current_label
	current_label = current_label - 1

for i in range(0,len(myGraph)):
	if i not in exploredNodes:
		dfs(myGraph,i)
	else:
		pass

print(labels)

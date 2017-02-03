import copy

t = 0 # number of nodes processed by DFS so far
s = 0 # most recent source from which a DFS was initiated
	
graph = [[3], [7], [5], [6], [1], [8], [0], [4, 5], [2, 6]] # The graph used as an example during the lecture

finishing_time = [0]*len(graph)
leaders = [0]*len(graph)
explored_nodes = []

def dfs(graph,node):
    global t
    global s
    global explored_nodes
    global leaders

    explored_nodes.append(node)
    leaders[node] = s

    for adj_node in graph[node]:
        if adj_node not in explored_nodes:
            dfs(graph,adj_node)

    t += 1
    finishing_time[node] = t
    

def reverse(graph):
	reversed_graph = []
	for i in range(0,len(graph)):
		reversed_graph.append([])

	for i in range(0,len(graph)):
		for adj_node in graph[i]:
			reversed_graph[adj_node].append(i)

	return reversed_graph

# First pass
reversed_graph = reverse(graph)
for i in range(len(reversed_graph)-1,-1,-1):
	if i not in explored_nodes:
		dfs(reversed_graph,i)
print(finishing_time)


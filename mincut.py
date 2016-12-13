# suppose the adjacency list is a list of list
# e.g. [[],[2,4],[1,3,4],[2,4],[1,2,3]]
import random

def contraction(adj_list):
	u = random.randint(1,len(adj_list)-1)
	v = adj_list[u][random.randint(0,len(adj_list[u]))-1]

	vertex_1 = min(u,v)
	vertex_2 = max(u,v)

	# list of vertices that are adjacent to vertex 1, except for vertex 2
	adj_to_vertex_1 = [vertex for vertex in adj_list[vertex_1] if vertex != vertex_2]

	for vertex in adj_to_vertex_1:
		adj_list[vertex].append(vertex_2)
		adj_list[vertex_2].append(vertex)
		adj_list[vertex].remove(vertex_1)
	
	adj_list[vertex_2] = [vertex for vertex in adj_list[vertex_2] if vertex != vertex_1]
	adj_list[vertex_1] = []

	return adj_list

print(contraction([[],[2,3,3],[1,3],[2,1,1]]))
print(contraction([[],[2,4],[1,3,4],[2,4],[1,2,3]]))

# suppose the adjacency list is a list of list
# e.g. [[],[2,4],[1,3,4],[2,4],[1,2,3]]
import random
import csv

def contraction(adj_list):
	u = 0
	while len(adj_list[u]) == 0:
		u = random.randint(1,len(adj_list)-1)

	v = adj_list[u][random.randint(0,len(adj_list[u])-1)]

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

def mincut(adj_list):
	while adj_list.count([]) < len(adj_list) - 2:
		#print(adj_list)
		adj_list = contraction(adj_list)
	#print(adj_list)
	vertices_left = [x for x in adj_list if x!= []]
	print(len(vertices_left[0]))
	return len(vertices_left[0])

# mincut([[],[2,3,4,7],[1,3,4],[1,2,4],[1,2,3,5],[4,6,7,8],[5,7,8],[1,5,6,8],[5,6,7]])
# mincut([[],[4,2,7,3],[4,1,3],[1,2,4],[5,1,2,3],[8,7,6,4],[8,5,7],[6,8,5,1],[7,6,5]])
# mincut([[],[2,3,4],[1,3,4],[1,2,4],[1,2,3,5],[4,6,7,8],[5,7,8],[5,6,8],[5,6,7]])
# mincut([[],[3,4,2],[1,4,3],[1,2,4],[5,3,2,1],[4,8,6,7],[8,7,5],[5,8,6],[5,7,6]])

graph = [[]]
with open('graph2.txt','rb') as f:
	reader = csv.reader(f,delimiter='\t')
	for row in reader:
		# print(row)
		graph.append([int(x) for x in row[1:-1]])
# print(graph[0:3])
mincut(graph)

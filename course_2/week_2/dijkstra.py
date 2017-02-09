import csv

graph = [[]]

# Preprocessing, reading the graph
with open("graph.txt","r") as csvfile:
	grpah_reader = csv.reader(csvfile, delimiter='\t')
	for row in grpah_reader:
		graph.append([])
		for item in row[1:-1]:
			graph[-1].append([])
			graph[-1][-1].append(int(item.split(",")[0]))
			graph[-1][-1].append(int(item.split(",")[1]))

source = 1

discovered_nodes = [1]

shortest_path_distances = [10000000]*len(graph) # i-th position is the shortest path from the source to vertex i
shortest_path_distances[source] = 0

# Dijkstra algorithm begins
while len(discovered_nodes) < len(graph)-1 :
	min_greedy_criterion = 100000000 # some large number

	for node in discovered_nodes:
		for adj_tuples in graph[node]:
			
			if adj_tuples[0] in discovered_nodes:
				pass
			else:
				greedy_criterion = shortest_path_distances[node] + adj_tuples[1]
				if greedy_criterion < min_greedy_criterion:
					min_greedy_criterion = greedy_criterion
					edge_to_be_added = adj_tuples[0]

	discovered_nodes.append(edge_to_be_added)

	shortest_path_distances[edge_to_be_added] = min_greedy_criterion


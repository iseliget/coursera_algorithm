import copy

def reverse(graph):
    reversed_graph = copy.deepcopy(graph) # cannot use graph[:] because the List "graph" contains Lists
    reversed_nodes = []

    for node in range(0,len(reversed_graph)):

        for adj_node in reversed_graph[node][:]: # [:] is important

            if adj_node not in reversed_nodes:
                reversed_graph[adj_node].append(node)
                reversed_graph[node].remove(adj_node)
            else:
                pass

        reversed_nodes.append(node)

    return reversed_graph

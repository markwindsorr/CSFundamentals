# Breadth First Search

"""
The breadth first search (BFS) is an algorithm that starts with a node, then checks
all the neighbours of the current neighbour node

BFS explores nodes one depth level at a time

"""


# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

# Visits all the nodes of a graph
def bfs(graph, start):

	# Keep track of all visited nodes
	explored_nodes = []

	# Keep track of nodes to be checked
	queue = [start]

	# Keep looping while there are nodes to be checked
	while queue:

		# Pop the first node from the queue
		node = queue.pop(0)

		# If the node has not been explored, then proceed
		if node not in explored_nodes:

			# Add node to the list of explored nodes
			explored_nodes.append(node)

			# Here, we can get neighbours 
			neighbours = graph[node]

			# Add neighbours of the node to queue
			for neighbour in neighbours:
				queue.append(neighbour)

	return explored




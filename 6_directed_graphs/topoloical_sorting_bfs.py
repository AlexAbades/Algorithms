# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of
# vertices such that for every directed edge uv, vertex u comes before v in the
#  ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
from collections import defaultdict
n, m = map(int, input().split())


# We need to created a Direct Graph and then perform topological sorting
# We must Asume That is DAG


class DirectedGraph:
    def __init__(self, n_nodes) -> None:
        # Create an adjacent list to store a list of vertices that are directly conected to the node
        self.adj_list = defaultdict(list)
        # Create a list to store the in degrees of each node
        self.in_degree = [0] * n_nodes
    
        # print(self.in_degree)

    # Function to add edges between nodes.
    def add_edge(self, u, v):
        # Keep track of the connetions of each node in the adjacent list
        self.adj_list[u].append(v)
        # Add one in-degree to the node that is being pointed
        self.in_degree[v] += 1
    
    # Create a function for topologycal sorting. 
    def topological_sort(self):
        # Create a queue to dokeep track of the nodes we have to visit in a BFS 
        queue = []
        # If node has no in-degree nodes, add them to the list, so we give them priority
        for i in range(len(self.in_degree)):
            if self.in_degree[i] == 0:
                queue.append(i)
        # Create a variable to check the maximum depth of graph
        
        max_depth = 0
        # Check if queueu is not empty
        while queue:
            # Check current node and mark it as visited
            curr_node = queue.pop(0)
            # for all neighbour nodes check the adjacent list
            for neighbor in self.adj_list[curr_node]:
                # print(max_depth)
                # Decrease the the incoming degree of the neighbour as we've just visited it.
                self.in_degree[neighbor] -= 1
                # Update the max depth of graph
                max_depth = max(max_depth, self.in_degree[neighbor])
                # Checks if the incoming degree of the neighbour is 0, if so, all incoming edges of the neihghbour have been checked
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return max_depth + 1

g = DirectedGraph(n)

for i in range(m):
    x, y = map(int, input().split())
    # Substract 1 to the courses to convert them into a 0 based for the adjacent list
    g.add_edge(y-1, x-1)

print(g.topological_sort())
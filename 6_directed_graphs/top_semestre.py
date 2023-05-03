from collections import defaultdict, deque


# We need to keep track of how many nodes with in-degree 0 we have at the
# begining and every time we remove a node. 
# If at the begining we have a graph with 2 nodes with in degree 0, 
# those two nodes will be in the first semester. Afterwards, we will check for nodes with in-degree 0.
# All nodes with in-degree 0 will go to the same semester. and we repeat the process.
# We need to created a Direct Graph and then perform topological sorting
# We must Asume That is DAG

n, m = map(int, input().split())

# Create the directed graph and initialize in-degrees of all nodes to 0
graph = defaultdict(list)
in_degree = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
    in_degree[x] += 1

# Create a queue to store nodes with in-degree 0 and add them to the queue
queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

# Initialize the semester counter
semester = 0

# Perform topological sort to find the minimum number of semesters needed
while queue:
    # Increment the semester counter
    semester += 1
    # Process all nodes with in-degree 0 in the current semester
    for _ in range(len(queue)):
        node = queue.popleft()
        # Decrement the in-degree of all nodes that the current node points to
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If the neighbor node now has in-degree 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

# Output the minimum number of semesters needed
print(semester)

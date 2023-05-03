from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

# read input values
n, m, a, b = map(int, input().split())

# initialize adjacency list
graph = defaultdict(list)

# read edges and construct the graph
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# breadth-first search function to check if b is reachable from a
def bfs(start, end):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False

# check if b is reachable from a
if bfs(a, b):
    print("YES")
else:
    print("NO")

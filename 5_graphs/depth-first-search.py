import sys 
sys.setrecursionlimit(10000)

def dfs(graph, visited, start, end):
    visited[start] = True
    if start == end:
        return True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, visited, neighbor, end):
                return True
    return False

# Read input
n, m, a, b = map(int, input().split())

# Initialize graph
graph = {i: set() for i in range(1, n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

# Run DFS
visited = [False] * (n+1)
if dfs(graph, visited, a, b):
    print("YES")
else:
    print("NO")

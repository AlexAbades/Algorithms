import sys 
from collections import deque

sys.setrecursionlimit(10000)

# read the first line containing the number of operations
V, M, a, b = list(map(int,input().split()))

# create an empty list to store the operations

def addEdge(v, w):
    global adj
    adj[v].append(w)
    adj[w].append(v)


# read the next n lines containing the operations
for i in range(M):
    v, w = input().split()
    
    addEdge(v, w)   

# A BFS based function to check whether d is reachable from s.
def isReachable(s, d):
     
    # Base case
    if (s == d):
        return True
 
    # Mark all the vertices as not visited
    visited = [False for i in range(V)]
 
    # Create a queue for BFS
    queue = deque()
 
    # Mark the current node as visited and enqueue it
    visited[s] = True
    queue.append(s)
 
    while (len(queue) > 0):
       
        # Dequeue a vertex from queue and print
        s = queue.popleft()
        # queue.pop_front()
 
        # Get all adjacent vertices of the dequeued vertex s
        # If a adjacent has not been visited, then mark it
        # visited  and enqueue it
        for i in adj[s]:
 
            # If this adjacent node is the destination node,
            # then return true
            if (i == d):
                return True
 
            # Else, continue to do BFS
            if (not visited[i]):
                visited[i] = True
                queue.append(i)
    # If BFS is complete without visiting d
    return False




adj = [[] for i in range(V+1)]


if isReachable(a, b):
    print("YES")
else:
    print("False")
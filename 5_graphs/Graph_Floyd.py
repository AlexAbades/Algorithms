# Floyd Warshall Algorithm. 
# Time Complexity: O(V^3) 
# Auxiliary Space: O(V^2)

# read the first line containing the number of operations
N, M, a, b = list(map(int,input().split()))

# create an empty list to store the operations
operations = []

# read the next n lines containing the operations
for i in range(M):
    operation = input().split()
    operations.append(operation)

import sys 
sys.setrecursionlimit(10000)


class Graph():

    def __init__(self, V):
         
        self.V = V
        
        self.g = [[0 for j in range(self.V + 1)]
                     for i in range(self.V + 1)]
    
        for i in range(self.V + 1):
            self.g[i][i] = 1
 
    def addEdge(self, v, w):
 
        self.g[v][w] = 1
        self.g[w][v] = 1
        

    def computePaths(self):
        for k in range(1, self.V + 1):
 
            for i in range(1, self.V + 1):
                for j in range(1, self.V + 1):
                    self.g[i][j] = (self.g[i][j] | (self.g[i][k] and self.g[k][j]))
    def isReachable(self, s, d):
 
        if (self.g[s][d] == 1):
            return "YES"
        else:
            return "NO"

    def display(self):
        print(self.matrix)

    
G = Graph(M)

for i, j in operations:
    G.addEdge(i,j)

print(G.isReachable(a,b))
# read the first line containing the number of operations
n = int(input())

# create an empty list to store the operations
operations = []

# read the next n lines containing the operations
for i in range(n):
    operation = input().split()
    operations.append(operation)

# print the list of operations
print(operations)

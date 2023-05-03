# read the first line containing the number of operations
n = int(input())

# create an empty list to store the operations
operations = []

# read the next n lines containing the operations
for i in range(n):
    operation = input().split()
    operations.append(operation)



# n = 8
# operations = [['PU', '3'], ['PU', '5'], ['PU', '1'], ['PO'], ['PU', '4'], ['PU', '2'], ['PO'], ['PO']]



class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.elements = []

    def push(self, data):
        # Check if the top it's equal than the capacity to see if there is overflow
        if self.top <= self.capacity-1:  # capacity-1 becasue we are using python. For an array of 10 elements, we have till 9 index -> 0 1 2 3 4 5 6 7 8 9
            # If there's no oveflow append
            self.elements.append(data)
            # Add one to the count
            self.top += 1
        else:
            print("Overflow")

    def pop(self):
        # Check for underflow
        if self.top != -1:
            self.top -= 1
            return self.elements.pop()
        else:
            print("Underflow")

    def isEmpty(self):
        if self.top != -1:
            return False
        else:
            return True

    def display(self):
        print(self.elements)


L = Stack(n)

for oper in operations:
    if oper[0] == "PU":
        L.push(oper[1])
    else:
        print(L.pop())


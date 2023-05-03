# =============================================================================
# LIFO -> Last in First out
# Conceptual meaning: Pile of plates one on top of other.
#
# Push:    Add an element to the top of a stack
# Pop:     Remove an element from the top of a stack
# IsEmpty: Check if the stack is empty
# IsFull:  Check if the stack is full
# Peek:    Get the value of the top element without removing it.
#
#   Time:
#     Push, Pop, isEmpty --> O(n)
# Space:
#     O(N)
# =============================================================================


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
    




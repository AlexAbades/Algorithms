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
#
# WAY 2: We create an array of length elements, length N
# =============================================================================


class Stack1:

    def __init__(self, capacity):
        self.elements = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, data):
        if self.top < (self.capacity-1):
            self.top += 1
            self.elements[self.top] = data

        else:
            return 'Overflow'

    def pop(self):
        if self.isEmpty():
            return 'Underflow'
        else:
            value = self.elements[self.top]
            self.top -= 1
            self.elements[self.top+1] = None
            return value

    def display(self):
        print(self.elements)

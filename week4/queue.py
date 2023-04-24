# -*- coding: utf-8 -*-
"""
Created on Mon 24 April 2022
@author: AlexAbades
"""

# =============================================================================
# FIFO -> First In First Out
# Conceptual: Que on a cinema, first that arruves first to get the tiquet
# and first to get out the que
#
# Enqueue:  Add an element to the end of the queue
# Dequeue:  Remove an element from the front of the queue
# IsEmpty:  Check if the queue is empty
# IsFull:   Check if the queue is full
# Peek:     Get the value of the front of the queue without removing it
#
# Time:
#     Enqueue, Dequeue, isEmpty --> O(1)
# Space:
#     O(N)
# =============================================================================


class Queue:

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.tail = -1
        self.head = -1
        self.elements = []

    def is_empty(self):
        # We have to check if the head and the tail are the same. Additionally there is option that the tail points to the head so we need to check if the array is empty
        if self.tail == self.head and not self.elements:
            return True
        else:
            return False

    def is_full(self):
        if self.head == self.tail and self.elements:
            return True
        else:
            return False

    def equeue(self, data):
        # Check for overflow
        if not self.is_full():
            # Check if it is the first time it is being something added, as we need to initialize head and tail
            if self.head == -1:
                self.head += 1
                self.tail += 1
                self.elements.append(data)
            else:
                self.tail += 1
                self.elements.append(data)
                # check if the tail it is bigger than the capcaity, so we can set it to 0 and start again the loop. Again, an N elements array would be a 9 index
                if self.tail > self.capicity-1:
                    self.tail = 0

        else:
            print("Overflow")
            return False
    
    def dequeue(self):
        # Check for underflow
        if not self.is_empty():
            
           if self.head == self.tail and self.elements:
               return self.elements.pop(0) 
        else:
            print("Is Empty")
            return False 


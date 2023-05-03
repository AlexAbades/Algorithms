# read the first line containing the number of operations
n = int(input())

# create an empty list to store the operations
operations = []

# read the next n lines containing the operations
for i in range(n):
    operation = input().split()
    operations.append(operation)


class Node():
    
    def __init__(self, value):
        self.key = value 
        self.next = None
        self.prev = None 



class LinkedList_Queue():
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.head.prev = None 
        
    def dequeue(self):

        # Check for Underflow: If the array has element
        if not self.tail:
            print('Underflow')
            return False
        dequeued_element = self.tail.key
        # Check if the element has more than one number, if it has exactly one number then:
        if not self.head.next:
            self.tail = None
            self.head = None
            return dequeued_element
        self.tail = self.tail.prev 
        self.tail.next = None
        return dequeued_element
        
    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
            
        
        
    def display(self):
        # Displays the key values of each node
        # Linear time O(n)
        n = self.head
        el = []
        if not n:
            return print(el)
        while n.next:
            el.append(n.key)
            n = n.next
        el.append(n.key)
        print(el)
        


L = LinkedList_Queue()

for oper in operations:
    if oper[0] == "E":
        L.enqueue(oper[1])
    else:
        print(L.dequeue())
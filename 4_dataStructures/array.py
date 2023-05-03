

class Array():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.idx = 0
        self.array = [None]*self.capacity
        
    def append(self, value):
        if self.idx < self.capacity:
            self.array[self.idx] = value 
            self.idx += 1
        else:
            print('Overflow')
            return False
    def pop(self):
        if self.idx:
            self.idx -=1
            self.array[self.idx] = None
            
            return
        else: 
            print('Underflow')
            return False 
    
    def isEmpty(self):
        if self.idx:
            return False
        else:
            return True
    
    def display(self):
        return print(self.array)



L = Array(10)
L.display()
L.append(5)
L.display()
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.display()

L1 = Array(11)
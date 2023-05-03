class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap)-1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._percolate_down(0)
        return max_val

    def print_heap(self):
        print(*self.heap)

    def _percolate_up(self, idx):
        if idx <= 0:
            return
        parent_idx = (idx-1) // 2
        if self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._percolate_up(parent_idx)

    def _percolate_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        max_idx = idx
        if (left_child_idx < len(self.heap)) and (self.heap[left_child_idx] > self.heap[max_idx]):
            max_idx = left_child_idx
        if (right_child_idx < len(self.heap)) and (self.heap[right_child_idx] > self.heap[max_idx]):
            max_idx = right_child_idx
        if max_idx != idx:
            self.heap[max_idx], self.heap[idx] = self.heap[idx], self.heap[max_idx]
            self._percolate_down(max_idx)


queue = PriorityQueue()

n = int(input())

for i in range(n):
    op = input().split()

    if op[0] == "I":
        val = int(op[1])
        queue.insert(val)
    elif op[0] == "E":
        max_val = queue.extract_max()
        print(max_val)
    elif op[0] == "P":
        queue.print_heap()

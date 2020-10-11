


# 
# 1 2 4 3 5 9 6 

class index_max_heap2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.indexes = [0] * (capacity + 1)
        self.data = [0] * (capacity + 1)
        self.count = 0

    def insert(self, index, k):
        index += 1
        self.data[index] = k
        self.count += 1
        self.indexes[self.count] = index
        self._shift_up(self.count)

    def _shift_up(self, k):
        while k // 2 >= 1 and self.data[self.indexes[k // 2]] < self.data[self.indexes[k]]:
            self.indexes[k // 2], self.indexes[k] = self.indexes[k], self.indexes[k // 2]
            k = k // 2
    
    def extract_max(self):
        assert self.count > 0
        s = self.data[self.indexes[1]]
        self.indexes[1] = self.indexes[self.count]
        self.count -= 1
        self._shift_down(1)
        return s

    def _shift_down(self, k):
        while k * 2 <= self.count:
            j = k * 2
            if j + 1 < self.count and self.data[self.indexes[j + 1]] > self.data[self.indexes[j]]:
                j += 1
            
            if self.data[self.indexes[k]] < self.data[self.indexes[j]]:
                self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]
                k = j
            else:
                break
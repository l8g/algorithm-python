
class index_max_heap:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * (capacity + 1)
        self.indexes = [0] * (capacity + 1)
        self.count = 0
    
    def insert(self, index, v):
        assert self.count < self.capacity
        self.count += 1
        self.data[index + 1] = v
        self.indexes[self.count] = index + 1

        self._shift_up(self.count)

    def _shift_up(self, k):
        while k > 1 and self.data[self.indexes[k]] > self.data[self.indexes[k // 2]]:
            self.indexes[k], self.indexes[k // 2] = self.indexes[k // 2], self.indexes[k]
            k = k // 2

    def print_index(self):
        [print(self.indexes[i], end = " ") for i in range(self.count + 1)]
        print()

    def print_data(self):
        [print(self.data[i], end = " ") for i in range(self.count + 1)]
        print()

    def extract_max(self):
        assert self.count > 0
        v = self.data[self.indexes[1]]
        self.data[self.indexes[1]] = 0

        self.indexes[1] = self.indexes[self.count]
        self.count -= 1
        self._shift_down(1)
        return v

    def _shift_down(self, k):
        while k * 2 <= self.count:
            j = k * 2
            if j + 1 <= self.count and self.data[self.indexes[j + 1]] > self.data[self.indexes[j]]:
                j += 1
            if self.data[self.indexes[k]] < self.data[self.indexes[j]]:
                self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]
                k = j
            else: 
                break



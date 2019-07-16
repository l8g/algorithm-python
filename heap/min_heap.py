class min_heap:
    """ 
    index from 1
    """
    def __init__(self, capacity):
        assert capacity > 0
        self.capacity = capacity
        self.count = 0
        self.data = [0] * (self.capacity + 1)

    def is_full(self):
        return self.count == self.capacity
    
    def insert(self, v):
        assert not self.is_full()
        self.count += 1
        self.data[self.count] = v
        self._shift_up(self.count)

    def _shift_up(self, index):
        parent_index = index // 2
        if self.data[index] < self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self._shift_up(parent_index)

    def remove(self):
        assert self.count > 0
        first = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        return first

    def _shift_down(self, index):
        left = index * 2
        right = left + 1
        if left <= self.count:
            min_index = left
            if right <= self.count:
                if self.data[right] < self.data[left]:
                    min_index = right
            if self.data[index] > self.data[min_index]:
                self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
                self._shift_down(min_index)






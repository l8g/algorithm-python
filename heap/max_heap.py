
class max_heap:
    '''
    index from 1
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.data = []
    
    def is_full(self):
        return self.capacity == self.count + 1

    def insert(self, item):
        assert not self.is_full()
        self.data[self.count + 1] = item
        self.count = self.count + 1
        self._shift_up(self.count)


    def _shift_up(self, index):
        parent = index // 2
        if self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
        self._shift_up(parent)

    def remove(self):
        val = self.data[1]
        self.data[1] = self.data[self.count]
        self._shift_down(1)
        return val

    def _shift_down(self, index):
        left = index * 2
        if left > self.count:
            return
        max = left
        right = left + 1
        if right <= self.count and self.data[left] < self.data[right]:
            max = right
        self.data[index], self.data[max] = self.data[max], self.data[index]
        self._shift_down(max)






    
    
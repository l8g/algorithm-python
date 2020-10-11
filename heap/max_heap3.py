class max_heap3:
    def __init__(self, capacity):
        self.data = [0] * (capacity + 1)
        self.capacity = capacity
        self.count = 0

    def insert(self, v):
        assert self.count < self.capacity
        self.count += 1
        self.data[self.count] = v
        self._shift_up(self.count)
    
    def _shift_up(self, v):
        while v > 1 and self.data[v // 2] < self.data[v]:
            p = v // 2
            self.data[p], self.data[v] = self.data[v], self.data[p]
            v = p
            
    def extract_max(self):
        assert self.count > 0
        v = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        return v

    def _shift_down(self, v):
        while v * 2 <= self.count:
            j = v * 2 # 在此轮循环中data[j]和data[v]交换位置
            if j + 1 <= self.count and self.data[j + 1] > self.data[j]:
                j += 1
            if self.data[j] > self.data[v]:
                self.data[j], self.data[v] = self.data[v], self.data[j]
                v = j
            else:
                break
    


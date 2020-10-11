
class max_heap2:
    def __init__(self, capacity):
        self.data = [0] * (capacity + 1)
        self.capacity = capacity
        self.count = 0
    
    def is_full(self):
        return self.count == self.capacity

    def insert(self, v):
        assert not self.is_full()
        print("insert", v)
        self.count += 1
        self.data[self.count] = v
        self._shift_up(self.count)

    def _shift_up(self, index):
        if index <= 1:
            print("shift up finished, index = ", index, ', heap data is : ', end = " ")
            [print(self.data[i], end = " ") for i in range(1, self.count + 1)]
            print(", count : ", self.count)
            return
        print("shift up, index = ", index)

        parent = index // 2
        if self.data[index] > self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            [print(self.data[i], end = " ") for i in range(1, self.count + 1)]
            print(", count : ", self.count)
            self._shift_up(parent)
        else:
            print("shift up finished, index = ", index, ", heap data is : ", end = " ")
            [print(self.data[i], end = " ") for i in range(1, self.count + 1)]
            print(", count : ", self.count)

    def extra_max(self):
        assert self.count > 0
        v = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self._shift_down(1)
        return v

    def _shift_down(self, i):
        left = i * 2
        if left > self.count:
            return
        max_index = left
        right = left + 1
        if right <= self.count:
            if self.data[right] > self.data[left]:
                max_index = right
        if self.data[max_index] > self.data[i]:
            self.data[max_index], self.data[i] = self.data[i], self.data[max_index]
            self._shift_down(max_index)


        
        
    

    

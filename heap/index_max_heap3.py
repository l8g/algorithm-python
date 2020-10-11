

class index_max_heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.indexes = [0] * (capacity + 1)
        self.data = [0] * (capacity + 1)
        self.reverse = [0] * (capacity + 1)
        self.count = 0

    def insert(self, index, val):
        assert self.count < self.capacity
        index += 1
        self.data[index] = val
        self.count += 1
        self.indexes[self.count] = index
        self.reverse[index] = self.count
        self._shift_up(self.count)

    def _shift_up(self, k):
        while k // 2 >= 1 and self.data[self.indexes[k // 2]] < self.data[self.indexes[k]]:
            self.indexes[k], self.indexes[k // 2] = self.indexes[k // 2], self.indexes[k]
            self.reverse[k], self.reverse[k // 2] = self.reverse[k // 2], self.reverse[k]
            k = k // 2
    
    # 1 2 0   revers index[revers[i]]  == i 数据的索引在index中的位置
    # 2 0 1   index 数据的索引的排列关系
    # 8 9 7   data  一组放在数组里的数据
    # 0 1 2   i     数据的索引

    # 如果索引的排列关系发生变化，数据的索引在索引排列的位置也发生了变化，
    # 一个元素在数组中的位置发生变化，R
    def extract_max(self):
        assert self.count > 0
        s = self.data[self.indexes[1]]
        self.indexes[1] = self.indexes[self.count]
        self.reverse[1]
        self.count -= 1
        self._shift_down(1)
        return s

    def _shift_down(self, k):
        while k * 2 <= self.count:
            j = k * 2

            if j + 1 <= self.count:
                if self.data[self.indexes[j]] < self.data[self.indexes[j + 1]]:
                    j += 1
            
            if self.data[self.indexes[k]] < self.data[self.indexes[j]]:
                self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]
                k = j
            else:
                break





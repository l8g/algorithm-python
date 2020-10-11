
import sys
sys.path.append('.')

from heap.index_max_heap3 import index_max_heap


heap = index_max_heap(10)

import random

a = [i for i in range(10)]
random.shuffle(a)

# a = [2, 5, 0, 4, 1, 7, 8, 9, 3, 6]
# a = [2, 5, 0]
print(a)

[heap.insert(i, v) for i, v in enumerate(a)]

print("insert finished")
[print(heap.indexes[i], end = " ") for i in range(heap.count + 1)]
print()
[print(heap.data[i], end = " ") for i in range(heap.count + 1)]
print()

print("start extract")
while heap.count > 0:
    print(heap.extract_max(), end = " ")

print()

print("finish")
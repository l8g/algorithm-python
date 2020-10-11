
import sys
sys.path.append(".")
import random

from heap.min_heap import min_heap
from heap.max_heap2 import max_heap2
from heap.max_heap3 import max_heap3

heap = max_heap3(100)
# heap.insert(3)
# print(heap.data)
# heap.insert(4)
# print(heap.data)
# heap.insert(2)
# print(heap.data)

# print(heap.remove())
# print(heap.remove())
# print(heap.remove())

a = [i for i in range(10)]
random.seed = 6
random.shuffle(a)
print("data is : ", a)
for i in a:
    heap.insert(i)

print("data : ")
while heap.count > 0:
    print(heap.extract_max(), end = " ")
print()



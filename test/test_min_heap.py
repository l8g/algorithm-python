
import sys
sys.path.append(".")
import random

from heap.min_heap import min_heap

heap = min_heap(100)
heap.insert(3)
print(heap.data)
heap.insert(4)
print(heap.data)
heap.insert(2)
print(heap.data)

print(heap.remove())
print(heap.remove())
print(heap.remove())

a = [i for i in range(100)]
random.shuffle(a)
print(a)
for i in a:
    heap.insert(i)
while heap.count > 0:
    print(heap.remove())

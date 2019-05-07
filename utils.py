import sys
import random
import time

class recursion_limit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()
    
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    
    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


def generate_random_array(num, minimum, maximum):
    return [random.randint(minimum, maximum) for _ in range(num)]

def time_run(desc, func):
    with recursion_limit(1000000):
        start = time.process_time()
        func()
        print(desc, time.process_time() - start)

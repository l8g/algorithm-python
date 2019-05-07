import sort.quick_sort
import sort.quick_sort_3way


from utils import recursion_limit, generate_random_array, time_run


# a = [i for i in range(100000, 0, -1)]

a = generate_random_array(1000000, 0, 10)
# b = a.copy()


# print (a)
time_run('quick_sort', lambda : sort.quick_sort_3way.quick_sort(a))
# print (a)

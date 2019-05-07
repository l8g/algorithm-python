import random


def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)

def _quick_sort(a, l, r):
    if l >= r : 
        return

    t = random.randint(l, r)
    a[t], a[l] = a[l], a[t]
    p, q = _partition(a, l, r)
    _quick_sort(a, l, p - 1)
    _quick_sort(a, q + 1, r)

def _partition(a, l, r):
    ''' 
        return p, q for a[l, p-1] < a[p], a[p + 1, q] == a[p], a[q + 1, r] > a[p]
    '''


    j = l
    k = l
    # a[l + 1, j] < a[l], a[j + 1, k] == a[l], a[k + 1, i) > a[l]

    for i in range(l + 1, r + 1):
        if a[i] < a[l]:
            a[i], a[k + 1] = a[k + 1], a[i]
            k = k + 1
            a[k], a[j + 1] = a[j + 1], a[k]
            j = j + 1
        elif a[i] == a[l]:
            a[i], a[k + 1] = a[k + 1], a[i]
            k = k + 1
    
    a[l], a[j] = a[j], a[l]
    return j, k
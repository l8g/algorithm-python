
import random

def _partition(a, l, r):
    '''
    a[l, p-1] < a[p], a[p+1, r] >= a[p]
    '''
    
    j = l
    # a[l + 1, j] < a[l], a[j, i) >= a[l]
    for i in range(l+1, r + 1):
        if a[i] < a[l]:
            a[i], a[j + 1] = a[j + 1], a[i]
            j = j + 1
    a[l], a[j] = a[j], a[l]
    return j

def _quick_sort(a, l, r):
    '''
    sort in a[l, r]
    '''
    if l >= r :
        return

    t = random.randint(l, r) # 

    a[l], a[t] = a[t], a[l]
    p = _partition(a, l, r)
    _quick_sort(a, l, p - 1)
    _quick_sort(a, p + 1, r)

def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)
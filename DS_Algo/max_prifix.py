# 1. Given an array a[] of size n. For every i from 0 to n-1 output max(a[0],a[1],.....a[i]).

def max_prifix(array):
    l = []
    mx = array[0]
    for i in range(len(array)):
        mx = max(mx,array[i])
        l.append(mx)
    return l

array = [0,-9,1,3,-4,5]
print(max_prifix(array))
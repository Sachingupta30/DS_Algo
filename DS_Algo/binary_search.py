# Given a sorted array and key cheak key in array.
# Binary Search algorithms
# time complexity = O(log(n))

def binary_search(array,key):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return -1
        
array = [1,2,4,7,8]
key = 3
print(binary_search(array,key))

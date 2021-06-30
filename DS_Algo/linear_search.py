# Given a sorted array and key cheak key in array.
# Linear Search algorithms
# time complexity = O(n)

def linear_search(array,key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

array = [1,2,4,7,8]
key = 3
print(linear_search(array,key))

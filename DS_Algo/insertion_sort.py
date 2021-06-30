# Sort the given array.
# insertion sort---->> Insert an element from unsorted array to its currect position in sorted array.
# time coplexeity = o(n**2)

def insertion_sort(array):
    for i in range(1,len(array)):
        current = array[i]
        j = i-1
        while array[j] > current and j >=0:
            array[j+1] = array[j]
            j-=1
        array[j+1] = current
    return array

array = [3,4,6,1,2]
print(insertion_sort(array))

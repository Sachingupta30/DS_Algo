# Sort the given array.
# Selection sort ---->> Find the minimum element in unsorted array and swap it with element at beginning.
# time coplexeity = o(n**2)

def selection_sort(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                array[j] , array[i] = array[i] , array[j]
    return array

array = [3,4,6,1,2]
print(selection_sort(array))

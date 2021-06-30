# Sort the given array.
# Bubble sort---->> Repeatedly swap two adjacent elements if they are in wrong order.
# time coplexeity = o(n**2)

def bubble_sort(array):
    counter = 1
    while counter < len(array):
        for i in range(len(array)-counter):
            if array[i] > array[i+1]:
                array[i] , array[i+1] = array[i+1] , array[i]
        counter+=1
    return array

array = [3,4,6,1,2]
print(bubble_sort(array))

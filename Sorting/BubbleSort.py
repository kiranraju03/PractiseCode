"""
Bubble Sort
Complexities:

"""


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def bubble_sort(array):
    # assuming the array is not sorted
    array_is_sorted = False
    counter = 0
    # while not sorted, lets sort it
    while not array_is_sorted:
        array_is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                # if value is swapped, then the array is not sorted, shift the flag
                swap(i, i + 1, array)
                array_is_sorted = False
        # to reduce the iteration, as the right most element will be sorted after each iteration
        counter += 1
    return array


print(bubble_sort([23, 14, -15, 5, 2, 9]))


# Approach 2 : Using only for loops

def bubble_sort_for(array):
    for passesLeft in range(len(array) - 1, 0, -1):
        for arrayIndex in range(passesLeft):
            if array[arrayIndex] > array[arrayIndex + 1]:
                swap(arrayIndex, arrayIndex + 1, array)
    return array


print(bubble_sort_for([23, 14, -15, 5, 2, 9]))

"""
Insertion Sort Implementation
Time and Space Complexity

Time : O(N^2) ; if the array is sorted then, O(N) : Reason : Array is traversed twice [N : length of the array]
Space : O(1)
"""


def swap(first_pos, second_pos, array):
    array[first_pos], array[second_pos] = array[second_pos], array[first_pos]


def insertion_sort(array):
    for pos in range(1, len(array)):
        index_value = pos

        while index_value > 0 and array[index_value] < array[index_value - 1]:
            swap(index_value, index_value - 1, array)
            index_value -= 1
    return array


unsortedArray = [2, 3, 8, 9, 6, 3]

print(insertion_sort(unsortedArray))

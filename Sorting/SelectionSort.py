"""
Selection Sort : Using the first element as a reference,
                sort the array by swapping with the smaller element than the first element considered
Complexities :
Best : O(n^2) time | O(1) space
Average : O(n^2) time | O(1) space
Worst : O(n^2) time | O(1) space

Time complexity is n^2 as the re-iteration is happening
Space is 1 as only swapping is taken care
"""


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def selection_sort(array):
    current_index = 0
    while current_index < len(array) - 1:
        smallest_index = current_index
        for each_ele in range(current_index + 1, len(array)):
            if array[smallest_index] > array[each_ele]:
                smallest_index = each_ele
        swap(smallest_index, current_index, array)
        current_index += 1

    return array


print(selection_sort([4, 2, 6, 1, 9]))

"""
Two number sum :
Find a pair of numbers producing a expected sum from a 1-D array

Input : [unsorted array], total_sum
Output :
If total_sum optainable from any 2 values in the array, return sorted array
Else return empty array

Technique used here : two pointers, one at the start of the array and the other traversing the rest of the elements,
                        finding the sum of the traversed elements and check if its the expected result, return the sorted array.

Complexity :
O(N^2) Time : As all the nodes have to traversed twice with i & j, in the worst case
O(1) Space : Only total_sum variable is taken care
"""


def two_number_finder(num_array, total_sum):
    for i in range(len(num_array) - 1):
        array_first_value = num_array[i]

        for j in range(i + 1, len(num_array)):
            array_second_value = num_array[j]

            if array_first_value + array_second_value == total_sum:
                return sorted([array_first_value, array_second_value])
    return []


# Function call
# Case 1 : with pair
print(two_number_finder([3, 5, -4, 8, 11, 1, -1, 6], 10))
# Case 2 : without pair
print(two_number_finder([2, 4, 8, -3], 7))

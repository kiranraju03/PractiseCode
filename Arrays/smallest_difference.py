"""
Find the smallest difference between 2 array elements from 2 different arrays

Technique : pointers to both the arrays, and pointers are moved depending on which value is greater, if they are then to
            make the diff less, move the lesser array pointer forward. Update the closer value to the smallest,
            the last comparision between smallest and closest is the decider.

Complexity:
Time : O(N*log(N) + M*log(M)) : both arrays maybe of diff sizes, N&M, Log(N & M) as we are sorting them.
Space : O(1) : We are taking care of only smallest and closest values
"""


def smallest_diff(first_array, second_array):
    # Initialize
    first_array.sort()
    second_array.sort()
    array_first_index = 0
    array_second_index = 0
    smallest = float("inf")
    closest = float("inf")

    # Loop
    while array_first_index < len(first_array) and array_second_index < len(second_array):
        first_value = first_array[array_first_index]
        second_value = second_array[array_second_index]
        # increment the first array index, if the second array value is higher to reduce the difference
        if first_value < second_value:
            closest = second_value - first_value
            array_first_index += 1
        elif first_value > second_value:
            closest = first_value - second_value
            array_second_index += 1
        else:
            return [first_value, second_value]

        # closest value update
        if smallest > closest:
            smallest = closest
            smallest_pair = [first_value, second_value]

    return smallest_pair


print(smallest_diff([-1, 5, 20, 10, 28], [134, 135, 26, 15, 17]))

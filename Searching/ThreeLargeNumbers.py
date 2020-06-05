"""
Find the 3 largest numbers in a array
Complexity :
Time : O(N) : N is the length of the array
Space : O(1) : Only shifting of values is involved
"""


# Helper method : Used to assign values to the three number array
# if the index is 2, then the values have to be left shifted once and so for others
def shift_update(array, numb, index):
    for i in range(index + 1):
        if i == index:
            array[i] = numb
        else:
            array[i] = array[i + 1]


# Helper method : Used to call a particular shift function based on the index value
def update_large_num(large_array, num):
    if large_array[2] is None or num > large_array[2]:
        shift_update(large_array, num, 2)
    elif large_array[1] is None or num > large_array[1]:
        shift_update(large_array, num, 1)
    elif large_array[0] is None or num > large_array[0]:
        shift_update(large_array, num, 0)


# Main caller
def three_large_numbers(array):
    large_number_array = [None, None, None]
    for each_num in array:
        update_large_num(large_number_array, each_num)
    return large_number_array


print(three_large_numbers([123, 78, 90, -45, 89, 3, 7]))

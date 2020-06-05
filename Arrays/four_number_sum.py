"""
Four number sum : find quadraplets/pair of 4 numbers forming the target sum

Technique : pointers with i,j traversing the array to get a sum value of them and finding the diff of it from
            the required sum, the diff value has to be kept in a dict created by the elements from the start to i'th pointer,
            which is targetting the elements after the i&j pointers have been moved on with and including them in a dict.
            By adding so we can avoid repeatation of quadraplets, which is done using the kth for loop

Complexity :
Time : Avg case : O(n^2)
     : Worst case : O(n^3) : if the number of pairs in the dict for a difference increases
Space : O(n^2)
"""


def four_number_sum(array, target_sum):
    # Create a dict with small sum values
    small_sums_dict = {}
    # resultant array containing pair of 4 numbers
    four_pairs_array = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            diff_from_target = target_sum - current_sum
            if diff_from_target in small_sums_dict:
                for each_sum_pair in small_sums_dict[diff_from_target]:
                    four_pairs_array.append(each_sum_pair + [array[i], array[j]])

        for k in range(0, i):
            dict_sum_value = array[k] + array[i]
            if dict_sum_value not in small_sums_dict:
                small_sums_dict[dict_sum_value] = [[array[k], array[i]]]
            else:
                small_sums_dict[dict_sum_value].append([array[k], array[i]])

    return four_pairs_array


print(four_number_sum([7, 6, 4, 1, -1, 2], 16))
print(four_number_sum([9, 65, 20, 6, -20, -5, 6, -10, 7, 4, -10, 3, 20], 25))


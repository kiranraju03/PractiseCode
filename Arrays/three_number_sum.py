"""
Three number sum :
Find 3 numbers of the array producing a expected sum.

Input : [unsorted array], total_sum
Output :
If total_sum optainable from a set of 3 values in the array, return all the triplets in a 2-D array
Else return empty array

Technique : Using pointers, with 1st element in the array pointed by i ranging from 0 to last 2nd element,
            next element pointed by left pointer and the rightmost element by right pointer, add the values in these
            find the total and append these 3 values in a array.
Complexity :
O(N^2) Time : as the traversal is performed twice using for(i) and while(left and right pointers) loops
O(N) Space : as in the worst case, all elements might combine to form required triplets.
"""


def three_number_finder(num_array, total_sum):
    num_array.sort()
    pairArray = []

    for i in range(len(num_array) - 2):
        leftPointer = i + 1
        rightPointer = len(num_array) - 1

        while leftPointer < rightPointer:
            currentSum = num_array[i] + num_array[leftPointer] + num_array[rightPointer]
            if currentSum == total_sum:
                pairArray.append([num_array[i], num_array[leftPointer], num_array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1
            elif currentSum < total_sum:
                leftPointer += 1
            elif currentSum > total_sum:
                rightPointer -= 1

    return pairArray


# Function call
# Case 1 : with pair
print(three_number_finder([12, 3, 1, 2, -6, 5, -8, 6], 0))
# Case 2 : without pair
print(three_number_finder([2, 4, 8, -3], 5))

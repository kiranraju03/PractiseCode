"""
Find the maximum subset sum with no adjacent elements of the array
Input : [7,10,12,6,9,8]
maxsum array : [7,10,19,19,28,28]
Indexs:
0 : 0th element of the array
1 : max of 0th and 1st element of the array
2 : max of (1st element of maxsum array) and (sum of 1st and 0th element of the array)
so on..

Formula :
maxsum[i] = max{
                maxsum[i-1],
                maxsum[i-2]+array[i]
            }

Complexity:
Time: O(N) : As all the elements are traversed
Space: O(N) : If we store the maxsum values in the array
     : O(1) : If we keep track of only 2 values necessary for the computation of maxsum
"""


# Storing in array approach : O(N) time and space
def maxSubsetNoAdj(array):
    if len(array) == 0:
        return -1
    if len(array) == 1:
        return array[0]

    # copy all the contents
    maxSum = array[:]
    # Manipulate the values
    maxSum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + array[i])

    print(maxSum)


maxSubsetNoAdj([7, 10, 12, 6, 9, 8])


# Storing in variables approach : O(N) time and O(1) space

def maxSubsetViaVariables(array):
    if len(array) == 0:
        return -1
    if len(array) == 1:
        return array[0]
    firstValue = array[0]
    secondValue = max(array[0], array[1])
    for i in range(2, len(array)):
        maxValue = max(secondValue, firstValue + array[i])
        # print(firstValue,secondValue)
        firstValue = secondValue
        secondValue = maxValue

    return secondValue


print(maxSubsetViaVariables([7, 10, 12, 6, 9, 8]))

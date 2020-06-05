""""
Kadane's Algorithm
-This method is used for finding the maximum sum that can be produced from an array of integers
-max sum at a certain index with the max of either the number itself or the sum of the number and the sum computed
 till that point
-final max sum will be the max of either the maxsum computed at a particular index or maxsum computed till then,
 so updating wrt the computed max value at a point

Time : O(N) : N is the length of the array
Space : O(1) :  Constant, as we take care of only some variables.
"""


def kadaneSum(array):
    maxSumCalculated = array[0]
    maxSumAtCertainIndex = array[0]

    # looping through the array
    for i in range(1, len(array)):
        value = array[i]
        print("\nMax Sum value :"+str(maxSumCalculated))
        maxSumAtCertainIndex = max(value, maxSumAtCertainIndex + value)
        print("Max Value at index " + str(i) + " is " + str(maxSumAtCertainIndex))
        maxSumCalculated = max(maxSumCalculated, maxSumAtCertainIndex)
        print("Max Sum selected : "+str(maxSumCalculated))

    return maxSumCalculated


arrayTest = [3, 5, -9]
print(kadaneSum(arrayTest))

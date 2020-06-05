"""
Binary Search
Returns the position of the element found as the target in the array given
"""

"""
Recursive Call Approach
Time Complexity : O(log(N)) : Reason : Half of the array is eliminated while searching
Space : O(log(n)) : Reason : Call stack is filled will function call returns
"""
def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middlePos = (left + right) // 2
    if target == array[middlePos]:
        return middlePos
    elif target < array[middlePos]:
        return binarySearchHelper(array, target, left, middlePos - 1)
    else:
        return binarySearchHelper(array, target, middlePos + 1, right)

print(binarySearch([23,14,58,12,56,111,523,985], 523))


"""
Iterative Approach
Time Complexity : O(log(N)) : Reason : Half of the array is eliminated while searching
Space : O(1) : Reason : Only the target value is taken care of
"""
def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middlePos = (left + right) // 2
        if target == array[middlePos]:
            return middlePos
        elif target < array[middlePos]:
            right = middlePos - 1
        else:
            left = middlePos + 1
    return -1

print(binarySearch([23,14,58,12,56,111,523,985], 523))
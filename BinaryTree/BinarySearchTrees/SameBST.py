"""
Same BST

Given 2 arrays, find out if both arrays form the same BST

Complexity:
Time : O(N^2) : As multiple for loops are included
Space : O(N^2) : As subarrays are sorted for each iteration
"""


def getSmallerElements(array):
    smallerElements = []
    for i in range(1, len(array)):
        # Find smaller elements than the 1st element of the array and append
        if array[i] < array[0]:
            smallerElements.append(array[i])
    return smallerElements


def getGreaterEqualElements(array):
    greaterEqual = []
    for i in range(1, len(array)):
        # Find bigger or equal elements than the 1st element of the array and append
        if array[i] >= array[0]:
            greaterEqual.append(array[i])
    return greaterEqual


def sameBSTChecker(arrayOne, arrayTwo):

    # Check if both arrays are of same length
    if len(arrayOne) != len(arrayTwo):
        return False

    # Check if both are empty, then the end case has been reached
    # Should be checked before the next if check, because the array will be empty
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    # Check if the first element is the same, treating 1st element as the root
    if arrayOne[0] != arrayTwo[0]:
        return False

    # Split the arrays wrt the 1st element to the left and right subtree elements
    # First Array
    leftTreeOfArrayOne = getSmallerElements(arrayOne)
    rightTreeOfArrayOne = getGreaterEqualElements(arrayOne)

    # Second Array
    leftTreeOfArrayTwo = getSmallerElements(arrayTwo)
    rightTreeOfArrayTwo = getGreaterEqualElements(arrayTwo)

    # Recursive call for the subtrees created, until it gets empty
    return sameBSTChecker(leftTreeOfArrayOne, leftTreeOfArrayTwo) and sameBSTChecker(rightTreeOfArrayOne, rightTreeOfArrayTwo)


print(sameBSTChecker([10, 6, 16, 3, 13, 9, 19], [10, 16, 6, 13, 19, 3, 9]))

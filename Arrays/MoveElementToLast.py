"""
Move matching element to the end of the list
Input : [1,2,3,4,2,2,5,6,2,7]
Output : [1,3,4,5,6,7,2,2,2,2]

Technique : Using inbuilt func, we find the required element in the array, remove it and add it at the end
            Using pointers : We keep track of i & j, i at the left and j at the right, if j finds it decrement
                           :  as it should be at the end. If i finds it swap it with j place.
Complexity :
Time : O(N) : Needs to iterate through all elements in the worst case
Space : O(1) : Only the value to be swapped is managed
"""


# Using inbuilt functions
def moveElementToEnd(array, elem):
    for eachElement in array:
        if eachElement == elem:
            array.remove(eachElement)
            array.append(elem)
    return array


# print(moveElementToEnd([1, 2, 3, 4, 2, 2, 5, 6, 2, 7], 2))


# Without inbuilt function
# Using pointers
def moveElementToEndPlain(array, elem):
    i = 0
    j = len(array) - 1
    while i < j:
        # i<j Check again for the last while iteration and move j to the left
        while i < j and array[j] == elem:
            j -= 1
        if array[i] == elem:
            array[i], array[j] = array[j], array[i]
    return array


print(moveElementToEndPlain([1, 2, 3, 4, 2, 2, 5, 6, 2, 7, 2], 2))

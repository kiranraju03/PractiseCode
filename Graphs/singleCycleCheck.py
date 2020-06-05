"""
Single Cycle Check
Given an array check if the array elements can be used to form a single cycle without loops and traversing each
node only once
> Here we can take the first node (0th) as the start and end of the cycle [startingIndex]
Time : O(N) : N being the size of the array, as all the elements have to be traversed
Space : O(1) : constant as there is no duplications of the array and only 2 variables used
"""


def getNewIndex(indexPos, array):
    posValue = array[indexPos]
    # bound the new index value to array limits
    posValue = (indexPos + posValue) % len(array)
    # convert the negative indexes if any, by adding to the total length
    return posValue if posValue >= 0 else posValue + len(array)


def singleCycleCheck(array):
    visitedNodes = 0
    startingIndex = 0
    currentIndex = 0
    # keeping track of no of nodes visted
    while visitedNodes < len(array):
        # check for inner loops, if any
        if visitedNodes > 0 and currentIndex == startingIndex:
            return False
        visitedNodes += 1
        # fetch new index using the array position value
        currentIndex = getNewIndex(currentIndex, array)
    # checking if current index is back to starting point
    return currentIndex == startingIndex


cyclesArray = [2, 2, 3, 1, 2, -4]
nonCyclesArray = [2, 3, 5]

print("Cycles")
print(singleCycleCheck(cyclesArray))

print("No Cycle")
print(singleCycleCheck(nonCyclesArray))

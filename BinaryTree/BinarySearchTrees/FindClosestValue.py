"""
Finding the closest possible node for a given target value

Technique : Updating the target and closest values depending on the tree node values
            If we find a closest target, then rest of the cases fail

Complexity :
Time : O(N) : Need to traverse all the nodes if the closest one is not found
Space : O(1) : Handling only the closest value
"""


def closestValueInBstFinder(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        # if the below condition satisfies, meaning, the closest value is far, need to be updated.
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


def closestValueInBst(tree, target):
    return closestValueInBstFinder(tree, target, float("inf"))

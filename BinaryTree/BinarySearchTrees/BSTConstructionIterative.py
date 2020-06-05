"""
Binary Search Tree(BST)
A BST is a type of binary tree which follows the rule that,
for any given node, the nodes value should be,
left_descendent <= node_value <= right_descendent

The below code, shows the construction of the BST with, insertion,searching and deletion of the nodes.

Note : In BST, a node need not have 2 children, rather it can have a single child also.
"""


class BST:
    # Constructor class for instantiating a node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """
    Iterative approach
    Average : O(log(n)) time | O(1) space
    Worst : O(log(n)) time | O(1) space
    """

    def insert(self, value):
        # Assigning the starting node as the current node
        currentNode = self
        while True:
            # Checking if the value needed to be inserted fits in the left tree
            if value < currentNode.value:
                # if the left tree does not exist, create a new node and assign to left path
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    # let the node goto the left tree
                    currentNode = currentNode.left
            else:
                # logic for the right tree, if the value is greater than the current node'
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    """
    Iterative approach
    Average : O(log(n)) time | O(1) space
    Worst : O(n) time | O(1) space
    """

    def contains(self, value):
        currentNode = self
        # Until the end of the tree
        while currentNode is not None:
            # check if the value to be searched is less than the currentNodes value, explore left tree
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                # explore right tree to find the value
                currentNode = currentNode.right
            else:
                # if the value matches the currentNode itself
                return True
        # if the value is not found
        return False

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    """
    Iterative approach
    Average : O(log(n)) time | O(1) space
    Worst : O(n) time | O(1) space
    """

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # found the value currentNode.value == value(applies to root case having 2 children as well)
                # if the value found node has 2 children, replace the currentNode with the rightmost least value
                if currentNode.left is not None and currentNode.right is not None:
                    # find the min value on the right tree and assign to the currentNode
                    currentNode.value = currentNode.right.getMinValue()
                    # now remove the right node
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    # No right child
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.left = currentNode.left.left
                        currentNode.right = currentNode.left.right
                    # No left child
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # if no children at all, meaning the BST is empty with only one root element, replacing that
                        # will be almost deleting the existing tree
                        currentNode.value = None

                # if the currentNode has only one child, replace the child of the currentNode with the currentNode
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                # if the value is the root and has just 1 of the 2 children

                break
        return self


# Traversals
def inOrderTraversal(tree, array):
    if tree is not None:
        inOrderTraversal(tree.left, array)
        array.append(tree.value)
        inOrderTraversal(tree.right, array)
    return array


a = BST(10).insert(15).insert(11).insert(22).remove(10)
b = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
print(a.value)
print(a.left.value)
print(a.right.value)
print(inOrderTraversal(a, []))
print(inOrderTraversal(b, []))

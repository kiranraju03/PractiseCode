"""
BST Traversal methods

In-Order : left,root,right : Called so as after the traversal the traversed elements are in sorted manner
Pre-Order : Root,left,right : Called pre, as the root is first visited and then the child from left to right
Post-Order : left,Right,root : called post, as the root is visited after the left and right child have been visited
"""

"""
Space and time complexity of all the 3 functions
Time  : O(n), as we are accessing each node
Space : O(n), as we are storing each node in the array, if we were printing the node value, the, O(d), where d is the depth of the tree
"""


def inOrderTraverse(tree, array):
    # if the tree is not empty
    if tree is not None:
        # fetch the left-most node of the tree, so calls are getting accumulated in the call stack
        # Once the left most node is reached, the tree nodes value will get appended to the array
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        # Call to get the right node, if right node has children, again the call will be made from left.
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


import unittest


class BSTTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTTree(value)
            else:
                self.right.insert(value)
        return self


test1 = (
    BSTTree(10)
        .insert(5)
        .insert(15)
        .insert(5)
        .insert(2)
        .insert(1)
        .insert(22)
        .insert(13)
        .insert(14)
)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inOrderTraverse(test1, []), [1, 2, 5, 5, 10, 13, 14, 15, 22])

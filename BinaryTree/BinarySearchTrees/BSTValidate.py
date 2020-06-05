"""
BST Validation : Check if the tree follows the BST rules
Time Complexity : O(n)
Space Complexity : O(d) : d is the depth/length of the tree from the root to the farthest child node.
"""


def BSTValidate(tree):
    return BSTValidateHelper(tree, float("-inf"), float("inf"))


def BSTValidateHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftTreeIsValid = BSTValidateHelper(tree.left, minValue, tree.value)
    return leftTreeIsValid and BSTValidateHelper(tree.right, tree.value, maxValue)


# Test Cases :
# import program
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
        self.assertEqual(BSTValidate(test1), True)

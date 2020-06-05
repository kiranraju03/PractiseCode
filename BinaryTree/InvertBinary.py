"""
Invert a Binary tree

Technique : Recursive solution, to check if a  node has a children, then swap it and move further until no children are present
            Iterative solution, using queue structure, add children of a node to the queues and process them.
Complexity  :
Recursive:
Time : O(N) : Number of nodes of the tree
Space : O(d) : depth of the tree
Iterative:
Time : O(N) : Nodes of the tree
Space : O(N) : As adding nodes into the queue
"""


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def swapChildNodes(tree):
    tree.left, tree.right = tree.right, tree.left


# Recursive solution
def invertBinaryTree(tree):
    if tree is None:
        return

    swapChildNodes(tree)

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


# Iterative Solution: Using Queues
def invertBinaryTreeQueue(tree):
    tree_queue = [tree]
    while len(tree_queue):
        currentNode = tree_queue.pop(0)
        if currentNode is None:
            continue
        # Adding the child elements into the queue for processing
        tree_queue.append(currentNode.left)
        tree_queue.append(currentNode.right)


# Creating the Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


tree = BinaryTree(10).insert([2, 3, 4])

# Solution check by traversing in pre-order technique
print(preOrderTraverse(tree, []))
invertBinaryTree(tree)
print(preOrderTraverse(tree, []))

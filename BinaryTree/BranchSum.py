"""
Branch Sum : Find the sum of the branches in the tree
Complexity :
Time : O(N) : As N nodes have to traversed to find the sum
Space : O(N) : If the branch is single and long, it has to take the recursive function calls at O(log(N))
                and also the array which holds the sum of the branches in the tree, will be O(N/2) as there are
                half the nodes of the total nodes at the leaf of the tree
"""
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def branchSumCaller(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums


def calculateBranchSum(node, branchSum, sums):
    # Check if the tree exist
    if node is None:
        return
    # Add the node value
    calculatedBranchSum = branchSum + node.value
    # Check if the node has children
    if node.left is None and node.right is None:
        sums.append(calculatedBranchSum)
        return

    calculateBranchSum(node.left, calculatedBranchSum, sums)
    calculateBranchSum(node.right, calculatedBranchSum, sums)

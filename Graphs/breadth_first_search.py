"""
Breadth-First Search
Traversing the nodes one level at a time
Time : O( V+E ): as we tranverse each vertice and children of the same, which is same as the edges count of the vertice
Space : O(E) : as we store only the nodes traversed
"""


class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def appendChild(self, name):
        self.children.append(Node(name))
        return self

    def breathFirstSearch(self, array):
        # create a queue ds to access each node in the tree
        treeNodes = [self]
        while len(treeNodes) > 0:
            # fetch the first element in the queue and make it visited by adding to the end array
            currentNode = treeNodes.pop(0)
            array.append(currentNode.name)
            # add each child of the node to the queue to traverse later by popping
            for eachChild in currentNode.children:
                treeNodes.append(eachChild)
        return array


tree_traverse = Node("K")
tree_traverse.appendChild("I").appendChild("R")
tree_traverse.children[0].appendChild("A")
tree_traverse.children[1].appendChild("N")

print(tree_traverse.breathFirstSearch([]))

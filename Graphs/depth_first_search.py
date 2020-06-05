"""
Depth First Search
Traversing the tree of nodes till each of its branch ends and goes back up to the next branch to complete the traversal
Time : O(v + e) : as we traverse each vertex and children(edges count)
Space : O(v) : as we store only the vertices in a array
v : vertices
e : edges
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # to keep track of the nodes traversed
        array.append(self.name)
        # to traverse to the leaf of the tree
        for everyChild in self.children:
            everyChild.depthFirstSearch(array)
        return array

new_tree = Node("A")
new_tree.addChild("B").addChild("C")
print(type(new_tree.children[0]))
# new_tree.children[0].addchild("D")


print(new_tree.depthFirstSearch([]))

"""
Traverse with DFS 
TIme : O(m*n) : n edges and m vertices
the runtime complexity is O(m*n). The
reason is that the main loop takes m iterations because each neighbor is
put into the stack and there are O(m) neighbors.
In each iteration, we check whether the current vertex
u is in the discovered list. Checking whether an element is in a list has
linear runtime complexity in the size of the list - n. Note that
this could be improved by using a (hash) set with constant complexity for
checking whether an element is in the set.
"""

import networkx as nx


def DFS(G, v):
    stack = []
    discovered = []
    # Starting node
    stack.append(v)
    # Till the end of tree
    while len(stack) > 0:
        nextEle = stack.pop()
        if not nextEle in discovered:
            discovered.append(nextEle)
            for neigh in G.neighbors(nextEle):
                stack.append(neigh)
    return discovered


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5])
G.add_path([0, 1, 2, 3])
G.add_path([1, 4, 5])
print(DFS(G, 0))

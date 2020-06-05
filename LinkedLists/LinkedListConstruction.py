"""
Doubly Linked List:

Create various functionalities present in a doubly linked list operation

"""


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        # Write your code here.
        # if head is not there, create a new list
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # else add the new node before the present head node
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        # Write your code here.
        # if no tail, then create a new list
        if self.tail is None:
            self.setHead(node)
            return
        # else add after the tail node
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # to remove the bindings
        self.remove(nodeToInsert)
        # Assigning the insert nodes left pointer
        nodeToInsert.prev = node.prev
        # Assigning the right pointer of the insert node
        nodeToInsert.next = node
        # Check if the before node is a head, if so, make the insertNode as head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # Attaching after the node
        nodeToInsert.prev = node
        # Attching the nodes next element
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) time : p is position | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        # Check is the position is head node
        if position == 1:
            self.setHead(nodeToInsert)
            return
        # Start traversing
        currentNode = self.head
        currentPosition = 1
        while currentNode is not None and currentPosition != position:
            currentNode = currentNode.next
            # Incrementing current position, made mistake
            currentPosition += 1
        # if the position is found
        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        # if the position is not found, add to the tail
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        # Write your code here.
        currentNode = self.head
        while currentNode is not None:
            # Keeping a copy of the next node, as we need to remove all nodes with the value given
            removeNode = currentNode
            currentNode = currentNode.next
            if removeNode.value == value:
                self.remove(removeNode)

    # O(1) time | O(1) space
    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.detachNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        # Write your code here.
        currentNode = self.head
        while currentNode is not None and currentNode.value != value:
            currentNode = currentNode.next
        return currentNode is not None

    def detachNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = node.next = None

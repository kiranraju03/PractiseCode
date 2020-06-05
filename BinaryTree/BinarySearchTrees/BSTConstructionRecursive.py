"""
BST Construction Recursive
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value < value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        elif self.value > value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        if self.value < value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        elif self.value > value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            return True

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            self.left.getMinValue()

    def remove(self, value, parent=None):
        if value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        elif value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.value = None
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self


a = BST(10).insert(15).insert(11).insert(22).remove(10)

b = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)

print(a.value)
print(a.left.value)
print(a.right.value)

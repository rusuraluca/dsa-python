class BinaryTree(object):
    def __init__(self, r):
        self.key = r
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            # a new instance of a binary tree (left subtree)
            self.leftChild = BinaryTree(newNode)

        else:
            # push the previous left child down one level
            # insert the new one before
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, value):
        self.key = value

    def getRootValue(self):
        return self.key


t = BinaryTree(3)

r = t.getRootValue()
print(r)

t.insertLeft(4)
t.insertRight(7)
t.insertLeft(5)
t.insertRight(8)

l = t.getLeftChild().getRootValue()
print(l)

r = t.getRightChild().getRootValue()
print(r)
"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/insert-into-a-binary-search-tree/


Solutions:
-----------------------------------------------
@description:
Recursive:
- Start from the root
- Compare the inserting element with root
    - If less than root
        - Recursively call left subtree
        - Else recursively call right subtree
- After reaching the end, just insert that node at left(if less than current) or else right

Iterative:
- It is to be noted that new keys are always inserted at the leaf node
- Start from root and run a loop until a null pointer is reached
    - Keep the previous pointer of the current node stored
    - If the current node is null then create and insert the new node there
      and make it as one of the children of the parent/previous node depending on its value
    - If the value of current node is less than the new value then move to the right child of current node
      else move to the left child

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space: O(n), for the BST
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insertRecursive(self, root, val):
        if root is None:
            return Node(val)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                root.right = self.insertRecursive(root.right, val)
            else:
                root.left = self.insertRecursive(root.left, val)

        return root

    def inorderRecursive(self, root):
        if root:
            self.inorderRecursive(root.left)
            print(str(root.val) + " ", end="")
            self.inorderRecursive(root.right)

    def insertIterative(self, val):
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        prev = None
        temp = self.root
        while temp is not None:
            prev = temp
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
        if prev.val > val:
            prev.left = node
        else:
            prev.right = node

    def inorderIterative(self):
        temp = self.root
        stack = []

        while (temp != None) or (not (len(stack) == 0)):
            if temp is not None:
                stack.append(temp)
                temp = temp.left

            else:
                temp = stack.pop()
                print(str(temp.val) + " ", end="")
                temp = temp.right


# Recursive

# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
t = BST()
r = Node(50)
r = t.insertRecursive(r, 30)
r = t.insertRecursive(r, 20)
r = t.insertRecursive(r, 40)
r = t.insertRecursive(r, 70)
r = t.insertRecursive(r, 60)
r = t.insertRecursive(r, 80)

# Print inoder traversal of the BST
t.inorderRecursive(r)


print()


# Iterative

# Let us create the following BST
#     30
#   /     \
#  15     50
#  / \    / \
# 10 20 40  60
tree = BST()
tree.insertIterative(30)
tree.insertIterative(50)
tree.insertIterative(15)
tree.insertIterative(20)
tree.insertIterative(10)
tree.insertIterative(40)
tree.insertIterative(60)

# Print inoder traversal of the BST
tree.inorderIterative()
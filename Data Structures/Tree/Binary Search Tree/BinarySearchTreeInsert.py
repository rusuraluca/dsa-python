"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/insert-into-a-binary-search-tree/


Recursive Solution:
-----------------------------------------------
@description:
- Start from the root
- Compare the inserting element with root
    - If less than root
        - Recursively call left subtree
        - Else recursively call right subtree
- After reaching the end, just insert that node at left(if less than current) or else right

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        For height-balanced BSTs, with each comparison, skip about half of the tree
        so that each insertion operation takes time
        proportional to the logarithm of the total number of items n stored in the tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space: O(h), used by the recursive routine that is proportional to the tree’s height


Iterative Solution:
-----------------------------------------------
@description:
- It is to be noted that new keys are always inserted at the leaf node
- Initially, the key is compared with that of the root
- If its key is less than the root’s, it is then compared with the root’s left child’s key
- If its key is greater, it is compared with the root’s right child
- This process continues until the new node is compared with a leaf node, and then it is added as this node’s right or left child, depending on its key:
    - If the key is less than the leaf’s key, then it is inserted as the leaf’s left child
    - Otherwise, as to the leaf’s right child

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        For height-balanced BSTs, with each comparison, skip about half of the tree
        so that each insertion operation takes time
        proportional to the logarithm of the total number of items n stored in the tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space:  O(1), no additional space required
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

        parent = None
        curr = self.root
        while curr is not None:
            parent = curr
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right

        if parent.val > val:
            parent.left = node
        else:
            parent.right = node

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
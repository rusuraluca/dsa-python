"""
Problem:
-----------------------------------------------
This question is asked by Google. Given the reference to the root of a binary search tree and a search value,
return the reference to the node that contains the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.
Ex: Given the tree...
        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the tree
        7
       / \
      5   9
         / \
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the tree
        8
       / \
      6   9
and the search value 7 return null.


Traversing Solution:
-----------------------------------------------
@description:
Recursively pass through the BST,
at each step we choose the subtree we need to go on with.
The exit loop is a null node.
If the current value is smaller => go to the right subtree
If the current value is bigger => go to the left subtree
Return root

@complexity:
Time:   O(n) | can be O(log n) if balanced, where n is the number of nodes in the tree
Space:  O(n) | can be O(h) if balanced, where h is the height of the tree
"""


class BST:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


class Solution:
    def findValue(self, root, value):
        if root is None:
            return None

        if value > root.value:
            return self.findValue(root.right, value)
        elif value < root.value:
            return self.findValue(root.left, value)

        return root


#     3
#    / \
#   1   4

bst = BST(3)
bst.left = BST(1)
bst.right = BST(4)

s = Solution()

assert (s.findValue(bst, 1).value) == 1

#     7
#    / \
#   5   9
#      / \
#     8   10

bst = BST(7)
bst.left = BST(5)
bst.right = BST(9)
bst.right.left = BST(8)
bst.right.right = BST(10)

assert (s.findValue(bst, 9).value) == 9


#     8
#    / \
#   6   9

bst = BST(8)
bst.left = BST(6)
bst.right = BST(9)

assert (s.findValue(bst, 7)) is None

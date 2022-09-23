"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/increasing-order-search-tree/

Given a binary search tree, rearrange the tree
such that it forms a linked list where all its values are in ascending order.
Ex: Given the following tree...
        5
       / \
      1   6
return...
1
 \
  5
   \
    6
Ex: Given the following tree...
       5
      / \
    2    9
   / \
  1   3
return...
1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...
5
 \
  6
return...
5
 \
  6


Increasing BST (In-Order Traversal) Solution:
-----------------------------------------------
A simple approach will be to recreate the BST from its in-order traversal.
This will take O(N) extra space where N is the number of nodes in BST.
Re-draw the entire tree such that left part of each node takes None.

@complexity:
Time:   O(n), where n is the number of nodes in the tree
Space:  O(h), where h is the height of the tree and the size of the implicit call stack in our in-order traversal
"""


class BST:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


class Solution:
    def convert(self):
        pass

    def increasingBST(self, root, tail=None):
        if not root:
            return tail

        res = self.increasingBST(root.left, root)

        root.left = None

        root.right = self.increasingBST(root.right, tail)

        return res


class Tests:

    def __init__(self):
        root = BST(5)
        root.left = BST(1)
        root.right = BST(6)

        root = BST(5)
        root.left = BST(2)
        root.right = BST(9)
        root.left.left = BST(1)
        root.left.right = BST(3)

        s = Solution()

        def printList(parent):
            curr = parent
            while curr is not None:
                print(curr.value, end=' ')
                curr = curr.right

        printList(s.increasingBST(root))


t = Tests()

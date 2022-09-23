"""
Problem:
-----------------------------------------------
Given a binary search tree, return the minimum difference between two given nodes in the tree.
Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98.


Solution:
-----------------------------------------------
@description:
We cam start from the root and for every node, we do following.
- If both keys are greater than the current node, we move to the right child of the current node.
- If both keys are smaller than current node, we move to left child of current node.
- If one keys is smaller and other key is greater, current node is Lowest Common Ancestor (LCA) of two nodes.
  We find distances of current node from two keys and return sum of the distances.

@complexity:
Time:   O(h), where h is height of Binary Search Tree
Space:  O(n)
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    # This function returns distance of x from
    # root. This function assumes that x exists
    # in BST and BST is not NULL.
    def distanceFromRoot(self, root, x):
        if root.key == x:
            return 0
        elif root.key > x:
            return 1 + self.distanceFromRoot(root.left, x)
        return 1 + self.distanceFromRoot(root.right, x)

    # Returns minimum distance between a and b.
    # This function assumes that a and b exist
    # in BST.
    def distanceBetween2(self, root, a, b):
        if root == None:
            return 0

        # Both keys lie in left
        if root.key > a and root.key > b:
            return self.distanceBetween2(root.left, a, b)

        # Both keys lie in right
        if root.key < a and root.key < b:  # same path
            return self.distanceBetween2(root.right, a, b)

        # Lie in opposite directions
        # (Root is LCA of two nodes)
        if root.key >= a and root.key <= b:
            return self.distanceFromRoot(root, a) + self.distanceFromRoot(root, b)

    # This function make sure that a is smaller
    # than b before making a call to findDistWrapper()
    def getMinimumDifference(self, root, a, b):
        if a > b:
            a, b = b, a
        return self.distanceBetween2(root, a, b)
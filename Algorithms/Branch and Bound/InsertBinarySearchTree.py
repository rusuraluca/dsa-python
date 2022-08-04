"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        if root is None:
            return TreeNode(val)

        if root.val == val:
            return root

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

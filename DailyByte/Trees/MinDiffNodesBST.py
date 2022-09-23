"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Given a binary search tree, return the minimum difference between any two nodes in the tree.
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
@complexity:
Time:   O(n), where n is the number of nodes in the BST
Space:  O(n), for the recursive call stack

DFS Solution:
-----------------------------------------------
@complexity:
Time:   O(n), where n is the number of nodes in the BST
Space:  O(log n) - average | O(n), for the recursive call stack
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = -float('inf')
        self.res = float('inf')

    def minDiffInBST(self, root):
        def inorder(root):
            if not root:
                return

            if root.left:
                inorder(root.left)

            self.res = min(self.res, root.key - self.pre)
            self.pre = root.key

            if root.right:
                inorder(root.right)

        inorder(root)
        return self.res

    def minDiffInBSTDFS(self, root):
        def dfs(node, lo, hi):
            if not node:
                return hi - lo

            left = dfs(node.left, lo, node.value)
            right = dfs(node.right, node.value, hi)

            return min(left, right)

        return dfs(root, float('-inf'), float('inf'))

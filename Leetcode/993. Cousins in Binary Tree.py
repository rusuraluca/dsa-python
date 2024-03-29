"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/cousins-in-binary-tree/


DFS Solution:
-----------------------------------------------
@complexity:
Time: O(n), where n is the number of nodes in the tree
Space: O(h), it's the depth of DFS recursion, where h is the height of the binary tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = False

    def isCousins(self, root, x, y):

        def dfs(node, depth):
            if self.ans or not node:
                return 0

            if node.val == x or node.val == y:
                return depth

            l = dfs(node.left, depth + 1)
            r = dfs(node.right, depth + 1)

            if not (l and r):
                return l or r

            if l == r and l != depth + 1:
                self.ans = True

            return 0

        dfs(root, 0)
        return self.ans

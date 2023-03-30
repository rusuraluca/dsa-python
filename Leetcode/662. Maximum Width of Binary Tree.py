"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/k-diff-pairs-in-an-array/


BFS Solution:
-----------------------------------------------
@complexity:
Time:   O(n+e) since we are doing a bfs traversal where n is the number of nodes and e the number of edges
Space:  O(n),  since we store the nodes in a stack/ array
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        res = 0

        if not root:
            return res

        q = deque([(root, 0)])
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                curr, pos = q.popleft()

                if curr.left:
                    q.append((curr.left, pos*2))
                if curr.right:
                    q.append((curr.right, pos*2 + 1))

        return res

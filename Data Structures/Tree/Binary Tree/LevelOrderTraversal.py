"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/binary-tree-level-order-traversal/


Naive Solution:
-----------------------------------------------
@description:
A simple solution is to print all nodes of level 1 first, followed by level 2,
until level h, where h is the tree’s height.
We can print all nodes present in a level by modifying the preorder traversal on the tree.

@complexity:
Time:  O(n^2), where n is the total number of nodes in the binary tree
Space: O(h), for the call stack, where h is the height of the tree

We can reduce the time complexity by using extra space.


Queue Solution:
-----------------------------------------------
@description:
Queue-based level order traversal,
which requires space proportional to the maximum number of nodes at a given depth.
It can be as much as half the total number of nodes.
levelorder(root)
    q —> empty queue
    q.enqueue(root)
    while (not q.isEmpty())
      node —> q.dequeue()
      visit(node)
      if (node.left not null)
        q.enqueue(node.left)
      if (node.right not null)
        q.enqueue(node.right)

@complexity:
Time:  O(n), where n is the total number of nodes in the binary tree
Space: O(n)


Hashing Solution:
-----------------------------------------------
@description:
We can also solve this problem by using hashing.
The idea is to traverse the tree in a preorder fashion
and store every node and its level in a multimap using the level number as a key.
Finally, print all nodes corresponding to every level starting from the first level.
We can also traverse the tree in inorder or postorder fashion.

@complexity:
Time:  O(n), where n is the total number of nodes in the binary tree
Space: O(n)
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderQueue(self, root):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                res.append(level)
        return res

    def preorder(self, root, level, d):
        if root is None:
            return

        d.setdefault(level, []).append(root.val)

        self.preorder(root.left, level + 1, d)
        self.preorder(root.right, level + 1, d)

    def levelOrderHashing(self, root):
        d = {}

        self.preorder(root, 1, d)

        res = []
        for i in range(1, len(d) + 1):
            res.append(d[i])

        return res

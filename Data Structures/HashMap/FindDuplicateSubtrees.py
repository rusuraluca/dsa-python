"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-duplicate-subtrees


Hash Map Solution:
-----------------------------------------------
@description:
We need to somehow serialize the tree for every node in the tree.
Then in a hash map (dict),
we need to increment the count when serialization from another matches the existing key in hmap.

   1
2     3
If we serialize from each node, the output is as follows (I am doing preorder serialization)
from node with value 2: 2,#,#
from node with value 3: 3,#,#
from node with value 1: 1,2,#,#,3,#,#

   1
2     1'
    2'
If we serialize from each node, the output is as follows (I am doing preorder serialization)
from node with value 2': 2',#,# (MATCHED)
from node with value 1': 1',2',#,#,#
from node with value 2: 2,#,# (MATCHED)
from node with value 1: 1,2,#,#,1',2',#,#,#

Lets just generate this preorder serialization
and lets build a hash map with key as path and value as the number of times it appears
We collect all the paths for which hashmap[path] == 2 (which means it is repeated at least once)

@complexity:
Time:   O(n^2), for preorder and an extra O(n) string copy&paste time at each node
Space:  O(N^2).
"""


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        res = []
        hash_map = {}

        def recurse(node, path):
            if node is None:
                return '#'

            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])

            if path in hash_map:
                hash_map[path] += 1
                if hash_map[path] == 2:
                    res.append(node)
            else:
                hash_map[path] = 1

            return path

        recurse(root, '')
        # print(hash_map) PRINT THIS TO UNDERSTAND WHAT IS HAPPENING.
        return res

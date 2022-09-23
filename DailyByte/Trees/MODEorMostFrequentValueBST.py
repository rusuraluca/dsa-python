"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-mode-in-binary-search-tree/
Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.
Ex: Given the following tree...
        2
       / \
      1   2
return 2.
Ex: Given the following tree...
         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9
return 9.


Hash Map Solution:
-----------------------------------------------
Naive:
Keep a hash map of all elements, dfs traversal, check hash map
@complexity:
Time:   O(n)
Space:  O(n)

Improved:
Keep a var like a dic of 4 items:
    els = {"current_count" : float("-inf"),
           "current_elem" : None,
           "max_count" : float("-inf"),
           "max_elem" : None}
Traverse dfs
Return the max_el

@complexity:
Time:   O(n)
Space:  O(1)
"""


# Definition for a binary search tree node
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def findModeNaive(self, root):
        if not root:
            return -1

        hash_map = {}

        def dfs(root, hash_map):
            if not root:
                return

            dfs(root.left, hash_map)

            if root.value not in hash_map:
                hash_map[root.value] = 1
            else:
                hash_map[root.value] += 1

            dfs(root.right, hash_map)

            return

        dfs(root, hash_map)

        mode = None
        cur_max = float("-inf")

        for key in hash_map.keys():
            if hash_map[key] > cur_max:
                cur_max = hash_map[key]
                mode = key

        return mode

    def findMode(self, root):
        if not root:
            return -1

        dic = {
               "current_count": float("-inf"),
               "current_elem": None,
               "max_count": float("-inf"),
               "max_elem": [None]
               }

        def dfs(root, dic):
            if not root:
                return

            dfs(root.left, dic)

            if root.value == dic["current_elem"]:
                dic["current_count"] += 1

            else:
                dic["current_elem"] = root.value
                dic["current_count"] = 1

            if dic["current_count"] > dic["max_count"]:
                dic["max_count"] = dic["current_count"]
                dic["max_elem"] = dic["current_elem"]

            dfs(root.right, dic)

            return

        dfs(root, dic)

        return dic["max_elem"]

    def findModes(self, root):
        if not root:
            return -1

        dic = {
            "current_count": float("-inf"),
            "current_elem": None,
            "max_count": float("-inf"),
            "max_elem": []
        }

        def dfs(root, dic):
            if not root:
                return

            dfs(root.left, dic)

            if root.value == dic["current_elem"]:
                dic["current_count"] += 1

            else:
                dic["current_elem"] = root.value
                dic["current_count"] = 1

            if dic["current_count"] == dic["max_count"]:
                dic["max_elem"].append(dic["current_elem"])

            if dic["current_count"] > dic["max_count"]:
                dic["max_count"] = dic["current_count"]
                dic["max_elem"].clear()
                dic["max_elem"].append(dic["current_elem"])

            dfs(root.right, dic)

            return

        dfs(root, dic)

        return dic["max_elem"]


class Tests:
    def __init__(self):
        s = Solution()
        root = Node(7)
        root.left = Node(4)
        root.left.left = Node(1)
        root.left.right = Node(4)
        root.right = Node(9)
        root.right.left = Node(8)
        root.right.right = Node(9)
        root.right.right.right = Node(9)

        assert (s.findMode(root)) == 9

        root.right.left.right = Node(8)
        root.right.left.left = Node(8)

        assert (s.findModes(root)) == [8, 9]

t = Tests()

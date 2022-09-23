"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array of numbers sorted in ascending order,
return a height-balanced binary search tree using every number from the array.
Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.
Ex: Given the following nums...
nums = [1, 2, 3] return a reference to the following tree...
        2
      /  \
     1    3
Ex: Given the following nums...
nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
      \  / \
       1 4  6


Solution:
-----------------------------------------------
@description:
This is very modified binary search question.

Always picking the mid value of a sorted array to be the root for a binary search tree
is a good choice since this will create a balanced BST.

@complexit:
Time:   O(n), where n is the number of nodes in the tree
Space:  O(1), no auxiliary space required
"""


class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, arr):
        if len(arr) == 0:
            return None

        # find middle index
        mid = len(arr)//2

        # make the middle element the root
        root = Node(arr[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(arr[mid+1:])

        return root


class Tests:
    def __init__(self):
        s = Solution()
        arr = [1, 2, 3]
        root = s.sortedArrayToBST(arr)

        assert (root.key == 2)
        assert (root.right.key == 3)
        assert (root.left.key == 1)

        arr = [1, 2, 3, 4, 5, 6]
        root = s.sortedArrayToBST(arr)

        assert (root.key == 4)
        assert (root.left.key == 2)
        assert (root.left.left.key == 1)
        assert (root.left.right.key == 3)
        assert (root.right.key == 6)
        assert (root.right.left.key == 5)


t = Tests()

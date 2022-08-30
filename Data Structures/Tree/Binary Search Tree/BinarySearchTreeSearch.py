"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/search-in-a-binary-search-tree/


Recursive Solution:
-----------------------------------------------
@description:
- The algorithm depends on the property of BST that if each left subtree has values below root and each right subtree has values above the root
- Start from the root
    - Compare the searching element with root, if less than root, then recursively call left subtree, else recursively call right subtree
    - If the element to search is found anywhere, return true, else return false

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        For height-balanced BSTs, with each comparison, skip about half of the tree
        so that each insertion operation takes time
        proportional to the logarithm of the total number of items n stored in the tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space: O(h), used by the recursive routine that is proportional to the tree’s height


Iterative Solution:
-----------------------------------------------
@description:

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        For height-balanced BSTs, with each comparison, skip about half of the tree
        so that each insertion operation takes time
        proportional to the logarithm of the total number of items n stored in the tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space:  O(1), no additional space required
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def searchBSTRecursively(self, root, val):
        if root is None or root.val == val:
            return root

        if root.val > val:
            return self.searchBSTRecursively(root.left, val)

        return self.searchBSTRecursively(root.right, val)

    def searchBSTIteratively(self, root, val):
        if root is None or root.val == val:
            return root

        curr = root

        while curr is not None:
            if curr.val == val:
                return curr

            if curr.val > val:
                curr = curr.left

            else:
                curr = curr.right

        return None

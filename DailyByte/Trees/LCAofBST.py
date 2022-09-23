"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree that contains unique values and two nodes within the tree, a, and b,
return their lowest common ancestor.
Note: the lowest common ancestor of two nodes is
the deepest node within the tree such that both nodes are descendants of it.
Ex: Given the following tree...
       7
      / \
    2    9
   / \
  1   5
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...
        8
       / \
      3   9
     / \
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...
        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.


Naive Solution:
-----------------------------------------------
@description:
A simple solution would be to store the path from root to x
and the path from the root to y in two auxiliary arrays.
Then traverse both arrays simultaneously till the values in the arrays match.
The last matched value will be the LCA.
If the end of one array is reached, then the last seen value is LCA.
Either p or q is the root => return root

@complexity:
Time:   O(n), for a binary search tree with n nodes
Space:  O(n), for storing two arrays


Solution:
-----------------------------------------------
@description:
We can recursively find the lowest common ancestor of nodes x and y present in the BST.
The trick is to find the BST node,
which has one key present in its left subtree and the other key present in the right subtree.
If any such node is present in the tree, then it is LCA
If y lies in the subtree rooted at node x, then x is the LCA
Otherwise, if x lies in the subtree rooted at node y, then y is the LCA

@complexity:
Recursive:
Time:   O(n), for a binary search tree with n nodes
Space:  O(h), it requires space proportional to the tree’s height for the call stack
Iterative:
Time:   O(n), for a binary search tree with n nodes
Space:  O(1), no auxiliary space required
"""


class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def LCArecursive(self, root, p, q):
        # Base case: empty tree
        if root is None:
            return None

        # If both p and q are smaller than the root, LCA exists in the left subtree
        if root.key > max(p.key, q.key):
            return self.LCArecursive(root.left, p, q)

        # If both p and q are greater than the root, LCA exists in the right subtree
        elif root.key < min(p.key, q.key):
            return self.LCArecursive(root.right, p, q)

        # If one key is greater (or equal) to the root
        # and one key is smaller (or equal) than the root
        # then the current node is LCA
        return root

    def LCAiterative(self, root, p, q):
        if root is None:
            return None

        curr = root

        while curr:
            if curr.key > max(p.key, q.key):
                curr = curr.left
            elif curr.key < min(p.key, q.key):
                curr = curr.right
            else:
                return curr

        return curr

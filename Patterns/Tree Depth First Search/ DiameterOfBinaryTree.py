"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/diameter-of-binary-tree/


The max diameter of a binary tree is simply the sum of
the height of the left tree and the height of the right tree.


Naive Solution:
-----------------------------------------------
@description:
We note that the diameter of a tree can be written as
the maximum of the diameter of the left subtree of the current node,
the diameter of the right subtree of the current node,
and the diameter of the current tree.
We can recursively calculate the sum of the left and right subtree to get the diameter of the current tree
and update the maximum value of diameter by the sum for each node in a recursive manner using DFS.

@complexity:
Time:   O(n^2), there are n nodes in the tree
                for every node we are calculating the height of its left and right subtree
                that takes O(n) time
Space:  O(h)


Post-order Solution:
-----------------------------------------------
@description:
We can solve this problem in linear time by doing a postorder traversal on the tree.
Instead of calculating the height of the left and the right subtree for every node in the tree,
get the height in constant time.
The idea is to start from the bottom of the tree
and return the height of the subtree rooted at a given node to its parent.
The height of a subtree rooted at any node is one more than the maximum height of the left or right subtree.

The idea for the optimal approach is the same as that for the naive approach.
However, in the optimal approach, we change the implementation such that
the calculation for depths of the subtrees and the maximum diameter of the tree,
is done in the same recursive function simultaneously to optimize the time complexity.

@complexity:
Time:   O(n), there are n nodes in the tree
              for every node we are calculating the height of its left and right subtree
              that takes O(n) time
Space:  O(h), extra space for the call stack, where h is the height of the tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDiameter(self, root, diameter):
        # Base case: tree is empty
        if root is None:
            return 0, diameter

        # Gets heights of left and right subtrees
        left_height, diameter = self.getDiameter(root.left, diameter)
        right_height, diameter = self.getDiameter(root.right, diameter)

        # Calculate diameter "through" the current node
        max_diameter = left_height + right_height

        # Update maximum diameter
        # (note that diameter "excluding" the current
        # node in the subtree rooted at the current node is already updated
        # since we are doing postorder traversal)
        diameter = max(diameter, max_diameter)

        # It is important to return the height of the subtree rooted at the current node
        return max(left_height, right_height) + 1, diameter

    def diameterOfBinaryTree(self, root) -> int:
        diameter = 0
        return self.getDiameter(root, diameter)[1]

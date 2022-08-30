"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/symmetric-tree/


Recursive Solution:
-----------------------------------------------
@description:
Using a level-order traversing visualization.
We check first the children of the root,
then we need to check the left-children left-child with the right-children right-child
and the left-children right-child with the right-children left-child
And so on with the rest of the nodes
If we ever find a mismatch we just return False
Some base cases would be
if the children are None or if at least one is None => return False
if the children's values aren't equal => return False


@complexity:
n is the number of nodes in the given tree
Time:   O(n), as the helper function is called n times
Space:  O(n), for the recursive stack


Iterative Solution:
-----------------------------------------------
@description:
As in the recursive solution, but we transform the recursive stack in an actual stack.


@complexity:
n is the number of nodes in the given tree
Time:   O(n), as we check all the n elements
Space:  O(n), for the stack
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        def isMatch(rootL, rootR):
            if not rootL and not rootR:
                return True

            if (rootL and not rootR) or (not rootL and rootR):
                return False

            if rootL.val != rootR.val:
                return False

            if rootL.val == rootR.val:
                return isMatch(rootL.left, rootR.right) and isMatch(rootL.right, rootR.left)

        return isMatch(root.left, root.right)

    def isSymmetricIterative(self, root) -> bool:
        stack = []
        if root:
            stack.append([root.left, root.right])

        while stack:
            left, right = stack.pop()

            if left and right:
                if left.val != right.val:
                    return False
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])

            elif left or right:
                return False

        return True

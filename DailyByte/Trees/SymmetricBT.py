"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/symmetric-tree/


Solution:
-----------------------------------------------
Recursive
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


Iterative:
@description:
As in the recursive solution, but we transform the recursive stack in an actual stack.

@complexity:
n is the number of nodes in the given tree
Time:   O(n), as we check all the n elements
Space:  O(n), for the stack
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root) -> bool:
        def treeMatch(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.key != root2.key:
                return False
            return treeMatch(root1.left, root2.right) and treeMatch(root1.right, root2.left)

        return treeMatch(root.left, root.right)

    def isSymmetricIterative(self, root) -> bool:
        stack = []
        if root:
            stack.append([root.left, root.right])

        while stack:
            left, right = stack.pop()

            if left and right:
                if left.key != right.key:
                    return False
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])

            elif left or right:
                return False

        return True


class Tests:
    def __init__(self):
        s = Solution()

        root1 = Node(2)
        root1.left = Node(3)
        root1.right = Node(3)

        assert s.isSymmetric(root1) is True
        assert s.isSymmetricIterative(root1) is True

        root1 = Node(1)
        root1.left = Node(2)
        root1.right = Node(2)
        root1.left.right = Node(3)
        root1.right.right = Node(3)

        assert s.isSymmetric(root1) is False
        assert s.isSymmetricIterative(root1) is False


t = Tests()

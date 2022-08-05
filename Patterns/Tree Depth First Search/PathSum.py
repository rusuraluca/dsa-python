"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/path-sum/


Morris Traversal Solution:
-----------------------------------------------
@description:
The intuition behind it is that we keep track of the path sum so far while we traverse down the tree,
where m is updated when we move the root pointer down the tree,
and n is updated when we're setting up successor relationships / threading the tree.
When we're about to explore a different path,
we subtract the current path's sum n from the total path sum m.

@complexity:
Time:   O(n)
Space:  O(1)


Recursive Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)


Iterative Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)
"""


class Solution:

    def hasPathSumRecursive(self, root, target: int) -> bool:
        if root is None:
            return False

        curr = target - root.val

        # a leaf
        # if this is required end node of path
        if not root.left and not root.right and curr == 0:
            return True

        return self.hasPathSumRecursive(root.left, curr) or self.hasPathSumRecursive(root.right, curr)

    def hasPathSumIterative(self, root, target: int) -> bool:
        if root is None:
            return False

        stack = [(root, target - root.val)]

        while len(stack) > 0:

            node, remainder = stack.pop()

            if node.left is None and node.right is None and remainder == 0:
                return True

            if node.left is not None:
                stack.append((node.left, remainder - node.left.val))

            if node.right is not None:
                stack.append((node.right, remainder - node.right.val))

        return False

    def hasPathSumMorrisTraversal(self, root, target: int) -> bool:

        m = 0
        while root is not None:
            if root.left is None:
                m += root.val
                root = root.right

                if root is None and m == target:
                    return True

            else:
                prev = root.left
                n = prev.val

                while prev.right is not None and prev.right is not root:
                    prev = prev.right
                    n += prev.val

                if prev.right is None:
                    m += root.val
                    prev.right = root

                    if prev.left is None and m + n == target:
                        return True

                    root = root.left

                else:
                    prev.right = None
                    root = root.right
                    m -= n

        return False

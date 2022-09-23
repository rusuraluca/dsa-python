"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


Solution:
-----------------------------------------------
@description:
Recursive solution
If the current (sub)tree contains both p and q, then the function result is their LCA.
If only one of them is in that subtree, then the result is that one of them.
If neither are in that subtree, the result is null/None/nil.

Iterative solution
I do a post-order traversal with a stack.
Each stack element at first is a [node, parent] pair,
where parent is the stack element of the node's parent node.
When the children of a parent get finished,
their results are appended to their parent's stack element.
So when a parent gets finished, we have the results of its children/subtrees available
(its stack element at that point is [node, parent, resultForLeftSubtree, resultForRightSubtree]).

@complexity:
Time:   O(n), where n is the number of nodes in the BT
Space:  O(n), for the recursive call stack
        O(n), for the stack
"""


class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        if root == p or root == q:
            return root

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        # If looking for me, return myself
        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res

    def lowestCommonAncestorIterative(self, root, p, q):
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node,
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs),
        return answer[0]

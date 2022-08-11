"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/n-ary-tree-preorder-traversal/


Iterative Solution:
-----------------------------------------------
@description:
Till there is element in stack the loop runs.
    Pop the last element from the stack and store it into temp.
    Append the value of temp to output
    Add the children of the temp into the stack in reverse order.
    This continues till the stack is empty.
Return the output

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(n), for the stack


Recursive Solution:
-----------------------------------------------
@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(n), for the recursive call stack
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorderRecursive(self, root):
        output = []

        def preorder(root):
            # if root is None return
            if root is None:
                return

            # Add the val
            output.append(root.val)

            # Then add all the children to the output
            for child in root.children:
                preorder(child)

        preorder(root)
        return output

    def preorder2(self, root):
        if root is None:
            return []

        stack = [root]
        output = []

        # Till there is element in stack the loop runs.
        while stack:
            # Pop the last element from the stack and store it into temp.
            temp = stack.pop()

            # Append the value of temp to output
            output.append(temp.val)

            # Add the children of the temp into the stack in reverse order.
            # Children of 1 = [3,2,4]
            # If not reveresed then 4 will be popped out first from the stack.
            # If reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(temp.children[::-1])

        # return the output
        return output

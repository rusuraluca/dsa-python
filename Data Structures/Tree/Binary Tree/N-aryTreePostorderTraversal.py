"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/n-ary-tree-postorder-traversal/s


Iterative Solution:
-----------------------------------------------
@description:
Till there is element in stack the loop runs.
    Pop the last element from the stack and store it into temp.
    Add the children of the temp into the stack.
    Append the value of temp to output
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
    def postorderRecursive(self, root):
        output = []

        def postorder(root):
            # if root
            if root:
                # Add all the children to the output
                for child in root.children:
                    postorder(child)

                # Add the val to the output
                output.append(root.val)

        postorder(root)
        return output

    def postorder(self, root):
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
            stack.extend(temp.children)

        # return the output
        return output[::-1]

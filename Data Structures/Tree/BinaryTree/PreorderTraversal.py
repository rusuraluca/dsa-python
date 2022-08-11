"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/binary-tree-preorder-traversal/


Definition:
-----------------------------------------------
Postorder Traversal: ROOT -> LEFT -> RIGHT


Base cases:
-----------------------------------------------
- if root is NULL => return empty list
- if root doesn't have any children => return list with root's value


Stack Solution:
-----------------------------------------------
@description:
1) create an empty list
2) check base case
3) create an empty stack
4) push root to stack
5) until stack is empty
    6) current is the top item from stack
    7) if current is not NULL
        a) append the popped item's value to the list
        b) push root's right child to stack
        c) push left's right child to stack
8) if stack is empty then we are here and we return the list

@complexity:
Time:   O(n), n is the number of nodes in the tree
Space:  O(h), h is the height of the tree


Recursive Solution:
-----------------------------------------------
@description:
1) create an empty list
2) check base case
3) if root is not NULL
    b) append root's value to list
    a) call the function for the root's left child and append the result to the list
    c) call the function for the root's right child and append the result to the list
4) return list

@complexity:
Time:   O(n), n is the number of nodes in the tree
Space:  O(n), for the call stack

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalStack(self, root):
        ans = []

        if root is None:
            return ans

        # create an empty stack and push root to it
        stack = []
        stack.append(root)

        while stack:

            curr = stack.pop()

            if curr:
                ans.append(curr.val)

                # stack is last in first out

                # push right child
                stack.append(curr.right)

                # push left child
                stack.append(curr.left)

        return ans

    def preorderTraversalRecursive(self, root):
        ans = []

        if root:
            ans.append(root.val)
            ans += self.preorderTraversalRecursive(root.left)
            ans += self.preorderTraversalRecursive(root.right)

        return ans


class Tests:
    def __init__(self):
        s = Solution()

        n3 = TreeNode(3)
        n2 = TreeNode(2, n3)
        n1 = TreeNode(1, None, n2)

        assert s.preorderTraversalStack(n1) == [1, 2, 3]
        assert s.preorderTraversalRecursive(n1) == [1, 2, 3]


t = Tests()
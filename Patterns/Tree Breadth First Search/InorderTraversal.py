"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/binary-tree-inorder-traversal/


Definition:
-----------------------------------------------
Inorder Traversal: LEFT -> NODE -> RIGHT


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
4) initialize current node as root
5) until current is NULL and stack is empty
    6) if current is not NULL and stack is not empty then
        a) push the current node to stack
        b) set current to the current's left child

    7) if current is NULL and stack is not empty then
        a) pop the top item from stack
        b) append the popped item's value to the list
        c) set current as the popped_item's right child
        d) back to step 5

8) if current is NULL and stack is empty then we are here and we return the list

@complexity:
Time:   O(n), n is the number of nodes in the tree
Space:  O(h), h is the height of the tree


Recursive Solution:
-----------------------------------------------
@description:
1) create an empty list
2) check base case
3) if root is not NULL
    a) call the function for the root's left child and append the result to the list
    b) append root's value to list
    c) call the function for the root's right child and append the result to the list
4) return list

@complexity:
Time:   O(n), n is the number of nodes in the tree
Space:  O(n), for the call stack


Iterative Solution:
-----------------------------------------------
@description:
1) create an empty list
2) check base case
3) initialize current as root
4) until current is not NULL
   5) if current does not have left child
      a) append current's value to the list
      b) go to the right, i.e. current becomes current's right child
   6) else, if current has a left child
      a) find rightmost node in current left subtree or node whose right child == current
         i) if we found right child == current
             - update the right child of that node whose right child is current as NULL
             - append current's value to the list
             - go to the right, i.e. current becomes current's right child
         ii) else
             - make current as the right child of that rightmost node we found
             - go to the left, i.e. current becomes current's left child

@complexity:
Time:   O(n), n is the number of nodes in the tree
            , if we take a closer look, we can notice that every edge of the tree is traversed at most three times
              and in the worst case, the same number of extra edges (as input tree) are created and removed
Space:  O(1), no auxiliary space required
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalStack(self, root):
        ans = []

        if root is None:
            return ans

        stack = []
        curr = root

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()

                ans.append(curr.val)

                curr = curr.right

        return ans

    def inorderTraversalRecursive(self, root):
        ans = []

        if root:
            ans += self.inorderTraversalRecursive(root.left)
            ans.append(root.val)
            ans += self.inorderTraversalRecursive(root.right)

        return ans

    def inorderTraversalIterative(self, root):
        ans = []

        if root is None:
            return ans

        curr = root

        while curr:
            # if the current does not have left child
            if curr.left is None:
                # append node
                ans.append(curr.val)
                # go right
                curr = curr.right
            else:
                # find the inorder predecessor of current
                pre = curr.left
                while pre.right is not None and pre.right is not curr:
                    pre = pre.right

                if pre.right is None:
                    pre.right = curr
                    curr = curr.left

                else:
                    pre.right = None
                    ans.append(curr.val)
                    curr = curr.right

        return ans


class Tests:
    def __init__(self):
        s = Solution()

        n3 = TreeNode(3)
        n2 = TreeNode(2, n3)
        n1 = TreeNode(1, None, n2)

        assert s.inorderTraversalStack(n1) == [1, 3, 2]
        assert s.inorderTraversalRecursive(n1) == [1, 3, 2]
        assert s.inorderTraversalIterative(n1) == [1, 3, 2]


t = Tests()

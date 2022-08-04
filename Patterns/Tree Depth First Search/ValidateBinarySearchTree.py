"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/validate-binary-search-tree/

The BST property “every node on the right subtree has to be larger
than the current node and every node on the left subtree has to be smaller than the current node”
is the key to figuring out whether a tree is a BST or not.


Greedy Solution:
-----------------------------------------------
@description:
The greedy algorithm:
Traverse the tree
At every node check whether the node contains a value
    larger than the value at the left child
    smaller than the value on the right child

But this does not work for all cases. Consider the following tree:
      20
     /  \
   10    30
        /  \
       5    40
In the tree above, each node meets the condition that the node contains a value
larger than its left child and smaller than its right child hold,
and yet it’s not a BST: the value 5 is on the right subtree of the node containing 20,
a violation of the BST property.
Instead of deciding based solely on a node’s values and its children,
we also need information flowing down from the parent.
In the tree above, if we could remember about the node containing the value 20,
we would see that the node with value 5 is violating the BST property contract.

So, the condition we need to check at each node is:

If the node is the left child of its parent,
    it must be smaller than (or equal to) the parent,
    and it must pass down the value from its parent to its right subtree
    to make sure none of the nodes in that subtree is greater than the parent.
If the node is the right child of its parent,
    it must be larger than the parent,
    and it must pass down the value from its parent to its left subtree
    to make sure none of the nodes in that subtree is lesser than the parent.

@complexity:
Time:   O(n), for a binary search tree with n nodes
Space:  O(h), it requires space proportional to the tree’s height for the call stack


Inorder Traversal Solution:
-----------------------------------------------
@description:
We know that an inorder traversal of a binary search tree returns the nodes in sorted order.
To determine whether a given binary tree is a BST,
keep track of the last visited node while traversing the tree.
Then for each encountered node in the inorder traversal,
check whether the last visited node is smaller (or smaller/equal,
if duplicates are to be allowed in the tree) compared to the current node.

@complexity:
Time:   O(n), for a binary search tree with n nodes
Space:  O(h), it requires space proportional to the tree’s height for the call stack
"""


class Solution:
    def __init__(self):
        self.pre = None

    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, cur):

        if cur is None:
            return True

        if not self.helper(cur.left):
            return False

        if self.pre is not None and self.pre.val >= cur.val:
            return False
        self.pre = cur

        return self.helper(cur.right)

    def isValidBST2(self, root) -> bool:
        return self.helper2(root, float('-inf'), float('inf'))

    def helper2(self, node, minVal, maxVal):
        if node == None:
            return True

        if node.val <= minVal or node.val >= maxVal:
            return False

        left = self.helper(node.left, minVal, node.val)
        right = self.helper(node.right, node.val, maxVal)

        return left and right

    def isValidBST3(self, root) -> bool:
        values = []
        self.in_order_traversal(root, values)
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False
        return True

    def in_order_traversal(self, root, values):
        if root is None:
            return
        self.in_order_traversal(root.left, values)
        values.append(root.val)
        self.in_order_traversal(root.right, values)

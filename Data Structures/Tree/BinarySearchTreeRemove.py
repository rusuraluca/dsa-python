"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/delete-node-in-a-bst/


Recursive Solution:
-----------------------------------------------
@description:
- Considering it's a BST, we can easily locate the target node to delete
    - If the given key is less than the current node, go to the left subtree;
    - Otherwise, go to the right subtree
- Once we find the target node, we need to reconstruct the current subtree.
  There are generally two cases:
    - There is only one branch or no branch
        - Then we just replace current node with the existed branch or NULL
    - Both left and right branches exist,
        - Then we replace the current node with the node X with the 'closest' value and delete that X
        - We find the closest larger node which is the most left node in the right branch
        - Then delete Z
        - In this time, it will fall in case 1 since X has no left branch

@complexity:
Time:   O(log(n)) <=> O(h), where h is height of binary search tree.
        For height-balanced BSTs, with each comparison, skip about half of the tree
        so that each insertion operation takes time
        proportional to the logarithm of the total number of items n stored in the tree.
        In the worst case, we may have to travel from root to the deepest leaf node.
        In worst case the height is equal to number of nodes
        and the time complexity of search and insert operation may become O(n).

Space:  O(h), used by the recursive routine that is proportional to the tree’s height
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNodeRecursively(self, root, key: int):
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNodeRecursively(root.left, key)

        elif root.val < key:
            root.right = self.deleteNodeRecursively(root.right, key)

        else:
            if not (root.left and root.right):
                return root.left or root.right

            t = root.right

            while t.left:
                t = t.left

            root.val = t.val

            root.right = self.deleteNodeRecursively(root.right, root.val)

        return root

    def deleteNodeInorder(self, root, val: int):
        if root is None:
            return None

        # Reaching the node we want to delete

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if val < root.val:
            root.left = self.deleteNodeInorder(root.left, val)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif val > root.val:
            root.right = self.deleteNodeInorder(root.right, val)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:
            # Noe is a leaf node, i.e. no child
            if root.left is None and root.right is None:
                return None

            # Node with only one child
            elif root.left is None:
                curr = root.right
                root = None
                return curr

            elif root.right is None:
                curr = root.left
                root = None
                return curr

            # Node has two children
            else:
                # Get the inorder successor
                # (smallest in the right subtree)
                inorder_succ = root.right
                while inorder_succ.left:
                    inorder_succ = inorder_succ.left

                # Copy the inorder successor's content to this node
                root.val = inorder_succ.val

                # Delete the inorder successor
                root.right = self.deleteNodeInorder(root.right, inorder_succ.val)

        return root



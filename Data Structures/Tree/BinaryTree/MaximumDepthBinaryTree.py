"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/maximum-depth-of-binary-tree/


Iterative Solution:
-----------------------------------------------
@description:
The maximum depth of a binary tree is the number of nodes from the root down to the furthest leaf node.
In other words, it is the height of a binary tree.
Whenever move down to a level, increment height by 1 (height is initialized as 0).
Count number of nodes at each level,
stop traversing when the count of nodes at the next level is 0.
Empty tree = > has a height of 0

- Create a queue
- Push root into the queue
- Keep a var representing the number of nodes in the current level
- Keep a var representing the maximum depth aka height

- While the queue is not empty
    - Number of nodes in the current level = size of queue
    - Otherwise, process each node of the current level and enqueue their non-empty left and right child
    - Increment height by 1 for each level

- If the number of nodes in the queue is 0, it implies that all the levels of the tree have been parsed
  So, return height

@complexity:
Time:   O(n), traverse once the n nodes of the binary tree
Space:  O(n), for the queue data structure
              it will hold at most (1/2)*n nodes <=> n nodes


Recursive Solution:
-----------------------------------------------
@description:
The idea is to traverse the tree in a postorder fashion
and calculate the height of the left and right subtree.
The height of a subtree rooted at any node will be one more
than the maximum height of its left and right subtree.
Recursively apply this property to all tree nodes in a bottom-up manner (postorder fashion)
and return the subtree’s maximum height rooted at that node.

@complexity:
Time:   O(n), traverse once the n nodes of the binary tree
Space:  O(h), for the call stack
              where h is the height of the tree
"""


class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def heightRecursive(self, root):
        if root is None:
            return 0

        # Recur for the left and right subtree and consider maximum depth
        return 1 + max(self.heightRecursive(root.left), self.heightRecursive(root.right))

    def heightIterative(self, root):
        if root is None:
            return 0

        height = 0
        q = [root]

        # Loop till queue is empty
        while q:
            # Calculate the total number of nodes at the current level
            size = len(q)

            # Process each node of the current level and enqueue their non-empty left and right child
            while size > 0:
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
                size = size - 1

            # Increment height by 1 for each level
            height = height + 1

        return height


class Tests:
    def __init__(self):
        s = Solution()

        n9 = Node(9)
        n8 = Node(8)
        n7 = Node(7)
        n6 = Node(6)
        n5 = Node(5)
        n4 = Node(4, n8, n9)
        n3 = Node(3, n6, n7)
        n2 = Node(2, n4, n5)
        n1 = Node(1, n2, n3)

        assert s.heightIterative(n1) == 4
        assert s.heightRecursive(n1) == 4


t = Tests()

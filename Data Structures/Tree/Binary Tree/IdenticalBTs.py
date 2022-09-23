"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/same-tree/

Given two binary trees, return whether or not the two trees are identical.
Note: identical meaning they exhibit the same structure and the same values at each node.
Ex: Given the following trees...
        2
       / \
      1   3
    2
   / \
  1   3
return true.
Ex: Given the following trees...
        1
         \
          9
           \
           18
    1
   /
  9
   \
    18
return false.
Ex: Given the following trees...
        2
       / \
      3   1
    2
   / \
  1   3
return false.


Solution:
-----------------------------------------------
Recursive:
@description:
The simplest strategy here is to use recursion.
Check if p and q nodes are not None, and their values are equal.
If all checks are OK, do the same for the child nodes recursively.

@complexity:
Time:   O(n), where n is a number of nodes in the tree, since one visits each node exactly once
Space:  O(n), in the worst case of completely unbalanced tree, to keep a recursion stack

Iterative
@description:
Start from the root and then at each iteration pop the current node out of the deque.
Then do the same checks as in the first approach:
    - p and p are not None,
    - p.val is equal to q.val,
and if checks are OK, push the child nodes.

@complexity:
Time:   O(n), where n is a number of nodes in the tree, since one visits each node exactly once
Space:  O(n), in the worst case, where the tree is a perfect fully balanced binary tree,
              since BFS will have to store at least an entire level of the tree in the queue,
              and the last level has O(n) nodes
"""
from collections import deque


class Node:
    def __init__(self, key, right=None, left=None):
        self.key = key
        self.right = right
        self.left = left


class Solution:
    def isSameTree(self, p, q):
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.key != q.key:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def isSameTreeIteartive(self, p, q) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            p, q = queue.popleft()

            if not p and not q:
                continue
            if not p or not q or p.key != q.key:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True


class Tests:
    def __init__(self):
        s = Solution()

        root1 = Node(2)
        root1.left = Node(1)
        root1.right = Node(3)

        root2 = Node(2)
        root2.left = Node(1)
        root2.right = Node(3)

        assert s.isSameTree(root1, root2) is True
        assert s.isSameTreeIteartive(root1, root2) is True

        root1 = Node(2)
        root1.left = Node(1)
        root1.right = Node(3)

        root2 = Node(2)
        root2.left = Node(3)
        root2.right = Node(1)

        assert s.isSameTree(root1, root2) is False
        assert s.isSameTreeIteartive(root1, root2) is False

        root1 = Node(1)
        root1.right = Node(9)
        root1.right.right = Node(18)

        root2 = Node(2)
        root2.left = Node(9)
        root2.left.right = Node(18)

        assert s.isSameTree(root1, root2) is False
        assert s.isSameTreeIteartive(root1, root2) is False


t = Tests()

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/invert-binary-tree/


Iterative Solution:
-----------------------------------------------
@description:
BFS (level order traversal) alike approach

         1                              1
        / \                            / \
       2   3                          3   2
     / \  / \                       / \   / \
    4  5  6  7      ->             7  6  5  4
   / \                                     / \
  8  9                                   9   8
Initialize a queue []
Traverse the BT level by level
    Swap every child nodes we explore

q = [1]
q not empty
    pop 1 from the q
    swap 1 child nodes, i.e swap 2 and 3
    push 2 and 3 to the q

q [3, 2]
q not empty
    pop 3 from the q
    swap 3 child nodes, i.e swap 6 and 7
    push 6 and 7 to the q

q [2, 7, 6]
q not empty
    pop 2 from the q
    swap 2 child nodes, i.e swap 4 and 5
    push 4 and 5 to the q

q [7, 6, 5, 4]
q not empty
    pop 7 from the q
    swap 7 child nodes, i.e swap NULL and NULL
    check NULL before adding to queue

q [6, 5, 4]
q not empty
    pop 6 from the q
    swap 6 child nodes, i.e swap NULL and NULL
    check NULL before adding to queue

q [5, 4]
q not empty
    pop 5 from the q
    swap 5 child nodes, i.e swap NULL and NULL
    check NULL before adding to queue

q [4]
q not empty
    pop 4 from the q
    swap 4 child nodes, i.e swap 8 and 9
    push 8 and 9 to the q

q [9, 8]
q not empty
    pop 9 from the q
    swap 9 child nodes, i.e swap NULL and NULL
    check NULL before adding to queue

q [8]
q not empty
    pop 8 from the q
    swap 8 child nodes, i.e swap NULL and NULL
    check NULL before adding to queue

q []
q empty
and
BT inverted

@complexity:
Time:  O(n), we traverse once the n nodes in our BT
             swapping is constant
Space: O(n), for the queue
             in the worst case it can hold about n/2 nodes => n


Recursive Solution:
-----------------------------------------------
@description:
Start at the root
Swap roots children -> Swap the left and right children
Invert left subtree
Invert right subtree
We just skip the NULL

@complexity:
Time:  O(n), we traverse once the n nodes in our BT
             swapping is constant
Space: O(h), for the stack call
           , largest is going to mount to the height of the tree
"""


class Node:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution:
    def invertBTIterative(self, root):
        q = [root]
        while q:
            # pop element from queue
            curr = q.pop(0)
            if curr is not None:
                # swap children
                curr.left, curr.right = curr.right, curr.left
                # append children to the queue
                q.append(curr.left)
                q.append(curr.right)

    def invertBTRecursive(self, root):
        # base case
        if root is None:
            return

        # swap children
        root.left, root.right = root.right, root.left
        self.invertBTRecursive(root.left)
        self.invertBTRecursive(root.right)


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

        s.invertBTIterative(n1)

        assert n1.left == n3
        assert n1.right == n2
        assert n3.left == n7
        assert n3.right == n6
        assert n4.left == n9
        assert n4.right == n8

        n9 = Node(9)
        n8 = Node(8)
        n7 = Node(7)
        n6 = Node(6)
        n5 = Node(5)
        n4 = Node(4, n8, n9)
        n3 = Node(3, n6, n7)
        n2 = Node(2, n4, n5)
        n1 = Node(1, n2, n3)

        s.invertBTRecursive(n1)

        assert n1.left == n3
        assert n1.right == n2
        assert n3.left == n7
        assert n3.right == n6
        assert n4.left == n9
        assert n4.right == n8


t = Tests()

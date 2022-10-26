"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/merge-two-sorted-lists/


Recursive Solution:
-----------------------------------------------
@description:
Given the 2 lists are sorted, we can think of a recursive approach
We could compare the head of both linked lists
Find the smaller among the two
The current element will be the smaller one
Now run a recursive function with parameters, the next node of the smaller element, and the other head
that will return the next smaller element linked with rest of the sorted element
Handle some corner cases.
    If both the heads are NULL => return NULL
    If one head is NULL => return the other

@complexity:
Time:   O(n+m), only one traversal of the n + m nodes of the linked lists are needed
Space:  O(n), if the recursive stack space is taken into consideration


Iterative Solution:
-----------------------------------------------
@description:
Traverse the list from start to end.
If the head node of second list lies in between two nodes of the first list
    Insert it there and make the next node of second list the head.
    Continue this until there is no node left in both lists, i.e. both the lists are traversed.
If the first list has reached end while traversing, point the next node to the head of second list.

@complexity:
Time:   O(n+m), only one traversal of the n + m nodes of the linked lists are needed
Space:  O(1), no auxiliary space required
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeRecursive(self, h1, h2):
        if h1 is None and h2 is None:
            return None

        if h1 is None:
            return h2

        if h2 is None:
            return h1

        if h1.val < h2.val:
            h1.next = self.mergeRecursive(h1.next, h2)
            return h1

        else:
            h2.next = self.mergeRecursive(h1, h2.next)
            return h2

    def mergeIterative(self, h1, h2):
        p1 = h1
        dummy = None
        p2 = h2

        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                dummy = p1
                p1 = p1.next

            elif p1.val >= p2.val:
                if dummy is not None:
                    dummy.next = p2

                dummy = p2
                p2 = p2.next
                dummy.next = p1

        if p1 in None:
            dummy.next = p2

        return h1 if h1.val < h2.val else h2


class Tests:
    def __init__(self):

        head1 = Node(1)
        head1.next = Node(3)
        head1.next.next = Node(5)

        head2 = Node(0)
        head2.next = Node(2)
        head2.next.next = Node(4)

        s = Solution()

        mergedhead = s.mergeRecursive(head1, head2)

        assert mergedhead == head2

        mergedhead = s.mergeIterative(head1, head2)

        assert mergedhead == head2


t = Tests()

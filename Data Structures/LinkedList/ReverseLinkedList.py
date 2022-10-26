"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/reverse-linked-list/


Base Case:
-----------------------------------------------
Empty linked list: head Node is None
One-node linked list head.next Node is None


No-swapping Solution:
-----------------------------------------------
@description:
Only reverse the pointers, no need to swap the elements
1 -> 2 -> 3 -> 4 -> 5 -> NULL
NULL <- 1 <- 2 <- 3 <- 4 <- 5

<= 1 -> 2 -> 3 -> 4 -> 5 -> NULL

curr = head
prv = NULL
nxt = NULL

curr = 1
nxt = 2
curr.next = NULL
prv = 1

curr = 2
nxt = 3
curr.next = 2
prv = 2

curr = 3
nxt = 4
curr.next = 3
prv = 3

curr = 4
nxt = 5
curr.next = 4
prv = 4

curr = 5
nxt = NULL
curr.next = 4
prv = 5
curr = NULL

=> 5 -> 4 -> 3 -> 2 -> 1 -> NULL

@complexity:
Time:   O(n), traverse once the n nodes of the linked list
Space:  O(1), no auxiliary space required


Swapping the Nodes Solution:
-----------------------------------------------
@description:
1 -> 2 -> 3 -> 4 -> 5
2 -> 1 -> 3 -> 4 -> 5
3 -> 2 -> 1 -> 4 -> 5
4 -> 3 -> 2 -> 1 -> 5
5 -> 4 -> 3 -> 2 -> 1

<= 1 -> 2 -> 3 -> 4 -> 5

curr = 1
temp = 2
curr.next = curr.next.next = 3
temp.next = 1
head = 2
2 -> 1 -> 3 -> 4 -> 5

curr = 2
temp = 3
curr.next = curr.next.next = 4
temp.next = head = 2
head = 3
3 -> 2 -> 1 -> 4 -> 5

curr = 3
temp = 4
curr.next = curr.next.next = 5
temp.next = head = 3
head = 4
4 -> 3 -> 2 -> 1 -> 5

curr = 4
temp = 5
curr.next = curr.next.next = NULL
temp.next = head = 4
head = 5
4 -> 3 -> 2 -> 1 -> 5

=> 5 -> 4 -> 3 -> 2 -> 1 -> NULL

@complexity:
Time:   O(n), traverse once the n nodes of the linked list
Space:  O(1), no auxiliary space required


Recursive Solution:
-----------------------------------------------
@description:
1 -> 2 -> 3 -> 4 -> 5
5 -> 4 -> 3 -> 2 -> 1 -> NULL

revNode => 5

revNode => 5
4.next.next = 4
4.next = NULL
1 -> 2 -> 3 -> 4 -> NULL -> 4

revNode => 5
3.next.next = 3
3.next = NULL
1 -> 2 -> 3 -> NULL -> 3 -> 4

revNode => 5
2.next.next = 2
2.next = NULL
1 -> 2 -> NULL -> 2 -> 3 -> 4

revNode => 5
1.next.next = 1
1.next = NULL
5 -> NULL -> 1 -> 2 -> 3 -> 4

@complexity:
Time:   O(n), traverse once the n nodes of the linked list
Space:  O(n), for then recursive call stack
"""


# definition for a singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # only reverse the pointers, no need to swap the nodes
    def reverseListNoSwappingIterative(self, head):
        # base case
        if head is None or head.next is None:
            return head

        curr = head
        prv = None
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt

        return prv

    # swap the nodes
    def reverseListSwappingIterative(self, head):
        # base case
        if head is None or head.next is None:
            return head

        curr = head

        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = head
            head = temp

        return head

    # recursive
    def reverseListRecursive(self, head):
        # base case
        if not head or not head.next:
            return head

        revHead = self.reverseListRecursive(head.next)

        # update links
        head.next.next = head
        head.next = None

        return revHead

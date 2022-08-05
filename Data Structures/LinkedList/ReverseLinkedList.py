"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/reverse-linked-list/


Base Case:
-----------------------------------------------
Empty linked list
Head-only linked list


Iterative Solution:
-----------------------------------------------
@description:
Only reverse the pointers, no need to swap the elements
1 -> 2 -> 3 -> 4 -> 5
1 <- 2 <- 3 <- 4 <- 5

prv         =   5
prv.next    =   None
crr         =   5
crr.next    =   None
nxt         =   5
nxt.next    =   None


Also swaping the of nodes
1 -> 2 -> 3 -> 4 -> 5
2 -> 1 -> 3 -> 4 -> 5
3 -> 2 -> 1 -> 4 -> 5
4 -> 3 -> 2 -> 1 -> 5
5 -> 4 -> 3 -> 2 -> 1

@complexity:
Time:   O(n), traverse once the n nodes of the linked list
Space:  O(1), no auxiliary space required


Recursive Solution:
-----------------------------------------------
@complexity:
Time:   O(n), traverse once the n nodes of the linked list
Space:  O(n), for then recursive call stack

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseListRecursive(self, head):
        if not head or not head.next:
            return head

        revHead = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return revHead

    # Also swaping the of nodes
    def reverseListIterative(self, head):
        if head is None or head.next is None:
            return head

        curr = head

        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = head
            head = temp

        return head

    # Only reverse the pointers, no need to swap the elements
    def reverseList(self, head):
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

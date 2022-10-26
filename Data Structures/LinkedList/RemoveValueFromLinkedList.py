"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-duplicates-from-sorted-list/


One-pass Solution:
-----------------------------------------------
@description:
Traverse the linked list, if we find a value equal to the input value we update the links
Else we continue

@complexity:
Time: O(n), n is the number of nodes in the linked list
Space: O(1), no auxiliary space required
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        prev, curr = ListNode(None), head

        while curr:
            if curr.val == val:

                if curr == head:
                    head = head.next

                prev.next = curr.next

            if curr.val != val:
                prev = curr

            curr = curr.next

        return head

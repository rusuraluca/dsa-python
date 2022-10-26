"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/reorder-list/
"""


# definition for a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        if head:
            arr = []

            while head:
                arr += head,
                head = head.next

            l, r, prev = 0, len(arr) - 1, ListNode(0)

            while l < r:
                prev.next = arr[l]
                arr[l].next = arr[r]
                prev = arr[r]
                l = l + 1
                r = r - 1

            if l == r:
                prev.next = arr[l]

            arr[l].next = None

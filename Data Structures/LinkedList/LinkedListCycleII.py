"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/linked-list-cycle


Hash Table Solution:
-----------------------------------------------
@description:
Consider a set to keep track of the visited nodes in a table where the value is the index
Traverse the linked list
    If a node is marked as visited then return its index
    Otherwise, marked node as visited then continue
Return NULL

@complexity:
Time:  O(n),  for traversing once the n nodes in the linked list
Space: O(n), for the worst case to store in the set all the n nodes in the linked list


Fast & Slow Pointer Solution:
-----------------------------------------------
@description:
Slow moves one step at a time, fast moves 2 steps.
If they ever meet, means there was a cycle.
While traversing we keep a variable of the movement index of the slow pointer.

@complexity:
Time:  O(n), for traversing once the n nodes in the linked list
Space: O(1), no auxiliary space required
"""


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Solution:
    def detectCycleHash(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next

        return None

    def detectCycle(self, head) -> bool:
        if not head or not head.next:
            return None

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if there is a cycle
            if fast == slow:
                # the head and slow nodes move step by step
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None

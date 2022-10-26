"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/linked-list-cycle-ii/

or

This question is asked by Apple.
Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts.
If the list does not contain a cycle, return null.


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
    def startOfCycle(self, head):
        visited = set()

        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next

        return None


class Tests:
    def __init__(self):
        l1 = Node(1)
        l1.next = Node(2)
        l1.next.next = Node(3)
        s = Solution()
        assert s.startOfCycle(l1) is None

        l1 = Node(1)
        l1.next = Node(2)
        l1.next.next = Node(3)
        l1.next.next.next = Node(4)
        l1.next.next.next.next = Node(5)
        l1.next.next.next.next.next = l1.next
        s = Solution()
        assert s.startOfCycle(l1) == l1.next

        l1 = Node(1)
        l1.next = Node(9)
        l1.next.next = Node(3)
        l1.next.next.next = Node(7)
        l1.next.next.next.next = l1.next.next.next
        s = Solution()
        assert s.startOfCycle(l1) == l1.next.next.next


t = Tests()

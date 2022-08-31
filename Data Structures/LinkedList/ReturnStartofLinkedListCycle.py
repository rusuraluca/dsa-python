"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/linked-list-cycle-ii/

or

This question is asked by Apple.
Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts.
If the list does not contain a cycle, return null.


Hashing Solution:
-----------------------------------------------
@description:
consider a set to keep track of the visited nodes
traverse the linked list
    if a node is marked as visited then return the node
    otherwise, marked node as visited then continue
return null

@complexity:
Time:  O(n), for traversing once the n nodes in the linked list
Space: O(n), for the worst case to store in the set all the n nodes in the linked list

@remember:
In python,
- lists are slightly faster than sets when you just want to iterate over the values
- sets, however, are significantly faster than lists if you want to check if an item is contained within it,
  they can only contain unique items though


Fast & Slow Pointer Solution:
-----------------------------------------------
@description:


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

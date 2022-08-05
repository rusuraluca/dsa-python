"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/middle-of-the-linked-list/


Iterative Fast & Slow Pointers Solution:
-----------------------------------------------
@description:
The intuition is to traverse once the linked list and update two pointers
1st (fast): move 2 steps each iteration until it reaches the end
2nd (slow): move 1 steps ahead to keep the current mid position
Standard two pointers, one fast and one slow:
- slow traverses at a speed of x.
- fast traverses at a speed of 2x.
Thus, slow will be behind fast by a factor of two at every point in time.

@complexity:
Time:   O(n), more specifically O(n/2) because fast will always reach the end in n/2 steps
Space:  O(1)


Recursive Fast & Slow Pointers Solution:
-----------------------------------------------
@description:
Just a recursive method of the iterative solution.

@complexity:
Time:   O(n), more specifically O(n/2) because fast will always reach the end in n/2 steps
Space:  O(n), for the call stack
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNodeRecursive(self, slow, fast):
        # Detect if fast pointer is at the end of the linked list
        if not fast or fast.next:
            # If fast is at the end, slow pointer must be at the middle
            return slow

        # Make recursive call
        return self.middleNodeRecursive(slow.next, fast.next.next)


    def middleNodeIterative(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


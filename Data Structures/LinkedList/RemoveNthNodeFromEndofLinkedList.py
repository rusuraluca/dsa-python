"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-nth-node-from-end-of-list/


Fast & Slow Pointers Solution:
-----------------------------------------------
@description:
With a singly linked list, the only way to find the end of the list, and thus the n'th node from the end,
is to actually iterate all the way to the end.
The challenge here is attemping to find the solution in only one pass.
A naive approach here might be to store pointers to each node in an array,
allowing us to calculate the n'th from the end once we reach the end,
but that would take O(M) extra space, where M is the length of the linked list.

A slightly less naive approach would be to only store only the last n+1 node pointers in the array.
This could be achieved by overwriting the elements of the storage array in circlular fashion
as we iterate through the list. This would lower the space complexity to O(N+1).

In order to solve this problem in only one pass and O(1) extra space,
however, we would need to find a way to both reach the end of the list with one pointer
and also reach the n'th node from the end simultaneously with a second pointer.

To do that, we can simply stagger our two pointers by n nodes by giving the first pointer (fast) a head start
before starting the second pointer (slow).
Doing this will cause slow to reach the n'th node from the end at the same time that fast reaches the end.

Since we will need access to the node before the target node in order to remove the target node,
we can use fast.next == null as our exit condition, rather than fast == null, so that we stop one node earlier.
This will unfortunately cause a problem when n is the same as the length of the list,
which would make the first node the target node, and thus make it impossible to find the node before the target node.
If that's the case, however,
we can just return head.next without needing to stitch together the two sides of the target node.

Otherwise, once we successfully find the node before the target,
we can then stitch it together with the node after the target, and then return head.

@complexity:
Time:   O(n), where n is the number of nodes in the list
Space:  O(1), since we use constant extra space to track the next node
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next

        return head
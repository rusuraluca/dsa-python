"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-duplicates-from-sorted-list/


Base Cases:
-----------------------------------------------
If input linked list is empty just return head


Two Pointers Solution:
-----------------------------------------------
@description:
Input: head = [1,1,2]
Output: [1,2]

head = [1,1,2]
ans = 1 (initiate with the head)
ans.next = 1 => ans == ans.next => ans.next = ans.next.next = 2
ans.next = 2 => ans != next => ans = ans.next = NULL => STOP
return ans = [1,2]

@pseudocode:
while we still have nodes in the linked list
- if next node has same value as current, skip next node (i.e update head's next node)
- otherwise, we keep moving
return answer

@complexity:
Time:  O(n), we traverse once the n nodes of the linked list
Space: O(1), no auxiliary space needed
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        # if input linked list is empty just return head
        if head is None:
            return head

        # keep head in answer
        ans = head

        # while we still have nodes in the linked list
        while head.next:

            # if next node has same value as current
            # skip next node
            if head.val == head.next.val:
                head.next = head.next.next

            # else if it's not the same
            # keep moving
            else:
                head = head.next

        # return answer
        return ans


class Tests:
    def __init__(self):
        s = Solution()

        n3 = ListNode(2)
        n2 = ListNode(1, n3)
        n1 = ListNode(1, n2)
        assert s.deleteDuplicates(n1) == n1
        assert n1.next == n3


t = Tests()

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/merge-k-sorted-lists/


Min Heap / Priority Queue Solution:
-----------------------------------------------
@description:
Create a min-heap and insert the first element of all the ‘k’ linked lists.

As long as the min-heap is not empty:
    Remove the top element of the min-heap (which is the current minimum among all the elements in the min-heap) and add it to the result list.
    If there exists an element (in the same linked list) next to the element popped out in previous step, insert it into the min-heap.

Return the head node address of the merged list.

@complexity:
Time:   O(n·log(k)), where n is the total number of elements and k is the number of linked lists
Space:  O(k), where k is the number of linked lists


Divide and Conquer Solution:
-----------------------------------------------
@description:
We already know that two linked lists can be merged in O(n) time and O(1) space
(For arrays, O(n) space is required).
The idea is to pair up k lists and merge each pair in linear time using the O(1) space.
After the first cycle, K/2 lists are left each of size 2×N. After the second cycle, K/4 lists are left each of size 4×N and so on. Repeat the procedure until we have only one list left.

Pair up k lists and merge each pair.
After the first pairing, k lists are merged into k/2 lists with average 2n/k length,
then k/4, k/8 and so on.
Repeat this procedure until we get the final sorted linked list.
Thus, we'll traverse almost NN nodes per pairing and merging, and repeat this procedure about logk times.

@complexity:
Time:   O(n·log(k)), where n is the total number of elements and k is the number of lists
                   , we can merge two sorted linked list in O(n)
                   , sum up the merge process and we can get: O(n·log(k))
Space:  O(1), we can merge two sorted linked lists in O(1) space
"""
import heapq


# Definition for a node of the singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        # validate input
        if not lists:
            return None

        # shortcut, just return 1st linked list if only a single list
        if len(lists) == 1:
            return lists[0]

        head = ListNode(0)
        curr = head
        h = []

        for i in range(len(lists)):
            # if the list is not empty
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next


class DivideandConquerSolution(object):
    def mergeKLists(self, lists):
        # validate input
        if not lists:
            return None

        # shortcut, just return 1st linked list if only a single list
        if len(lists) == 1:
            return lists[0]

        start = 0
        end = len(lists) - 1

        while start != end or end != 0:

            if start >= end:
                start = 0

            else:
                lists[start] = self.mergeTwoLists(lists[start], lists[end])
                start += 1
                end -= 1

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        current = head = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return head.next

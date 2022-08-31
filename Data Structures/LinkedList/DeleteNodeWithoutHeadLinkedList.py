"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/delete-node-in-a-linked-list


Brainfart Solution:
-----------------------------------------------
@description:
One of the most important things in any Linked List solution
is to have a pointer to the head.
In the absence of that we need to ask ourselves what is the information that we have,
which can help us iterate the part of the list that the question is asking for.
Here, we are interested in removing the current node.
We do not have a head pointer with which we can access the node prev to the curr node
and jump to the next node.
However , we can alway morph the list to get to the solution that we are looking for.
To do that , we copy the data from the next node to the current node,
effectively deleting the data from the current node and update the link
to point to the node after next
(effectively removing the next node, data of which we already have copied into the current node).

@complexity:
Time:   O(1), since only 1 node needs to be updated
Space:  O(1), since we use constant extra space to track the next node


Delete next node instead of current one Solution:
-----------------------------------------------
@description:
To solve the problem, let's look at the condition carefully,
It is guaranteed that the node to be deleted is not a tail node in the list.
There are a few observations here,
The conventional deletion approach will fail
here since we are not able to get the previous node by iterating from the head of the linked list.
In fact, we do not have any method to fetch the previous node.
Without the knowledge of the previous node, it's not possible to delete the current node.
Notice that we are told the given node is not a tail node.
Therefore, we can delete the next node instead of the current node given,
and "pretend" that the node we are given is the next node.

By analyzing the above two key observations, we can derive the following algorithm,
    Store the next node in a temporary variable.
    Copy data of the next node to the current node.
    Change the next pointer of the current node to the next pointer of the next node.

@complexity:
Time:   O(1), since only 1 node needs to be updated
Space:  O(1), since we use constant extra space to track the next node
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        # Since we know input node is not last node, so nextNode will not be null
        nextNode = node.next
        # Step 2
        node.val = nextNode.val
        # Step 3
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)

    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next

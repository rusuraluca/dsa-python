"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/palindrome-linked-list/


Copy into Array List and then Use Two Pointers Solution:
-----------------------------------------------
@description:
There are two commonly used List implementations, the Array List and the Linked List.
If we have some values we want to store in a list,
how would each List implementation hold them?

An Array List uses an underlying Array to store the values.
We can access the value at any position in the list in O(1) time, as long as we know the index.
This is based on the underlying memory addressing.
A Linked List uses Objects commonly called Nodes. Each Node holds a value and a next pointer to the next node.
Accessing a node at a particular index would take O(n) time because we have to go down the list using the next pointers.

Determining whether or not an Array List is a palindrome is straightforward.
We can simply use the two-pointer technique to compare indexes at either end, moving in towards the middle.
One pointer starts at the start and goes up, and the other starts at the end and goes down.
This would take O(n) because each index access is O(1) and there are nn index accesses in total.

However, it's not so straightforward for a Linked List.
Accessing the values in any order other than forward, sequentially, is not O(1).
Unfortunately, this includes (iteratively) accessing the values in reverse.
We will need a completely different approach.

On the plus side, making a copy of the Linked List values into an Array List is O(n).
Therefore, the simplest solution is to copy the values of the Linked List
into an Array List (or Vector, or plain Array). Then, we can solve the problem using the two-pointer technique.

@pseudocode:
We can split this approach into 2 steps:
    Copying the Linked List into an Array.
    Checking whether or not the Array is a palindrome.

To do the first step, we need to iterate through the Linked List, adding each value to an Array. We do this by using a variable currentNode to point at the current Node we're looking at,
and at each iteration adding currentNode.val to the array and updating currentNode to point to currentNode.next.
We should stop looping once currentNode points to a null node.
The best way of doing the second step depends on the programming language you're using.
In Python, it's straightforward to make a reversed copy of a list and also straightforward to compare two lists.
In other languages, this is not so straightforward and so it's probably best to use the two-pointer technique to check for a palindrome.
In the two-pointer technique, we put a pointer at the start and a pointer at the end,
and at each step check the values are equal and then move the pointers inwards until they meet at the center.

When writing your own solution, remember that we need to compare values in the nodes,
not the nodes themselves. node_1.val == node_2.val is the correct way of comparing the nodes.
node_1 == node_2 will not work the way you expect.

@complexity:
Time:   O(n), where n is the number of nodes in the Linked List.
            , in the first part, we're copying a Linked List into an Array List
            , iterating down a Linked List in sequential order is O(n)
            , and each of the n writes to the ArrayList is O(1)
            , therefore, the overall cost is O(n)O(n)

            , in the second part, we're using the two pointer technique to check whether or not the Array List is a palindrome
            , each of the n values in the Array list is accessed once
            , and a total of O(n/2) comparisons are done
            , therefore, the overall cost is O(n)
            , the Python trick (reverse and list comparison as a one liner) is also O(n)

Space:  O(n), where n is the number of nodes in the Linked List
            , we are making an Array List and adding nn values to it


Reverse Second Half In-place Solution:
-----------------------------------------------
@description:
The only way we can avoid using O(n) extra space is by modifying the input in-place.
The strategy we can use is to reverse the second half of the Linked List in-place
(modifying the Linked List structure), and then comparing it with the first half.
Afterwards, we should re-reverse the second half and put the list back together.
While you don't need to restore the list to pass the test cases,
it is still good programming practice
because the function could be a part of a bigger program that doesn't want the Linked List broken.

@pseudocode:
Specifically, the steps we need to do are:
    Find the end of the first half.
    Reverse the second half.
    Determine whether or not there is a palindrome.
    Restore the list.
    Return the result.

To do step 1,
we could count the number of nodes,
calculate how many nodes are in the first half,
and then iterate back down the list to find the end of the first half.
Or, we could do it in a single parse using the two runners pointer technique.
Either is acceptable, however I'l choose the two runners pointer technique.
Imagine we have 2 runners one fast and one slow, running down the nodes of the Linked List.
In each second, the fast runner moves down 2 nodes, and the slow runner just 1 node.
By the time the fast runner gets to the end of the list, the slow runner will be half way.
By representing the runners as pointers, and moving them down the list at the corresponding speeds,
we can use this trick to find the middle of the list, and then split the list into two halves.
If there is an odd-number of nodes, then the "middle" node should remain attached to the first half.

Step 2 uses the algorithm to reverse the second half of the list.

Step 3 is fairly straightforward.
Remember that we have the first half, which might also contain a "middle" node at the end,
and the second half, which is reversed.
We can step down the lists simultaneously ensuring the node values are equal.
When the node we're up to in the second list is null, we know we're done.
If there was a middle value attached to the end of the first list,
it is correctly ignored by the algorithm.
The result should be saved, but not returned, as we still need to restore the list.

Step 4 requires using the same function you used for step 2,
and then for step 5 the saved result should be returned.

The downside of this approach is that in a concurrent environment
(multiple threads and processes accessing the same data),
access to the Linked List by other threads or processes would have to be locked while this function is running,
because the Linked List is temporarily broken.
This is a limitation of many in-place algorithms though.

@complexity:
Time:   O(n), where n is the number of nodes in the Linked List.
            , finding the middle is O(n), reversing a list in place is O(n)
            , and then comparing the 2 resulting Linked Lists is also O(n)
Space:  O(1), we are changing the next pointers for half of the nodes
            , this was all memory that had already been allocated
            , so we are not using any extra memory and therefore it is O(1).

Some may say that it is O(n) because we're creating a new list.
This is incorrect, because we are changing each of the pointers one-by-one, in-place.
We are not needing to allocate more than O(1) extra memory to do this work,
and there is O(1) stack frames going on the stack.
It is the same as reversing the values in an Array in place (using the two-pointer technique).
"""


# definition for a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    def isPalindrome(self, head) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

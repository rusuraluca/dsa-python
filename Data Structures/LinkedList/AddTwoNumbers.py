"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/add-two-numbers/


Base case:
-----------------------------------------------
Leading zeros?
- It is guaranteed that the list represents a number that does not have leading zeros.


Dummy Node Solution:
-----------------------------------------------
@description:

l1 = [2,4,3]
l2 = [5,6,4]

# to hold a possible carry
carry = 0

# to keep the final result, initialized with 0
result = ListNode(0)

# for moving towards the next node at every iteration
pointer = result
shared references -> any update in pointer will have an immediate effect on result
                     as well as both of these variables are sharing the same object reference

While iterating we would need to stop when:
-> there are no more nodes in either lists
   and when we don't have any carry left

    Retrieve the digits from the individual nodes
    Since the linked lists could be of different size
    (or even reach the end of both lists but still carrying over a unit)
    we also need to handle the cases where the value of the node is None
    first_num = l1.val if l1.val else 0
    second_num = l2.val if l2.val else 0

    Then we need to perform the addition and see whether this will have any impact.
    To do so, we first add together the two numbers as well as the carry.
    Then we compute the next digit of the solution by taking the modulo between the sum and number 10 (base 10)
    and then carry by performing a floor division between the sum and number 10.
    For instance, if the sum of the two digits is 12,
    num variable will be set to 2 (because 12 % 10 = 2) and carry will be 1 (since 12 // 10 = 1).

    summation = first_num + second_num + carry
    num = summation % 10
    carry = summation // 10

    Finally, we store the result to the pointer
    (that will also update result since these two variables are sharing the reference to the same object)
    and the move the pointer to the next node (if any):
    pointer = pointer.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

Finally, we return result.next since the initial node of the result was actually a 0.
return result.next

@complexity:
Time:   O(max(n, m)), length of l1 linked list is m and the length of l2 linked list is n
Space:  O(1), no auxiliary space required
"""


# definition for a singly-linked list
class Node:
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = Node(-1)
        cur = result

        while (l1 or l2 or carry):
            n1 = l1.key if l1 and l1.key else 0
            n2 = l2.key if l2 and l2.key else 0

            # carry, num = divmod(sum(l and l.val or 0 for l in (l1, l2)) + left, 10)

            s = n1 + n2 + carry
            num = s % 10
            carry = s // 10

            cur.next = cur = Node(num)
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        return result.next


class Tests:
    def __init__(self):
        s = Solution()
        # l1 = [2,4,3]
        # l2 = [5,6,4]
        # res = [7,0,8]

        l2 = Node(2, Node(4, Node(3, None)))

        l7 = Node(7, None)
        l6 = Node(6, l7)
        l5 = Node(5, l6)

        r8 = Node(8)
        r0 = Node(0, r8)
        r7 = Node(7, r0)

        res = s.addTwoNumbers(l2, l5)

        while res:
            print(res.key, " ")
            res = res.next


t = Tests()

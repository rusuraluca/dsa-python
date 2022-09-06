"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/design-hashset


Array Solution:
-----------------------------------------------
Faster, but need more (redundant) space.


Linked List [Chaining] Solution:
-----------------------------------------------
Slower, but less space.
"""


class MyHashSet:

    def __init__(self):
        self.hash_set = [0] * 10000000

    def add(self, key: int) -> None:
        self.hash_set[key] += 1

    def remove(self, key: int) -> None:
        self.hash_set[key] = 0

    def contains(self, key: int) -> bool:
        if self.hash_set[key] > 0:
            return True

        return False


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 100
        self.hash_set = [None] * self.size

    def add(self, key: int) -> None:
        id = key % self.size
        # if the node at given index is None then set it with given key
        if self.hash_set[id] is None:
            self.hash_set[id] = ListNode(key, True)
        else:
            # if there are nodes at given index
            currNode = self.hash_set[id]
            # traverse the linked-list and attach the key at the end
            self.hash_set[id] = ListNode(key, True)
            self.hash_set[id].next = currNode

    def remove(self, key: int) -> None:
        id = key % self.size
        # if the node at given index is None then do nothing
        if self.hash_set[id] is None:
            return
        else:
            currNode = self.hash_set[id]
            while currNode:
                # find given key in the linked-list at current index
                if currNode.key == key:
                    # set its value to False
                    currNode.val = False
                currNode = currNode.next

    def contains(self, key: int) -> bool:
        id = key % self.size
        # if there's no linked list at given index then return False
        if self.hash_set[id] is None:
            return False
        else:
            # traverse the linked-list to check if the desired element is present and its value is True
            currNode = self.hash_set[id]
            while currNode:
                if currNode.key == key:
                    if currNode.val is True:
                        return True
                    else:
                        return False
                currNode = currNode.next
            return False

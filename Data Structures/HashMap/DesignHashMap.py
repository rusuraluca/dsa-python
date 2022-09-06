"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/design-hashset


Array Solution:
-----------------------------------------------
Faster, but more (redundant) space.
get: O(1)
put: O(1)
remove: O(1)


Chaining Solution:
-----------------------------------------------
Slower, but less space.
get: O(n)
put: O(n)
remove: O(n)


Double Hashing Solution:
-----------------------------------------------
get: O(1)
put: O(1)
remove: O(1)
"""


class MyHashMap:
    def __init__(self):
        self.hash_map = [None for _ in range(1001)]

    def put(self, key, value):
        hash_one = self.get_hash_one(key)
        hash_two = self.get_hash_two(key)
        if not self.hash_map[hash_one]:
            self.hash_map[hash_one] = [None for _ in range(1001)]

        self.hash_map[hash_one][hash_two] = value

    def get(self, key):
        hash_one = self.get_hash_one(key)
        hash_two = self.get_hash_two(key)
        if self.hash_map[hash_one]:
            if self.hash_map[hash_one][hash_two] is not None:
                return self.hash_map[hash_one][hash_two]
        return -1

    def remove(self, key):
        hash_one = self.get_hash_one(key)
        hash_two = self.get_hash_two(key)
        if self.hash_map[hash_one]:
            if self.hash_map[hash_one][hash_two] is not None:
                self.hash_map[hash_one][hash_two] = None

    def get_hash_one(self, key):
        return key % 1001

    def get_hash_two(self, key):
        return key // 1001


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hash_map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        if not self.hash_map[idx]:
            self.hash_map[idx] = ListNode(key, value)
        else:
            currNode = self.hash_map[idx]
            while currNode:
                if currNode.key == key:
                    currNode.val = value
                    break
                elif currNode.next:
                    currNode = currNode.next
                else:
                    currNode.next = ListNode(key, value)
                    break

    def get(self, key: int) -> int:
        idx = key % self.size
        if not self.hash_map[idx]:
            return -1
        currNode = self.hash_map[idx]
        while currNode:
            if currNode.key == key:
                return currNode.val
            else:
                currNode = currNode.next
        return -1

    def remove(self, key):
        idx = key % self.size
        if self.hash_map[idx]:
            currNode = self.hash_map[idx]
            if currNode.key == key:
                self.hash_map[idx] = currNode.next
            else:
                prevNode = self.hash_map[idx]
                currNode = currNode.next
                while currNode:
                    if currNode.key == key:
                        prevNode.next = currNode.next
                    else:
                        prevNode = prevNode.next
                        currNode = currNode.next


class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            idx = self.keys.index(key)
            self.values[idx] = value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        idx = self.keys.index(key)
        return self.values[idx]

    def remove(self, key: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.values[idx]

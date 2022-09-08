"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/insert-delete-getrandom-o1/


Hash Map Solution:
-----------------------------------------------
We just keep track of the index of the added elements,
so when we remove them, we copy the last one into it.

From Python docs (https://wiki.python.org/moin/TimeComplexity)
we know that list.append() takes O(1),
both average and amortized.
Dictionary get and set functions take O(1) average, so we are OK.
"""
import random


class RandomizedSet:

    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop();
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
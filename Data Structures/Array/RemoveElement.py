"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-element/
"""


class Solution(object):
    def removeElement(self, nums, val):
        step = 0
        while step < len(nums):
            if nums[step] == val:
                nums.pop(step)
                continue
            step += 1
        return len(nums)

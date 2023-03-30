"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/first-missing-positive/


Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(1)
"""


class Solution:
    def firstMissingPositive(self, nums) -> int:
        minn = float('inf')
        maxx = 0

        numsSet = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > 0:
                if nums[i] < minn:
                    minn = nums[i]
                if nums[i] > maxx:
                    maxx = nums[i]
                numsSet.add(nums[i])
            del nums[i]

        if minn >= 2:
            return 1
        if len(numsSet) == maxx:
            return maxx + 1

        for i in range(2, len(numsSet) + 1):
            if i not in numsSet:
                return i


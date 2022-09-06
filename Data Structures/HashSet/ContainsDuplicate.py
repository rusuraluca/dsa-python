"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/contains-duplicate

Sorting Solution:
-----------------------------------------------
@complexity:
Time:   O(nlog(n))
Space:  O(n)


Hash Table [Dictionary or Set] Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)
"""
class Solution:
    def containsDuplicate(self, nums):
        # first-exit case
        if len(nums) == 0:
            return False

        hash_set = set()

        # loop through numbers in array
        for num in nums:
            # check for appearance
            if num in hash_set:
                return True
            hash_set.add(num)

        return False

    def containsDuplicateDic(self, nums) -> bool:
        count = {}

        if len(nums) == 1:
            return False

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                return True

    def containsDuplicateSorting(self, nums):
        # first-exit case
        if len(nums) == 0: return False

        # sort the array
        nums.sort()

        # loop through numbers in array
        for i in range(len(nums) - 1):
            # check for appearance
            if nums[i] == nums[i + 1]:
                return True

        return False




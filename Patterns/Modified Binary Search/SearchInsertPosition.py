"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/search-insert-position/
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid - 1] < target and target < nums[mid]:
                return mid

            elif nums[mid] < target and mid == len(nums) - 1:
                return mid + 1

            elif nums[mid] < target and target < nums[mid + 1]:
                return mid + 1

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return 0


class Tests:
    def __init__(self):
        s = Solution()
        assert s.searchInsert([1,3,5,6], 5) == 2
        assert s.searchInsert([1,3,5,6], 2) == 1
        assert s.searchInsert([1,3,5,6], 7) == 4


t = Tests()





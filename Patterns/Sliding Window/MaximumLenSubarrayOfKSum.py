"""
Problem:
-----------------------------------------------
Maximum Size Subarray Sum

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 5
Explanation: The subarray [2,3,1,2] has the maximum length under the problem constraint

Sliding Window Solution:
-----------------------------------------------
@description:
@complexity:
Time:  O(n)
Space: O(n)
"""


class Solution:
    def maxSizeSubArray(self, nums, target):
        currSum = 0
        start = 0
        maxCount = 0

        for i in range(len(nums)):
            currSum += nums[i]

            while currSum >= target:
                maxCount = max(maxCount, i - start + 1)
                currSum -= nums[start]
                start += 1

        if maxCount == 0:
            return 0

        return maxCount


class Tests:
    def __init__(self):
        s = Solution()
        assert s.maxSizeSubArray([2, 3, 1, 2, 4, 3], 7) == 4


t = Tests()

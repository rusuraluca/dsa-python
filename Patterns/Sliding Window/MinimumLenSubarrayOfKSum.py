"""
Problem:
-----------------------------------------------
Minimum Size Subarray Sum

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint

Sliding Window Solution:
-----------------------------------------------
@description:
@complexity:
"""


class Solution:
    def minSizeSubArray(self, nums, target):
        currSum = 0
        start = 0
        minCount = float("inf")

        for i in range(len(nums)):
            currSum += nums[i]

            while currSum >= target:
                minCount = min(minCount, i - start + 1)
                currSum -= nums[start]
                start += 1

        if minCount == float("inf"):
            return 0

        return minCount


class Tests:
    def __init__(self):
        s = Solution()
        assert s.minSizeSubArray([2, 3, 1, 2, 4, 3], 7) == 2


t = Tests()

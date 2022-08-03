"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/subarrays-with-k-different-integers/solution/


Sliding Window Solution:
-----------------------------------------------
@description:

@complexity:
"""


class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMostK(nums):
            d = {}
            j = 0
            ans = 0
            for i in range(len(nums)):
                if nums[i] not in d:
                    d[nums[i]] = 1
                else:
                    d[nums[i]] += 1
                while(len(d) > k):
                    d[nums[j]] -= 1
                    if d[nums[j]] == 0:
                        del d[nums[j]]
                    j += 1

                ans += i - j + 1
            return ans

        def lessThanK(nums):
            d = {}
            j = 0
            ans = 0
            for i in range(len(nums)):
                if nums[i] not in d:
                    d[nums[i]] = 1
                else:
                    d[nums[i]] += 1
                while(len(d) >= k):
                    d[nums[j]] -= 1
                    if d[nums[j]] == 0:
                        del d[nums[j]]
                    j += 1

                ans += i - j + 1
            return ans

        return atMostK(nums) - lessThanK(nums)

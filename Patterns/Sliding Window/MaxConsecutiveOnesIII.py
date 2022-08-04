"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/max-consecutive-ones-iii/


Sliding Window Solution:
-----------------------------------------------
@complexity:
Time:   O(n), we traverse once the n elements in the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def maxConsecutiveOnes(self, nums, k: int) -> int:
        n, end, start = len(nums), 0, 0

        for end in range(n):

            if nums[end] == 0:
                k -= 1

            if k < 0:
                if nums[start] == 0:
                    k += 1

                start += 1

        return end - start + 1


class Tests:
    def __init__(self):
        s = Solution()
        assert s.maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
        assert s.maxConsecutiveOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10


t = Tests()


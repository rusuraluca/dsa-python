"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/maximum-average-subarray-i/


Base Case:
-----------------------------------------------
If k is greater than the len of the array => Return 0.0


Sliding Window Solution:
-----------------------------------------------
@description:
Traverse the array
    Keep a window of elements and it's sum
    When the window's len is equal to K
        Calculate average
        Compare it with maximum average
        Slide the window to the right with one element

Return maximum

@remember:
A slight performance improvement:
avoid division until the return statement.
In other words just keep a sliding window of the sum of k elements and return max-sum / k.

@complexity:
Time:   O(n), n is the number of elements in the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def maxAverageSubarray(self, arr, k):
        maxSum = float('-inf')
        currSum = 0.0
        windowStart = 0

        for windowEnd in range(len(arr)):
            currSum += arr[windowEnd]

            if windowEnd - windowStart + 1 >= k:
                maxSum = max(maxSum, currSum)
                currSum -= arr[windowStart]
                windowStart += 1

        return maxSum / k


class Tests:
    def __init__(self):
        s = Solution()
        assert s.maxAverageSubarray([1, 12, -5, -6, 50, 3], 4) == 12.75000
        assert s.maxAverageSubarray([5], 1) == 5.00000
        assert s.maxAverageSubarray([-1], 1) == -1.00000


t = Tests()

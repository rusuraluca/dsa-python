"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/running-sum-of-1d-array/


Naive Approach:
-----------------------------------------------
@description:
Consider a new array to hold the running sum of the given array
Loop once through the array
    Update a sum variable that holds the running sum at the current point
    Append the current sum to the new array
Return the new array

@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(n), for the resulting array


Changing Approach:
-----------------------------------------------
@description:
In order to reduce the space we are using,
we can change the given array instead of creating a new one
and not use a sum variable, but the previous element of the list
s
@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def runningSum(self, nums):
        if len(nums) <= 1:
            return nums

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums

    def runningSumNaive(self, nums):
        if len(nums) <= 1:
            return nums

        ans = []
        run_sum = 0

        for num in nums:
            run_sum += num
            ans.append(run_sum)

        return ans

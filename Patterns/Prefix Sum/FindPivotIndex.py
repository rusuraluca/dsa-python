"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-pivot-index/


Base Case:
-----------------------------------------------
The array is empty => return -1


Naive Solution:
-----------------------------------------------
@description:
Check every one of the elements to find the pivot.

@complexity:
Time:   O(n^2), we traverse at least twice the n numbers in the array
Space:  O(1), no auxiliary space required


Prefix Sum Solution:
-----------------------------------------------
@description:
right_sum = sum of all the nums
left_sum = 0
We loop once through the elements
    From right_sum we extract the num at the current position
    If they are equal we return the current position
    Otherwise we add to left_sum the num at the current position
If we exit the loop, it means we haven't found any so we return -1

Example
nums = [1,7,3,6,5,6]
right_sum = 28
left_sum = 0

i=0 -> nums[i] = 1
right_sum = 27
left_sum = 1

i=1 -> nums[i] = 7
right_sum = 20
left_sum = 8

i=2 -> nums[i] = 3
right_sum = 17
left_sum = 11

i=3 -> nums[i] = 6
right_sum = 11 = left_sum -> return 3


@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(1), no auxiliary space required
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum -= nums[i]

            if right_sum == left_sum:
                return i

            left_sum += nums[i]

        return -1

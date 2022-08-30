"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/move-zeroes/


Two Pointers Solution:
-----------------------------------------------
@description:
Take two pointers,
first pointing to the beginning of the array and the second to the end.
Traverse once the elements, add at the beginning the non-zero elements.
Now, the number of zero elements is the difference between the two pointers.
Until they are equal we keep appending to the array zeros.
Return the array

@complexity:
Time:   O(n), n is the length of the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        # base case
        if len(nums) < 1:
            return nums

        # two pointers
        start = 0
        end = len(nums)

        for i in range(end):
            # add at the beginning the non-zero values
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1

        # add at the end the zero values
        while start < end:
            nums[start] = 0
            start += 1

        return nums

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/rotate-array/


Naive Solution:
-----------------------------------------------
@description:
A solution would be to keep a variable previous to store the number being replaced.

@complexity:
Time: O(n*k), all the numbers are shifted by one step (O(n)) k times(O(k)).
Space: O(1), no extra space required


Additional Space Solution:
-----------------------------------------------
@description:
The easiest solution would use additional memory.
We use an extra array in which we place every element of the array at its correct position
i.e. the number at index i in the original array is placed at the index (i+k)%(length of array)(i+k).
Then, we copy the new array to the original one.

@complexity:
Time: O(n), one pass is used to put the numbers in the new array and another pass to copy the new array to the original one
Space: O(n), for another array of the same size


Reversing Solution:
-----------------------------------------------
@description:
This approach is based on the fact that when we rotate the array k times,
k%nk elements from the back end of the array come to the front
and the rest of the elements from the front shift backwards.

We firstly reverse all the elements of the array.
Then, reversing the first k elements followed by reversing the rest n-k elements gives us the required result.


Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

@complexity:
Time:  O(n), elements are reversed a total of three times
Space: O(1), no auxiliary space required
"""


class Solution:
    def rotate(self, nums, k: int) -> None:
        if len(nums) > 1:
            k %= len(nums)
            self.reverse(nums, 0, len(nums)-1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        while start < end:
            # nums[start], nums[end] = nums[end], nums[start]
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotateArray(self, nums, k: int) -> None:
        a = [0] * len(nums)

        for i in range(len(nums)):
            # recycle
            a[(i + k) % len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = a[i]

    def rotateNaive(self, nums, k: int) -> None:
        for _ in range(k):
            # initiate a first previous
            previous = nums[-1]
            for i in range(len(nums)):
                # hold nums[i]
                temp = nums[i]
                # overwrite the current index
                nums[i] = previous
                # swap the value
                previous = temp

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/shuffle-an-array/


Solution:
-----------------------------------------------
@description:
Swapping elements around within the array itself,
we can avoid the linear space cost of the auxiliary array and the linear time cost of list modification.
On each iteration of the algorithm,
we generate a random integer between the current index and the last index of the array.
Then, we swap the elements at the current index and the chosen index
- this simulates drawing (and removing) the element from the hat,
as the next range from which we select a random index will not include the most recently processed one.
One small, yet important detail is that it is possible to swap an element with itself
- otherwise, some array permutations would be more likely than others.

@complexity:
Time:   O(n), the Fisher-Yates algorithm runs in linear time
            , as generating a random index and swapping two values can be done in constant time
Space:  O(n), although we managed to avoid using linear space on a auxiliary array
            , we still need it for reset, so we're stuck with linear space complexity
"""
import random


class Solution:

    def __init__(self, nums):
        """
        self.nums = nums
        self.shuffles = nums[:]
        """
        self.array = nums
        self.original = list(nums)

    def reset(self):
        """
        self.shuffles = self.nums[:]
        return self.shuffles
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        """
        random.shuffle(self.shuffles)
        return self.shuffles
        """
        array = list(self.original)

        for i in range(len(array)): # run @i from 0 up
            # randomly select 1 element from @i up to end
            r = random.randrange(i, len(array))
            array[i], array[r] = array[r], array[i]
        return array


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        shuffled_array = self.nums.copy()
        # randomly generates the idx of the element that'll be the ith element of the array
        for i in range(len(self.nums) - 1, 0, -1):
            idx = random.randint(0, i)
            shuffled_array[i], shuffled_array[idx] = shuffled_array[idx], shuffled_array[i]
        return shuffled_array

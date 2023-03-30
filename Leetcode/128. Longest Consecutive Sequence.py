"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/longest-consecutive-sequence/


HashSet Solution:
-----------------------------------------------
First turn the input into a set of numbers.
Then go through the numbers.
If the number x is the start of a streak (i.e., x-1 is not in the set),
then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set.
The length of the streak is then simply y-x and we update our global best with that.
Since we check each streak only once, this is overall O(n).

@complexity:
Time:   O(n)
Space:  O(n)
"""


class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0

        for x in nums:
            if x - 1 not in nums:
                y = x + 1

                while y in nums:
                    y += 1

                best = max(best, y - x)

        return best

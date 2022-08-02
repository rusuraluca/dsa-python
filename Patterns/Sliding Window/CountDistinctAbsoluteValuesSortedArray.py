"""
Problem:
-----------------------------------------------
Count distinct absolute values in a sorted array

Input:  { -1, -1, 0, 1, 1, 1 }
Output: 2
Explanation: The total number of distinct absolute values is 2 (0 and 1)
"""


class Solution:
    def countDistinctAbsolute(self, arr):
        count = 0
        d = {}

        for elem in arr:
            if elem >= 0 and elem not in d:
                d[elem] = 1
                count += 1

        return count


class Tests:
    def __init__(self):
        s = Solution()
        assert s.countDistinctAbsolute([-1, -1, 0, 1, 1, 1]) == 2


t = Tests()
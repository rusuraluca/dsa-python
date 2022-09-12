"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/two-furthest-houses-with-different-colors/
"""


class Solution:
    def maxDistance(self, colors) -> int:
        res = 0
        for i, x in enumerate(colors):
            if x != colors[0]:
                res = max(res, i)
            if x != colors[-1]:
                res = max(res, len(colors) - 1 - i)
        return res

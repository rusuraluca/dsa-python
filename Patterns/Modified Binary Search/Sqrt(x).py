"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/sqrtx/
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return 0
        low = 0
        high = x
        result = None
        while low <= high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid - 1

            elif mid * mid <= x:
                result = mid
                low = mid + 1

        return result


class Tests:
    def __init__(self):
        s = Solution()
        assert s.mySqrt(4) == 2
        assert s.mySqrt(8) == 2


t = Tests()

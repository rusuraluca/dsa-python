"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/valid-perfect-square/
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo = 0
        hi = num
        mid = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if mid ** 2 < num:
                lo = mid + 1

            elif mid ** 2 > num:
                hi = mid - 1

            else:
                return True

        return False


class Tests:
    def __init__(self):
        s = Solution()
        assert s.isPerfectSquare(16) == True
        assert s.isPerfectSquare(14) == False


t = Tests()

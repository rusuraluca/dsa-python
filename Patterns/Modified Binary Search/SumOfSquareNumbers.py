"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/sum-of-square-numbers/
"""
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(math.sqrt(c))

        while a <= b:

            res = (a * a + b * b)
            if res == c:
                return True

            elif res > c:
                b -= 1

            elif res < c:
                a += 1

        return False


class Tests:
    def __init__(self):
        s = Solution()
        assert s.judgeSquareSum(5) is True
        assert s.judgeSquareSum(3) is False


t = Tests()

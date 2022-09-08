"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Traditional solution
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

        # One line solution
        return sum(1 for k in stones if k in jewels)

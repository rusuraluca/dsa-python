"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/fruit-into-baskets/


Sliding Window Solution:
-----------------------------------------------
@description:
Exactly like the Longest Substring with K Distinct Characters, but K = 2.

@complexity
"""


class Solution:
    def totalFruit(self, fruits):
        maxNum = 0
        windowStart = 0
        typeFreq = {}

        for windowEnd in range(len(fruits)):
            currEnd = fruits[windowEnd]
            if currEnd not in typeFreq:
                typeFreq[currEnd] = 0
            typeFreq[currEnd] += 1

            while len(typeFreq) > 2:
                currStart = fruits[windowStart]
                typeFreq[currStart] -= 1
                if typeFreq[currStart] == 0:
                    del typeFreq[currStart]
                # shrink the window
                windowStart += 1

            maxNum = max(maxNum, windowEnd - windowStart + 1)

        return maxNum


class Tests:
    def __init__(self):
        s = Solution()
        assert s.totalFruit([1,2,1]) == 3
        assert s.totalFruit([0,1,2,2]) == 3
        assert s.totalFruit([1,2,3,2,2]) == 4


t = Tests()
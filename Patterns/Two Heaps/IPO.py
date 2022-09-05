"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/ipo/
"""
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        cp = sorted(zip(capital, profits))
        i = 0
        queue = []
        for _ in range(k):
            while i < len(cp):
                c, p = cp[i]
                if c > w:
                    break
                heappush(queue, (-p,))
                i += 1
            if not queue:
                break
            w -= heappop(queue)[0]
        return w

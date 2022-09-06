"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappySimple(self, n):
        while n > 4:
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1

    def isHappyHashSet(self, n):
        stop = {}
        while n not in stop:
            stop.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1

    def isHappy(self, n):
        def getNext(n):
            tsum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                tsum += digit ** 2
            return tsum

        slow = n
        fast = getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1


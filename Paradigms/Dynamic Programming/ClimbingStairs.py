"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/climbing-stairs/


Base Case:
-----------------------------------------------
If n = 1 => 1 way
If n = 2 => 2 ways


Fibonacci Solution:
-----------------------------------------------
@description:
We can see that the problem is actually the fibonacci problem.
If n = 1 => 1 way
If n = 2 => 2 ways
If n = 3 => 1+2 ways
If n = 4 => 1+2+3 ways
If n = 4 => 1+2+3+4 ways
.
.
.

@complexity:
Time:   O(n), where n is the number of steps
Space:  O(1), no auxilairy space required


DP Solution:
-----------------------------------------------
@description:
Like above, but we keep the steps by memoization in an array.

@complexity:
Time:   O(n), traversing once through the n elements of the DP array
Space:  O(n), for memoizing the n elements DP array
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            total = prev + cur
            prev = cur
            cur = total

        return cur

    def climbStairsDP(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/wildcard-matching/


Solution:
-----------------------------------------------
@complexity:
Time:   O(n*m)
Space:  O(1)
"""


class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][0] = True
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[j-1] == p[i-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif p[i - 1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[n][m]

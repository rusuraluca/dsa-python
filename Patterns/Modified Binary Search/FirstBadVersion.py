"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/first-bad-version/

Naive Linear Search Solution:
-----------------------------------------------
@description:
Linear search to find the first bad version.

@complexity:
Time:  (n), n is the number of software versions
Space: O(1), no auxiliary space needed


Modified Binary Search Solution:
-----------------------------------------------
@description:
Just use binary search to minimize the number of calls to the API.

@complexity:
Time:  (log(n)), n is the number of software versions
Space: O(1), no auxiliary space needed
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 1
        r = n
        res = 0

        while l <= r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                res = mid
                r = mid - 1

            else:
                l = mid + 1

        return res

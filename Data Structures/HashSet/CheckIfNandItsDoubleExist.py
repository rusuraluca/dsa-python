"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/check-if-n-and-its-double-exist/


Hash Set Solution:
-----------------------------------------------
@description:
To do this in one pass we need to keep track of possible M and N
that could be derived from the current element a.
As we iterate through the array,
check if a is a possible M or N based on elements we've seen so far.
If it is, return True.
If we iterate through the entire list can't find a match, we can safely return False.
We can use a set() to store possible M and N because we don't care about duplicates.
We only need to add something to the possible M set if its even.
This decreases the amount of elements when searching through the possible M set.

We can simplify it further by just checking a single set for 2*value or 0.5*value.

@complexity:
Time:   O(n), we pass once the n elements in the array
Space:  O(n), for the hash set
"""


class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for val in arr:
            if 2 * val in seen or 0.5 * val in seen:
                return True
            seen.add(val)

        return False
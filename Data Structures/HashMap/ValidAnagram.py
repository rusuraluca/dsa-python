"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/valid-anagram/


Hash Map Solution:
-----------------------------------------------
@description:
Using a dictionary
Check if char frequency is the same

@complexity:
Time:   O(s+t)
Space:  O(s)


Sorting Solution:
-----------------------------------------------
@description:
Sort the strings,
If they are equal => anagrams
Otherwise => not anagrams

@complexity:
Time:   O(s+t)
Space:  O(s)


Counter Solution:
-----------------------------------------------
@description:
If the strings counters are equal => anagrams
Otherwise => not anagrams

@complexity:
Time:   O(s+t)
Space:  O(s+t)
"""
from collections import Counter


class Solution:
    def isAnagramHashMap(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        for x in t:
            if x in d:
                d[x] -= 1
                if d[x] < 0:
                    return False
            else:
                return False

        return True

    def isAnagramSorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagramCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Tests:
    def __init__(self):

        s = Solution()

        assert s.isAnagramHashTable("anagram", "nagaram") is True
        assert s.isAnagramHashTable("rat", "cat") is False

        assert s.isAnagramSorting("anagram", "nagaram") is True
        assert s.isAnagramSorting("rat", "cat") is False

        assert s.isAnagramCounter("anagram", "nagaram") is True
        assert s.isAnagramCounter("rat", "cat") is False


t = Tests()

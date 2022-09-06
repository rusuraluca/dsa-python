"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/first-unique-character-in-a-string/


HashMap Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] and s[i] not in s[i + 1:]:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}

        for char in s:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] = frequency[char] + 1

        for index in range(len(s)):
            if frequency[s[index]] == 1:
                return index

        return -1
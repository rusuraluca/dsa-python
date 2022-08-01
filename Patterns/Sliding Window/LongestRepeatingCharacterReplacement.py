"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        maxRepeatLetterCount = 0
        windowStart = 0
        maxLen = 0

        for windowEnd in range(len(s)):
            if s[windowEnd] not in freq:
                freq[s[windowEnd]] = 0

            freq[s[windowEnd]] += 1
            maxRepeatLetterCount = max(maxRepeatLetterCount, freq[s[windowEnd]])
            if (windowEnd - windowStart + 1 - maxRepeatLetterCount) > k:
                freq[s[windowStart]] -= 1
                windowStart += 1

        maxLen = max(maxLen, windowEnd - windowStart + 1)

        return maxLen


class Tests:
    def __init__(self):
        s = Solution()
        assert s.characterReplacement("ABAB", 2) == 4
        assert s.characterReplacement("AABABBA", 1) == 4


t = Tests()

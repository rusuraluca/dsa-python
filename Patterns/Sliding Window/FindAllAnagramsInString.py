"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Sliding Window Solution:
-----------------------------------------------
@complexity:
Time:  O(n)
Space: O(1)
"""


class Solution:
    def findAnagramString(self, s, p):
        target = [0] * 26
        count = [0] * 26

        result = []
        start = 0

        for c in p:
            target[ord(c) - ord('a')] += 1

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1

            # shrink window
            if i - start == len(p):
                count[ord(s[start]) - ord('a')] -= 1
                start += 1

            # if it is anagram
            if count == target:
                result.append(start)

        return result


class Tests:
    def __init__(self):
        s = Solution()
        assert s.findAnagramString("cbaebabacd", "abc") == [0, 6]
        assert s.findAnagramString("abab", "ab") == [0, 1, 2]


t = Tests()

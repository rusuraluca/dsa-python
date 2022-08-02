"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1’s permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Sliding Window Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(1)
"""

class Solution():
    def checkPermutationInclusion(self, s1, s2):
        num1 = [0] * 26
        num2 = [0] * 26

        for c in s1:
            num1[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            num2[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1) - 1:
                if num2 == num1:
                    return True
                # shrink the window
                num2[ord(s2[i - len(s1) + 1]) - ord('a')] -= 1

        return False


class Tests():
    def __init__(self):
        s = Solution()
        assert s.checkPermutationInclusion("ab", "eidbaooo") is True
        assert s.checkPermutationInclusion("wq", "eidbaooo") is False


t = Tests()

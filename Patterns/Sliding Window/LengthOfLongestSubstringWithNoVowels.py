"""
Problem:
-----------------------------------------------

Return the length of the longest substring of a given string that doesn’t contain any vowels.

Input: s = "codeforintelligents"
Output: 3
Explanation: 'nts' is the longest substring that doesn't contain any vowels.


Sliding Window Solution:
-----------------------------------------------
@description:
Traverse through the string
    If character is not a vowel we add it to the current word
        If the len of the current result is bigger than our global result
            Update global result
    Otherwise
        Current result becomes an empty string i.e. we start over
Return the length of the global result

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(1)
"""


class Solution:
    def longestSubstringNoVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = ""
        maxResult = ""

        for i in range(len(s)):
            if s[i] not in vowels:
                result += s[i]
                if len(result) > len(maxResult):
                    maxResult = result
            else:
                result = ""

        return len(maxResult)


class Tests:
    def __init__(self):
        s = Solution()
        assert s.longestSubstringNoVowels("codeforintelligents") == 3
        assert s.longestSubstringNoVowels("vtrw") == 4
        assert s.longestSubstringNoVowels("vtretoartykwqwrt") == 9


t = Tests()

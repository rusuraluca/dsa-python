"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.
Ex: Given the following strings...
    s = "abccba", return ""
    s = "foobar", return "fbar"
    s = "abccbefggfe", return "a"


Stack Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)
"""


class Solution:
    def removeDuplicates(self, s):
        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
                continue
            stack.append(ch)

        return "".join(stack)


class Tests:
    def __init__(self):
        s = Solution()
        assert (s.removeDuplicates("abccba")) == ""
        assert (s.removeDuplicates("foobar")) == "fbar"
        assert (s.removeDuplicates("abccbefggfe")) == "a"


t = Tests()

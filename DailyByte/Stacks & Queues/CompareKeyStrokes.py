"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/backspace-string-compare/
This question is asked by Amazon.
Given two strings s and t, which represents a sequence of keystrokes,
where # denotes a backspace, return whether or not the sequences produce the same result.
Ex: Given the following strings...
    s = "ABC#", t = "CD##AB", return true
    s = "como#pur#ter", t = "computer", return true
    s = "cof#dim#ng", t = "code", return false


Stack Solution:
-----------------------------------------------
@complexity:
Time:   O(n+m)
Space:  O(n+m)


One-Pass Solution:
-----------------------------------------------
@complexity:
Time:   O(n+m)
Space:  O(1)
"""


class Solution():
    def compareStack(self, s, t):
        def resolveString(s):
            stack = []

            for el in s:
                if el == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(el)
            return "".join(stack)

        return resolveString(s) == resolveString(t)

    def compareOnePass(self, s, t):
        i = len(s) - 1
        j = len(t) - 1

        skip_i = 0
        skip_j = 0

        while i >= 0 or j >= 0:
            # check backspace
            if i >= 0 and s[i] == "#":
                skip_i += 1
                i -= 1
                continue
            if j >= 0 and t[j] == "#":
                skip_j += 1
                j -= 1
                continue

            if i >= 0 and skip_i > 0:
                i -= 1
                skip_i -= 1
                continue
            if j >= 0 and skip_j > 0:
                j -= 1
                skip_j -= 1
                continue

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        if i == j:
            return True
        else:
            return False


class Tests:
    def __init__(self):
        s = Solution()
        assert (s.compareStack("ABC#", "CD##AB")) is True
        assert (s.compareStack("como#pur#ter", "computer")) is True
        assert (s.compareStack("cof#dim#ng", "code")) is False
        assert (s.compareStack("cof#dim#ng", "coding")) is True
        assert (s.compareStack("y#fo##f", "y#f#o##f")) is True

        assert (s.compareOnePass("ABC#", "CD##AB")) is True
        assert (s.compareOnePass("como#pur#ter", "computer")) is True
        assert (s.compareOnePass("cof#dim#ng", "code")) is False
        assert (s.compareOnePass("cof#dim#ng", "coding")) is True
        assert (s.compareOnePass("y#fo##f", "y#f#o##f")) is True


t = Tests()

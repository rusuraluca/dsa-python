"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/is-subsequence/


Base Cases:
-----------------------------------------------
If len of substring > len of string => not valid
If both empty => valid
If string empty => not valid
If substring empty => valid


Iterative Solution:
-----------------------------------------------
@description
t = "ahbgdc"
s = "abc"
traverse the given string
i = "a"
s = "a" => true we continue
i = "h"
s = "b" => false but we continue
i = "b"
s = "b" => true we continue
i = "g"
s = "c" => false but we continue
.
.
.
i = "c"
s = "c" => true we continue
stop when
- no more characters in the given string
- no more characters to check in the subsequence
--------------------------------------------------
t = "ab"
s = "rc"
traverse the given string
t = "a"
s = "r" => false but we continue
t = "b"
s = "r" => false but we continue
stop when
- no more characters in the given string
- no more characters to check in the subsequence

Check base cases
Loop through the chars in the string
    If current char is equal to the first char of the given substring
        Move forward in the substring
        If we are the end of the substring
            Return True
Return False

@complexity:
Time:   O(n) = O(len(s)), we traverse once all the characters of the givens string s
Space:  O(1), no auxiliary space required


Recursive Solution:
-----------------------------------------------
@complexity:
Time:   O(n) = O(len(s)), we traverse once all the characters of the givens string s
Space:  O(n) = O(len(s)), for the recursive stack calls
"""


class Solution:
    def isSubsequenceIterative(self, s: str, sub: str) -> bool:
        if len(s) < len(sub):
            return False

        if len(s) == len(sub) == 0:
            return True

        if len(s) == 0:
            return False

        if len(sub) == 0:
            return True

        i = 0
        for ch in s:
            if ch == sub[i]:
                i += 1
                if i == len(sub):
                    return True

        return False

    def isSubsequenceRecursive(self, sub: str, s: str) -> bool:
        def dp(i, j):
            if i == len(sub):
                return True

            if j == len(s):
                return False

            if sub[i] == s[j]:
                return dp(i + 1, j + 1)

            else:
                return dp(i, j + 1)

        return dp(0, 0)


class Tests:
    def __init__(self):
        s = Solution()
        assert s.isSubsequenceIterative("ahbgdc", "abc") == True
        assert s.isSubsequenceRecursive("ahbgdc", "axc") == False


t = Tests()

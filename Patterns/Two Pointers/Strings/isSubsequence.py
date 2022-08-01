"""
https://leetcode.com/problems/is-subsequence/

Two Pointers Solution:

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

@base cases:
- if len of substring > len of string => not valid
- if both empty => valid
- if string empty => not valid
- if substring empty => valid

@pseudocode:
check base cases
traverse the char of the string
    if current char is equal to the current subchar
        subchar becomes to the next char of the substring
        if subchar index is equal to subchar len
            then is valid

is substring is empty
    then is valid
otherwise
    not valid

@complexity:
Time:  O(n), n is the number of characters in the given string
           , we only traverse once the given string
Space: O(1), no auxiliary space needed
"""

class Solution:
    def isSubsequence(self, s: str, sub: str) -> bool:
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


s = Solution()
assert s.isSubsequence("ahbgdc", "abc") == True
assert s.isSubsequence("ahbgdc", "axc") == False

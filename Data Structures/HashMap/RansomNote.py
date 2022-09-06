"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/ransom-note/


Base Case:
-----------------------------------------------
Check if ransomNote is grater than magazine if true return false.


Hash Map Solution:
-----------------------------------------------
@description:
Construct a dictionary of magazine's chars and freq
Traverse ransomNote's chars
    If a ransomNote's char is not in the dictionary or exceeds the freq => Return False
Return True

@complexity:
Time:   O(n+m), n+m is the number of characters of the two strings
Space:  O(sigma), sigma = 1, we only keep a dictionary of 27 english letters and their frequency
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check if ransomNote is grater than magazine if true return false
        if (len(ransomNote) > len(magazine)):
            return False

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        dic = {c: 0 for c in alphabet}

        for c in magazine:
            dic[c] += 1

        for c in ransomNote:
            if dic[c] >= 1:
                dic[c] -= 1
            else:
                return False

        return True

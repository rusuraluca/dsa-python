"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/longest-palindrome/


Hash Map Solution:
-----------------------------------------------
@description:
Construct a dictionary of given string's word freq
Traverse the dictionary
    If a char's freq is even => add it to longest palindromes length
    Otherwise => add only the even part i.e. char's freq - 1
              => mark we can have one element without a pair in the element
Return the length + the mark of the one element (if it exist)

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(sigma), sigma = 1, we only keep a dictionary of 52 english letters and their frequency
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}

        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        # if there is a letter with count of odd ans must +=1
        odd = 0
        length = 0

        # checks if repetition of each char is even or odd
        for c in dic:
            if dic[c] % 2 == 0:
                length += dic[c]

            else:
                length += dic[c] - 1
                odd = 1

        return length + odd

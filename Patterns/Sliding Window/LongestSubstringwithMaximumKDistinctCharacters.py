"""
Problem:
-----------------------------------------------
https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String = "araaci", K = 2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String = "araaci", K = 1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String = "cbbebi", K = 3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String = "cbbebi", K = 10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".


Base Case:
-----------------------------------------------
If len of given string is smaller than k => return "" [empty string]


Brute Force Solution:
-----------------------------------------------
@description:
    Traverse once trough the arr
        For each current element


Sliding Window + Hashmap Solution:
-----------------------------------------------
@description:
We can use a HashMap to remember the frequency of each character we have processed.
    Traverse the arr through window blocks
        For each current sliding window we keep track of the char frequency in a dictionary
        When the len of the dictionary is greater than k
            we continuously shrink the sliding window,
            until we are left with k distinct characters in the char frequency dictionary
        Keep track of the maximum length so far

@complexity:
Time:  O(n), where n is the number of characters in the input string
             the outer for loop runs for all characters, and the inner while loop processes each character only once
             therefore, the time complexity of the algorithm will be O(n+n) <=> O(2n) <=> O(n)
Space: O(k), as we will be storing a maximum of k+1 characters in the hashmap
"""


class Solution:
    def longestSubstringwithMaximumKDistinctCharSlindingWindow(self, str, k):
        maxLen = 0
        windowStart = 0
        charFreq = {}

        for windowEnd in range(len(str)):
            endChar = str[windowEnd]
            if endChar not in charFreq:
                charFreq[endChar] = 0
            charFreq[endChar] += 1

            # shrink the sliding window, if the count of distinct characters in the HashMap is larger than k
            # shrink until we are left with 'k' distinct characters in the char_frequency
            # this is needed as we intend to find the longest window
            while len(charFreq) > k:

                # while shrinking, we’ll decrement the character’s frequency going out of the window
                # remove it from the HashMap if its frequency becomes zero
                startChar = str[windowStart]
                charFreq[startChar] -= 1
                if charFreq[startChar] == 0:
                    del charFreq[startChar]
                # shrink the window
                windowStart += 1

            # remember the maximum length so far
            # if the current window length is the longest so far, and if so, remember its length
            maxLen = max(maxLen, windowEnd - windowStart + 1)

        return maxLen


class Tests:
    def __init__(self):
        s = Solution()
        assert s.longestSubstringwithMaximumKDistinctCharSlindingWindow("cbbebi", 10) == 6
        assert s.longestSubstringwithMaximumKDistinctCharSlindingWindow("cbbebi", 3) == 5
        assert s.longestSubstringwithMaximumKDistinctCharSlindingWindow("araaci", 1) == 2
        assert s.longestSubstringwithMaximumKDistinctCharSlindingWindow("araaci", 2) == 4


t = Tests()
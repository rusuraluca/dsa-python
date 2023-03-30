"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/scramble-string/


Recursion Memoization Solution:
-----------------------------------------------
@description:
- check all possible partitions of the two strings and determine if they are scrambled versions of each other
- memoization is achieved using a dictionary m that stores the result of previous computations for the same inputs
- solve function takes in two strings s1 and s2, and returns a boolean value indicating whether they are scrambled versions of each other
- function first checks the length of the strings:
    - if they are both of length 1, it simply compares the characters
    - if the sorted characters in the two strings are not equal, it returns False
    - otherwise:
        - the function loops through all possible partitions of s1
        - and checks if they are valid scrambles of corresponding partitions in s2
            - the partitions are formed by looping through the length of s1 from index 1 to the end
        - if a valid partition is found, the function recursively checks the remaining partitions to see if they are also valid scrambles

@complexity:
Time:   O()
Space:  O()
"""


class Solution:
    def isScramble(self, s1, s2):
        def solve(s1, s2):

            if (s1, s2) in m:
                return m[(s1, s2)]
            # if the sorted characters in the two strings are not equal, it returns False
            if not sorted(s1) == sorted(s2):
                return False
            # if they are both of length 1, it returns True, as we already cheked that they have the same characters and no of characters
            if len(s1) == 1:
                return True

            # for all possible partitions of s1
            for i in range(1, len(s1)):
                # if they are valid scrambles of corresponding partitions in s2
                if solve(s1[:i], s2[-i:]) and solve(s1[i:], s2[:-i]) or solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    m[(s1, s2)] = True
                    return True

            m[(s1, s2)] = False
            return False

        m = {}
        return solve(s1, s2)


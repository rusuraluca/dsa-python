"""
Problem:
-----------------------------------------------
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7.
The first few sevenish numbers are 1, 7, 8, 49, and so on.
Create an algorithm to find the nth sevenish number.


Solution:
-----------------------------------------------
@description:
Hold in a list the sevenish numbers => sevenish = []
While we haven't reach the nth sevenish number:
    We calculate the next sevenish number
Return the last element in the sevenish list

@complexity:
Time: O(n), n is the given nth number
Space: O(n), for the sevenish list
"""

class Solution:

    def power(self, n, p):
        res = 1
        for i in range(p):
            res *= n
        return res

    def sevenishNumber(self, n):
        sevenish = []

        i = 0
        while len(sevenish) < n:
            sevenish.append(self.power(7, i))
            last_index = len(sevenish) - 1


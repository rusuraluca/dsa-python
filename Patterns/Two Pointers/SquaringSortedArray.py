"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/squares-of-a-sorted-array/


Naive Solution:
-----------------------------------------------
@description:
Squaring each element and sorting the new array

@complexity:
Time:   O(nlog(n)), n is the number of elems in the array
Space:  O(1), no auxiliary space needed


Two Pointers Solution:
-----------------------------------------------
@description:
We compute the squares of the elems 2 by 2 and compare them, adding the smallest first.

arr = [-4,-1,0,3,10]
sqarr = [0,1,9,16,100]

sol = [100, 16, 9, 1, 0]

l = -4  => ^2 => l = 16
r = 10 => ^2 => r = 100

l = 16
r = 3 ^ 2 = 9

l = 0 ^ 2 = 0
r = 3 ^ 2 = 9

l = 0 ^ 2 = 0
r = -1 ^ 2 = 1

reverse sol = [0, 1, 9, 16, 100]

@pseudocode:
- initialize empty result array
- initialize two pointers l, r one pointing at the first element of the array, the second at the last element of the arr
- loop until the left pointer is greater than the right pointer
    - if the square of the left pointer elem is smaller than the right pointer elem
        - append the right pointer elem to the result array
        - decrease the right pointer
    - otherwise
        - append the left square
        - increase the left pointer
- result array will be decreasing, so we return the reversed result array

@complexity:
Time:   O(n), n is the number of elems in the array
Space:  O(n), n is the number of elems in the array
"""


class Solution:
    def sortedSquares(self, arr):
        res = []
        l, r = 0, len(arr) - 1

        while l <= r:
            if arr[l] ** 2 < arr[r] ** 2:
                res.append(arr[r] ** 2)
                r -= 1
            else:
                res.append(arr[l] ** 2)
                l += 1

        return res[::-1]


class Tests:
    def __init__(self):
        s = Solution()
        assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
        assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


t = Tests()

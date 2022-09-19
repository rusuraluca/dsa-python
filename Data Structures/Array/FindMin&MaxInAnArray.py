"""
Problem:
-----------------------------------------------
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.


Sorting Solution:
-----------------------------------------------
@description:
Sort the array
Return the first and the last element of the sorted array

@complexity:
Time:   O(nlogn), where n is the number of elements in the array
Space:  O(1), constant space - but depends on the sorting algorithm


One-pass solution:
-----------------------------------------------
@description:
Keep two variables to represent the minimum and the maximum
Traverse the array once
At each visited element check if it is the smallest or the greatest
    If yes, update variables accordingly
    Otherwise, continue

@pseudocode:
    minn, maxx = 0, 0
    for e in elements of a
        if e is < minn : minn = e
        else if e is > maxx : maxx = e
    return minn, maxx

@complexity:
Time:   O(n), where n is the number of elements in the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def minmax(self, arr):
        if len(arr) < 2:
            return 0

        if len(arr) == 2:
            return min(arr[0], arr[1]), max(arr[0], arr[1])

        minn, maxx = float('inf'), float('-inf')
        for e in arr:
            if e > maxx:
                maxx = e
            if e < minn:
                minn = e

        return minn, maxx


class Tests:
    def __init__(self):
        arr = []
        s = Solution()
        assert s.minmax(arr) == 0
        arr = [1, 2, 3, 4]
        assert s.minmax(arr) == (1, 4)


t = Tests()

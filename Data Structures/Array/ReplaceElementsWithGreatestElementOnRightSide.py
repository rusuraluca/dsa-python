"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""


class Solution:
    def replaceElements(self, arr):
        maxright = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxright
            if temp > maxright:
                maxright = temp
        arr[-1] = -1

        return arr

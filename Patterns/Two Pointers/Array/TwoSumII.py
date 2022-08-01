"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


Naive Solution:
-----------------------------------------------
@description:
traverse the input 2 times and check for target

nums = [2,7,11,15]
target = 9

2
[7, 11, 15]
- we reach target sum with 7 -> [1, 2]

nums = [2,7,11,15]
target = 18
2
[7, 11, 15]
- we don't find target

7
[11, 15]
- we reach target sum with 11 -> [2, 3]

@complexity:
Time:  O(n^2), n is the number of elements in the given list
Space: O(1), no auxiliary space needed


Sort & Two Pointers Solution:
-----------------------------------------------
@description:
this is good only if we need to return the elements, not the indexes because after sorting the indexes may change
sort the input list in ascending order, and use two pointers to find the pair in the array
inspired by binary search

nums = [2,7,15,11]
target = 9

after sorting:
nums = [2,7,11,15]
target = 9

two pointers:
[2,7,11,15]
l       r
l + r = 17 > target => r-=1

[2,7,11,15]
l    r
l + r = 13 > target => r-=1

[2,7,11,15]
l  r
l + r = 9 == target => return [l, r]

@complexity:
Time:   O(n*log(n))         , where n is the length of the input array
Space:  O(log(n)) or O(n)   , depending on the sort algorithm
"""

class Solution:
    def twoSumII(self, arr, target):
        l = 0
        r = len(arr)-1
        while l < r:
            current = arr[l] + arr[r]
            if current == target:
                return [l+1, r+1]
            elif current > target:
                r -= 1
            else:
                l += 1

        return []

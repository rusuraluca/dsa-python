"""
Problem:
-----------------------------------------------

Given an array of positive numbers and a positive number ‘k,’
find the minimum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k = 3
Output: 6
Explanation: Subarray with minimum sum is [1, 3, 2].

Input: [2, 3, 4, 1, 5], k = 2
Output: 5
Explanation: Subarray with minimum sum is [2, 3].


Base Cases:
-----------------------------------------------
If len of array < given k => return NIL


Brute Force Solution:
-----------------------------------------------
@description:
[2, 1, 5, 1, 3, 2], k = 3

[2, 1, 5] => min = 8

[1, 5, 1] => min = 7

[5, 1, 3] => min = 7

[1, 3, 2] => min = 6

Traverse once the array from 0 to n-k, where n is the number of elements in the array
    At each element calculate the sum of the k elements starting from the current element
    If the current sum is smaller than our global minimum sum, update minimum sum
    Otherwise, continue

@complexity:
Time:  O(n*k)
Space: O(1)


Sliding Window Solution:
-----------------------------------------------
@description:
We realize that to calculate the sum of a contiguous subarray, we can utilize the sum of the previous subarray
This approach will save us from re-calculating the sum of the overlapping part of the sliding window

Let's consider each subarray as a Sliding Window of size 'k'
To calculate the sum of the next subarray, we need to slide the window ahead by one element
So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:
    Subtract the element going out of the sliding window, i.e. subtract the first element of the window
    Add the new element getting included in the sliding window, i.e. the element coming right after the end of the window

@complexity:
Time:  O(n)
Space: O(1)
"""


class Solution:
    def minimumSumSubarrayofSizeKSlidingWindow(self, arr, k):
        # base case
        if len(arr) == k:
            return sum(arr)

        # global min sum
        minSum = float('inf')
        # to retain temp window sum
        windowSum = 0
        # to retain temp index of starting elem of subarray
        windowStart = 0

        for w in range(len(arr)):
            # add the next element
            windowSum += arr[w]

            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            if (w - windowStart + 1) == k:
                minSum = min(minSum, windowSum)
                # subtract the element going out
                windowSum -= arr[windowStart]
                # slide the window ahead
                windowStart += 1

        return minSum


class Tests:
    def __init__(self):
        s = Solution()
        assert s.minimumSumSubarrayofSizeKSlidingWindow([2, 1, 5, 1, 3, 2], 3) == 6
        assert s.minimumSumSubarrayofSizeKSlidingWindow([2, 3, 4, 1, 5], 2) == 5
        assert s.minimumSumSubarrayofSizeKSlidingWindow([2, 3], 2) == 5


t = Tests()

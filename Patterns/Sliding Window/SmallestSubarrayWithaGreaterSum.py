"""
Problem:
-----------------------------------------------
https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

Given an array of positive integers and a number ‘S’,
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S = 7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

Input: [2, 1, 5, 2, 8], S = 7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].


Base Case:
-----------------------------------------------
If sum(arr) < S => return 0, because we only have positive integers


Brute Force Solution:
-----------------------------------------------
@description:
Consider traversing the elements twice
The outer loop picks a starting element, the inner loop considers all elements (on right side of current start) as ending element
    Whenever sum of elements between current start and end becomes more than the given number,
    if current length is smaller than the smallest length so far => update the result

@complexity:
Time:  O(n^2), traversing twice the n elems in the array
Space: O(1), no auxiliary space required


Sliding Window Solution:
-----------------------------------------------
@description:
    Following a Sliding Window Approach we can
    Traverse the array once
        Calculate the sum at the current element
        While the sum is greater than or equal to the given sum
            If the size of the subarray is smaller than our global min len -> update min len
            Shrink the sliding window, by removing the starting element

    Return the min len



@complexity
Time:  O(n), the outer for loop runs for all elements, and the inner while loop processes each element only once
       O(n+n) => O(2n) <=> O(n)
Space: O(1), no auxiliary space required
"""


class Solution():
    def smallestSubarrayWithaGeaterSumSlidingWindow(self, arr, s):
        minLen = len(arr)
        windowSum = 0
        windowStart = 0

        for windowEnd in range(len(arr)):
            # add the next element
            windowSum += arr[windowEnd]

            # shrink the window as small as possible until the 'window_sum' is smaller than 's'
            while windowSum >= s:
                minLen = min(minLen, windowEnd - windowStart + 1)
                windowSum -= arr[windowStart]
                windowStart += 1

        if minLen == len(arr):
            return 0

        return minLen


class Tests:
    def __init__(self):
        s = Solution()
        assert s.smallestSubarrayWithaGeaterSumSlidingWindow([2, 1, 5, 2, 3, 2], 7) == 2
        assert s.smallestSubarrayWithaGeaterSumSlidingWindow([2, 1, 5, 2, 8], 7) == 1
        assert s.smallestSubarrayWithaGeaterSumSlidingWindow([3, 4, 1, 1, 6], 8) == 3
        assert s.smallestSubarrayWithaGeaterSumSlidingWindow([1, 1], 8) == 0


t = Tests()

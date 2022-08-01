"""
Problem:
-----------------------------------------------

Difference between the maximum and minimum average of all k-length continuous subarrays

Input: arr[ ] = {3, 8, 9, 15}, K = 2
Output: 6.5
Explanation:
All subarrays of length 2 are {3, 8}, {8, 9}, {9, 15}
and their averages are (3+8)/2 = 5.5, (8+9)/2 = 8.5, and (9+15)/2 = 12.0 respectively.
Therefore, the difference between the maximum(=12.0) and minimum(=5.5) is 12.0 -5.5 = 6.5.


Base Case:
-----------------------------------------------
If k is greater than the len of the array => Return 0.0


Sliding Window Solution:
-----------------------------------------------
@description:
Traverse the array
    Keep a window of elements and it's sum
    When the window's len is equal to K
        Calculate average
        Compare it with maximum sum
        Compare it with minimum sum
        Slide the window to the right with one element

    Difference is equal to maximum sum minus minimum sum
    Return difference

@complexity:
Time:   O(n), n is the number of elements in the array
Space:  O(1), no auxiliary space required
"""

class Solution:
    def difference(self, arr, k):
        if len(arr) < k:
            return 0.0

        currAvrg = 0.0
        windowStart = 0
        maxSum = 0.0
        minSum = float("inf")
        currSum = 0.0

        for windowEnd in range(len(arr)):
            currSum += arr[windowEnd]

            if windowEnd - windowStart + 1 == k:
                currAvrg = currSum / k
                maxSum = max(maxSum, currAvrg)
                minSum = min(minSum, currAvrg)
                currSum -= arr[windowStart]
                windowStart += 1

        diff = maxSum - minSum
        return diff


class Tests:
    def __init__(self):
        s = Solution()
        assert s.difference([3, 8, 9, 15], 2) == 6.5


t = Tests()
"""
Problem:
-----------------------------------------------
https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
https://leetcode.com/problems/smallest-range-ii/


Sorting Solution:
-----------------------------------------------
@description:
The idea is to increase the first i towers by k and decrease the rest tower by k after sorting the heights,
then calculate the maximum height difference.
This can be achieved using sorting.
Given arr[] = {1, 15, 10}, n = 3, k = 6
Array after sorting => arr[] = {1, 10, 15}
Initially maxHeight = arr[n - 1] = 15
            minHeight = arr[0] = 1
            ans = maxHeight - minHeight = 15 - 1 = 14
At i = 1
minHeight = min(arr[0] + k, arr[i] - k) = min(1 + 6, 10 - 6) = 4
maxHeight = max(arr[i - 1] + k, arr[n - 1] - k) = max(1 + 6, 15 - 6) = 9
ans = min(ans, maxHeight - minHeight) = min(14, 9 - 4) = 5 => ans = 5
At i = 2
minHeight = min(arr[0] + k, arr[i] - k) = min(1 + 6, 15 - 6) = 7
maxHeight = max(arr[i - 1] + k, arr[n - 1] - k) = max(10 + 6, 15 - 6) = 16
ans = min(ans, maxHeight - minHeight) = min(5, 16 - 7) = 5 => ans = 5
Hence minimum difference is 5

@pseudocode:
Sort the array
Try to make each height of the tower maximum by decreasing the height of all the towers to the right by k
and increasing all the height of the towers to the left by k.
Check whether the current index tower has the maximum height or not by comparing it with a[n]-k.
    If the tower's height is greater than the a[n]-k then it's the tallest tower available.
Similarly, find the shortest tower and minimize the difference between these two towers.

@complexity:
Time:   O(n * log(n)), for sorting
Space:  O(1), without some space required for sorting
"""


class Solution:
    def getMinDiff(self, arr, k):
        if len(arr) == 1:
            return 0

        arr.sort()

        # maximum possible height difference
        ans = arr[-1] - arr[0]

        for i in range(len(arr) - 1):
            tempmin = min(arr[0] + k, arr[i + 1] - k)
            tempmax = max(arr[i] + k, arr[-1] - k)

            ans = min(ans, tempmax - tempmin)

        return ans

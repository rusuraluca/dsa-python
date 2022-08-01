"""
Problem:
-----------------------------------------------

Count negative elements present in every k-length subarray.

Input: arr = [-1, 2, -2, 3, 5, -7, -5], K = 3
Output: 2, 1, 1, 1, 2


Naive Solution:
-----------------------------------------------
@description:
The simplest approach is to traverse the given array,
considering every window of size K,
and find the count of negative numbers in every window.

@complexity:
Time:   O(n*k), we traverse once the n elements of the array and for every one we traverse the next k-1 elements as well
Space:  O(n), for the list of negative numbers counts


Sliding Window Solution:
-----------------------------------------------
@description:
Initialize a variable count as 0 to store the count of negative elements in a window of size K.
Initialize two variables i and j as 0 to store the first and last index of the window respectively.
Loop while j<N and perform the following steps:
    If arr[j] < 0, increment count by 1.
    If the size of the window, i.e, j-i+1 is equal to K, append the count, and check if arr[i] < 0,
    then decrement count by 1. Also, increment i by 1.
    Increment the value of j by 1.

@complexity:
Time:   O(n), we traverse once the n elements of the array
Space:  O(n), for the list of negative numbers counts
"""

class Solution:
    def getCountNegatives(self, arr, k):
        lst = []
        start = 0
        count = 0

        for i in range(len(arr)):
            if arr[i] < 0:
                count += 1

            if i - start + 1 == k:
                lst.append(count)
                if arr[start] < 0:
                    count -= 1

                start += 1

        return lst


class Tests:
    def __init__(self):
        s = Solution()
        assert s.getCountNegatives([-1, 2, -2, 3, 5, -7, -5], 3) == [2, 1, 1, 1, 2]


t = Tests()

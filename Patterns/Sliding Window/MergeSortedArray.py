"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/merge-sorted-array/


Forwards Solution:
-----------------------------------------------
@description:
Keep a copy of the elements in num1.
Start merging from the beginning in num1.
@complexity:
n+m is the number of elems in the given arrays
Time:   O(n+m),  since in the worst case the algorithm would need to swap every element of both arrays once
                 (for this case as an example: [4, 5, 6], [1, 2, 3])
Space:  O(m), extra memory for the elements of num1 is necessary


Backwards Solution:
-----------------------------------------------
@description:
Since we have free space (the zeros) at the end of nums1,
that is the direction into which we must "spread" the numbers of nums1 and nums2.
That is why we should compare and swap the numbers starting from the end of both given sorted arrays
and move through them backwards.
Starting from the beginning leads only to a mess of over-swapping.
We would start from the beginning and move forwards only if, for example, the free space was at the beginning of nums1.

We start merging from the ends of the lists
If second list is empty, nothing more to merge
Only merge from nums1 if there are items left to merge
Insert at current position the larger of the two values from nums1 and nums2

@complexity:
n+m is the number of elems in the given arrays
Time:   O(n+m),  since in the worst case the algorithm would need to swap every element of both arrays once
                 (for this case as an example: [4, 5, 6], [1, 2, 3])
Space:  O(1), no extra memory is necessary
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        e1, e2 = m-1, n-1

        for c in range(m + n - 1, -1, -1):
            if e2 < 0:
                return

            if e1 >= 0 and nums1[e1] > nums2[e2]:
                nums1[c] = nums1[e1]
                e1 -= 1

            else:
                nums1[c] = nums2[e2]
                e2 -= 1

    def mergeForwards(self, nums1, m: int, nums2, n: int) -> None:
        aux = nums1[:m]
        e1, e2 = 0, 0
        for c in range(n + m):
            if e2 >= n or (e1 < m and aux[e1] <= nums2[e2]):
                nums1[c] = aux[e1]
                e1 += 1
            else:
                nums1[c] = nums2[e2]
                e2 += 1

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/merge-intervals/


Sorting Solution:
-----------------------------------------------
@description:
https://leetcode.com/problems/merge-intervals/solution/

@complexity:
Time:   O(n log n), other than the sort invocation, we do a simple linear scan of the list,
        so the runtime is dominated by the O(n log n) complexity of sorting.
Space:  O(logN) or O(n), if we can sort intervals in place, we do not need more than constant additional space,
        although the sorting itself takes O(log n) space.
        Otherwise, we must allocate linear space to store a copy of intervals and sort that.
"""


class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # otherwise, there is overlap, so we merge the current and previous intervals
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

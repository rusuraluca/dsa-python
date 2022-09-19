"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/non-overlapping-intervals/


Sort by starting time Greedy Solution:
-----------------------------------------------
@description:
A classic greedy case: interval scheduling problem.

The heuristic is: always pick the interval with the earliest end time.
Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time
produces the maximal capacity to hold rest intervals.

e.g.
Suppose current earliest end time of the rest intervals is x.
Then available time slot left for other intervals is [x:].
If we choose another interval with end time y, then available time slot would be [y:].
Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time.
Once next interval's start time is earlier than current end time,
then we have to remove one interval.
Otherwise, we update earliest end time.


Attend the one with smaller start time first
(Greedy) Remove the one with bigger end time if overlapping occurs (because it will always incur more overlappings in the remaining array with asceding order of start time)

@complexity:
Time:   O(n log n), as sort overwhelms greedy search
Space:  O(logN) or O(n), if we can sort intervals in place, we do not need more than constant additional space,
        although the sorting itself takes O(log n) space.
        Otherwise, we must allocate linear space to store a copy of intervals and sort that.


Sort by ending time Greedy Solution:
-----------------------------------------------
@description:
If we think more clearly,
the first solution can be improved slightly (save a line of code) by sorting the intervals with end time.
Why? Becuase the greedy nature remains true even if we the remaining array is not sorted by start time.
Meanwhile, if we sort them by end time and if overlap occurs,
the interval that comes later must be the one to remove as it has larger end time.
Take a look at the following example.

Example:
1) sort by start time
Extra procedure: after comparing [1,10] and [2,3], we have to choose which one to remove by comparing the end time
[[1,10], [2,3], [3,4], [5,6]]
2) sort by end time
Saved procedure: after comparing [5, 6] and [1,10], we immediately can remove the later one which is [1,10]
as it must produce more overlaps in the following, i.e. with [6,11] and [9,12]
[[2,3], [3,4], [5,6], [1,10], [6, 11], [9, 12]]
"""


class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
                prev = min(prev, i[1])
        return ans

    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans

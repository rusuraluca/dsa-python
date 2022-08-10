"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/k-closest-points-to-origin/submissions/


Sorting Solution:
-----------------------------------------------
We sort the whole array and return the first k elements.
If we look at the sorting solution, we will find that we are sorting the WHOLE array
while the problem is asking for K-nearest, so we are doing extra work than we need to!
So can we reduce it by only sorting the K we need, yes thats is ahieved using heaps.
@complexity:
Time:   O(n*logn)
Space:  O(1)


Max Heap Solution:
-----------------------------------------------
This problem can easily be solved using Max heaps, why max heaps? because we are intrested in keeping the smallest elements, so we want to pop the largest ones from the top of the stack.
So make the heap pop biggest elements first, we multiply the calculated distance by -1.
@complexity:
Time:   O(n*logk)
Space:  O(k)
"""
import heapq


class Solution:
    def kClosest(self, points, k: int):
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]

            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return [tuple[1] for tuple in heap]

    def kClosestSorting(self, points, k: int):
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))[:k]

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-median-from-data-stream/


Brute Force Solution:
-----------------------------------------------
@description:
Maintain a sorted list of all numbers
Return the median whenever required in O(1) time
Inserting a number in a sorted list will take O(n) time in the worst case if there are n numbers in the list
Find median with formula will take O(1) time

@complexity:
Time: O(n^2), for inserting the n elements in the sorted list
Space: O(n), for the list


Optimization:
-----------------------------------------------
We are only interested in the middle element of an ordered array
We just need the middle element or the middle elements in order
odd  => 1 middle elem
even => 2 middle elems

Binary Heap or Balanced Binary Tree maintains the order with the data structure and the insertion takes O(log n)
Using heaps we can maintain the min and max elements

[2, 3, 4,   5, 6]
--------    -----
1st         2nd
--------    -----
MAX         MIN
MID = 4 = EXTRA IN MAX HEAP (1st half)

[2, 3,    4, 5]
-----     -----
1st       2nd
-----     -----
MAX       MIN
MID = (3+4)/2 = 3.5 EQUAL LEN => AVERGAE OF TOP FROM HEAPS


Two Heaps Solution:
-----------------------------------------------
@description:
Instead of keeping a sorted list, we could keep two heaps: a max_heap and min_heap
Let’s assume that x is the median of the list
This means that, half of the items in the list are smaller than (or equal to) x
and other half is greater than (or equal to) x
We can store the smaller part of the list in a max_heap, we are using max_heap
because we are only interested in knowing the largest number in the first half of the list
We can store the larger part of the list in a min_hea, again we are using min_heap
because we are only interested in knowing the smallest number in the second half of the list
Inserting a number in a heap will take O(log n) (better than the brute force solution)
The median of the current list of numbers can be calculated from the top element of the two heaps
We had decided to have more numbers in the max_heap in case of odd count
Size equal of heaps => We add to max heap


add(5)
add(3)
add(4)
add(2)
add(6)

MAX     MIN     MEDIAN
5               5

MAX     MIN     MEDIAN
3       5       4

MAX     MIN     MEDIAN
3       5       4
4

MAX     MIN     MEDIAN
3       4       3.5
2       5

MAX     MIN     MEDIAN
4       5       4
3       6
2

@complexity:
Time: O(n * log n), for inserting the n elements
Space: O(n), for the heaps


Follow up:
-----------------------------------------------
If all integer numbers from the stream are in the range [0, 100],
how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100],
how would you optimize your solution?

If all the numbers or 99% of the numbers are in a certain range (say 1-100), then:
Initialize an array of size same as range (so array of size 100, for numbers in range 1-100) this will keep track of counts
Everytime add_num is called increment the number at that index
Ex: you get add_num called with 23 you do counts[23]++.
You also increment the size instance variable to keep track of total number of numbers added
When find_median is called you re-iterate through the counts array size/2 times (handle odd and even),
in each iteration you go to the next count instead of the next count index
The Space complexity is fixed, but time complexity will be O(n) for find_median
"""
from heapq import *


class MedianFinder:

    def __init__(self):
        # containing first half of numbers
        self.max_heap = []
        # containing second half of numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Python only implements min heap => always multiply with -1 the elements to insert in max heap
        # every element in the max_heap must be smaller than every element in the min_heap
        # -self.max_heap[0] to reverse the false value of the top we added to the max heap
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both heaps will have equal number of elements or max-heap will have one more element
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # we have even number of elements, take the average of middle two elements
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        # we have odd number of elements, the first element in max-heap is the median element
        return -float(self.max_heap[0])

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/sliding-window-median/


Brute Force Solution:
-----------------------------------------------
@description:
A very obvious solution will be to sort the k numbers within a sliding window for each iteration.
Suppose the length of the array is n, the total time complexity will be O(nklogk).

@complexity:
Time:   O(n * k * log k), where n is the length of the array
Space:  O(1), no auxiliary space required


We can do better than that!
We notice that when the sliding window moves one step,
a new number is added to the window and an old number is removed from the window.
Therefore, for each iteration, we do not need to sort the whole sliding window again.
We just need to
    - remove the old number (O(k) time)
    - insert the new number at the correct position (O(k) time) of the already sorted window
Therefore, the total time complexity will be O(nk).

Can we still do better? Yes!
Now enters the secret ingredient — heap!
Heap is particularly good at dynamically tracking something like the x-th largest number.
Imagine that a stream of numbers is coming to you and you need to return
the x-th largest number of all the numbers you have seen so far when each new number is encountered.
This scenario is dynamic because you need to find the answers (x-th largest number)
many times over constantly changing data.
The solution is using a min heap to store the top x largest numbers
and the top of the heap is the x-th largest number.
When a new number comes, if it is smaller than the top of the heap,
it can be discarded because it will never be the x-th largest number.
If the new number is greater than the top of the heap,
it will be added to the heap and the old top of the heap will be popped out.

A median of k numbers is just roughly the k/2-th smallest number so it seems that a heap can be used here.
In this scenario, we need two heaps instead of only one heap in the previous scenario.
In the previous scenario, in order to find the x-th largest number,
only the new numbers greater than the old x-th largest number have to be recorded,
so only one heap is needed.
In order to find the median of the sliding window,
both new numbers greater than the old median and new numbers smaller than the old median need to be recorded,
because both kinds of new numbers are candidates for the median.
Since two heaps are needed and the median number(s) has to be at the top of the heap for easy access,
the ultimate data structure is easy to guess — a max heap storing the smaller half of numbers in the sliding window
and a min heap storing the larger half of numbers.
The top numbers of the heaps are what we need to compute the median.
When the length of the sliding window is an even number,
size of max heap is the same as size of min heap.
When it is an odd number,
max heap will have one more item than min heap.

Now that we know the data structure we want,
it is time to design an algorithm to maintain this data structure.

Maybe the following content would seem too trivial and obvious to you.
The first thing we know is that we need a loop that moves the sliding window.
Ok. Great first step. Now what will happen in each iteration of the loop?
Before we tackle this question, it is helpful to think about the loop invariants.
Loop invariants are qualities that do not change during the execution of the whole loop.
In this problem, the loop invariants are:
1. All numbers in the sliding window and only those should be in the two-heap stucture.
2. The maximum of the max heap ≤ the minimum of the min heap.
3. size of max heap = size of min heap or size of min heap + 1.

In order to maintain these loop invariants, each iteration should:
1. Add a new number encountered by the sliding window to the two-heap structure
   and remove an old number the sliding window just left from the structure.
2. If new number ≤ maximum of max heap,
   add it to the max heap; otherwise, add it to the min heap.
3. Maintain the size relationship between the two heaps by popping items from the heap
   that has too many items and pushing them in the other heap.

Now we got the complete algorithm. The total time complexity is O(nlog(size of heap)) = O(nlogk).

Since the algorithm design is done, now comes time for implementation, which will be coded in Python.
The heap in Python is a simple Python list plus heap functionalities supported in the heapq standard library.
The problem with this heapq library is that
although the theoretical time complexity for removing an item at any position of the heap is O(log(size of heap)),
this kind of removal is not supported in the heapq library.
The only way to remove an item at an arbitrary position is to loop through the whole heap
to remove that item and to call heapq.heapify(heap), which make time complexity deteriorate to O(size of heap).

There are two solutions to achieve the theoretical time complexity of O(log(size of heap)):
1. implementing a hash-heap data structure
2. using the lazy deletion technique

A hash-heap data structure is a standard heap
plus a hashing table mapping the value of an item to the index of the item.


The lazy deletion technique means that when items need to be removed,
it just records the items but does not actually remove them.
Actual deletions only happen when the top of the heap is queried
and the real top of the heap is blocked by items that should have been removed.
Only at that time are those removed items actually popped out of the heap.
This technique ensures that items are always removed from the top of the heap,
hence the O(log(size of heap)) time complexity for removing a item at any position.
However, when using this technique,
the overall time complexity for the whole problem is O(nlog(size of heap))
where size of heap is not always k because in the worst case scenario the size of heap can be n.
"""
from heapq import heappush, heappop


class Solution:
    def medianSlidingWindow(self, nums, k: int):
        result = []
        max_heap, min_heap = [], []
        removed_set = set()
        self.max_heap_size, self.min_heap_size = 0, 0

        for i, num in enumerate(nums):
            self._add_number(max_heap, min_heap, num, i, removed_set)

            if i < k - 1:
                continue

            if i > k - 1:
                self._delete_number(max_heap, min_heap, removed_set, nums[i - k], i - k)

            self._balance(max_heap, min_heap, removed_set)
            self._pop_removed_items(max_heap, min_heap, removed_set)
            if self.max_heap_size == self.min_heap_size + 1:
                median = -max_heap[0][0]
            else:
                median = (-max_heap[0][0] + min_heap[0][0]) / 2
            result.append(median)

        return result

    def _add_number(self, max_heap, min_heap, number, index, removed_set):
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if not max_heap or (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1
        else:
            heappush(min_heap, (number, index))
            self.min_heap_size += 1

    def _delete_number(self, max_heap, min_heap, removed_set, number, index):
        # it's guaranteed that max_heap is not empty
        self._pop_removed_items(max_heap, min_heap, removed_set)
        if (number, index) <= (-max_heap[0][0], -max_heap[0][1]):
            removed_set.add((-number, -index))
            self.max_heap_size -= 1
        else:
            removed_set.add((number, index))
            self.min_heap_size -= 1

    def _balance(self, max_heap, min_heap, removed_set):
        # at most one iteration in one of the while loops will be executed
        while self.max_heap_size > self.min_heap_size + 1:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            negative_number, negative_index = heappop(max_heap)
            self.max_heap_size -= 1

            heappush(min_heap, (-negative_number, -negative_index))
            self.min_heap_size += 1

        while self.max_heap_size < self.min_heap_size:
            self._pop_removed_items(max_heap, min_heap, removed_set)

            number, index = heappop(min_heap)
            self.min_heap_size -= 1

            heappush(max_heap, (-number, -index))
            self.max_heap_size += 1

    def _pop_removed_items(self, max_heap, min_heap, removed_set):
        while max_heap and max_heap[0] in removed_set:
            heappop(max_heap)

        while min_heap and min_heap[0] in removed_set:
            heappop(min_heap)


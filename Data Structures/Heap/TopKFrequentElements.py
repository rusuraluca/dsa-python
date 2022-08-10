"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/top-k-frequent-elements/


Sorting Solution:
-----------------------------------------------
@description:
The idea here is to first traverse an array and create a map of all numbers and their count.
The ideal data structure for storing key and value pairs is HashMap.
Sort the HashMap by its value and pick only k elements.

@complexity:
Time:  O(n*logn), for sorting the n elements
Space: O(n), for the hashmap


Priority Queue (Min Heap) Solution:
-----------------------------------------------
@description:
Let’s improve our previous solution using a priority queue.
To solve this problem first create a map of each element and its count.
Then use a priority queue (Min Heap) and we keep its size equal to k.
Take all the keys of a map and put them in a Priority Queue.
If the size of a priority queue is greater than k,
we poll the top element which is the minimum element.
Once all the elements of HashMap are put in a Priority queue, we only get the top k elements.

@complexity:
Time:   O(n·log(k))
Space:  O(k)
"""
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        # create dictionary of frequencies
        d = dict()

        # create hashmap
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        # use a min heap to only maintain the k most frequent elements
        min_heap = []
        for val, freq in d.items():
            heapq.heappush(min_heap, (freq, val))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [j for i, j in min_heap]

    def topKFrequentSorting(self, nums, k: int):
        d = {}

        # create hashmap
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        ans = []
        # sort the dic by key
        d = list(d.items())
        d.sort(key=lambda x: x[1], reverse=True)

        # return the first k elements
        return [x[0] for x in d[:k]]


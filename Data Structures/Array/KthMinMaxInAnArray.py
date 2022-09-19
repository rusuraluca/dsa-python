"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/kth-largest-element-in-an-array/


Sorting Solution:
-----------------------------------------------
@description:
Sort the array in ascending order
Return the element at index k-1 of the sorted array
and the element at index n-k+1 of the sorted array

@complexity:
Time:   O(nlogn), where n is the number of elements in the array
Space:  O(1), constant space - but depends on the sorting algorithm


Hash Set Solution:
-----------------------------------------------
@description:
Hash Set data structure can be used to find the kth smallest element
as it stores the distinct elements in sorted order.
Insert all array elements into a set.
Advance the iterator to the kth and the n-k element in the set.
Return the value of the element at which the iterator is pointing.

@complexity:
Time:   O(nlogn), where n is the number of elements in the array
Space:  O(n), for the Hash Set


Hash Map Solution:
-----------------------------------------------
@description:
Use a map and then map each element with its frequency.
And as an ordered map would store the data in a sorted manner,
so keep on adding the frequency of each element
till it does not become greater than or equal to k
so that the k’th element from the start can be reached i.e. the k’th smallest element.

Store frequency of every element in a Map mp
Now traverse over sorted elements in the Map mp and add their frequencies in a variable freq
If at any point the value of freq is greater than or equal to K,
then return the value of iterator of Map mp

@complexity:
Time:   O(nlogn), where n is the number of elements in the array
Space:  O(n), for the Hash Map


Heap Solution:
-----------------------------------------------
@description:
Min-Heap can be used to find the kth smallest element,
by inserting all the elements into Min-Heap
and then and call extractMin() function K times.

Max-Heap can be used to find the kth smallest element,
by inserting all the elements into Max-Heap
and then and call extractMax() function K times.

Insert all the array elements into the Min-Heap/Max-Heap
Call extractMin() and extractMax() function K times
Return the value obtained at the last call of extractMin() and extractMax() function

@complexity:
Time:   O(n + n-k log n), where n is the number of elements in the array
Space:  O(n), for the Hash Set




Priority Queue Solution:
-----------------------------------------------
@description:
To find the Kth minimum element in an array, insert the elements into the priority queue
until the size of it is less than K, and then compare remaining elements with the root
of the priority queue and if the element is less than the root then remove the root
and insert this element into the priority queue and finally return root of the priority queue

Build a priority queue of the first K elements (arr[0] to arr[K-1]) of the given array.
For each element, after the Kth element (arr[K] to arr[n-1]), compare it with the root of priority queue.
If the element is less than the root then remove the root and insert this element into the priority queue
Else ignore it.
Finally, the root of the priority queue is the Kth smallest element.
Same for the maximum.
@complexity:
Time: O(k log k +  (n – k) log k)
Space: O(k)
"""
import heapq


class Solution:
    def kthMinMax(self, arr, k):
        # Sort the given array
        arr.sort()

        # Return k'th element in the
        # sorted array
        return arr[k - 1], arr[len(arr) - k]

    def kthMinMaxHeapPriorityQueue(self, arr, k):
        # For finding min element we need (Max heap)priority queue
        pq = []
        for i in range(k):
            # First push first K elements into heap
            heapq.heappush(pq, arr[i])
            heapq._heapify_max(pq)

        # Now check from k to last element
        for i in range(k, len(arr)):

            # If current element is < first that means
            # there are  other k-1 lesser elements
            # are present at bottom thus, pop that element
            # and add kth largest element into the heap till curr
            # at last all the greater element than kth element will get pop off
            # and at the top of heap there will be kth smallest element
            if arr[i] < pq[0]:
                heapq.heappop(pq)

                # Push curr element
                heapq.heappush(pq, arr[i])
                heapq._heapify_max(pq)
        # Return first of element
        return pq[0]

    def kthMinMaxHeap(self, arr, k):
        class MinHeap:
            # Constructor
            def __init__(self, a, size):
                # list of elements in the heap
                self.harr = a

                # maximum possible size of min heap
                self.capacity = None

                # current number of elements in min heap
                self.heap_size = size

                i = int((self.heap_size - 1) / 2)
                while i >= 0:
                    self.minHeapify(i)
                    i -= 1

            def parent(self, i):
                return (i - 1) / 2

            def left(self, i):
                return 2 * i + 1

            def right(self, i):
                return 2 * i + 2

            # Returns minimum
            def getMin(self):
                return self.harr[0]

            # Method to remove minimum element (or root)
            # from min heap
            def extractMin(self):
                if self.heap_size == 0:
                    return float("inf")

                # Store the minimum value
                root = self.harr[0]

                # If there are more than 1 items, move the last item
                # to root and call heapify
                if self.heap_size > 1:
                    self.harr[0] = self.harr[self.heap_size - 1]
                    self.minHeapify(0)
                self.heap_size -= 1
                return root

            # A recursive method to heapify a subtree with root at
            # given index. This method assumes that the subtrees
            # are already heapified
            def minHeapify(self, i):
                l = self.left(i)
                r = self.right(i)
                smallest = i
                if ((l < self.heap_size) and
                        (self.harr[l] < self.harr[i])):
                    smallest = l
                if ((r < self.heap_size) and
                        (self.harr[r] < self.harr[smallest])):
                    smallest = r
                if smallest != i:
                    self.harr[i], self.harr[smallest] = (
                        self.harr[smallest], self.harr[i])
                    self.minHeapify(smallest)

        # Function to return k'th smallest element in a given array

        # Build a heap of n elements in O(n) time
        mh = MinHeap(arr, len(arr))

        # Do extract min (k-1) times
        for i in range(k - 1):
            mh.extractMin()

        # Return root
        return mh.getMin()

    def kthMinMaxHashSet(self, arr, k):
        s = set(arr)

        for itr in s:
            if k == 1:
                print(itr)  # itr is the Kth element in the set
                break
            k -= 1

    def kthMinMaxHashMap(self, mp, k):
        freq = 0
        for it in sorted(mp.keys()):
            freq += mp[it]  # adding the frequencies of
            # each element
            if freq >= k:  # if at any point frequency becomes
                return it  # greater than or equal to k then
                # return that element
        return -1  # returning -1 if k>size of the array which
        # is an impossible scenario

"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/sliding-window-maximum/


Brute Force Solution:
-----------------------------------------------
@description:
Run a nested loop:
    The outer loop will mark the starting point of the subarray of length K
    The inner loop will run from the starting index to index + K
        Print the maximum element among these K elements

@complexity:
Time:   O(n * k), the outer loop runs n-k+1 times and the inner loop runs k times for every iteration of the outer loop
                  so time complexity is O((n-k+1)*k) which can also be written as O(n * k)
Space:  O(1), no auxiliary space required


Deque Solution:
-----------------------------------------------
@description:
Create a Deque, dq of capacity k, that stores only useful elements of current window of k elements
An element is useful if
- it is in current window
- is greater than all other elements on right side of it in current window
Process all array elements one by one and maintain dq to contain useful elements of current window
These useful elements are maintained in sorted order
The element at front of the dq is the largest of current window
The element at rear/back of dq is the smallest of current window


[1, 2, 3, 4], k = 3
[       ]     -> 3
   [       ]  -> 4
We don't care about the [1, 2] after the first maximum

[1, 1, 1, 1, 1, 4, 5  ...], k = 6
[               ]
   [               ]
      [               ]
        [               ]

What if we use a deque that is always decreasing?

[1, 1, 1, 1, 1]

4 > topdeque = 1 => pop
                 => output 4
                 => push 4 to deque
[4]

5 > topdeque = 4 => pop
                 => output 5
                 => push 5 to deque
[5]

Deque stores index of the maximum element at the front and minimum element at the back
At any time it stores indexes which belong to current window

[1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
window: [1, 2, 3]
deque: {2}
maxelem: nums[2] = 3

window: [2, 3, 1]
deque: {2, 3}
maxelem: nums[2] = 3

window: [3, 1, 4]
deque: {4}
maxelem: nums[4] = 4

window: [1, 4, 5]
deque: {5}
maxelem: nums[5] = 5

window: [4, 5, 2]
deque: {5, 6}
maxelem: nums[5] = 5

window: [5, 2, 3]
deque: {5, 7}
maxelem: nums[5] = 5

window: [2, 3, 6]
deque: {8}
maxelem: nums[8] = 6

Create a deque to store k elements
Run a loop and insert the first k elements in the deque
Before inserting the element, check if the element at the back of the queue is smaller than the current element
If it is so remove the element from the back of the deque
until all elements left in the deque are greater than the current element
Then insert the current element, at the back of the deque
Now, run a loop from k to the end of the array.
Append the front element of the deque to the result
Remove the element from the front of the queue if they are out of the current window
Insert the next element in the deque
Before inserting the element, check if the element at the back of the queue is smaller than the current element
If it is so remove the element from the back of the deque
until all elements left in the deque are greater than the current element
Then insert the current element, at the back of the deque
Append the front element of the deque to the result

Monotonic decreasing Queue
Queue not Stack because we want to add/remove elements from beginning and end in O(1)

[8, 7, 6, 9], k = 2
[8, 7]
deque: 8, 7
res: 8
    [7, 6]
pop()
deque: 7 6
res: 8, 7
       [6, 9]
pop()
deque: 6
pop()
deque:
push(9)
deque: 9
res: 8, 7, 9

@complexity:
Time: O(n),  it seems more than O(n) at first look - it can be observed that every element of the array is added
             and removed at most once, so there are total of 2*n operations
Space: O(k), elements stored in the dequeue take O(k) space


Two Heap / AVL Tree Solution:
-----------------------------------------------
@description:
To reduce that time is to use an AVL tree which returns the maximum element in (log n) time.
So, traverse through the array and keep k elements in the BST and print the maximum in every iteration.
AVL tree is a suitable data structure as lookup, insertion, and deletion all take O(log n) time
in both the average and worst cases, where n is the number of nodes in the tree prior to the operation.

- Create a Self-balancing BST (AVL tree) to store and find the maximum element
- Traverse through the array from start to end
- Insert the element in the AVL tree
- If the loop counter is greater than or equal to k then delete i-kth element from the BST
- Append the maximum element of the BST


Instead of using the AVL tree, we could also use.
The elements of the current window will be stored in the Max-Heap
and the maximum element or the root will be printed in each iteration.

- Pick first K elements and create a Max-Heap of size K
- Perform heapify and print the root element
- Store the next and last element from the array
- Run a loop from k – 1 to n
    - Replace the value of the element which has got out of the window with a new element which came inside the window.
    - Perform heapify
    - Print the root of the Heap

@complexity:
Time: O(n * log n), insertion, deletion and search takes log k time in a AVL tree/Heap
                    so the overall time complexity is O(n * log k)
Space: O(k), elements stored in the BST/Heap take O(k) space
"""
import collections


class Solution:
    def maxSlidingWindowBruteForce(self, nums, k):
        res = []
        for i in range(len(nums) - k + 1):
            maxx = nums[i]
            for j in range(1, k):
                if nums[i + j] > maxx:
                    maxx = nums[i + j]
            res.append(max)
        return res

    def maxSlidingWindowDeque(self, nums, k):
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res

    def maxSlidingWindowAVL(self, nums, k):
        # creating the max heap, to get max element always
        queue = []

        res = []
        i = 0

        while i < k:
            queue.append(nums[i])
            i += 1

        queue.sort(reverse=True)

        # adding the maximum element among first k elements
        res.append(queue[0])

        # removing the first element of the array
        queue.remove(nums[0])

        # iterating for the next elements
        while i < len(nums):
            # adding the new element in the window
            queue.append(nums[i])
            queue.sort(reverse=True)

            # finding & adding the max element in the
            # current sliding window
            res.append(queue[0])

            # finally removing the first element from front end of queue
            queue.remove(nums[i - k + 1])
            i += 1
        return res

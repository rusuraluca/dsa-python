"""
You have a web server that keeps crashing each day.
You suspect it begins failing after a certain number of requests are served.
Luckily, you have the daily request logs for the server.
You see that it returns a status code of 200, but at some point it begins returning 500s instead:

200, 200, 200, ... 200, 500, 500, 500
In order to find the breaking point, let's write a function find_first(array, num)
that returns the index at which the number num first appears in the input array.
In this case, we want to efficiently find the first 500 in our server log.

Input:
an array of numbers, a number to find

Output:
the index of the array at which num first appears, or -1 if it does not

Examples
input = [200, 200, 200, 200, 500, 500, 500]
find_first(input, 200) # => 0
find_first(input, 500) # => 4
find_first(input, 100) # => -1


arr = [200, 200, 200, 200, 500, 500, 500]
indexes: 0    1    2    3    4    5    6

st = 0
en = 6

arr[0] = 200
arr[6] = 500

arr[0] < arr[6] (200 < 500)

mid = (0 + 6)/2 = 3 => arr[mid] = arr[3] = 200
arr[3] < arr[6]
    st = 3

arr[3] < arr[6]
mid = (3 + 6)/2 = 4 => arr[mid] = arr[4] = 500 - what we want


On the surface, this question seems rather straightforward.
We can find the answer in O(n) time simply by iterating over the input array until we find num.
But you should ask yourself: Can we find a more efficient approach? You bet we can!

Whenever you're given a problem statement like this,
try to discern what information in the question is most relevant to the solution.
The key to unlocking this problem is realizing that we're given an input array that is already sorted.
We know this because the statuses start at 200 and then change to 500.
(Note: In real life, you should verify assumptions like these with your interviewer
before proceeding down the rabbit hole)

- > Binary Search on input array
- > Time Complexity: O(logn), where n is the number of elements in the given array
- > Space Complexity: O(1)

Binary search is a great place to start since it works in O(log n) time for sorted arrays,
but we need to make some tweaks in order to find the first occurrence of num.
Remember, binary search normally stops when it finds any element that matches the search condition.

Here are two Solutions we could use to solve this problem:

When we find a 500, explore each element to the left until we hit a 200.
When we find a 500, keep performing binary search on the left subtree until we can't find another 500.
Solution #1 seems like a reasonable idea, but #2 has much better worst-case performance.
To see why, imagine our entire input was 500s;
with Solution #1, we end up iterating over half of the list once we find the first 500, which is still O(N).
In general, we should try to optimize this worst-case performance, so we'll go with Solution #2.
"""


def number_finder(array, num):
    start = 0
    end = len(array) - 1
    idx = -1

    while start < end:
        mid = int(start + (end - start) / 2)

        if array[mid] == num:
            # Save the index but keep searching left side
            idx = mid
            end = mid
            continue

        elif array[mid] > num:
            # Search left side
            end = mid
            continue

        elif array[mid] < num:
            # Search right side
            start = mid + 1
            continue

    return idx


print(number_finder([200, 200, 200, 200, 200, 500, 500, 500, 500, 500, 500, 500, 500], 500))

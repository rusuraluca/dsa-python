"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/find-the-duplicate-number

Proving that at least one duplicate must exist in the array
is an application of the pigeonhole principle.
Here, each number in array is a "pigeon"
and each distinct number that can appear in array is a "pigeonhole."
Because there are n+1 numbers and n distinct possible numbers,
the pigeonhole principle implies that if you were to put each of the n+1 pigeons into n pigeonholes,
at least one of the pigeonholes would have 2 or more pigeons.


Sorting Solution:
-----------------------------------------------
@description:
In an unsorted array, duplicate elements may be scattered across the array.
However, in a sorted array, duplicate numbers will be next to each other.

@pseudocode:
1.  Sort the input array.
2.  Iterate through the array, comparing the current number to the previous number
(i.e. compare arr[i] to arr[i-1] where i > 0).
3.  Return the first number that is equal to its predecessor.

@complexity:
Time:   O(n log n), n is the number of elements in the array
Space:  O(n), in Python, the sort() function is implemented using the Timsort algorithm,
        which has a worst-case space complexity of O(n)



Hash Set Solution:
-----------------------------------------------
@description:
As we traverse the array, we need a way to "remember" values that we've seen.
If we come across a number that we've seen before, we've found the duplicate.
An efficient way to record the seen values is by adding each number to a set
as we iterate over the array.

@pseudocode:
1.  In order to achieve linear time complexity,
    we need to be able to insert elements into a data structure
    and look them up in constant time.
    A HashSet/unordered_set is well suited for this purpose.
    Initialize an empty hashset, seen.
2.  Iterate over the array and first check if the current element exists in the hashset (seen).
    If it does exist in the hashset, that number is the duplicate and can be returned right away.
3.  Otherwise, insert the current element into seen,
    move to the next element in the array and repeat step 2

@complexity:
Time:   O(n), n is the number of elements in the array
Space:  O(n), for the hash set


Fast & Slow Pointer Solution:
-----------------------------------------------
@description:
Floyd's algorithm consists of two phases and uses two pointers, usually called tortoise[slow] and hare[fast].
In phase 1,
hare = nums[nums[hare]] is twice as fast as tortoise = nums[tortoise].
Since the hare goes fast,
it would be the first to enter the cycle and run around the cycle.
At some point, the tortoise enters the cycle as well,
and since it's moving slower
the hare catches up to the tortoise at some intersection point.
Now phase 1 is over, and the tortoise has lost.


Note that the intersection point is not the cycle entrance in the general case.
To compute the intersection point,
let's note that the hare has traversed twice as many nodes as the tortoise,
2d(tortoise)=d(hare), implying:

2(F+a)=F+nC+a, where n is some integer.

Hence the coordinate of the intersection point is F + a = nC.

In phase 2, we give the tortoise a second chance by slowing down the hare,
so that it now moves at the speed of tortoise:
    tortoise = nums[tortoise],
    hare = nums[hare].
The tortoise is back at the starting position, and the hare starts from the intersection point.
Let's show that this time they meet at the cycle entrance after F steps.
    The tortoise started at zero, so its position after F steps is F.
    The hare started at the intersection point F + a = nC,
    so its position after F steps is nC + F, that is the same point as F.
    So the tortoise and the (slowed down) hare will meet at the entrance of the cycle.

First of all, when traversing the array described in the problem by always using the current value
as the next index to go to, there must be a loop.
Let's say C is the length of the loop,
which is smaller than the size of the array, aka C < n + 1.
Before entering the loop, there are K steps to get from nums[0] to the beginning of the loop.
Apparently, K is also smaller than the size of the array, aka K < n + 1.

Now let's see what's happening during the first loop.
When Tortoise/Slow first reached the beginning of the loop, it moved K times;
Meanwhile, Hare/Fast moved K times past the beginning of the loop,
and is now somewhere in the loop.
We could take note of Fast's current distance from the beginning of the loop, which is (K % C).
At this point, how many moves it would take for Fast to catch up with Slow within the loop?
It would surely take less than C moves.
In fact, with each move, Fast would shorten the gap of the two by one.
We know Fast is (K % C) steps ahead of the start point of the loop,
so the gap between the two is (C - (K % C)).
This is to say, When Fast catches Slow, aka the first loop exits,
Slow has moved (C - (K % C)) steps past the beginning of the loop.

Time complexity of the first loop:
Slow moved K times before the loop, and then less than one loop to be caught up. O(K + C) = O(n).

And then we move to the second loop.
Slow's position remains the same while Fast is reset to nums[0].
Also Fast now moves at the same speed as Slow does.
If Fast and Slow were to meet, they should meet at the beginning of the loop.
Now would they? Let's take a look.
It would take Fast K moves to get to the beginning of the loop.
Where would Slow be after K moves? It would be (C - (K % C) + K) steps past the beginning of the loop.
Where the hell is that?
Let's mod it with C: (C - (K % C) + K) % C = (C % C) - ((K % C) % C) + (K % C) = 0 - (K % C) + (K % C) = 0.
So yes, after K moves, Slow is also at the beginning of the loop.
Thus, it would take exactly K moves to exit the second loop, and we found the beginning of the loop.

Time complexity of the second loop: O(K) = O(n).

Overall, time complexity of the solution is O(n).


@complexity:
Time:   O(n), n is the number of elements in the array
Space:  O(1)
"""


class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

    def findDuplicate(self, nums) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate(self, nums) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
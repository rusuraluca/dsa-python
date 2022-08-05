"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/majority-element/solution/


Brute Force Solution:
-----------------------------------------------
@description:
We can exhaust the search space in quadratic time
by checking whether each element is the majority element.
The brute force algorithm iterates over the array,
and then iterates again for each number to count its occurrences.
As soon as a number is found to have appeared more than any other can possibly have appeared,
return it.

@complexity:
Time:   O(n^2), traverse twice the n elements of the array, adding up to quadratic time complexity
Space:  O(1), no auxiliary space required


HashMap Solution:
-----------------------------------------------
@description:
We know that the majority element occurs more than [n/2] times,
and a HashMap allows us to count element occurrences efficiently.
We can use a HashMap that maps elements to counts in order to count occurrences in linear time by looping over nums. Then, we simply return the key with maximum value.

@complexity:
Time:   O(n^2), traverse once the n elements of the array
                and make a constant time HashMap insertion on each iteration,
                therefore, the algorithm runs in linear time.

Space:  O(n), at most, the HashMap can contain n - [n/2] associations, so O(n) space
              this is because an arbitrary array of length n can contain n distinct values,
              but nums is guaranteed to contain a majority element, which will occupy (at minimum) [n/2] + 1 array indices
              therefore, n -  [n/2] + 1 indices can be occupied by distinct, non-majority elements
              (plus 1 for the majority element itself), leaving us with (at most) n - [n/2] distinct elements.


Sorting Solution:
-----------------------------------------------
@description:
If the elements are sorted in monotonically increasing (or decreasing) order,
the majority element can be found at index [n/2] and also at [n/2]-1 if n is even.

For this algorithm, we simply do exactly what is described:
sort nums, and return the element in question.

@complexity:
Time:   O(nlogn), sorting the array costs O(nlgn) time in Python
Space:  O(1) or O(n), we sorted nums in place
                      if that is not allowed,
                      then we must spend linear additional space on a copy of nums and sort the copy instead


Boyer-Moore Voting Algorithm
-----------------------------------------------
@complexity:
Time:   O(n), traverse once the n elements in the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def majorityElement(self, nums) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

    def majorityElement(self, nums) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        return max(counts.keys(), key=counts.get)

    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[len(nums) // 2]

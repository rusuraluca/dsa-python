"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/third-maximum-number/

Foolproof:
-----------------------------------------------
Are the elements sorted?
# No
Elements are distinct?
# Yes
So we can have duplicates.
If the array is empty, what should it return?
# -1
Elements are only positive or also negative?
# Both


Base case:
-----------------------------------------------
When the array/list is empty
       => return -1
When the array/list has only three elements
      => if all of them are equal => return one's value
      => otherwise                => return the minimum of the 3


Sorting and Mapping Solution
-----------------------------------------------
@description:
Transform the array into a map to remove redundancy
Sort the array/list ascending or descending order
Loop once through the elements from beginning/end until we find the third distinct number

@complexity:
Time:  O(n*log(n)), using a good sorting algorithm
Space: O(1), but depends on the sorting algorithm
             can be O(n) with MergeSort for example


Shifting Search
-----------------------------------------------
@description:
Keep three vars to keep the first three largest numbers
Loop once through the elements
    If the current element is bigger than our first element var
           => m3 = m2
           => m2 = m1
           => m1 = current
    If the current element is smaller than our first element var but it is bigger than our second
           => m3 = m2
           => m2 = current
    If the current element is smaller than our first and second element var but it is bigger than our third
           => m3 = current
Return the m3 var

@complexity:
Time:  O(n), n is the number of numbers in nums
Space: O(1)
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) < 3:
            return max(nums)

        if len(nums) == 3:
            if nums[0] == nums[1] and nums[0] == nums[2]:
                return nums[0]

        m1, m2, m3 = None, None, None

        for num in nums:
            # no equal maximums allowed
            if num == m1 or num == m2 or num == m3:
                continue

            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num

            elif num > m2:
                m3 = m2
                m2 = num

            elif num > m3:
                m3 = num

        if m3 == None:
            return max(m1, m2)

        else:
            return m3


class Tests:
    def __init__(self):
        s = Solution()
        assert s.thirdMax([3, 2, 1]) == 1
        assert s.thirdMax([1, 2]) == 2
        assert s.thirdMax([2, 2, 3, 1]) == 1


t = Tests()

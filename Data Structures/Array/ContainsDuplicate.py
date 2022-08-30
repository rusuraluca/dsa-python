"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/contains-duplicate/


Naive Solution:
-----------------------------------------------
@description:
If array is empty => return false
Create a frequency array for the numbers
Traverse through the array
    If the frequency of a number becomes > 1 => return true
    Otherwise continue

@complexity:
Time: O(n), we traverse once the n elements of the array
Space: O(n), for the frequency array


Sorting Solution:
-----------------------------------------------
@description:
If array is empty => return false
Sort the array
Loop through the sorted array
    If the element at a position i is equal to the element at a position i+1
        => return true
    Otherwise => return false

@complexity:
Time: O(nlog(n)), for sorting - say we use quick sort
Space: O(1), no auxiliary space required


HashTable Solution:
-----------------------------------------------
@description:
If array is empty => return false
Create a hash table with the numbers of the array
    If the length of the set is different to the len of the array => return true
Otherwise => return false
or
Loop through elements in array
    If the elem is in the hash => return true
    Add element in tha hash table
Otherwise => return false

[easy python: return len(num) != len(set(num))]

@complexity:
Time: O(n), we traverse once the n elements of the array
Space: O(n), for the hash table
"""


class Solution(object):
    def containsDuplicate(self, nums):
        # first-exit case
        if len(nums) == 0:
            return False

        hash_set = set()

        # loop through numbers in array
        for num in nums:
            # check for appearance
            if num in hash_set:
                return True
            hash_set.add(num)

        return False

    def containsDuplicateSorting(self, nums):
        # first-exit case
        if len(nums) == 0: return False

        # sort the array
        nums.sort()

        # loop through numbers in array
        for i in range(len(nums) - 1):
            # check for appearance
            if nums[i] == nums[i + 1]:
                return True

        return False
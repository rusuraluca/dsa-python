"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/binary-search/


Naive solution:
-----------------------------------------------
@description:
search for the target by passing once through the elements
       until we find it,
       or until we reach the end of the list
return: target position, if element in the list
        -1             , otherwise

@pseudocode:
loop through the elements index-increasingly
    if current element is equal to target
        => element in the list
        => return position
    otherwise
        => continue looping
    if we reached the last element and we didn't find the element
        => elemnt not in the list
        => return -1

@complexity:
Time:  O(n), loop through all the n elements once
Space: O(1), no auxiliary space required


Binary Search Solution:
-----------------------------------------------
@description:
since the input is sorted, we can use binary search

@pseudocode:
    1. retrieve the midpoint and the middle element of the list
        a. if it is equal to target => return position
        b. if it is bigger then the target => no reason to go in the right side => we repeat the search with the first half of the list
        c. if it is smaller then the target => no reason to go in the left side =>     we repeat the search with the second half of the list

@complexity:
Time:  O(log(n)), where n is the number of elements in the list
                  because we divide by two the number of operations we do => n=2^k => k=log(n)
Space: O(1), no auxiliary space required

"""


class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] == target:
            return 0

        lo = 0
        hi = len(nums) - 1
        mid = 0

        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                hi = mid - 1

            else:
                lo = mid + 1

        return -1


class Tests:
    def __init__(self):
        s = Solution()
        assert s.search([-1,0,3,5,9,12], 9) == 4
        assert s.search([-1,0,3,5,9,12], 2) == -1


t = Tests()

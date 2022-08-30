"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/remove-duplicates-from-sorted-array/


Solution:
-----------------------------------------------
@description:
nums = [0,0,1,1,1,2,2,3,3,4]

0   0   1   1   1   2   2
p1 p2
0   0   1   1   1   2   2
p1      p2
0   0   1   1   1   2   2
        p1  p2
0   0   1   1   1   2   2
        p1     p2
0   0   1   1   1   2   2
                    p1  p2
0   0   1   1   1   2   2
                    p1  p2

x = 1
nums[x] = 1
x = 2
nums[x] = 2

@complexity:
Time:  O(n), we traverse once the n elements of the array
Space: O(1), no auxiliary space required
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        x = 1
        for i in range(len(nums)):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
        return x

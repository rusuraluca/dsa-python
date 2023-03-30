"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/k-diff-pairs-in-an-array/


HashTable Solution:
-----------------------------------------------
@complexity:
Time:   O(nlogn)
Space:  O(n)


Fast & Slow Pointers Solution:
-----------------------------------------------
@complexity:
Time:   O(nlogn)
Space:  O(1)
"""


class Solution:
    def findPairs(self, nums, k):
        nums.sort()
        dic = {}
        s = 0
        res = []
        for n in nums:
            if dic.get(n, None) is not None:
                res.append(n)
            dict[n+k] = n

        res = list(set(res))

        return len(res)

    def findPairs(self, nums, k):
        count = 0
        nums.sort()

        slow = 0
        fast = 1
        size = len(nums)

        while fast < size:
            # case 1, diff is less than k
            if nums[fast] - nums[slow] < k:
                fast += 1
            # case 2, diff is greater than k
            elif nums[fast] - nums[slow] > k:
                slow += 1
            # case 3, diff is equal to k so increment the count!
            else:
                count += 1
                fast += 1
                slow += 1

                # now ignore any duplicates, both slow and fast could be pointing to duplicates
                while slow < size - 1 and nums[slow] == nums[slow - 1]:
                    slow += 1

                while fast < size - 1 and nums[fast] == nums[fast - 1]:
                    fast += 1

            # fast should be at least one more than slow
            if fast <= slow:
                fast = slow + (slow - fast) + 1

        return count



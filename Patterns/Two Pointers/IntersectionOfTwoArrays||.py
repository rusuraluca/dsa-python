"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/intersection-of-two-arrays-ii/


HashMap Solution:
-----------------------------------------------
@description:
Use a hashmap to record all nums appeared in the first list,
then check if there are nums in the second list have appeared in the hashmap.

@complexity:
Time:   O(max(len(s),len(t)))
Space:  O(s), where s=len(nums1), t=len(nums2).


Two Pointers Solution:
-----------------------------------------------
@description:
Sort the two list,
use two pointer to search in the lists to find common elements.

@complexity:
Time:   O(n)
Space:  O(1)
"""


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        cnt = {}
        for nums in nums1:
            if nums not in cnt:
                cnt[nums] = 1
            else:
                cnt[nums] += 1

        ans = []
        for x in nums2:
            if x in cnt and cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1

        return ans


class Solution:
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res

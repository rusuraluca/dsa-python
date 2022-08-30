"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/intersection-of-two-arrays-ii/


Sort then Two Pointers Solution:
-----------------------------------------------
@description:
Consider a new array with the result
Sort the 2 arrays
Using two poniters add the elements in increasing order in the new array

@complexity:
Time:   O(nlogn+mlogm), where n and m are arrays' lengths
Space:  O(sorting) or O(m+n) if counting output as space


HashMap Solution:
-----------------------------------------------
@description:
Using HashMap to store occurrences of elements in the nums1 array.
Iterate x in nums2 array, check if cnt[x] > 0 then append x to our answer and decrease cnt[x] by one.
To optimize the space, we ensure len(nums1) <= len(nums2) by swapping nums1 with nums2 if len(nums1) > len(nums2).

@complexity:
Time:  O(n+m), where n and m are arrays' lengths
Space: O(min(m, n))
"""


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        # or use Counter
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

    def intersectSort(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

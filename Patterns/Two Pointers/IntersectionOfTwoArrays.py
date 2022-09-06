"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/intersection-of-two-arrays


Python Solution:
-----------------------------------------------
@description:
Use set operation in python, one-line solution.

@complexity:
Time:   O(len(s)*len(t))
Space:  O(1)


Brute-Force Solution:
-----------------------------------------------
@description:
Search each element of the first list in the second list.
To be more efficient, sort the second list and use binary search to accelerate.

@complexity:
Time:   O(len(s)*len(t))
Space:  O(s), where s=len(nums1), t=len(nums2)


HashTable Solution:
-----------------------------------------------
@description:
Use a hashtable to record all nums appeared in the first list,
then check if there are nums in the second list have appeared in the hashtable.

@complexity:
Time:   O(len(s)+len(t))
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
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)

        return res


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        hash_map = {}
        for i in nums1:
            hash_map[i] = hash_map[i] + 1 if i in hash_map else 1
        for j in nums2:
            if j in hash_map and hash_map[j] > 0:
                res.append(j)
                hash_map[j] -= 1

        return res


class Solution:
    def intersection(self, nums1, nums2):
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
                if not (len(res) and nums1[i] == res[len(res) - 1]):
                    res.append(nums1[i])
                i += 1
                j += 1

        return res


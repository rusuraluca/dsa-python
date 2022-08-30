"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/intersection-of-two-arrays/


Two Sets Solution:
-----------------------------------------------
@description:
The naive approach would be to iterate along the first array nums1
and to check for each value if this value in nums2 or not. If yes - add the value to output.
Such an approach would result in a pretty bad O(n*m) time complexity, where n and m are arrays' lengths.

* To solve the problem in linear time, let's use the structure set,
which provides in and contains operation in O(1) time in average case.

The idea is to convert both arrays into sets,
and then iterate over the smallest set checking the presence of each element in the larger set.

@complexity:
Time:   O(n+m)  , where n and m are arrays' lengths
                , O(n) time is used to convert nums1 into set
                , O(m) time is used to convert nums2
                , contains/in operations are O(1) in the average case

Space:  O(m+n)  ,i n the worst case when all elements in the arrays are different


Built-in Solution:
-----------------------------------------------
@description:
There are built-in intersection facilities, which provide O(n+m) time complexity in the average case
and O(n*m) time complexity in the worst case.
In Python it's intersection operator.

@complexity:
Time:  O(n+m) in the average case and O(n*m) in the worst case when load factor is high enough
Space: O(n+m),  in the worst case when all elements in the arrays are different
"""


class Solution:
    def setIntersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.setIntersection(set1, set2)
        else:
            return self.setIntersection(set2, set1)

    def intersectionBuiltIn(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

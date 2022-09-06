"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/minimum-index-sum-of-two-lists/


HashMap Solution:
-----------------------------------------------
@description:
1. Create the hashmap by iterating through list1
2. Create an infinite number we can update every time we see a smaller index sum
3. Iterates through list2 and does the following (if the current item is in the hashmap):
        4. Creates a "sum" containing the index sum of the 2 items (the common item in both lists)
        5. If the "sum" is less than the current minimum sum:
           - update the minimum sum to this
           - add the common item to the result list
        6. If the "sum" is equal to the current minimum sum:
           - this is the edge case
             "If there is a choice tie between answers, output all of them with no order requirement"
             just add the item to the result list

@complexity:
Time:   O(l1+l2), where l1 and l2 are the lengths of list1 and list2 respectively
Space:  O(l1 * x), where l1 is length of the maximum size word, x is the length of the resultant list
"""


class Solution:
    def findRestaurant(self, list1, list2):
        hashmap = {}
        for i in range(len(list1)):  # step 1
            hashmap[list1[i]] = i

        res = []

        minsum = float("inf")  # step 2

        for j in range(len(list2)):  # step 3
            if list2[j] in hashmap:
                cursum = j + hashmap[list2[j]]  # step 3a

                if cursum < minsum:  # step 3b
                    minsum = cursum
                    res = []
                    res.append(list2[j])
                elif cursum == minsum:  # step 3c
                    res.append(list2[j])
        return res

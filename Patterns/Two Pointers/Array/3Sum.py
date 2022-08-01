"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/3sum/

Naive Solution:
-----------------------------------------------
@description:
Traverse the input 3 times and check for all the 0 sums.
Generate all possible triplets and compare the sum of every triplet with the given value (=0)

@complexity:
Time:  O(n^3), n is the number of elements in the given list
Space: O(1),   no auxiliary space required


Two Pointers Solution:
-----------------------------------------------
@description:
We essentially need to find three numbers x, y, and z such that they add up to the given value
If we fix one of the numbers say x, we are left with the two-sum problem at hand

@pseudocode:
- sort the given array
- loop over the array and fix the first element of the possible triplet, arr[i]
    - then fix two pointers, one at i + 1 and the other at n – 1
    - look at the sum
        - if the sum is smaller than the required sum, increment the first pointer
        - else if the sum is bigger, decrease the end pointer to reduce the sum
        - else, if the sum of elements at two-pointer is equal to given sum, consider the triplet and continue

@complexity:
Time:  O(n^2), we traverse twice the n elements of the array
Space: O(1),   no auxiliary space needed


Hashing Solution:
-----------------------------------------------
@description:
This approach uses extra space but is simpler than the two-pointers approach.
Run two loops outer loop from start to end and inner loop from i+1 to end.
Create a hashmap or set to store the elements in between i+1 to j-1.
So if the given sum is x, check if there is a number in the set which is equal to x – arr[i] – arr[j].
If yes print the triplet.

@pseudocode:
- traverse the array from start to end (loop counter i)
    - create a HashMap or set to store unique pairs
    - another loop from i+1 to end of the array (loop counter j)
        - if there is an element in the HashMap/set which is equal to x - arr[i] – arr[j],
          then triplet (arr[i], arr[j], x-arr[i]-arr[j]) is valid
        - insert the jth element in the set

@complexity:
Time:  O(n^2), we traverse twice the n elements of the array
Space: O(n),   we need extra space for the HashMap
"""


class Solution:
    def threeSumTwoPointers(self, arr):
        arr.sort()
        sol = []
        for l in range(0, len(arr) - 2):
            if l > 0 and arr[l - 1] == arr[l]:
                continue

            m = l + 1
            r = len(arr) - 1

            while m < r:
                potential = arr[l] + arr[m] + arr[r]
                if potential > 0:
                    r -= 1
                elif potential < 0:
                    m += 1
                else:
                    sol.append([arr[l], arr[m], arr[r]])
                    while m < r and arr[m] == arr[m + 1]:
                        m += 1
                    while m < r and arr[r - 1] == arr[r]:
                        r -= 1
                    m += 1
                    r -= 1
        return sol

    def threeSumHashing(self, arr):
        arr.sort()
        sol, dic = [], {}

        for i, k in enumerate(arr):
            if k not in dic:
                dic[k] = [i]
            else:
                dic[k].append(i)

        for i in range(len(arr)):
            # avoid duplicates
            if i == 0 or arr[i] != arr[i-1]:

                for j in range(i+1, len(arr)):
                    # avoid duplicates
                    if j == i+1 or arr[j] != arr[j-1]:

                        t = 0 - arr[i] - arr[j]
                        if t in dic and max(dic[t]) > j:
                            sol.append([arr[i], arr[j], t])

        return sol


s = Solution()
assert s.threeSumTwoPointers([0, 1, 1]) == []
assert s.threeSumTwoPointers([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

assert s.threeSumHashing([0, 1, 1]) == []
assert s.threeSumHashing([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

assert s.threeSumHashing2([0, 1, 1]) == []
assert s.threeSumHashing2([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]

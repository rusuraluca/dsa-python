"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/two-sum/


Naive Solution:
-----------------------------------------------
traverse the input 2 times and check for target

nums = [2,7,11,15]
target = 9

2
[7, 11, 15]
- we reach target sum with 7 -> [0, 1]

nums = [2,7,11,15]
target = 18
2
[7, 11, 15]
- we don't find target

7
[11, 15]
- we reach target sum with 11 -> [1, 2]

@complexity:
Time:  O(n^2), n is the number of elements in the given list
Space: O(1), no auxiliary space needed


Sort & Two Pointers Solution:
-----------------------------------------------
@description:
this is good only if we need to return the elements, not the indexes because after sorting the indexes may change
sort the input list in ascending order, and use two pointers to find the pair in the array
inspired by binary search

nums = [2,7,15,11]
target = 9

after sorting:
nums = [2,7,11,15]
target = 9

two pointers:
[2,7,11,15]
l       r
l + r = 17 > target => r-=1

[2,7,11,15]
l    r
l + r = 13 > target => r-=1

[2,7,11,15]
l  r
l + r = 9 == target => return [l, r]

@complexity:
Time:   O(n*log(n))         , where n is the length of the input array
Space:  O(log(n)) or O(n)   , depending on the sort algorithm


One Pass Hash Table Solution:
-----------------------------------------------
@description:
nums = [2,7,11,15]
target = 9

currentelem = 2
potentialelem = 9-2 = 7
is potentialelem in the hash table? no -> add 2 to hashtable


currentelem = 7
potentialelem = 9-7 = 2
is potentialelem in the hash table? yes -> return [2, 7] or [0, 1]

nums = [2,7,11,15]
target = 13

currentelem = 2
potentialelem = 13-2 = 11
is potentialelem in the hash table? no -> add 2 to hashtable
hash_table = {
              2: 0
                   }
currentelem = 7
potentialelem = 13-7 = 6
is potentialelem in the hash table? no -> add 7 to hashtable
hash_table = {
              2: 0
              7: 1
                   }

currentelem = 11
potentialelem = 13-11 = 2
is potentialelem in the hash table? yes -> return [hashtable[2], currentelem_idx]


If we don't need to check if the complement is the current number itself
or if we just need to return the complements, not their indexes
it is not necessary to store each number's index as value in the hash table.


@pseudocode:
- let hashtable be a hashtable
- traverse the input array
    - potentialelem = target - curentelem
    - if potentialelem in the hashtable:
        return [ hashtable[potentialelem] and the currentelem_index]
    - else
        hashtable[curentelem] = currentelem_index

- return []

@complexity:
Time:   O(n)    , where n is the length of the input array
                , we traverse the list only once
                , each lookup in the table costs only O(1) time
Space:  O(n)    , the extra space required depends on the number of items stored in the hash table,
                  which stores at most n elements
"""

class Solution:
    def twoSum2(self, arr, target):
        arr.sort()
        l = 0
        r = len(arr) - 1

        while l < r:
            current = arr[l] + arr[r]
            if current == target:
                return [arr[l], arr[r]]
            elif current > target:
                r -= 1
            else:
                l += 1

        return []

    def twoSum3(self, arr, target):
        hashtable = {}

        for current_id, current in enumerate(arr):
            potential = target - current
            if potential in hashtable:
                return [hashtable[potential], current_id]
            else:
                hashtable[current] = current_id

        return []


s = Solution()

assert s.twoSum2([2, 7, 11, 15], 9) == [2, 7]
assert s.twoSum2([2, 7, 11, 15], 17) == [2, 15]
assert s.twoSum2([2, 7], 17) == []

assert s.twoSum3([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum3([2, 7, 11, 15], 17) == [0, 3]
assert s.twoSum3([2, 7], 17) == []





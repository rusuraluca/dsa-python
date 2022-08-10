"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/single-number/


Hash Map Solution:
-----------------------------------------------
@description:
Create a dictionary of each number's frequency.
Check which element in the dictionary has the frequency 1 and return it.
@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(n), keep n/2+1 => n elements in the dictionary 

XOR Solution:
-----------------------------------------------
@description:
Well we know that

if we take XOR of zero and some bit, it will return that bit
a XOR 0 = a
0 XOR a = a

if we take XOR of two same bits, it will return 0
a XOR a = 0 
a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b 
a  ⊕  b  ⊕  a = (a  ⊕  a)  ⊕  b = 0  ⊕  b = b

So we can XOR all bits together to find the unique number.

nums = [2,2,1]
a = 0
n = 2
a ^ n = 2

a = 2
n = 2
a ^ n = 0

a = 0
n = 1
a ^ n = 1

@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(1), no auxiliary space required


Sum Set Difference Solution:
-----------------------------------------------
@description:
The missing element is the difference between 2 times the sum of the set formed by the unique nums in the array and the sum of the nums in the array.

@complexity:
Time:   O(n), we traverse once the n numbers in the array
Space:  O(n), keep n/2+1 => n elements in the set 

"""


class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a

    def singleNumberSumSetDifference(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumberHashMap(self, nums) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1

        for key, val in dic.items():
            if val == 1:
                return key

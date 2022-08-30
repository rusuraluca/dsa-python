"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/plus-one/


Iterative Solution:
-----------------------------------------------
@description:
Traverse the digits backwards
If the current elem is different than 9 => Add 1 => Return
Otherwise current elem becomes 0
We just have to check at the end if the first element in digits is 0 => Add 1 => Append 0
Return digits

@complexity:
Time:   O(n), where n is the number of digits in the array
Space:  O(1), no auxiliary space required


Recursive Solution:
-----------------------------------------------
@description:
We only have to worry about adding a new elements in the digits list
when the last element is 9.
So here we have two cases - if the number is only 9 => just return [1, 0]
                          - otherwise => recursively call the function for the list without the last element(slicing)
                                         + [0] to add at the end

@complexity:
Time:   O(n), where n is the number of digits in the array
Space:  O(n), for the recursive call stack
"""


class Solution:
    def plusOne(self, digits):
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)

        return digits

    def plusOneRecursive(self, digits):
        if digits[-1] == 9:
            # we only have a 9
            if len(digits) == 1:
                return [1, 0]

            return self.plusOne(digits[:-1]) + [0]

        else:
            digits[-1] += 1
        return digits

"""
Problem:
-----------------------------------------------
Given an array of size n, print the reverse of it.


Extra Space Solution:
-----------------------------------------------
@description:
We call the function to reverse an array, which iterates through every element
and intelligently join each character in the beginning of a new array
so as to obtain the reversed array.

@complexity:
Time:   O(n), where n is the number of elements in the array
Space:  O(n), output array


Two Pointers Solution:
-----------------------------------------------
Iterative
@description:
Two pointers one to the start one to the end.
Swap elements at pointers and increase pointers,
until start pointer is greater than end pointer.

@complexity:
Time:   O(n), where n is the number of elements in the array
Space:  O(1), no auxiliary space required

Recursive
@description:
Base case string is empty
Recursively slice the part of the array except the first character
Concatenate the first character to the end of the sliced array

@complexity:
Time:   O(n), where n is the number of elements in the array
Space:  O(n), for the recursive call stack
"""


class Solution:
    def reverseString(self, s) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            # swap
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        """
        for l in range(len(s)//2):
            s[l], s[-l-1] =  s[-l-1], s[l]
        """

    def reverseStringRecursive(self, string) -> None:
        if len(string) == 0:
            return string
        # slice the part of the string except the first character
        # concatenate the first character to the end of the sliced string
        return self.reverseString(string[1:]) + string[0]

    def reverseStringSlicing(self, string) -> None:
        string = string[::-1]
        return string

    def reverseStringSpace(self, string):
        new_string = ""
        for char in string:
            # add the char at the beginning
            new_string = char + new_string

        return new_string

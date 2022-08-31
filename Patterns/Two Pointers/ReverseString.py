"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/reverse-string/

Python string library doesn't support the in-built “reverse()” as done by other python containers like list,
hence knowing other methods to reverse string can prove to be useful.


Two Pointers Solution:
-----------------------------------------------
@description:
Iterative
Two pointers one to the start one to the end.
Swap elements at pointers and increase pointers,
until start pointer is greater than end pointer.

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(1), no auxiliary space required

Recursive
@description:
Base case string is empty
Recursively slice the part of the string except the first character
Concatenate the first character to the end of the sliced string

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(n), for the recursive call stack


Extended slice syntax Solution:
-----------------------------------------------
@description:
Extended slice offers to put a “step” field as [start,stop,step],
and giving no field as start and stop indicates default to 0
and string length respectively and “-1” denotes starting from end and stop at the start,
hence reversing string.

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(1), no auxiliary space required


Reversed Solution:
-----------------------------------------------
@description:
The reversed() returns the reversed iterator of the given string
and then its elements are joined empty string separated using join().
And reversed order string is formed.

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(1), no auxiliary space required


Extra Space Solution:
-----------------------------------------------
@description:
We call the function to reverse a string, which iterates through every element
and intelligently join each character in the beginning of a new string so as to obtain the reversed string.

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(n), output string
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

    def reverseRecursive(self, string) -> None:
        if len(string) == 0:
            return string
        # slice the part of the string except the first character
        # concatenate the first character to the end of the sliced string
        return self.reverseRecursive(string[1:]) + string[0]

    def reverseStack(self, string) -> None:
        # function to create an empty stack
        # initializes size of stack as 0
        def create_stack():
            stack = []
            return stack

        # function to determine the size of the stack
        def size(stack):
            return len(stack)

        # boolean function to determine if stack is empty
        def is_empty(stack):
            if size(stack) == 0:
                return True

        # function to add an item to stack
        # increases size by 1
        def push(stack, char):
            stack.append(char)

        # function to remove an item from stack
        # decreases size by 1
        def pop(stack):
            if is_empty(stack):
                return
            return stack.pop()

        n = len(string)

        stack = create_stack()

        for i in range(0, n, 1):
            push(stack, string[i])

        string = ""

        for i in range(0, n, 1):
            string = string + pop(stack)

        return string

    def reverseStringSlicing(self, string) -> None:
        string = string[::-1]
        return string

    def reverseStringBuiltIn(self, string) -> None:
        string = "".join(reversed(string))
        return string

    def reverseSpace(self, string):
        new_string = ""
        for char in string:
            # add the char at the beginning
            new_string = char + new_string

        return new_string
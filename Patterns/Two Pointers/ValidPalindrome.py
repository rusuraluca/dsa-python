"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/valid-palindrome

Note: a palindrome is a sequence of characters that reads the same forwards and backwards.


Two Pointers Solution:
-----------------------------------------------
@description:
Iterative
Initialize two pointer variables
Left and right and point them with the two ends of the input string
Traverse all elements through the loop
    Move the left pointer to right so it points to a alphanumeric character
    Similarly move right pointer to left so it also points to a alphanumeric character
    Check if both the characters are same
        If it is not equal then the string is not a valid palindrome, hence return false

    If same, then continue to next iteration
    and move both pointers to point to next alphanumeric character till left < right

After loop finishes, the string is said to be palindrome, hence return true

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(1), no auxiliary space required

@description:
Recursive
Basically same thing but recursive

@complexity:
Time:   O(n), where n is the number of characters in the string
Space:  O(n), for the recursive call stack
"""


class Solution:
    def isPalindromeTwoPointersIterative(self, s: str) -> bool:
        s = s.lower()
        a = 0
        b = len(s) - 1

        while a <= b:
            while a <= b and not s[a].isalnum():
                a += 1

            while a <= b and not s[b].isalnum():
                b -= 1

            if a <= b and s[a] != s[b]:
                return False

            a += 1
            b -= 1

        return True

    def isPalindromeTwoPointersRecursive(self, s: str) -> bool:
        def valid(a, b, s):
            if a >= b:
                return True

            while s[a].isalnum() is False:
                if a >= b:
                    return True
                a += 1
            while s[b].isalnum() is False:
                if a >= b:
                    return True
                b -= 1

            if s[a].lower() != s[b].lower():
                return False

            return valid(a + 1, b - 1, s)

        return valid(0, len(s) - 1, s)

    def isPalindromeIterative(self, s: str) -> bool:
        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")
        s = s.lower()
        size = len(s)

        for i in range(0, size // 2):
            if s[i] != s[size - i - 1]:
                return False

        return True

    def isPalindromeReversing(self, s: str) -> bool:
        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")
        s = s.lower()

        rev = ''
        for c in s:
            rev = c + rev

        return s == rev

    def isPalindromeSlicing(self, s: str) -> bool:
        for char in s:
            if char in ':., ':
                s = s.replace(char, '')

        s = s.lower()

        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.casefold() for char in s if char.isalnum()])
        return s == s[::-1]

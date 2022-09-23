"""
Problem:
-----------------------------------------------
This question is asked by Google. Given a string only containing the following characters (, ), {, }, [, and ]
return whether or not the opening and closing characters are in a valid order.
Ex: Given the following strings...
    "(){}[]", return true
    "(({[]}))", return true
    "{(})", return false


Stack Solution:
-----------------------------------------------
@complexity:
Time:   O(n)
Space:  O(n)
"""


class Solution:
    def validateCharacters(self, string):
        correspondence = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for el in string:
            if el in correspondence.keys():
                stack.append(el)
            elif stack and correspondence[stack[-1]] == el:
                stack.pop()
            else:
                return False

        return stack == []


class Tests:
    def __init__(self):
        s = Solution()
        assert (s.validateCharacters("(){}[]")) is True
        assert (s.validateCharacters("(({[]}))")) is True
        assert (s.validateCharacters("{(})")) is False
        assert (s.validateCharacters("{")) is False


t = Tests()
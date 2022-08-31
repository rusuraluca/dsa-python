"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/string-to-integer-atoi/


DFA Solution:
-----------------------------------------------
DFA, which stands for Deterministic finite automaton,
is a state machine that either accepts or rejects a sequence of symbols
by running through a state sequence uniquely determined by the string.
The DFA I used to implement this answer is very simple:


"""


class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value

    def myAtoi2(self, s: str) -> int:
        out = 0
        neg = 1

        symbols = {
            "-": -1,
            "+": 1
        }

        left = 0

        # step 1
        while left < len(s) and s[left] == " ":
            left += 1

        # step 2
        if left < len(s) and s[left] in symbols:
            neg = symbols[s[left]]
            left += 1

        # step 3
        while left < len(s) and s[left].isdigit():
            out = (out * 10) + int(s[left])
            left += 1

        # bound check
        val = out * neg
        if val >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif val <= -2 ** 31:
            return -2 ** 31

        return val

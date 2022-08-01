"""
Given a balanced expression that can contain opening and closing parenthesis,
check if it contains any duplicate parenthesis or not.

e.g.
Input:  ((x+y))+z
Output: true
Explanation: Duplicate () found in subexpression ((x+y))

Input:  (x+y)
Output: false
Explanation: No duplicate () is found

Input:  ((x+y)+((z)))
Output: true
Explanation: Duplicate () found in subexpression ((z))

Base Case:
- if the len of the expression is smaller than 3
  => expression doesn't contain duplicate parenthesis

Stack Solution:

@description:
We can use a stack to solve this problem. The idea is to traverse the given expression and
- If the current character in the expression is not a closing parenthesis ')',
  push the character into the stack.
- If the current character in the expression is a closing parenthesis ')',
  check if the top/peek element in the stack is an opening parenthesis or not.
    - If it is an opening parenthesis, then the subexpression ending at the current character is of the form ((exp));
    - Otherwise, continue popping characters from the stack till matching '(' is found for current ')'.

@pseudocode:
- check base case
- declare an empty stack
- traverse the expression
    - if current parenthesis is an open parenthesis
      => push it to the stack
    - if current parenthesis is a closed parenthesis
        - if the top/peek element of the stack is an open parenthesis, we found a duplicate parenthesis
        - otherwise, pop until the matching open parenthesis is found for current parenthesis
        - pop it form the stack
- if we reach here, then the expression does not have any duplicate parenthesis

@complexity:
Time:  O(n), we traverse once the expression
Space: O(n), for the stack
"""
from collections import deque


class Solution:
    def duplicateParenthesis(self, exp: str) -> bool:
        if not exp or len(exp) <= 3:
            return False

        # take an empty stack of characters
        stack = deque()

        # traverse the input expression
        for c in exp:
            # if the current char in the expression is not a closing parenthesis
            if c != ')':
                stack.append(c)

            # if the current char in the expression is a closing parenthesis
            else:
                # if the stack's top element is an opening parenthesis,
                # the subexpression of the form ((exp)) is found
                if stack[-1] == '(':
                    return True

                # pop till '(' is found for current ')'
                while stack[-1] != '(':
                    stack.pop()

                # pop '('
                stack.pop()

        # if we reach here, then the expression does not have any
        # duplicate parenthesis
        return False


def testDuplicateParenthesis():
    s = Solution()
    assert s.duplicateParenthesis('(x+y)') == False
    assert s.duplicateParenthesis('((x+y))') == True


if __name__ == "__main__":
    testDuplicateParenthesis()
    print('ALL TEST CASES PASSED')

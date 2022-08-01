"""
https://leetcode.com/problems/valid-parentheses/

Base Case:

- length of the expression must be even

@pseudocode
- if the len of the expression is odd
  => expression is not valid

Stack Solution:

@description:
We can use a stack to solve this problem. The idea is to traverse the given expression, and
- If the current character in the expression is an opening brace ( or { or [, push it into the stack.
- If the current character in the expression is a closing brace ) or } or ], pop a character from the stack,
and return false if the popped character is not the same as the current character,
or it does not pair with the current character of the expression.
Also, if the stack is empty, the total number of opening braces is less than the closing brace number at that point,
so the expression cannot be balanced.

@pseudocode:
- check edge case
- declare an empty character stack
- traverse the expression
    - if the current character in the expression is an opening brace,
      => push it into the stack

    - if the current character in the expression is a closing brace
        -  if a mismatch is found (i.e., if the stack is empty,
           the expression cannot be balanced since the total number of opening
           braces is less than the total number of closing braces)
           => return false
        -  pop character from the stack
        -  if the popped character is not an opening brace or does not pair with the current character of the expression
           => return false
- the expression is only balanced if the stack is empty at this point

@complexity:
Time:  O(n), we only loop once through the expression
Space: O(n), for the stack as n is the number of bracket pairs

Stack & HashMap Solution:

@description:
A good solution traverses the given expression, and for each opening brace in the expression,
push the corresponding closing brace into the stack.
- If the expression’s current character is a closing brace,
it should match the stack’s top element.
- If a match is found, pop the top character from the stack;
- Otherwise, we can say that the expression is not balanced.
Also, note that the stack should be empty after we have processed all characters in the expression.

@pseudocode:
- check edge case
- declare an empty character stack
- declare a hash map of the open brackets and their corresponding closed brackets
- traverse the expression
    - if the current character is a open bracket i.e. is in the hash map
      => push it's corresponding closed bracket to the stack

    - if the current character is a closing bracket i.e is in the stack and the stack is not empty
      => pop from stack

    - otherwise
      => expression is not valid

- after complete traversal
  if there is some starting bracket left in stack (i.e.stack not empty)
  => expression is not valid
- otherwise
  => expression is valid

@complexity:
Time:  O(n), we only loop once through the expression
Space: O(n), for the stack as n is the number of bracket pairs
"""


class Solution:
    def validParanthesesStack(self, exp: str) -> bool:

        # base case: length of the expression must be even
        if not exp or len(exp) & 1:
            return False

        # take an empty stack of characters
        stack = []

        # traverse the input expression
        for ch in exp:

            # if the current character in the expression is an opening brace,
            # push it into the stack
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # if the current character in the expression is a closing brace
            if ch == ')' or ch == '}' or ch == ']':
                # return false if a mismatch is found (i.e., if the stack is empty,
                # the expression cannot be balanced since the total number of opening
                # braces is less than the total number of closing braces)
                if not stack:
                    return False

                # pop character from the stack
                top = stack.pop()

                # if the popped character is not an opening brace or does not pair
                # with the current character of the expression
                if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                    return False

        # the expression is only balanced if the stack is empty at this point
        return not stack

    def validParanthesesStackHashMap(self, exp: str) -> bool:

        # base case: length of the expression must be even
        if len(exp) % 2 != 0:
            return False

        # if not exp or len(exp) & 1:
            # return False

        hash_map = {'{': '}',
                    '(': ')',
                    '[': ']'}
        stack = []

        for c in exp:
            # if c is an open bracket
            # then push it's closed bracket to the stack
            if c in hash_map:
                stack.append(hash_map[c])

            # if c is not an open bracket
            # and the stack is not empty
            # and c is equal to the last bracket pushed in the stack
            # then they match and balancing is true so we pop it from the stack
            elif stack and c == stack[-1]:
                stack.pop()

            # otherwise the expression is clearly not valid
            else:
                return False

        # if any brackets remain in the stack, the expression is clearly not valid
        if stack:
            return False

        # otherwise the expression is valid
        return True


def testValidParantheses():
    s = Solution()
    assert s.validParanthesesStack('[](){([[[]]])}(') == False
    assert s.validParanthesesStack('[{{{(())}}}]((()))') == True
    assert s.validParanthesesStack('[[[]])]') == False
    assert s.validParanthesesStackHashMap('[](){([[[]]])}(') == False
    assert s.validParanthesesStackHashMap('[{{{(())}}}]((()))') == True
    assert s.validParanthesesStackHashMap('[[[]])]') == False


if __name__ == "__main__":
    testValidParantheses()
    print('ALL TEST CASES PASSED')

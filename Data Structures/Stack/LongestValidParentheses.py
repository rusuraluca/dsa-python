"""
https://leetcode.com/problems/longest-valid-parentheses/

Example foolproof:
Input: s = "(()"
Output: 2
(   (  )
0   1  2

(
0

longest = 2

Input: s = ")()())"
Output: 4
) ( ) ( ) )
0 1 2 3 4 5

longest = 0 -> max(0, 2) -> 2 -> max(2, 4-0=4) -> 4

Base case:
- if len of expression is less or equal to 1
  => return 0

Stack Solution:
@description:
We traverse the expression and
- If the current character is an open bracket add it's index to the stack to find if a pair exist
- Otherwise i.e. if it's a closed character
    - Pop the last element in the stack
    - If now the stack is empty
        - Add it's index to the stack to continue
    - Otherwise
        - Update the longest element, the longest will be the maximum between the current longest
          and the difference between the current index and the top of the stack

@pseudocode
- test base case
- consider an empty stack and a variable longest initialized with 0
- traverse the expression
    - if the current element is an open parenthesis
      => append it's index to the stack
    - otherwise
        - if the stack is empty
          => append it's index to the stack
        - else
          => longest = max(longest, i-stack[-1])
- return the longest len

@complexity
Time: O(n), we traverse only once the expression
Space: O(n), for the stack
"""


class Solution:
    def longestValidParentheses(self, exp: str) -> int:

        longest = 0

        # base case
        if len(exp) <= 1:
            return longest

        # index from the end of the list
        stack = [-1]

        # When you use enumerate(), the function gives you back two loop variables:
        #   - The count of the current iteration
        #   - The value of the item at the current iteration
        for i, c in enumerate(exp):
            if c == "(":
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)

                else:
                    longest = max(longest, i - stack[-1])

        return longest


def testLongestValidParentheses():
    s = Solution()
    assert s.longestValidParentheses("") == 0
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4


if __name__ == "__main__":
    testLongestValidParentheses()
    print("ALL TESTS PASSED")
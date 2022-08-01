from collections import deque


class Solution:
    def DequeStack(self) -> deque:

        stack = deque()

        stack.append("a")
        stack.append("b")
        stack.append("c")

        print("Initial stack:")
        print(stack)

        print("\nElements poped from stack:")
        print(stack.pop())
        print(stack.pop())
        print(stack.pop())

        print("\nStack after elements are poped:")

        return stack


s = Solution()
s.DequeStack()

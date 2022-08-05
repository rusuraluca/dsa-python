class Queue:

    def __init__(self):
        self.pushstack = []
        self.popstack = []

    def push(self, x: int) -> None:
        self.pushstack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.popstack.pop()

    def peek(self) -> int:
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())

        return self.popstack[-1]

    def empty(self) -> bool:
        return not self.pushstack and not self.popstack


class QueuePush:

    def __init__(self):
        self.stack = []
        self.stack_two = []

    def push(self, x: int) -> None:
        while self.stack:
            top = self.stack.pop()
            self.stack_two.append(top)

        self.stack.append(x)

        while self.stack_two:
            top = self.stack_two.pop()
            self.stack.append(top)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack

class Queue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        res = self.queue[0]
        del self.queue[0]
        return res

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True

        return False

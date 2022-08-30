class Solution:
    def fib(self, n):
        a = 0
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(1, n):
                c = a + b
                a = b
                b = c
            return b

    def fibRecursive(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

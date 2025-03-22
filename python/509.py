class Solution:
    def fib(self, n: int) -> int:
        f1 = 0
        f2 = 1

        if n <= 0:
            return 0

        if n == 1:
            return f2

        for _ in range(1, n):
            f3 = f1 + f2
            f1 = f2
            f2 = f3

        return f2


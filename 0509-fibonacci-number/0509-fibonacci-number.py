class Solution:
    def fib(self, n: int) -> int:
        return int(((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n)) / sqrt(5))
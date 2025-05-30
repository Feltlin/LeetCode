class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = 1
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            if n % 2:
                power *= x
            x *= x
            n //= 2
        return power

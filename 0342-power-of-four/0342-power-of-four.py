class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 4 != 0 or n < 0:
            return False
        i = 4
        while i * i < n:
            i *= i
        while i < n:
            i *= 4
        if i == n:
            return True
        else:
            return False
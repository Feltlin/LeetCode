class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        s = 0
        while s <= n:
            s += i
            i += 1
        return i - 2
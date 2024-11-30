class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        for i in range(x+1):
            if (i+1)*(i+1) > x:
                return i
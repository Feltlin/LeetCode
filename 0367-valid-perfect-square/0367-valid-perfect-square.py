class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        a, b = 2, num // 2
        while a <= b:
            if ((a+b) // 2) * ((a+b) // 2) == num:
                return True
            if (a+b) // 2 * (a+b) // 2 < num:
                a = (a+b) // 2 + 1
            else:
                b = (a+b) // 2 - 1
        return False
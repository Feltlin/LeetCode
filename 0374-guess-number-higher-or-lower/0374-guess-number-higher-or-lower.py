# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a, b = 1, n
        while a <= b:
            if guess(a) == 0:
                return a
            if guess(b) == 0:
                return b
            if guess((a + b) // 2) > 0:
                a = (a + b) // 2
            elif guess((a + b) // 2) < 0:
                b = (a + b) // 2
            else:
                return (a + b) // 2
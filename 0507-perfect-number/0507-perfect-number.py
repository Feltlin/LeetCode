class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2:
            return False
        sum = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                sum += i
            if sum > num:
                return False
        if sum == num:
            return True
        else:
            return False
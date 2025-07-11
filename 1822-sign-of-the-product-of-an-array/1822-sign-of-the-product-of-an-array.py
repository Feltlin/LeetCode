class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for i in nums:
            if i < 0:
                sign = -sign
            elif i == 0:
                return 0
        return sign
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        while len(nums):
            m = max(m, nums.pop(-1) + nums.pop(0))
        return m
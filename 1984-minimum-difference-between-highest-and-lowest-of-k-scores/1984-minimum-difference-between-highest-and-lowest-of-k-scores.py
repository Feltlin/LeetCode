class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = nums[k - 1] - nums[0]
        for i in range(len(nums) - k + 1):
            n = min(n, nums[i + k - 1] - nums[i])
        return n
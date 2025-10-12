class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if(len(nums) <= 1):
            return True
        
        inc = True
        dec = True
        for i in range(len(nums) - 1):
            inc &= nums[i + 1] >= nums[i]
            dec &= nums[i + 1] <= nums[i]
        return inc | dec
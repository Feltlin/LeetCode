class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        if target < nums[0] or target > nums[-1]:
            return -1
        while a <= b:
            c = (a + b) // 2
            if nums[c] == target:
                return c
            elif nums[c] < target:
                a = c + 1
            else:
                b = c - 1
        return -1
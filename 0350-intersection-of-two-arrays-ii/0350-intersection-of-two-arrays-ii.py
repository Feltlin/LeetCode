class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        while len(nums1) > 0 and len(nums2) > 0:
            i = nums1.pop(0)
            if i in nums2:
                nums2.remove(i)
                inter.append(i)
        return inter
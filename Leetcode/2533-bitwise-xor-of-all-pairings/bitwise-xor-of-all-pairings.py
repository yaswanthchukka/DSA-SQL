class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        res = 0
        if len(nums1) % 2 != 0:
            for i in nums2:
                res = res ^ i
        if len(nums2) % 2 != 0:
            for i in nums1:
                res = res ^ i
        return res
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        t = nums[-k:]+nums[:-k]

        for i in range(len(nums)):
            nums[i] = t[i]

        
        
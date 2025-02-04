class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        MAX_ = 0
        s = nums[0]

        i = 1
        while i < len(nums):
            if nums[i] <= nums[i-1]:
                if MAX_ < s:
                    MAX_ = s
                s = nums[i]
            else:
                s += nums[i]
            i += 1
        return max(MAX_,s)

        
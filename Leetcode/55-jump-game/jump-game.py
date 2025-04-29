class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_ = len(nums)

        curr_ = nums[0]
        if curr_ <= 0 and len(nums) > 1:
            return False

        for i in range(1,len(nums)):
            curr_ -= 1
            if curr_ < nums[i]:
                curr_ = nums[i]
            if curr_ == 0 and i != len(nums) - 1:
                return False

        return True
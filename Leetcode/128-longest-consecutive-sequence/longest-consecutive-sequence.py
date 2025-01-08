class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 0
        max_ = 1
        c = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                c += 1
            else:
                if c > max_:
                    max_ = c
                c = 1
        return max(c,max_)
        
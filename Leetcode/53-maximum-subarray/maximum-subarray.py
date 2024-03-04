class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=nums[0]
        t=0
        i=0
        while i<len(nums):
            t=t+nums[i]
            if t>s:
                s=t
            if t<0:
                t=0
            i+=1
        return s
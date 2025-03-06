class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = nums[0]
        temp = 0

        for i in nums:
            temp += i
            if temp > sum_:
                sum_ = temp
            if temp < 0:
                temp = 0
            
            
        return sum_
        
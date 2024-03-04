class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        while True:
            if nums[i:]+nums[:i]==sorted(nums):
                break
            else:
                i+=1
        return nums[i]
        


        
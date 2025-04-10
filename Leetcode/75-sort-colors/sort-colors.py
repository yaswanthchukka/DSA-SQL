class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1 = 0
        c2 = 0
        c3 = 0
        for i in nums:
            if i == 0:
                c1 += 1
            elif i == 1:
                c2 += 1
            else:
                c3 += 1
        k = 0
        for i in range(c1+c2+c3):
            if k < c1:
                nums[k] = 0
                k += 1
            elif k >= c1 and k < c1+c2:
                nums[k] = 1
                k += 1
            else:
                nums[k] = 2
                k += 1

        
        
        
        
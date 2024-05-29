class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0 
        t = 0
        c = 0
        while i<n:
            if nums[i]>=t:
                c+=1
                
            if c>t:
                i = 0
                c = 0
                t+=1
                continue
            i+=1
            
        if c==0 or c!=t:
            return -1
        return t
            

        
        
        
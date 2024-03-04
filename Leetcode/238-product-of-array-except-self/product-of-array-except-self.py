class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        c=0
        for i in nums:
            if i==0:
                c+=1
                continue
            prod*=i
        l=[]
        if c==0:
            for j in nums:
                l.append(prod//j)
            return l
        if c==1:
            for k in nums:
                if k==0:
                    l.append(prod)
                else:
                    l.append(0)
            return l
        else:
            return [0]*len(nums)
        
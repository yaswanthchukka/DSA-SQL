class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        l=list(d.values())
        return l.count(max(l))*max(l)

        

        
        
        
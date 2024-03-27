class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k=max(nums)
        if max(nums)<1:
            return 1
        l=set(filter(lambda x:x>0,nums))
        for i in range(1,k):
            if i not in l:
                return i
        return k+1
        
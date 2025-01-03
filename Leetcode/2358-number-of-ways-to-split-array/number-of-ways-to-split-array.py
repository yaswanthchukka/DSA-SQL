class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ps = [nums[0]]
        for i in range(1,len(nums)):
            ps.append(ps[-1] + nums[i])

        c = 0
        for j in range(len(nums)-1):
            if ps[j] >= (ps[-1]-ps[j]):
                c += 1
        return c
        
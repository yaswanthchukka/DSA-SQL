import math
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total = math.comb(len(nums),2)
        d = {}
        c = 0
        for i in range(len(nums)):
            k = nums[i] - i
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1

        for i in d:
            if d[i] > 1:
                c += math.comb(d[i],2)
        return total - c
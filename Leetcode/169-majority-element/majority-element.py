class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > len(nums)//2:
                    return i
            else:
                d[i] = 1
                if d[i] > len(nums)//2:
                    return i
        
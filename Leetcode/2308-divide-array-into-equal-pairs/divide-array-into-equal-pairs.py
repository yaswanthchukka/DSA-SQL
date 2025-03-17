class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        c = 0

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                if d[i] % 2 == 0:
                    c += 1
        return c == len(nums) // 2


        
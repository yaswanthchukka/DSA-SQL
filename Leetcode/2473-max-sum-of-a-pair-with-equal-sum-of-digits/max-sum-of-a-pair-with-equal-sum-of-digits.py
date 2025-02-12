class Solution:
    def sum_(self,n):
        s = 0
        while n > 0:
            s += n%10
            n = n//10
        return s
    def maximumSum(self, nums: List[int]) -> int:
        max_ = -1
        d = {}
        k = []
        nums = sorted(nums)
        for i in nums:
            k.append(self.sum_(i))

        for i in range(len(k)):
            if k[i] in d:

                t = d[k[i]][-1] + nums[i]
                if t > max_:
                    max_ = t
                d[k[i]].append(nums[i])
            else:
                d[k[i]] = [nums[i]]
        return max_


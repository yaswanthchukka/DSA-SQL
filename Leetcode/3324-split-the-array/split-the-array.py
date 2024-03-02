class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in nums:
            if nums.count(i)<=2:
                continue
            else:
                return False
        return True
        
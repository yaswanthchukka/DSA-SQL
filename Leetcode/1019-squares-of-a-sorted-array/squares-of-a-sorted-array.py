class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=list(map(lambda x:x*x,nums))
        l.sort()
        return l
        
        
        
        
        

        
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        t=0
        i=0
        j=len(height)-1
        while i<len(height) and j>=0:
            temp=min(height[i],height[j])*(j-i)
            if temp>t:
                t=temp
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return t

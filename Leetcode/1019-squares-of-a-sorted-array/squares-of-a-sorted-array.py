class Solution(object):
    def merge(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            l_arr=arr[:mid]
            r_arr=arr[mid:]
            self.merge(l_arr)
            self.merge(r_arr)
            i=j=k=0
            while i<len(l_arr) and j<len(r_arr):
                if l_arr[i]>r_arr[j]:
                    arr[k]=r_arr[j]
                    j+=1
                else:
                    arr[k]=l_arr[i]
                    i+=1
                k+=1
            while i<len(l_arr):
                arr[k]=l_arr[i]
                i+=1
                k+=1
            while j<len(r_arr):
                arr[k]=r_arr[j]
                j+=1
                k+=1



    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=list(map(lambda x:x*x,nums))
        self.merge(l)
        return l
        
        
        
        
        

        
class Solution:
    def isMonotonic(self,l):
        k = int(l[0])
        for i in range(1,len(l)):
            if int(l[i]) >= k:
                k = int(l[i])
            else:
                return i
        return -1
    
    
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        arr = list(str(n))
        while True:
            print(arr)
            k1 = self.isMonotonic(arr)
            if k1 == -1:
                return int("".join(arr))
            print(k1)
            arr = arr[:k1-1] + [str(int(arr[k1-1]) - 1)] + ['9']*len(arr[k1:])
        



        
        


        
        
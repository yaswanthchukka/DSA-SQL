import bisect
class Solution:
    def bin_(self,arr,k):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            k = target - numbers[i]
            if self.bin_(numbers[i+1:],k) != -1:
                return [i+1,i+1+self.bin_(numbers[i+1:],k)+1]
            


        

        
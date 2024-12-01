import math
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0 
        while i < len(arr):
            k1 = arr[i]/2
            k2 = arr[i]*2 
            if k2 in arr[:i] or k2 in arr[i+1:]:
                return True
            if math.ceil(k1)==math.floor(k1):
                if k1 in arr[:i] or k1 in arr[i+1:]:
                    return True
            i += 1
        return False
                    
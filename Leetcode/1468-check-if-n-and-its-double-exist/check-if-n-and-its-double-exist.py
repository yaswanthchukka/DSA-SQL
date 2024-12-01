import math
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0 
        while i < len(arr):
            k = arr[i]/2
            if math.ceil(k)==math.floor(k):
                if k in arr[:i] or k in arr[i+1:]:
                    return True
            i += 1
        return False
                    
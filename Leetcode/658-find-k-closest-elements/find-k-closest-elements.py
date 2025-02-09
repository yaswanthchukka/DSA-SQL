class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = len(arr) - 1
        if k == len(arr):
            return arr
        while (j-i) != k - 1:
            if abs(arr[i] - x) <= abs(arr[j] - x):
                j -= 1
            else:
                i += 1
        return arr[i:j + 1 ]
            
        
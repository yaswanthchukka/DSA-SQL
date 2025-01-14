class Solution:
    def fun(self,l,target):
        low = 0
        high = len(l) - 1

        while low <= high:
            mid = (high + low)//2
            if l[mid] == target:
                return True
            elif l[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target and i[-1] >= target:
                return self.fun(i,target)
        return False
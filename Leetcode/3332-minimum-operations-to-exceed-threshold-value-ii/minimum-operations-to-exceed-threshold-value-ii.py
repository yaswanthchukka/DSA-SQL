import bisect
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        c = 0
        i = 0
        while len(arr) > 1:
            if arr[i] < k:
                t1 = min(arr[i],arr[i+1])*2 + max(arr[i],arr[i+1])
                arr.pop(i)
                arr.pop(i)
                t2 = bisect.bisect(arr,t1)
                arr.insert(t2,t1)
                c += 1
            else:
                return c
        if arr[-1] < k:
            return c + 1
        return c

                

        
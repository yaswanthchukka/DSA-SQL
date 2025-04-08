class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = [-1]*100
        max_ = -1
        for i in range(len(nums)):
            if arr[nums[i] - 1] == -1:
                arr[nums[i] - 1] = i 
            else:
                if max_ < arr[nums[i] - 1]:
                    max_ = arr[nums[i] - 1]
                arr[nums[i] - 1] = i
        if max_ != -1:
            return max_//3 + 1
        return 0


        

        
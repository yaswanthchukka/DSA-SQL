class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in range(len(numbers)):
            num_to_look = target-numbers[num]
            num_to_look_arr = numbers[num+1:]
            if num_to_look in num_to_look_arr:
                return [num+1,num+1+num_to_look_arr.index(num_to_look)+1]
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = sorted(citations)

        for i in range(len(arr)):
           if arr[i] >= len(arr[i:]):
            return len(arr[i:])
        return 0
        
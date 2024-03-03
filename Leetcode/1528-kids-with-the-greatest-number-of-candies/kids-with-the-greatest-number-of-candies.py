class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k=max(candies)
        t=[]
        for i in candies:
            if i+extraCandies>=k:
                t.append(True)
            else:
                t.append(False)
        return t
        
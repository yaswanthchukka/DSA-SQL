class Solution:
    def countLargestGroup(self, n: int) -> int:
        k = [0]*37
        for num in range(1,n+1):
            digits = [int(d) for d in str(num)]
            sum_ = reduce(lambda x,y:x+y,digits)
            k[sum_]+=1
        return k.count(max(k))

        
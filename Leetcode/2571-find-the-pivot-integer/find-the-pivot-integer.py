class Solution:
    def pivotInteger(self, n: int) -> int:
        l=list(range(1,n+1))
        if len(l)==1:
            return l[0]
        i=len(l)-2
        while i>0:
            if sum(l[:i+1])==sum(l[i:]):
                return l[i]
            else:
                i-=1
        return -1





        
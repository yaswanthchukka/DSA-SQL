class Solution:
    def fun(self,n):
        s=0
        while n>0:
            r=n%10
            s+=(r*r)
            n=n//10
        return s
    def isHappy(self, n: int) -> bool:
        s=set()
        while True:
            t=self.fun(n)
            if t == 1 or t in s:
                return t==1
            print(t)
            s.add(t)
            n=t
        


        
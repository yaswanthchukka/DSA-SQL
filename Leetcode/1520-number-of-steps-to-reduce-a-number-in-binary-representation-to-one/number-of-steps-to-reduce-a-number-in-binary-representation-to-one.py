class Solution:
    def numSteps(self, s: str) -> int:
        t = int(s,base=2)
        c=0
        while t != 1:
            if t%2==0:
                t = t//2
            else:
                t = t+1
            c+=1
        return c
        
        
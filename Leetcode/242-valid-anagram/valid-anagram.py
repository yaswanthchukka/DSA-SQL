class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                continue
            else:
                return False
        if i==len(s) and j==len(t):
            return True
        return False
        
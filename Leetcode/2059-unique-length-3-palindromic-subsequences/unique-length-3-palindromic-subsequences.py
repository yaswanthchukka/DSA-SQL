class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i,i,1]
            else:
                d[s[i]][1] = i
                d[s[i]][2] += 1
        print(d)
        c = 0
        for j in d:
            t = set()
            if d[j][1]-d[j][0]>=2:
                if d[j][2] >= 3:
                    c += 1
                for k in range(d[j][0]+1,d[j][1]):
                    if s[k]!=j and s[k] not in t:
                        t.add(s[k])
                        c += 1
        return c

        
        
         
        
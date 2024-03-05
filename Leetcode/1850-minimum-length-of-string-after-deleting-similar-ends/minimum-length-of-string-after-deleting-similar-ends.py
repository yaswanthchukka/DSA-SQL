class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        k=''
        while i<j:
            if s[i]==s[j]:
                k=s[i]
                i+=1
                j-=1
                
            else:
                if k=='':
                    return j-i+1
                if s[i]!=k and s[j]!=k:
                    return j-i+1
                if k==s[i]:
                    i+=1
                elif k==s[j]:
                    j-=1
        if i==j and k!=s[i]:
            return 1
        return 0



        
        
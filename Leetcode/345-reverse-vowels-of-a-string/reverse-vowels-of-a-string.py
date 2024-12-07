class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['A','E','I','O','U','a','e','i','o','u']
        i = 0
        j = len(s)-1
        s = list(s)
        while i <= j:
            if s[i] in v and s[j] in v:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif s[i] in v:
                j -= 1
            else:
                i += 1
        return "".join(s)
            
        
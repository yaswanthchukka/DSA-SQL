class Solution:
    def clearDigits(self, s: str) -> str:
        l = list(s)
        k = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                l[k[-1]] = ""
                l[i] = ""
                k.pop()
            elif s[i].isalpha():
                k.append(i)
            i += 1
        return "".join(l)


        
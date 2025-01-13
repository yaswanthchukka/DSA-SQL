class Solution:
    def fun(self,l):
        if len(l) >= 3:
            l.pop(2)
            l.pop(0)
            self.fun(l)
        return len(l)
    def minimumLength(self, s: str) -> int:
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)

        res = 0
        for i in d:
            if len(d[i]) % 2 == 0:
                res += 2
            else:
                res += 1
        return res
        
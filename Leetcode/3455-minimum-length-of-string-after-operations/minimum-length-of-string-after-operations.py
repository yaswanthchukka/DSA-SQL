class Solution:
    def minimumLength(self, s: str) -> int:
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        res = 0
        for i in d:
            if d[i] % 2 == 0:
                res += 2
            else:
                res += 1
        return res
        
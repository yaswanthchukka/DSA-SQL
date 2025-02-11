class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = []

        for i in s:
            l.append(i)
            if len(l) >= len(part) and "".join(l[-len(part):])==part:
                l = l[:-len(part)]
        return "".join(l)
        
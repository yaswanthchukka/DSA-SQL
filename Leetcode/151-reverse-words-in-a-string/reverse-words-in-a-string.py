class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split()
        l = l[::-1]
        return " ".join(l)        
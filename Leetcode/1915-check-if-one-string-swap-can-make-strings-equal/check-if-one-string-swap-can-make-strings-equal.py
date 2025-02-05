class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
        i = -1
        j = -1

        k = 0
        while k < len(s1):
            if s1[k] != s2[k] and i == -1:
                i = k
            elif s1[k] != s2[k] and j == -1:
                j = k
            elif s1[k] != s2[k]:
                return False
            k += 1
        if (i != -1 and j != -1):
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
        return False


        
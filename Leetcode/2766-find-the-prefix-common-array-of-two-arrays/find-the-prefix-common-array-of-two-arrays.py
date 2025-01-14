class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        s1 = set()
        s2 = set()
        res = []
        i = 0
        while i < len(A):
            if A[i] in s1:
                s2.add(A[i])
            else:
                s1.add(A[i])
            if B[i] in s1:
                s2.add(B[i])
            else:
                s1.add(B[i])
            res.append(len(s2))
            i += 1
        return res
        
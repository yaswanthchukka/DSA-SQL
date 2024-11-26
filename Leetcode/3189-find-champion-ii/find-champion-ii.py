class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n==1:
            return 0
        s1 = set()
        s2 = set()
        for i in edges:
            s1.add(i[0])
            s2.add(i[1])

        if len(s1.difference(s2))==1 and n == len(s1.union(s2)):
            return list(s1.difference(s2))[0]
        return -1

        
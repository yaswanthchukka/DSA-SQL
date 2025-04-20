class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = {}
        c = 0
        for i in answers:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in d:
            if d[j]%(j+1) == 0:
                c += (d[j]//(j+1))*(j+1)
            else:
                c += (d[j]//(j+1) + 1)*(j+1)
        return c
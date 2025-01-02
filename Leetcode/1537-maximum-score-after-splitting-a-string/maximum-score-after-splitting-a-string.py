class Solution:
    def maxScore(self, s: str) -> int: 
        ps = [[0,0]]
        for i in s:
            if i == "1":
                ps.append([ps[-1][0],ps[-1][1]+1])
            else:
                ps.append([ps[-1][0]+1,ps[-1][1]])
        ones = ps[-1][1]
        res = 0
        for j in range(1,len(ps)-1):
            if (ones-ps[j][1])+ps[j][0] > res:
                res = (ones-ps[j][1])+ps[j][0]
        return res
        
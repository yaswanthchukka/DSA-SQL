class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = set(['a','e','i','o','u'])
        ps = [0]
        for i in words:
            if i[0] in v and i[-1] in v:
                ps.append(ps[-1]+1)
            else:
                ps.append(ps[-1])
        res = []
        for j in queries:
            res.append(ps[j[-1]+1]-ps[j[0]])
        return res
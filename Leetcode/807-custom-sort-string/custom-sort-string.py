class Solution:
    def customSortString(self, order: str, s: str) -> str:
        t=list(s)
        k=[]
        for i in order:
            if i in t:
                k.append(i)
                t.remove(i)
        for j in t:
            if j in order:
                k.insert(k.index(j)+1,j)
            else:
                k.append(j)
        return ''.join(k)


        
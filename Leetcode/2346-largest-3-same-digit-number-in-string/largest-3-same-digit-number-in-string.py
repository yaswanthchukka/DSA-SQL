class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=[]
        i=0
        j=1
        while j<len(num):
            if num[i]!=num[j]:
                i+=1
                j=i+1
            else:
                if (j-i)==2:
                    l.append(int(num[j]))
                    i=j+1
                    j=i+1
                    continue
                j+=1
        if len(l)==0:
            return ""
        return str(max(l))*3
        
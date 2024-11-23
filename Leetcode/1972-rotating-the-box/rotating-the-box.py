import numpy 
class Solution:
    def down(self,l):
        for i in range(1,len(l)):
            m = l[i]
            j = i-1
            if m == ".":
                while j>=0 and l[j]=='#':
                    l[j+1] = "#"
                    j -= 1
                l[j+1] = '.'
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        for i in range(len(box)):
            self.down(box[i])

        box = list(map(list, zip(*box)))
        result = []
        for i in box:
            result.append(reversed(i))
        return result
        
        
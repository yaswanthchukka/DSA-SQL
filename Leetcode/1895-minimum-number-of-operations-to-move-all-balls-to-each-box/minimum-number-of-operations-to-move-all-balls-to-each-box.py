class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        l = [0]
        c = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                l[0] += i
                c += 1
        if boxes[0] == "1":
            Left = 1
            Right = c - 1
        else:
            Left = 0
            Right = c

        for j in range(1,len(boxes)):
            l.append(l[-1] + Left - Right)
            if boxes[j] == "1":
                Left += 1
                Right -= 1
        return l


                
                
        
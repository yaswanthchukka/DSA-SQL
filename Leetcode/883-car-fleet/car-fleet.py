class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            d[position[i]] = speed[i]

        v = sorted(d.keys())
        print(v)

        res = []

        for j in v:
            res.append((target-j)/d[j])
        print(res)

        c = 1
        k = len(res)-1
        t = k - 1

        while t>=0:
            if res[k] < res[t]:
                c += 1
                k = t
                t = k - 1
            else:
                t -= 1
        return c



        
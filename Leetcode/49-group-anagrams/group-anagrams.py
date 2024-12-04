class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        t = {}

        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in t:
                d[strs[i]] = []
                t[''.join(sorted(strs[i]))] = strs[i]
            else:
                d[t[''.join(sorted(strs[i]))]].append(strs[i])
        l = []
        for key,values in d.items():
            k = []
            k.append(key)
            k.extend(values)
            l.append(k)
        return l

        

            
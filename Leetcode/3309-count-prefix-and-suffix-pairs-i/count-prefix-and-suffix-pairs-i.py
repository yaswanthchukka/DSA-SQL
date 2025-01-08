class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c = 0

        for i in range(len(words)-1):
            k = len(words[i])
            for j in range(i+1,len(words)):
                if words[i] == words[j][:k] and words[i] == words[j][-k:]:
                    c += 1
                

        return c
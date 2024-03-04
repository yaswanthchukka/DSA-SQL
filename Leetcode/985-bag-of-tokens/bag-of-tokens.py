class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        k=sorted(tokens)
        i=0
        j=len(tokens)-1
        t=0
        score=0
        while i<=j:
            if power>=k[i]:
                power-=k[i]
                i+=1
                score+=1
            else:
                if score>0:
                    power+=k[j]
                    j-=1
                    if score>t:
                        t=score
                    score-=1
                else:
                    return max(score,t)
        return max(score,t)
                



        
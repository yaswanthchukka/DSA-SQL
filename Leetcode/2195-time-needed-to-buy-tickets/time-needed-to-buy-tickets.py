class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        k1 = sum(list(filter(lambda x:x<=tickets[k],tickets[:k])))
        k2 = len(list(filter(lambda x:x>tickets[k],tickets[:k])))
        k3 = sum(list(filter(lambda x:x<tickets[k],tickets[k+1:])))
        k4 = len(list(filter(lambda x:x>=tickets[k],tickets[k+1:])))
        return k1+k3+(k2*tickets[k])+(k4*(tickets[k]-1))+tickets[k]
        
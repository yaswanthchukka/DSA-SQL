class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=s.count('1')
        t=len(s)
        res=['0']*t
        for i in range(k-1):
            res[i]='1'
        res[-1]='1'
        return ''.join(res)

        
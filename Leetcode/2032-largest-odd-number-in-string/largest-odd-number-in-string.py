import sys
sys.set_int_max_str_digits(500000)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=int(num)
        while n>0:
            if n%2!=0:
                return str(n)
            n=n//10
        return ""
        
        
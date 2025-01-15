class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if bin(num1)[2:].count('1') == bin(num2)[2:].count('1'):
            return num1

        if bin(num1)[2:].count('1') < bin(num2)[2:].count('1'):

            res = ['0'] * len(bin(num2)[2:]) + list(bin(num1)[2:])

            l1 = bin(num1)[2:].count('1')
            l2 = bin(num2)[2:].count('1')

            l = l2 - l1

            i = 0
            j = -1

            while i < l:
                if res[j] == "0":
                    res[j] = "1"

                    i += 1
                j -= 1
            return int("".join(res),2)

        
        if bin(num1)[2:].count('1') > bin(num2)[2:].count('1'):

            b = ["0"] * len(bin(num2)[2:])   + list(bin(num1)[2:])

            res = ["0"] * len(bin(num2)[2:]) + ["0"] * len(bin(num1)[2:])

            l = bin(num2)[2:].count('1')

            i = 0
            j = 0

            while i < l:
                if b[j] == "1":
                    res[j] = "1"
                    i += 1
                j += 1
            return int("".join(res),2)
                


        
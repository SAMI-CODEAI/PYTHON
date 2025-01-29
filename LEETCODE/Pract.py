from openpyxl.styles.builtins import output


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d=abs(dividend)
        dv=abs(divisor)
        output=0

        while d>=dv:
            temp=dv
            mul=1
            while d>=temp:
                d-=temp
                output+=mul
                mul+=mul
                temp+=temp
        if(dividend<0 and divisor>=0) and (divisor<0 and dividend>=0) :
            output=-output

        return min(2147483647 ,max(-2147483647,output))




sol=Solution()
print(sol.divide(100000,3))
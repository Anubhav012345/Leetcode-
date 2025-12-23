class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        if dividend==0:
            return 0
        sign=-1 if (dividend < 0) ^ (divisor < 0) else 1
        
        a=abs(dividend)
        b=abs(divisor)
        
        ans=0
        
        while a>=b:
            power = 0
            while a>=b*(2**(power+1)):
                power+=1

            a-=b*(2** power)
            ans+=2**power

        return sign *ans
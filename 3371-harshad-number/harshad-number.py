class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        num=0
        while x>0:
            rem=x%10
            num+=rem
            x//=10
        
        if(original%num==0):
            return num
        else:
            return -1

        
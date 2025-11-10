class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if(num<0):
            num+=2**32
        hexa_decimal='0123456789abcdef'
        result=[]
        while num!=0:
            remainder=num%16
            result.append(hexa_decimal[remainder])
            num//=16
        return ''.join(result[::-1])        
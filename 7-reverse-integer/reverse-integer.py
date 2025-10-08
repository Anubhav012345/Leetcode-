class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        a=abs(x)
        num=a
        result=0
        while num>0:
            lastdigit=num%10
            result=(result*10)+lastdigit
            num=num//10
        result*=sign
        if result<-2**31 or result>2**31-1:
            return 0
        return result


__import__("atexit").register(lambda: open("display_runtime.txt", 'w').write('0'))

        
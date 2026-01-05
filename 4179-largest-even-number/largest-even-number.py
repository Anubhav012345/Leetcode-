class Solution:
    def largestEven(self, s: str) -> str:
        n=len(s)-1
        while n>=0:
            if(s[n]=='2'):
                return(s[:n+1])
            n-=1
        return ""

        
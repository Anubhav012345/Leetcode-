class Solution:
    def minimumFlips(self, n: int) -> int:
        s=""
        num=n        
        while num>0:
            remainder=num%2
            s=str(remainder)+s
            num//=2
        r=""
        for i in range(len(s)-1,-1,-1):
            r+=s[i]        
        flips=0
        for i in range(len(s)):
            if s[i]!=r[i]:
                flips+=1
        
        return flips
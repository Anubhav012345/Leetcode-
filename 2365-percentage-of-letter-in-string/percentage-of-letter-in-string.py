class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n=len(s)
        occur=0
        for i in range(len(s)):
            if(s[i]==letter):
                occur+=1
            
        ans=int((occur / n) * 100)
        return ans

        
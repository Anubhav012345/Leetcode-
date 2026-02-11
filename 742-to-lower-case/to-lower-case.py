class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            ans+=s[i].lower()
        
        return ans
        
        
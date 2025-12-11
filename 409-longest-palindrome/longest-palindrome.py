class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hash_map={}

        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1

        ans=0

        for key,value in hash_map.items():
            ans+=(value//2)*2
        
        if(ans<len(s)):
            ans+=1
        
        return ans
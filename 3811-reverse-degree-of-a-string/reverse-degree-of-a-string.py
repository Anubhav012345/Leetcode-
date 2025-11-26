class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            char_index=ord(s[i])-96
            reverse=(27-char_index)*(i+1)
            ans+=reverse
        return ans
        
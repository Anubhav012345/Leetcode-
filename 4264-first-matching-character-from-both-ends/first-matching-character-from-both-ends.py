class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        right=len(s)-1
        left=0
        while left<=right:
            if s[left]==s[right]:
                return left
            left+=1
            right-=1
        return -1
        